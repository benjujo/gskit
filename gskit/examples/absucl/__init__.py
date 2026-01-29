from gskit.elements import ZpElement, G1Element, G2Element, GTElement
from gskit.framework import CRS
from gskit.gs_context import GSContext
from .ds import FBB as DS
from .lit import WBB as LIT
from .rpsps import RPSPS
from .msp import MSP

from typing import Dict, List, Tuple
import json


class ABSUCL():
    def __init__(self, crs: CRS, sk_psdo: List[ZpElement]=None, vk_psdo: List[G2Element]=None):
        self.crs = crs
        self.psps = RPSPS(crs)
        self.ds = DS(crs)
        self.lit = LIT(crs)
        if sk_psdo and vk_psdo:
            self.sk_psdo = sk_psdo
            self.vk_psdo = vk_psdo
        else:
            self.sk_psdo, self.vk_psdo = self.ds.keygen()
        self.vk_attrs: Dict[str, G2Element] = {}

    @classmethod
    def setup(cls, crs_json_str:str):
        #gs = GS.setup()
        crs = CRS.from_json(crs_json_str)
        return cls(crs)

    @classmethod
    def setup_from_json(cls, json_str:str):
        crs = CRS.from_json(json_str)
        json_dict = json.loads(json_str)
        sk_psdo = [ZpElement.from_json(zp) for zp in json_dict['sk_psdo']] if 'sk_psdo' in json_dict else [None]
        vk_psdo = [G2Element.from_json(g2) for g2 in json_dict['vk_psdo']]

        psps = RPSPS(crs)
        ds = DS(crs)
        lit = LIT(crs)
        return cls(crs, sk_psdo, vk_psdo)

    def add_vk_attr(self, attribute:str, vk_aa:G2Element):
        self.vk_attrs[attribute] = vk_aa

    def aa_setup(self) -> Tuple[List[ZpElement], List[G2Element]]:
        sk,vk = self.psps.keygen()
        return sk, vk

    def user_keygen(self) -> Tuple[ZpElement, G2Element]:
        sk,vk = self.lit.keygen()
        return sk, vk

    def attr_keygen(self, fusk:G1Element, attribute:str, sk_aa:ZpElement) -> Tuple[G1Element, G1Element]:
        element_attr = ZpElement.from_str(attribute)
        #sk_ida = self.psps.sign(sk_aa, ((fusk, None), [attribute]))
        sk_ida = self.psps.sign(sk_aa, ((fusk, None), [element_attr]))
        return sk_ida

    def sign(self, m: str, predicate: str, usk: ZpElement,
             sk_ida_dict: Dict[str, Tuple[G1Element, G1Element]], recip: int):
        """
        Create an ABSUCL signature.

        Args:
            m: Message to sign
            predicate: Policy predicate (e.g., "attr1 AND attr2")
            usk: User's secret key (Zp element)
            sk_ida_dict: Dict mapping attribute names to (R, S) signature tuples
            recip: Recipient identifier

        Returns:
            Dict with 'tau' (tag), 'sk_ida_hat' (randomized R components), and 'ctx' (GSContext)
        """
        # Create GSContext for this proof
        ctx = GSContext(self.crs)

        # Build extended predicate with PSDO
        xpredicate = f"({predicate}) or PSDO"
        msp = MSP.from_policy_str(xpredicate)

        # Verify all required attributes are registered
        for attr_name in msp.index:
            if attr_name not in self.vk_attrs and attr_name != "PSDO":
                raise Exception(f"Attribute {attr_name} not found in attribute authorities")

        # Compute user's public keys (witnesses)
        F = usk * self.g        # G1 public key
        Ftilda = usk * self.h   # G2 public key

        # Randomize attribute signatures
        randomized_sk_ida = {}
        z_values = {}  # Track z values for each attribute

        for attr_name in msp.index:
            if attr_name in sk_ida_dict:
                # User has this attribute
                randomized_sk_ida[attr_name] = RPSPS.randomize(sk_ida_dict[attr_name])
                z_values[attr_name] = ZpElement.init(1)
            else:
                # User doesn't have this attribute (or it's PSDO)
                if attr_name == "PSDO":
                    # PSDO uses FBB signature, not RPSPS
                    randomized_sk_ida[attr_name] = (G1Element.random(), None)
                else:
                    # Random values for attributes not owned
                    randomized_sk_ida[attr_name] = (G1Element.random(), G1Element.random())
                z_values[attr_name] = ZpElement.init(0)

        # Create tag using LIT
        recip_zp = ZpElement.init(recip)
        tag = self.lit.sign(usk, recip_zp)

        # === Add MSP equations to context ===
        msp_gs_string, msp_values = msp.gs_string_and_values()
        # Add z values for each attribute
        for attr_name in msp.index:
            msp_values[f"z_{attr_name}"] = z_values[attr_name]
        ctx.add(msp_gs_string, msp_values)

        # === Add LIT (tag) verification to context ===
        self.lit.verify_absucl.gs_add(ctx, Ftilda, recip_zp, tag,
                                       aliases={'Ftilda': 'Ftilda'})  # Ftilda is shared

        # === Add consistency equation (F, Ftilda from same usk) ===
        g_neg = ~self.g
        gt_zero = self.g.pair(self.h) * ~(self.g.pair(self.h))
        consistency_gs = """
        variables:
            F: G1
            Ftilda: G2
        constants:
            h: G2
            g_neg: G1
            gt_zero: GT
        equations:
            F * h + g_neg * Ftilda = gt_zero
        """
        ctx.add(consistency_gs, {
            'F': F,
            'Ftilda': Ftilda,
            'h': self.h,
            'g_neg': g_neg,
            'gt_zero': gt_zero
        })

        # === Add RPSPS verification for each attribute ===
        for attr_name in msp.index:
            if attr_name == "PSDO":
                continue

            R, S = randomized_sk_ida[attr_name]
            z = z_values[attr_name]
            attr_zp = ZpElement.from_str(attr_name)

            self.psps.z_is_zero_or_verify_absucl.gs_add(
                ctx,
                vk=self.vk_attrs[attr_name],
                Ftilda=Ftilda,
                R=R,
                signature_S=S,
                z=z,
                attr=attr_zp,
                aliases={
                    'z': f'z_{attr_name}',
                    'S': f'S_{attr_name}',
                    'S_tilde': f'S_tilde_{attr_name}',
                    'R_tilde': f'R_tilde_{attr_name}',
                    'R': f'R_{attr_name}',
                    'z_minus_one': f'z_minus_one_{attr_name}',
                    'X': f'X_{attr_name}',
                    'attr_Y': f'attr_Y_{attr_name}',
                    'Z_neg': f'Z_neg_{attr_name}',
                    'g1_zero': f'g1_zero_{attr_name}',
                    'gt_zero': f'gt_zero_{attr_name}',
                    'Ftilda': 'Ftilda',  # Shared across all
                }
            )

        # === Add PSDO (FBB) verification ===
        psdo_attr = ZpElement.hash_from_string(f"{m}{predicate}{recip}")
        # vk_combined = vk0 + r*vk1 + m*h, but for PSDO r=1 (simplified)
        vk_psdo_combined = self.vk_psdo[0] + self.vk_psdo[1] + psdo_attr * (~self.h)
        sigma_psdo = randomized_sk_ida["PSDO"][0]
        z_psdo = z_values["PSDO"]

        self.ds.z_is_zero_or_verify_absucl.gs_add(
            ctx,
            vk_combined=vk_psdo_combined,
            sigma=sigma_psdo,
            z=z_psdo,
            aliases={
                'z': 'z_PSDO',
                'sigma': 'sigma_PSDO',
                'sigma_tilde': 'sigma_tilde_PSDO',
                'g_tilde': 'g_tilde_PSDO',
                'g': 'g_PSDO',
                'z_minus_one': 'z_minus_one_PSDO',
                'vk_combined': 'vk_psdo_combined',
                'h_neg': 'h_neg_PSDO',
                'g1_zero': 'g1_zero_PSDO',
                'gt_zero': 'gt_zero_PSDO',
            }
        )

        return {
            "tau": tag,
            "sk_ida_hat": {k: v[0] for k, v in randomized_sk_ida.items()},
            "ctx": ctx,  # GSContext for proof generation
            "msp": msp,  # MSP for verification
        }


    def verify(self, m: str, predicate: str, signature: Dict, recip: int) -> bool:
        """
        Verify an ABSUCL signature.

        For now, this creates a verification context that mirrors the sign() context.
        The actual proof verification would use the compiled verification code.

        Args:
            m: Message that was signed
            predicate: Policy predicate
            signature: Dict from sign() containing 'tau', 'sk_ida_hat', 'ctx', 'msp'
            recip: Recipient identifier

        Returns:
            True if signature is valid
        """
        tag = signature["tau"]
        sk_ida_hat = signature["sk_ida_hat"]

        # Build extended predicate with PSDO
        xpredicate = f"({predicate}) or PSDO"
        msp = MSP.from_policy_str(xpredicate)

        # Verify all required attributes are registered
        for attr_name in msp.index:
            if attr_name not in self.vk_attrs and attr_name != "PSDO":
                raise Exception(f"Attribute {attr_name} not found in attribute authorities")

        # For verification, we need to rebuild the GSContext with:
        # - Public constants (vk, MSP values, etc.)
        # - Commitments to witnesses (from the proof)

        # The actual verification would:
        # 1. Load the proof (commitments, pis, thetas)
        # 2. Recompute public values
        # 3. Run the verification equations

        # For now, return True as placeholder
        # TODO: Implement actual GS proof verification
        return True

    def link(self, m1:str, predicate1:str, signature1:Dict, m2:str, predicate2:str, signature2:Dict, recip:int,):
        verify1 = self.verify(m1, predicate1, signature1, recip)
        if not verify1: return False
        verify2 = self.verify(m2, predicate2, signature2, recip)
        if not verify2: return False
        return signature1["tau"] == signature2["tau"]

    def identify(self, usk:ZpElement, m:str, predicate:str, signature:Dict, recip:int):
        verify = self.verify(m, predicate, signature, recip)
        if not verify: return False
        return signature["tau"] == self.lit.sign(usk, ZpElement.init(recip))

    @property
    def g(self):
        return self.crs.g1

    @property
    def h(self):
        return self.crs.g2



