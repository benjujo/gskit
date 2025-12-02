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
    
    @gsfy(witness=['vk'], aliases={'signature': 'tag'})
    def verify(self, vk: G2Element, m: ZpElement, signature: G1Element) -> bool:
        """
        Verify a WBB signature.
        
        In ABSUCL protocol, 'signature' is called 'tag'.
        Both witness and aliases are defined together in the decorator.
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
