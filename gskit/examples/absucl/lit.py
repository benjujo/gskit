from gskit.elements import ZpElement, G1Element, G2Element
from typing import Tuple, Dict
from gskit.framework import CRS
from gskit.gsfy import gsfy


class WBB():
    '''Weak Boneh-Boyen signature scheme'''
    def __init__(self, crs: CRS
    ):
        self.g = crs.g1
        self.h = crs.g2

    def keygen(self) -> Tuple[ZpElement, G2Element]:
        sk = ZpElement.random()
        vk = sk * self.h

        return (sk, vk)
    
    def sign(self, sk: ZpElement, m: ZpElement) -> G1Element:
        if m == -sk:
            return None
        exp = sk + m
        sigma = ~exp * self.g

        return sigma
    
    @gsfy(witness=['Ftilda'])
    def verify_absucl(self, Ftilda: G2Element, m: ZpElement, tag: G1Element) -> bool:
        """
        Verify a WBB tag in ABSUCL context.

        In ABSUCL, Ftilda = usk * h is the user's secret key in G2 (witness).
        The tag = 1/(usk + m) * g.

        Verification: e(tag, Ftilda + m*h) = e(g, h)
        Rearranged:   e(tag, Ftilda) + e(tag, m*h) = e(g, h)
        As PPE:       e(tag, Ftilda) + e(tag, m_h) + e(-g, h) = 1

        Where m_h = m * h is precomputed.
        """
        m_h = m * self.h
        g_neg = ~self.g

        # Note: h, gt_zero are reserved CRS constants (auto-available)

        GS_STRING = """
        variables:
            Ftilda: G2
        constants:
            tag: G1
            m_h: G2
            g_neg: G1
        equations:
            tag * Ftilda + tag * m_h + g_neg * h = gt_zero
        """

        lhs = tag.pair(Ftilda + m*self.h)
        rhs = self.g.pair(self.h)
        return lhs == rhs

    @gsfy(witness=['vk'], aliases={'signature': 'tag'})
    def verify(self, vk: G2Element, m: ZpElement, signature: G1Element) -> bool:
        """
        Verify a WBB signature (original version).

        In ABSUCL protocol, 'signature' is called 'tag'.
        Both witness and aliases are defined together in the decorator.

        Note: This uses complex expressions not supported by grammar.
        Use verify_absucl for ABSUCL integration.
        """
        GS_STRING = """
        variables:
            vk: G2
        constants:
            m: ZP
            signature: G1
        equations:
            signature * (vk + m*h) = g * h
        """
        lhs = signature.pair(vk + m*self.h)
        rhs = self.g.pair(self.h)
        return lhs == rhs