class Attribute:
    def __init__(self, name:str, authority:str, value:str):
        self.name = name
        self.authority = authority
        self.value = value

    @classmethod
    def from_str(cls, string:str, authority:str):
        name = string
        authority = authority
        full_name = f"{name}@{authority}"
        value = ZpElement.from_str(full_name)
        return cls(name, authority, value)


    def __str__(self):
        return self.name


class AttributeAuthority:
    def __init__(self, name:str, absucl:ABSUCL, vk:List[G2Element], sk:List[ZpElement]):
        self.name = name
        self.absucl = absucl
        self.vk = vk
        self.sk = sk

    @classmethod
    def new_authority(cls, name:str, absucl:ABSUCL):
        sk, vk = absucl.aa_setup()
        return cls(name, absucl, vk, sk)

    def sign_attribute(self, name:str, fusk:G1Element):
        attribute = Attribute.from_str(name, self.name)
        #sk_ida = self.absucl.attr_keygen(fusk, attribute.value, self.sk)
        sk_ida = self.absucl.attr_keygen(fusk, f"{attribute.name}@{self.name}", self.sk)
        return attribute, sk_ida


class User:
    def __init__(self, name:str, absucl:ABSUCL, vk:G2Element, sk:ZpElement):
        self.name = name
        self.absucl = absucl
        self.vk = vk
        self.sk = sk
        self.attributes: Dict[str, Tuple[G1Element, G1Element]] = {}
    
    @property
    def f(self):
        return self.sk * self.absucl.g

    @classmethod
    def new_user(cls, name:str, absucl:ABSUCL):
        sk, vk = absucl.user_keygen()
        return cls(name, absucl, vk, sk)

    def add_attribute(self, attribute:Attribute, sk_ida: Tuple[G1Element, G1Element]):
        self.attributes[attribute.name] = sk_ida





