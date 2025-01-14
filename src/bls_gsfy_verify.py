from gskit.framework import CRS, Equation, equations, verify
from gskit.utils import NamedArray, UnamedArray
import numpy as np
import gskit.elements as elements

crs = CRS.from_json({'u1': ['eJw9jT0OwyAMha+CmBnsBBvoVaoKJVW2bLSVqqp373OgGcDW93788bXe96W1Wv3F+fX92JoPDvS17M/toNdYgpMcnGpwBTNhMvP5xY4SJCbTCFgIZDxNXS2YOY8IE2oz2WIF1kRz98rU8wKoMqxM1mIq7BlULY9zcbbGaeSZjwP6Tw6jyu37A0eOMCE=', 'eJw1TkEOwyAM+0rEOQdoCYR9ZapQN/XWG9ukadrf5wC7OInj2Pm4Wu/n3lqt7kLu9n4czTGBfe3n8+jsNRYmUaa8MKlnCl4wJKaSMYQVTWcBGowxPVYax0aXOedRg8etpKn2pl7tDBFxxgQfR1bRqc9okv5vAIIn1BZlmNkzEqdhN1Nz9YAk2/cHvwgvsQ=='], 'u2': ['eJw1jrEOwjAMRH/FypzBbrHj8CsIRQV161ZAQoh/59yEIVbu+c72J7V235Z9by2dKd3ej3VPmUBfy/ZcD3o51UzqmUwzlSmTiEaRTLWAxGM4OKBHKd3rMwQDW40Pkna0gVWCWChglzGYYxaExwLWEZcJvTL3dc7/A1g6detHKFwKXawf49jqI2l2/f4ADbEv2w==', 'eJw1jEsOwyAMRK+CWLOwKWDoVaoIpVV22ZFUqqrevWMIi/Hn2TNfW+trX1ur1d6NfX6OrVlnQN/rfm6dPkJxJmZnhCF0Zg+AJd8gnZMzBU8S9CgY/PhmAimkVH0UtaSrRBlxIgrKpHCEvtAkUI6jM5dp0EvP02SP5+hHXoDy5WHyWmBIafn9AXvqMF4='], 'v1': ['eJxFUEEOAjEI/Eqz5x5Kty3UrxjTrGZve1s1Mca/O9CuHqB0YGDgPbV225Z9b206uen6uq/75B3Q57I9VkPPOXiXxTuevUt4iao6BlK8EyAZGY4wSyCQogF4SZFIKEkwoCXDrAwA88GpvRHFqG4Qi3SeDqYAJ9wV1NpjTeoopv9LQRlqWRvDCSzHo3lQOMhwkg6NyJXRXhBXaKj4yzw0cy/WRlIHKVAXKXirXcaUhjFGa3jsq71Mmm1nu9JQ/LuAqbXDWM4wm02XzxcfNVIH', 'eJxNUMtuwzAM+xUjZx+s+CGrv1IUQVfkllu6AcPQfy9pq8AOtiWKEin/Ldv2OO7nuW3LJSxfv8/9XGIA+nM/vveBXmuKofYYVGKQVHgpEKAdqPE1gIKrr6wi0BxDUaLgNwRq8xVp6EVVKxNcFT2mDiRWABTSOxlIOvvWoQ6O2SwPOyJTvYrbEkmuvNIYxFTnSPIVecluj+NTYgui1ph130Mku9WhYD5qMM0+tmwmw292xbE9ndfiqyHuMh3SF218PqTnf/9Gn2N/F1evNR65vd6geFJB'], 'v2': ['eJxNUEEOAjEI/ErTcw9tt6XUrxjTrGZve1s1Mca/O7Ss7gECA8wAb9vabZ23rTV7Mvb6ui+bdQboc14fS0fP2TuT2RkiZ1JBnJ0pyPPkDAcY8BClKQ2rFYAHmtHNPREXpDdLALiIRQBFyiwOpYoggZaKAsRjpreykoSILCGrQgJhqmOE/UEh7SpqotS5SbmDl8q07xCP7JTHKcEnhaVRLh6HdTSqiP+LjMJPRe+Xh8in+nxgXbAz6Wv0dhnnuG/jp7EIhcvnCxYjUeo=', 'eJxFUDuuAjEMvEq09RZxEscJV0FPK0B0dAtICHF3ZhI/Ufg3/o39Xrbtcjvt+7Yth7CcX/frvqwB6PN0e1wHetS4Bm1rMFhJCSraGnqn43ADWs0BSUSQrhVZ2NKmr5DmHUbLOMMqamzWVPhWgKOmcoVgtEFU5zCRPqe3ERQqpFr9RwZBpSoOjYhtJpgjv+USCSSvlUjebOKqPDmYTb4K23hhEr+QbzH19eoUeCrLenMqJc8Znc+L2T/Iazl9lJCj5il8JFcNuvxFlb/PF9QaUTI=']})

