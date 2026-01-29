from gskit.elements import ZpElement, G1Element, G2Element
from typing import List, Tuple, Dict
from gskit.framework import CRS
from gskit.gsfy import gsfy


class FBB():
    '''Full Boneh-Boyen signature scheme'''
    def __init__(self, crs: CRS):
        self.g = crs.g1
        self.h = crs.g2

    def keygen(self) -> Tuple[List[ZpElement], List[G2Element]]:
        sk = [ZpElement.random() for _ in range(2)]
        vk = list(map(lambda x: x * self.h, sk))

        return (sk, vk)
    
    def sign(self, sk: List[ZpElement], m: ZpElement) -> Tuple[G1Element, ZpElement]:
        r = ZpElement.random()
        exp = sk[0] + r*sk[1] + m
        while exp == ZpElement.zero():
            r = ZpElement.random()
            exp = sk[0] + r*sk[1] + m
        sigma = ~exp * self.g

        return (sigma, r)
    
    def verify(self, vk: List[G2Element], m: ZpElement, signature: Tuple[G1Element, ZpElement]) -> bool:
        sigma = signature[0]
        r = signature[1]
        lhs = sigma.pair(vk[0] + r*vk[1] + m*self.h)
        rhs = self.g.pair(self.h)
        return lhs == rhs
    
    @gsfy(witness=['z', 'sigma', 'sigma_tilde', 'g_tilde'])
    def z_is_zero_or_verify_absucl(self, vk_combined: G2Element,
                                    sigma: G1Element,
                                    z: ZpElement) -> bool:
        """
        Prove: z = 0 OR FBB signature is valid (ABSUCL version).

        This is the ABSUCL-specific version where:
        - vk_combined = vk0 + r*vk1 + m*h is precomputed
        - sigma is the signature (witness)
        - z is the selector (0 or 1)

        The equations prove:
        1. sigma_tilde = z * sigma  (MS1)
        2. g_tilde = z * g  (MS1)
        3. e(sigma_tilde, vk_combined) + e(g_tilde, -h) = 1  (PPE)

        If z = 0, all equations trivially hold.
        If z != 0, reduces to FBB verification.

        Witnesses: z, sigma, sigma_tilde, g_tilde
        """
        # Compute z-blinded values
        sigma_tilde = z * sigma
        g_tilde = z * self.g

        # Constants for equations
        z_minus_one = ZpElement.init(-1)
        h_neg = ~self.h  # -h for the equation
        g1_zero = G1Element.zero()
        gt_zero = self.g.pair(self.h) * ~(self.g.pair(self.h))  # Identity in GT

        GS_STRING = """
        variables:
            z: ZP
            sigma: G1
            sigma_tilde: G1
            g_tilde: G1
        constants:
            g: G1
            z_minus_one: ZP
            vk_combined: G2
            h_neg: G2
            g1_zero: G1
            gt_zero: GT
        equations:
            z * sigma + z_minus_one * sigma_tilde = g1_zero
            z * g + z_minus_one * g_tilde = g1_zero
            sigma_tilde * vk_combined + g_tilde * h_neg = gt_zero
        """

        # For local variable capture
        g = self.g

        # Standard verification (for return value)
        lhs = sigma_tilde.pair(vk_combined)
        rhs = g_tilde.pair(self.h)
        return lhs == rhs
