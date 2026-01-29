from gskit.elements import ZpElement, G1Element, G2Element
from typing import List, Tuple, Dict
from functools import reduce
import operator
from gskit.framework import CRS
from gskit.gsfy import gsfy


class RPSPS():
    '''Ghadafi PSPS scheme
    ref: '''
    def __init__(self, crs: CRS, N: int=1):
        self.g = crs.g1
        self.h = crs.g2
        self.N = N

    def keygen(self) -> Tuple[List[ZpElement], List[G2Element]]:
        sk = [ZpElement.random() for _ in range(self.N+2)] # sk = (x, y_1, ..., y_n, z)
        vk = list(map(lambda x: x * self.h, sk))

        return (sk, vk)
    
    def sign(self, sk: List[ZpElement], message: Tuple[Tuple[G1Element, G2Element], List[ZpElement]]) -> Tuple[G1Element, G1Element]:
        x,*y,z = sk

        U = message[0][0]
        V = message[0][1]
        m = message[1]

        r = ZpElement.random()

        R = r * self.g

        my_sum = sum([m[i] * y[i] for i in range(self.N)], ZpElement.zero())
        S = ~z * (r*U + (r * (x + my_sum)) * self.g)

        return (R, S)
    
    def verify(self, vk: List[G2Element], message: Tuple[Tuple[G1Element, G2Element], List[ZpElement]], signature: Tuple[G1Element, G1Element]) -> bool:
        X,*Y,Z = vk

        U = message[0][0]
        V = message[0][1]
        m = message[1]

        R,S = signature

        if U.pair(self.h) != self.g.pair(V):
            return False
        
        lhs = S.pair(Z)
        rhs = R.pair(V) * R.pair(X) * reduce(operator.mul, [R.pair(m[i] * Y[i]) for i in range(self.N)])

        return lhs == rhs
    
    @staticmethod
    def randomize(signature: Tuple[G1Element, G1Element]) -> Tuple[G1Element, G1Element]:
        R,S = signature

        r_prime = ZpElement.random()
        R_prime = r_prime * R
        S_prime = r_prime * S

        return (R_prime, S_prime)

    @gsfy(witness=['z', 'S', 'S_tilde', 'R_tilde'])
    def z_is_zero_or_verify_absucl(self, vk: List[G2Element],
                                    Ftilda: G2Element,
                                    R: G1Element,
                                    signature_S: G1Element,
                                    z: ZpElement,
                                    attr: ZpElement) -> bool:
        """
        Prove: z = 0 OR RPSPS attribute signature is valid.

        This is the ABSUCL-specific version where:
        - Ftilda is the user's G2 public key (shared across all attribute proofs)
        - R is public (the randomized R component)
        - S is the witness (randomized S component)
        - attr is the attribute value (as Zp element)

        The equations prove:
        1. S_tilde = z * S  (MS1: G1 = Zp * G1)
        2. R_tilde = z * R  (MS1: G1 = Zp * G1)
        3. RPSPS verify: e(S_tilde, -Z) + e(R_tilde, Ftilda + X + attr*Y) = 1  (PPE)

        If z = 0, all equations trivially hold (S_tilde = R_tilde = 0).
        If z != 0, the equations reduce to RPSPS verification.

        Witnesses: S, S_tilde, R_tilde
        """
        X, Y, Z = vk[0], vk[1], vk[2]

        S = signature_S

        # Compute z-blinded values
        S_tilde = z * S
        R_tilde = z * R

        # Constants for equations
        z_minus_one = ZpElement.init(-1)
        Z_neg = ~Z  # -Z for the PPE equation
        attr_Y = attr * Y  # Precompute attr * Y as G2 constant
        g1_zero = G1Element.zero()
        gt_zero = self.g.pair(self.h) * ~(self.g.pair(self.h))  # Identity in GT

        GS_STRING = """
        variables:
            z: ZP
            S: G1
            S_tilde: G1
            R_tilde: G1
        constants:
            R: G1
            z_minus_one: ZP
            Ftilda: G2
            X: G2
            attr_Y: G2
            Z_neg: G2
            g1_zero: G1
            gt_zero: GT
        equations:
            z * S + z_minus_one * S_tilde = g1_zero
            z * R + z_minus_one * R_tilde = g1_zero
            S_tilde * Z_neg + R_tilde * Ftilda + R_tilde * X + R_tilde * attr_Y = gt_zero
        """

        # Standard verification (for return value)
        lhs = S.pair(Z)
        rhs = R.pair(Ftilda) * R.pair(X) * R.pair(attr * Y)

        return lhs == rhs