c = NamedArray([])
d = NamedArray([])
c_prime = NamedArray([])
d_prime = NamedArray([])


eqs = equations()
const = {}

signature = [elements.load_element('eJw1jsEOAiEMRH+l4cyBstCCv2IMWc3e9oaaGOO/O92Fw7TlZTrl61p77GvvrbkLufvnuXXnCfS97q/toNdUPeXiSaAimBd0sIQ3c0YJkyxG0ihZPVXzBAyFPanBiCCdthgHga2CqpxrJkVyMWeoZrf4IdvgwEbLPMHn9WzdApCuPL4mcvv9AcnTL7A=', 1), elements.load_element('eJwtjksOwjAMBa9iZZ1FHJqPuQqqooK66y6AhBB3572ki9jOeGT761p7HFvvrbmruPvnuXfnBfS9Ha990NtiXlL1krOXiqy6IAT8ivKHdiHRyABsBSSdckgMEM1mJ7EDv168cDRzyZQCijIBXzbOA7TAos41xkwQ43kFPQ4dyjigYl216aoqT19/fyofMCE=', 1)]
c = c.append('signature', signature, True)

g2 = elements.load_element('eJxFUEGOAyEM+wqaMwdCgUC/UlWj2VVvvc1uparq32uHjHqAmdiJ7fBa1vX3vu37ui7nsPw8/277EgPQx3b/vxl6qSmG2mNoIwYR/HQcbTEUBXFCjQbJQlYmIsmugqqQyw4NTGj3okNvUC67doZOU8q0iQ5rhaYyAoBe8aVGdceKUyjM0cbR7JceecyLA735UAdQxrQwU4bUdvQLehV05YwJdN8j1eMFyrSeW6c0lzEtC8/gxV/JaBGdQWv+sgxNkzHcVcSTiSRfkuH5OE2u7w8YXFJb', 2)
const['g2'] = g2

rhs = elements.load_element('eJxNVstu3DAM/JXFnvcgyZIo9VeKYpEGueW2aYGi6L9XMxzKPsRry3wMh0M6f+/P5/vn2+v1fN6/3e4//3x9vO6P2zr9/fb564On31t+3Np43Ppcv/1xy3k95NRwtx5HxtOBJ1tG67hOnCRdcJLTMprLbSQZVwv3ddrqMkPkssxsmRjDrTBWlh/DMfGhxIAER9rAmzc5rbu2XvcVfNAB2DJzmlxxzop4WlTOQFDzfCdY+kylYoTCYocAoQhHlx3GTM5HXUBHcSZakUszuTWUUdKFLBQGQKMJr8kenJPAvC7W/cWozhKaYYAA4FXEkg2kQ+A+nAyEAPV4BjbiMhFVPQ3eW/OiRjttQBbRTjv/1HAiQ8JSordioM/9PkeR7QRiQS0jtyZP5Gc1KWKKSNoCuSk+/WCOwhENNKM8/A5lYQjSDpCgjh5ZqBAcMdnCHMrEE/kQB7Caaff+kG79zh8PyQNm1FVWDf5QPQja1YSayutt5+0uzFH3ZM2Q6CFrSjS5GC0yujHk52MWdG2sFXqZThFAQOD4GyXEzmwaM3AP4ug1ornUO3u5U8YuYD+3Ri1GKonqqVluoRZImAkODYYnSGo5cECTmD6L3iXNp2oNzaHxvkXKqQSMrPe36obzGzNWj7MFiO3SqjF0Mfy+hyxk2kR4CYhoE9uQpCSTOkeMuC+VQxFyv0ohqphbobHNnLvi/DOTr9GcrkyRb4nFBTOdWK8khTgRlsfMOgWKF1aaz/ZPda+pZvAPbtvWeIrVS4Io4SyjbhtnjFqPLQfkI1aCdscIZ2fWXElzb+msHlKiWfCCYV+307tNeeVN+RUwpglVNCV3+kMHbhL7SPO5d4KoDm001cBupxw9ldr8IxZtYHQAbzrlZ23nnRtF0f7eX0///sUa5b6doY/jUrM3cu7dY7EnQlHsb/XI/I0PXT2dgkRfLIfy2B6TeZUHdTS8rLFlwDa3qNj2coiZQ6erFpDTGF+F1C4l07PEhjfNpMUbl10P0fTLsoP0LE5N/weMvVdaTFFsW13i+5Hyj3//Abzvn2c=', 3)
const['rhs'] = rhs
pis = [
    UnamedArray([
        [
            elements.load_element('eJyrVoqPT85JLC6Oj1eyUlBKqixJLVbSUQCKliXmlKaCRaNNDXQUTC10FMxMRzHNsGFsLQAje0zR', 2),
            elements.load_element('eJw1UEkOwzAI/IqVsw/G8YL7laqK0iq33NJWqqr+vcOSgzEMMAx8p2V57OtxLMt0CdP989yOKQag73V/bYpea4qhcgwdPyUJOh7FMAYAmmPgjGwFCL+zJeVv7jN+yiQmWYaVq4hBLw9PUVIvC6+So6JrRN6jVSQCmsOqQHtqlegsV/oGaKC6ga2jo2sCRpZiaSQlFKHZZg320nbqlVIylZIkarZE8ae3YBskInVdGdJFPsCCzjLbjXxrRLX4kNSMvLDr0ftlmyrKG91+fxOwUdU=', 2),
        ],
        [
            elements.load_element('eJyrVoqPT85JLC6Oj1eyUlBKqixJLVbSUQCKliXmlKaCRaNNDXQUTC10FMxMRzHNsGFsLQAje0zR', 2),
            elements.load_element('eJxVUEsOAiEMvQqZNQuKQFuvYgwZzexmN2pijHe3pR2NCz7lffrKa+r9us7b1vt0DNPleVu2KQZ5fczrfRmvp5piqBQDQgwsJ0sNQLodBMEYCnsBIJwil8bOoWywnihCEgIkRbNWTQyS03NWDbtLVYE6qQmaGFIzABIZWqsW2X1BOLhnIYFqUVjVwxtdCansrYZRsqXBURDmnxq148j8nVpD2MRonPEpHmifkYp5aVpiGwFATIv/JCXP8WeF3ro1D9i0gPP7A9xQUco=', 2),
        ],
    ]),
]
thetas = [
    UnamedArray([
        [
            elements.load_element('eJyrVoqPT85JLC6Oj1eyUlBKqixJLVbSUQCKliXmlKaCRaNNLHUUTC10FMxMhxKOrQUAb6wtaQ==', 1),
            elements.load_element('eJyrVoqPT85JLC6Oj1eyUlBKqixJLVbSUQCKliXmlKaCRaNNLHUUTC10FMxMhxKOrQUAb6wtaQ==', 1),
        ],
        [
            elements.load_element('eJyrVoqPT85JLC6Oj1eyUlBKqixJLVbSUQCKliXmlKaCRaNNLHUUTC10FMxMhxKOrQUAb6wtaQ==', 1),
            elements.load_element('eJyrVoqPT85JLC6Oj1eyUlBKqixJLVbSUQCKliXmlKaCRaNNLHUUTC10FMxMhxKOrQUAb6wtaQ==', 1),
        ],
    ]),
]

eq = Equation([], [g2], [[]], rhs, 3)
eqs.append(eq)
v=verify(crs, eqs, c, c_prime, d, d_prime, pis, thetas)
print(v)
