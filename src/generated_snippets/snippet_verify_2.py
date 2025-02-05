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

v0 = [elements.load_element('eJw1jk0OAiEMha/SsO4CGEqpVzGGjGZ2s0NNjPHuvsq4INDv/ZR36P22r2P0Hk4Urq/7NgIT6HPdH9uPnosxSWOqypRyZmoLjgOZUPFO0WFhKu6KFQpoi1CRMFSkBMVcTcvMit9wSnVos0jT4WigKj4caxwYHFJmqWTfhFi12dH+H9RlDqq+4PL5AkIqL0w=', 1), elements.load_element('eJwtTssOAiEQ+5UJZw6U5emvGENWs7e9oSbG+O92gANpp9N2+JrWHufee2vmIub+eR7dWKH63s/XMdRrqFZisZKdlQJi4BzJ3eRV0VsBspWgj4HCQOQiBl2QwPlpH45tcoA98NB1na2AntpUGbIyYJbpRYC5XJYRqMuZxw12Z/0aMTKZ6rKkdPv9ATnQMAg=', 1)]
c = c.append('v0', v0, True)

v1 = [elements.load_element('eJw1jkEOAyEIRa9CXLMQKzj0Kk1jps3sZudMk6bp3QtqFyB5n//xE2p97mtrtYYrhMf72FpAMPpa93Pr9JYVgRcEEQSiiLCQlb1ikKLRkqzUVUbIRvmCoGWqGl3JY40SObamOhKK7WbfJWvSB51Oim5NfpL/GTZwGsCD/XMyi/vFMn2eS0QzT/j+/QF4rjBS', 1), elements.load_element('eJw9jrEOwyAMRH/FYmawCRjor1QRSqts2WgrVVX/vWeSdMCYd3c2H9fafVt6b81dyN3ej7U7T6CvZXuug15j9ZSKJ82eJAiKWMcTUPJU8VBYChsMaEwVqBGhDKB245S4M5FqVmTLmGaFzTOC1oBUPj35v9GMgfdhwgpNj50iemanQxfeswlKsl/o/P0B3+4wuQ==', 1)]
c = c.append('v1', v1, True)

v2 = [elements.load_element('eJwtjjsOAjEMRK9ipU6Rn/PhKmgVLWi77QJICHF3ZkIKO8r4eTwf0/v93Mfo3VzE3N6PYxgrUF/7+Tymek3NilYrJVpJKO8zG1QfnJUaMMK4JggOTQs++mc5nC/LE5i7oAqoAo8MISvFuAynf0U1IAqDXLkYV2sTCcsrkXErT2IMJuUR51cUHtHt+wMYKS/6', 1), elements.load_element('eJw1TUsOAjEIvQrpmkVxWqBexUya0cxudlUTY7y7UHQBeb+89069345tjN7TGdL1dd9HQjD1uR2PfaqX0hCqIsiC4FgzAjMC0cmfIDRz2a8aNlfcyBbXmTAg+lOdVC+womYnOcxZTDGiiwdLEMolJil73NZU/oSjx2M+PdeyvWqGUKSZ188XNR8vKQ==', 1)]
c = c.append('v2', v2, True)

v3 = [elements.load_element('eJw9jjsOAjEMRK9ipXYRZ/PlKghFC9puuwASQtydsTdQjBI/jz1+u95v+zpG7+5E7vq6b8MxgT7X/bEZPcfGlCpTThDeKlBkEslMTQEa4gNTWfAJHqQoAS5ot6YFWtloPbZE82KoQjlPv8hyLDev+D8OP7ceo+EeIwVKMo1J49r0HgdYsC0Szbh8vuD0MLI=', 1), elements.load_element('eJwtjkEOQiEQQ68yYT0LBhlgvIox5Gv+7u9QE2O8ux1hUWjKS+kn9H4/tjF6D2cKt/djH4EJ6Ws7nvs/vWRj0sZUE5NIhBGmhrtlCL7CG4B8YiqAc3VQJ2h1gXhUqJYpiw6ZH+hVmRJZfSJeEt3FtKKUVp59DToL/ijo8oXN5j+qc6k6HH1RuX5/UykvKA==', 1)]
c = c.append('v3', v3, True)

v4 = [elements.load_element('eJw1jsEOAiEMRH+l4dwDJdsC/ooxZDV72xtqYoz/bgd2D23KzPSVb2jtsa+9txYuFO6f59YDk6vvdX9tQ70ulUkLk3lJXJiKC5aZsrggoxlahZ+YFg+qei4elp0PuMUFlYnLSNrUQCteCkKeXh4nfbNiEMdIwr3ok9nhFQTTXMZfkQWg1gk3vf3+jvgvgQ==', 1), elements.load_element('eJxNjr0OwjAMhF/FyuwhbuP88Cqoigrq1i2AhBDvzjnJwHK5nO+T/XG13s+9tVrdhdzt/TiaY0L62s/n0dNrKEyamWLEm5jCyiQiTAlGFwwwlAVGvGcqVgGSA6azFSYek6HBZJ2SgKiOquJf/Kh1HHnqSDHpLo/Iaob2lRr+LrJdOi8TDxN1+/4Ag2AvUA==', 1)]
c = c.append('v4', v4, True)

v5 = [elements.load_element('eJw9jcEOAiEMRH+l4cwBENrirxhDVrO3vaEmxvjvThfWS9uZTuZ9XGv3bem9NXcmd3s/1u48wX0t23Pd3Uuunop6YvFUsU0Ldg2eYkoYISOBQ9JwBclSPCl0lpmMEGzmCc+/IfOw6F6u1oeIgqLZBD4FBx/YozAYiUeZGjFOOltnGDQu1+8PA4Eu5g==', 1), elements.load_element('eJxNjrEOwjAMRH/FypzBpomd8iuoigrq1i2AhBD/zjkNEoMt5/x8l3eo9bavrdUazhSur/vWQiSoz3V/bF29pDlSLpGMUZiFM5oYXlCLHiUyYThFUoizuQDVgKrjzAeuMDBBJdBOurkOv+R+ADP7RY9yj+mXgHUCluXvxk38V2YjSXS04tuev3y+odovqw==', 1)]
c = c.append('v5', v5, True)

v6 = [elements.load_element('eJwtTssOAiEM/JWGcw90txTwV4whq9nb3lZNjPHfnQIHhuk8Ct/Q2uPYzrO1cKFw/zz3MzBBfW/Ha+/qVStTKkxZcC9MIjoGkQiIsHRlqpmpgNfqTreT2+oAVn2FIYtcBrc0uERzWGYbp6Bc1pHqhq/OOpcVf93TeboiAOuT51BMOtX+lwjF7Pb7A01nMDM=', 1), elements.load_element('eJw9jUsOQjEIRbdCOu6g9AOtWzGmeZo3e7OqiTHuXSjVAb9z4fJ2vd+ObYze3Qnc9XXfh/Mg9Lkdj33Sc24eSvVAGuwBMWiKQmWqorKANpUkQAQmEYuEzrgEDE07dSNzUinPO/rbVl3MshPsY0kLzMTRvrGaRrRGrTj9QLXbtqoKVC6fL+emL7M=', 1)]
c = c.append('v6', v6, True)

v7 = [elements.load_element('eJw1jcEOAiEMRH+FcOZAsaXgr5gNWc3e9oaaGOO/O2XZQ9vJ9HX69a099rX31vzV+fvnuXUfHNz3ur+24d64BiclOL2gMIkgKCW0aCrm4LKiMBlGYcxqCzI4TWScseWArfFgiegMxYWCFaCKbRYkxSOZEoSwBdX5tUBUnY/FTONPwTox+6MDWX5/QpwwHQ==', 1), elements.load_element('eJxFjs0OwjAMg18l6rmHZnT94VUQqrZpt90KSAjx7tgZsIsVf3abvFxryzb13po7i5uft7U7L6CPabuvRi+xehmLl5S86DBAFK5+STFwSN5x5qMTYngNEQP6GY1qIFDKXtFgQq78EOUcaRR5+ueYeMnh+NZyW8wd4+8CLlNlW1FKGLLddX1/ADzzMQw=', 1)]
c = c.append('v7', v7, True)

v8 = [elements.load_element('eJwtTksOAiEMvUrDmgUtv45XMYaMZnazQ02M8e6+Agug70u/rrXHuffemruQu3+eR3eewL7383UM9po2T1k9leyJGUCNqAASMOAUA8xQxFMFUeN8EwQtEIOYXSbS5WQGyIs0q8WY4wSj3YakVoBM5tmaYa9Ypm4mBLtGEJTG9aHIWtbMpdx+f+HpL7I=', 1), elements.load_element('eJxFjrEOwyAMRH/FYmbADRjcX6kilETZstFWqqr+e88pqAP26fzs4+1q3Y6ltVrdldz6uu/NeYL7XI7Hfrq3qJ5S8ZQvnjR7KqbhCTqHhMKY5IjHcAU92ASm6BBgU+goMxg9mTDEZAXHI8AifUstaSTivmRbBqr6DxL8IHG/mqcfyVz6xMJl/nwBvmovow==', 1)]
c = c.append('v8', v8, True)

v9 = [elements.load_element('eJw1jrEOwjAMRH/FyuzBbp0m5VdQFRXUrVsACSH+HV8Shkjnd86dP6GU+7nXWkq4ULi9H0cNTE5f+/k8Gr3ayhQzU5qZVNcucnKo/hYmg2nODAvRhTgYP2KDGFI3Vtcq2EIMBkUGSgTOxLTEv9MqkSA2PJUEJiNEBUe4SDKSWpnN/QKdHOeIyO37A35vMEs=', 1), elements.load_element('eJw9jrEOwjAMRH/FyuzBbpPG4VcQigrq1q2AhBD/zjkJDLF1zz5f3qHW274eR63hROH6um9HYAJ9rvtja/QcC1Mypix4M5NKZioQMbvwycS0mIvIZGOSAFX/ReRXJpSkzks/qgIV4U+wGaCht1T03DYXBCRAxJexoOIwD6f2ULO+pKrjOyqzey+fLwqUL9s=', 1)]
c = c.append('v9', v9, True)

v10 = [elements.load_element('eJw9UEtuAyEMvQqaNQtMwMa9ShWNkii77CatFEW9e/2wyWIYY78ffm/7fntcjmPft6+0XV/P+7HlZN3fy+PnPrvfveTUR05COTWxuuc07E9kh9g32C5Fc+KBLqAFheGkGZ4wZidPEttlYHJaKgalWnHADAVROJ2iKyiKHWLjUYMgZtvZw8HeuabdDMkaFCowKHOmHm/qIuswpqLRQ6264ketIj/xSugqU098EQobMj1sSiVMugSDxZ+uI2AeCSFFV6IWm2i6LEpbC8VmzY/p/PcPGslS/g==', 2), elements.load_element('eJxNkEEOAiEMRa9CWLOgONDWqxhDRjM7d6Mmxnh321KSWQwD/N/XX76x9/tj3ffe4znE2+e57TEFuX2vj9dmt5eaU6iUAoJ8JYVF9rWmANBkyaJCUWlJgdqwNJNZNmop+XjK4kPRK4rfsXSaom7IDQrjYWBWsY0OJGJDZda5ZDnipC9KBm3sUUj+6A4lEs9UWkd5IK3WRjF4nroOZLNqWgBJiNlfQOM6SI6MB1DT5DRTlzGSFbBXk7YD8p5Mngvm+1mSOkgNrr8/7zlSZg==', 2)]
d = d.append('v10', v10, True)

v11 = [elements.load_element('eJw9kEtuwzAMRK8ieK0FGZsinasUgZEW2WXntkAQ5O6dMZkuKFLDz6P0nLbt637d922bzm36fHzf9qk3qL/X+8/tUD9MerPobQx4782X3vQEcRgCnXlopU64CPIGc/bRLEtZcBi0QMPKGD7m1FfoTgYswHPLGSorD69K5WUQCtlIF1KVlWq1GnccUUUqWhtxsufkyqzFRM8yp09RchGfMz4WwoiwN4ZALuPOFrLEiuXFIGuJbA6p5L8o9Xse7zfqKCmW/LIBdejl9QclCVFU', 2), elements.load_element('eJw1UEFuwzAM+4qRsw9WainyvjIUQVv01lu6AUWxv4+01ANjSSYpOu9l32+Py3Hs+/JVluvreT+WWjD9vTx+7nP6ra0W9VoM6KOWDfAVp9YyUEvDp28oBBM94YboqAE/kcGBgMVmbUmnjubSLDkiLR16uHCfKm8pWCVVBoECNoLK00kTMDZQN+TzniT0ukbmuU64TjA1SHx6aqZwj3eJeKQdHoY+ojdLeneyMh5NPr8mUk77ESum2dw681oKmVFaDwcb2Uw5n05Pqk3Of/9XxVGJ', 2)]
d = d.append('v11', v11, True)

v12 = [elements.load_element('eJw9UEEOAiEM/ArhzIGytAW/YgxZzd68rZoY499tadcDu53pTKfwiWPc7uu+jxFPIV7fj22PKQj7Wu/PbbJnzClgS4EwhQYpdE6BBfMiWOre5a9YelBKCnUxQEJCVhayVq4lOayeSZIAVKMgLspkiwAgG6G6tlg2Hh6U08hVlT0dpMDFIrqmg4zu6ingH2bbtjabysdt0LfHYg21aZzOYfLFVDX3B99DlTP2753L0MHC7Be/ILI9mzFQhZGBXM01n6m7RG+rSQSX7w8RZVFJ', 2), elements.load_element('eJw9UMsOAiEM/BXCmQNFKOCvGENWs7e9rZoY47/boXUPPDrMMJ1+/Bj3bdn3MfzZ+dv7se4+OEFfy/ZcJ3opMbjSgqun4JiD613uUlOssqUUXDsp2uQ1/1+qLAaDSPSyKphVVxEF/iWSosulwYQhBdsYRNE+7ngp2ATJEGdBCYD4taZ2Kp60ZB7JitnN/OUQRu2vylmzJenonpqhxVoALVdLzpoT92J2SILJIECfqVjHdbg1yw4WT4+icqKszSEQH01i1MJgun5/ECVQuw==', 2)]
d = d.append('v12', v12, True)

v13 = [elements.load_element('eJw9UMsOwyAM+xXEmQOhPPcr04S6qbfeuk2apv374gR6AFLHsZ1+be+PfT2O3u3F2PvnuR3WGUbf6/7aBL0m70yqzuTkTC3ORK5r1Zco8OUjI4RiAcRXk147IWYVgZhVmU0BcwRF7sNBlMH1ecoSVwVkXzCBGGUcWLB6TYOW26SpKQ0v8QFLDmuleLaLfsG4tmGAAtlBh0nJmpBozEaRDzNYm6sE0hCqj+Ck+5SkUbE+lNOMpsxlKs0k/OasPthUGPjzmW6/P4XbUrQ=', 2), elements.load_element('eJxFUEEOwjAM+0q1cw9L17QpX0FoGmi33QZICPF3nCaDQ9vEcRyn72Geb9uy7/M8nMJwfd3XfYgB6HPZHmtHzzzGwBJDqTEQIaGR9ZpiEFIIeMMpxes1a7khAIVxKmitN2olqR4UpCNoKs35RGKakkDJrp/Sr6zpSIeDhKhWV9SWwjZP3ZgyAsGbxU3gZeQ1GUlr3NdqRm7NJ9iy2cyJ+EhdSG2rFrMPsa26gvgOTIeJ35+l/8d1+qRRx8S7+5Un+8hyoJwOcfQWuny+CblTgg==', 2)]
d = d.append('v13', v13, True)

v14 = [elements.load_element('eJxNUMsOwjAM+5Wq5x2a0ie/glA10G67DZAQ4t+xm1bikC51bcfLx7Z239fjaM2ejb29H9thFwP0te7PraOX6BYTy2Kyxxe9eMHhiJzQSEVDRMJ4F6dkcXkxtSOiHAoqhMUPmngcKQKFS+EgMKJoiZtakTwMWOgTqkBWSA8qFRdGrpTYYEZ2Yybp3THqpXNDUUOGLpVT4hzqqoYMeQbVLFxBN2eO+ucjHk+pjKidGKoOJ0oRi7/a805JBpCTzu8+3CJ3lvLYLSVJrt8fPkpR5g==', 2), elements.load_element('eJxNULsOwjAM/JUoc4a4rWOHX0EoKqhbtwISQvw7fqSFIa19uTuf846t3dZ521qLpxCvr/uyxRQEfc7rYzH0jDkF5BRolP+QAuQqhYAkIE9yQA7phTBYGIjSQNFP76pICju1slJFV8gbJWjN3D1qdgVkdcbuY1cA1gqO5AlIE3QRDOCg0yyPIvkfAaCjAh9E5Hrdwmpj8F4U37fwngRG1+H02wCycLEc/uQUrh7PXACqBz4mdz9brz+pzxPSVD1+0feBy+cLSilSoQ==', 2)]
d = d.append('v14', v14, True)

v15 = [elements.load_element('eJw1UEEOgzAM+0rFuYcEWpruK9OE2MSNG9ukadrfZ6flEIQdx07zHZblsa/HsSzDJQz3z3M7hhjAvtf9tTl7zRJDthjKhBrxD1xqDCoAqhpDQsfA6ugMe9qF3m/8CFg5m09GpoYS3WeKAawASCOK+9FGIMkJ0kIg3S4hqtYOWhSDaTHTT7QBN24M1Da3UuEmaufO4vMIsfMFTc6CslqP5iyTeRA2uFdmAHec+sYU1dLX46XsfKCH8TY09BneSvsqxR+Ij/E4YOfcS2+/P6K0Usg=', 2), elements.load_element('eJw1UEEOwzAI+0rUcw6BhoTsK9MUdVNvvXWbNE37+yCEg6tiwHb4Lr0/ju08e18uYbl/nvu5xCDsezte+2CvlGIgjqEIKMcA0GJoUjDGUEkAAmnUps1VmrLRvMgyCagaUrB3krBVCAIjspMASf9IP2mWzDaoJqPFRVBNjnB6pNUimJSOS7dIwZqxzJzkA0McpyuvBkCYsWlivFZluZkXQDFjv0fxrDR2lak2qrl1beRGdPmE8xhoWUZ6i5L9CpimtT6gwO33B0MsUeo=', 2)]
d = d.append('v15', v15, True)

v16 = [elements.load_element('eJw1UDmOwzAM/IrgWgUpizr2K4vAcIJ06ZwECIL9+86IciGKHA6P4XfZtttjP45tW37Ccv0878cSA9D3/njdB/prEoO1GEqNofP1GCp+W4EBV4WjUmJowqjQwKvIVQRVJpABtOSFrZ/07AnVTqPoz0iMEaY0vtXJbbRGh0KuwKmkCdKm52hBQc1zpAo8S77E+PEy+Ln7Hl3O8ensv3o9N9Qk7gyt5uuPCUPv6K7SPce78EbU3ea9eB8qMJtyk06Q5Sk5k8vlqVFFp6Rh2Ljo5e8f8UhRxQ==', 2), elements.load_element('eJxNUMtuAyEM/BW0Zw4MYMzmV6polVS55bZtpSjKv9eD2TYHyzCeGT+ey7Z93i/7vm3LKSzXx9dtX2Iw9Ody/74N9ENSDNJjaM0yYlhXe4u/iQE1hm4AkjHVqsiUjJI9miE9x1At00uLRSe9ulE3o65TPyRIFCdxO6F/8VDykN1BKUzTFSzA7YFhp958tSz5z1//V6BI9BhH5kzIhMv0A9ipObnq0YBLvRWQMDuOc4h4kOIbEeW1avGF6qAes/IEbfQvE9Y2f4Qbzq9fc5RR+A==', 2)]
d = d.append('v16', v16, True)

v17 = [elements.load_element('eJxNUMuKwzAM/BWTsw+WE0Vyf6WU0F1y6y3bQin992okFfYQLI8m8/Br2rbf2/U4tm06lenn+bcfUy2GPq63++7omVstrLUI1aKrnTYz10JtrmUZNhAFKjMuGMQ2uDTjLYKhBapGXZMqSyy1x8kmrg1kI7EBYouVYyayLffUJfjTSDuIUu9BVNurRjIoilEHKtg3RmgI/mwjc6EUJJABbM/IUdhlIaVu+z81ZyhERh2YeRxHh+TNX6gnB6/kni7FcxoIZ56o/y2HECtd3h/6qVE/', 2), elements.load_element('eJw9UEFuAzEI/Iq1Zx/AawObr1TVKq1yy23bSlGUv5cBZw9GgIeZgeey79/363Hs+3Ipy9fj53YstXj373r/vUX3Y1Atw2rRtRZm8WJ4QoqKELZaZEPirS3a7OgAdQ8NIPJSPdFWi70HCIXm664gOumYKBmUZ2e4roLfprbJhHFzFjmnzxB/cAK78K6WFOYfItMYljOenP29YRiHVId0y5mwH1DcACtiO1pTHaiN8okrWgOXh7GeN7DzZG3S9rQUl2C25AVdmB1JhVsJf77+ASq4UmE=', 2)]
d = d.append('v17', v17, True)

v18 = [elements.load_element('eJxNkD0OwjAMha8SZc4Qp/FPuQpCUUHduhWQEOLu2HGKGNrE9me/57xja7dt2ffW4inE6+u+7jEFzT6X7bH27BlzCigp8JQCcQp11pNSgDz9/0Q/FkcAxLKojdOIBLSsk4Qdg0zOkgbVxisgCszsce/C4h2Eh2av8Og3HkD9SB3ivWy6igi56R9qFOodcbhjcodW5OGlg+RytupsI0t2gwDZheTYq2cAyrF4sdHsgIwVIYM/gBkQHA+G1cXs7C3dJ4A98zz2sgvB5fMFvPdRvA==', 2), elements.load_element('eJw9UMsOwyAM+xXEmQOhPMJ+ZZpQN/XWW7dJ07R/nwOhh9DgGDvu17b22NfjaM1ejL1/ntthnQH6XvfX1tFr8s4kdqaQM1X64gz5gAuaqAOijmaMvTR+jIn0AYPPC7i4M/iZZSj0NMB0KvtTDbwSUVUQCKQoDVQoYMR5ePCUkqaCW3lUXzLyqenVvqh9EMuse5VR/T2+Se0kGwtvUT1RiHUAJQkoB9VhX/JMATRPbdaNOypBc1Fq0Kw8I/YgskT/SSJCt98f54ZRQg==', 2)]
d = d.append('v18', v18, True)

v19 = [elements.load_element('eJxNkE0OAiEMha9CWLOgA4XiVYwho5nd7EZNjPHu9s/EzUz5+l774B3nvO3rccwZTyFeX/ftiCkwfa77Y1N6xpwCUgqtp0AlhT5SAGDQgYvMtFfuOOiN4bKkUElk3Qih+eSvyiwq9bOU8p83s6QWKZhW9o9hHuIaZX8xNbqzSX+xfDpFztUCkA4iz6lx1KaL+NO4hQJ/UQTYdp8OMGy1XbmYWTx2B5bJA6k0Fz+gq2QqgEcmizXII0lm8pezMLwJBYDVDS6fL4M+UHk=', 2), elements.load_element('eJw9j7EOwyAMRH8FMTPgBAPpr1QVSqts2dJWqqr+e302ZIgDZ/Pu/PWtPfb1OFrzF+fvn+d2+OBEfa/7a1P1yjE4rsEV+RPl4NIcXE3BZRFTkSZLIy4oepK5IoeKVoEwo8ipsj1mAgklTlKmyXiMS4Q80YDBDzB42TPxWRZjdT91ToYufBrWTtMsMlNgU0ebJGXO8MJaMQ8QIQRJ2CQ3TmfQYgtBrSJkdJUzG0fNsfkynqgDdzhkNR9oIr312JYWUTjbsgUfZkdioDLdfn/3RFNw', 2)]
d = d.append('v19', v19, True)

c0 = elements.load_element('eJxNUEEOwjAM+0q1cw9JaZqUryA0DbTbbgMkhPg7SZNJHJa1ju04/UzzfN+WfZ/n6Zym2/ux7lNOir6W7bkO9EKQE0lOXHKqJ/2zfpgTQstJqh2U0RRtykLUIsUvlV3SSC1UQooLGUkPXY5Ldzn38CJyC1Fp7S4XjuYoXdEeTESIws3a1aNSREU4WZscQaAjo1qQTQXPSkNsgWMBIyAqyqYrJXYMibTwIQh7BPGJJmR7ioKe+1i99gjaw4DD9C/VmAUR2xZveP3+AEavUWo=', 2)
const['c0'] = c0

c1 = elements.load_element('eJxFUEFuwzAM+4qRsw9Waltyv1IMQTb01lu2AsWwv5eUHOwgWxZJifLvsm1fj/04tm25puXz9X0/lpxQfe6Pn7tXb63k1Cyn3nOyFTFyUrylAFANQIofgCsq7QKaILyIZJAvRFYmqOj476Sg94bb6TY1xmQt5EPUamhESszoCKVIyEcH+lQy0aVJ3N5Vp1+ObRpqEVokUmKramGXXqRUHkCthpYL+WRZwR30js715Npc0eZSJHjj81OGjxznp9kJjendJ9cQx86sdry6fPy9AQgLUWI=', 2)
const['c1'] = c1

c2 = elements.load_element('eJxVkL0OwjAMhF8l6pwh1/w45VUQigrqxlZAQoh3x86lA0uUfL7zOf5Mrd3u6763Np3cdH0/tn3yTulrvT+3Ts85eJerdyV7J9E7zAqSAiCTJqNYvKtaQeiHGYoaC7WisjqbDIQISSuiFa3mMICoJMMeM6ksVIjeazZ/ZUxZOE3RFqUypFqgGkVZjrwjRHYxIYINmY6MEdjD+iHpvzEwIBCOj9tfg9BJdxqfsHQZAIjHXgoHqzI2oZ5FuDgb0PL6VgQUcdDISsHl+wOHXlD0', 2)
const['c2'] = c2

c3 = elements.load_element('eJxFUEEOwjAM+0q1cw9N1zQtX0FoGmi33QZICPF3nKTSDpk6O7GdfKdleezrcSzLdAnT/fPcjikGoO91f22GXjnFwC2GyjG0HEOZY6AEgKgAIbBAqgDIpKjxPQbBAAPmqgB6GXQXLyJItTJaGQ8BK2it+G/oqHiX7tVMGJ8GX8k6dfpVt5DZi1IdYgjeuwuaaD4XYIvQ3dEEc/I8dazKJkUjOhEGRIYdJSVz9pBmnEdIM9cW4hHZlKW5srShZcfzlXRHg5XXk85+EE1hRbffH/EIUdI=', 2)
const['c3'] = c3

c4 = elements.load_element('eJxFUMsOwjAM+5Vq5x6aro+UX0GoGmi33QZICPHvxEkHh66em9hO3lPvt23Z996nk5uur/u6T94J+1y2x6rsOQfvMntX5HCUk7yjQN6lWQAJk8EQg474CKoHoJDxSEDNuwaRKncwMQqHGkSSvFTgQxmeTdqqiHAepP7M1gGfVo/qImSwDhhoHCZzZCFzGWaqG4Y99Gr7RQWK8pbY4lJEeJJW1nmQcbYubEBLdFIaO8nRHLVH62GHuVhdgiklLfnFHLn/q0rNwhe5C10+X9SeUlI=', 2)
const['c4'] = c4

c5 = elements.load_element('eJxFkM1uAyEMhF8F7ZkDs/wY+ipVtEqj3HLbtFJV9d07g4l6ANlj843Nz3Yct8f1PI9jewvbx/fzfm4xUP26Pj7vU32vKYbaY7DM0xjXGBpzJOOFEUNXJb1UtnQGnUJhx0gSi1p3RUxND3dmVXJiMGyVinBYXKteER9gr/X1Blj+cqkE2BASnkySD/LfzKhTMdXRfBUkOpTuA8vaB015zQhxdl0wlyp8CiC7+eohtQ13mPQxYVhzezRB2lZ/pd2ma147FidMc2D+5HhxstcaLr9/uFVTSg==', 2)
const['c5'] = c5

c6 = elements.load_element('eJw9UMsOwyAM+xXUMwegPMJ+ZZqqbuqtt26Tpmn/PjtADyAS27HDd1qWx74ex7JMFzPdP8/tmKxB973ur0271+SsSWJN8db4wMsHa6RYE3EqUdTeFSIVyMwKvMQzD1EAURLGUBxJQSFARLpaDXyGKPEhDS4sHARJDeYxqrJNDgSCRlZe6CGapwM75/7QXL50D7VXjCO5hbazDBI3qPWUoF+Hlt5crmVwzZ+FwD7Onen8eSF9HnkLBkS6BJCrtOAljG9VPoOU8a8yFmFgf/v9AU+eU6A=', 2)
const['c6'] = c6

c7 = elements.load_element('eJw9UEEOwjAM+0q1cw9N17QZX0GoGmi33QZICPF34qRwiuLYjpP31PttX4+j9+kUpuvrvh1TDIo+1/2xGXrmFANLDHWJgdKsTY6hkdamIAaMAQBlEhWdKiLKXJLLBFhxJmOm5AI7qjpITha1a9kr03Aigu/scttOBMOMLjuxCJrkodrPycTsIOXkcSmjS38HHkqLT0l+F9qekYMRfGSznW6Lk6r7FORrY3d2tnnbSrJD1VrED/XL2fWWyDLiF5YD31tkKPGySpfPFw1uUcc=', 2)
const['c7'] = c7

c8 = elements.load_element('eJw9UEEOAjEI/Eqz5x6gltL6FWOa1extb6smxvh3oVAPZYGdGQY+S+/3fT2O3pdzWG7vx3YsMUj3te7PbXQvBDFQjaFwDFUeImnQDKpmErL+a1pkAZYYuP0x0mGVQPkKM58cRgLDhEYcHFUDNHIh19diIKrxBxdBVYBNFlFDAs3AtciNNnBnkAScbIVaHJqHTamIfdJUatrQl41Sqmsg0LzDGD23VgKmZBOZHZ0nsE4wT+dNFCm7EV9IPc7E+8luUfQEeP3+AOrdU2I=', 2)
const['c8'] = c8

c9 = elements.load_element('eJw1UEEOwzAI+0rUcw4hLQnZV6Yp6qbeeus2aZr29+FAD6UEjG34Tr0/9vU4ep8uYbp/ntsxxaDV97q/tlG9coqBJYZSYpBZP46hVq1RDEuznEhBVQFN/4uCOVveAMRgAyhbUtlAlMhoiApCs9cQWNBGNWGgGZsoW9FcwJiNaMgntkYT9zY7X81Iqo0QAQ9NZRe4rLaWKVHzAJZhKyf0ZhuA4yK2M9YaWmwScpow34yAs7ktri7urXxa9osV9iuNo4iLYrLQ7fcH44lRWA==', 2)
const['c9'] = c9

c10 = elements.load_element('eJwtjksOwyAMRK9isWaBA+bTq1QVSqPssiOtVFW9e8cxCwYzbwb4ut63Yx2jd3cj9/yc+3Ce4L7X47Vf7j01T1I9ZeyVPXEonsqCJTCizRriJSiFSDQqiFetaT2bfwVMGLjoZcCSLCo4N8CqPniKNjd9IMTZ4pDme9pjFpU4paaZyvPXWR6/P+cIL74=', 1)
const['c10'] = c10

c11 = elements.load_element('eJw9js0OAiEMhF+FcObQIj/FVzGGrGZve0NNjPHdnVnUA3T4Op3y8r1ft2WM3v3R+cvztg4fHOhj2e7rTk+pBZctuHqYRwVXAUwVD0VHY0Sr8UWPkgiE/QbiNNNSUHNBZTNPXTmOaim4Bm7MVJlRVr+5/IeK/Xeib0KUiCIV0e7iIgYyuFKf3x8heTAL', 1)
const['c11'] = c11

c12 = elements.load_element('eJwtTssOwiAQ/JUN5z2wlKe/YgypprfeUBNj/HdnaA87LPOCr+v9sa9j9O4u4u6f5zacCtj3ur+2yV5jU0lVJWNSUimLSs04MRY8FhqiSiswYa/gqmFgzOAqQmbhMJkxSpUEK3w5+lrjxRMWwkyxmjXQE6UQKMWz9PBM4Jswl3LSrK/8dWL69vsD83gv2A==', 1)
const['c12'] = c12

c13 = elements.load_element('eJwtjsEOAiEMRH+l4cwB2JaCv2IMWc3e9oaaGOO/OwUOTTuv02a+rrXHuffemruQu3+eR3eeQN/7+ToGvXL1JMVTFhTmGCA0eCqbJ95mj7HYJkFFU4wbtsEIvDEBF5AMnyTz5rUWrLnMqmowzP86bHYcBtaJFF2QpSJLxpO6ogyr8nKyubcZJ8vt9wfeuS+v', 1)
const['c13'] = c13

c14 = elements.load_element('eJxNjr0OwjAMhF/FyuwhbvNj8yqoigrq1i2AhBDvzjntwJLYd5/P/oTW7vvae2vhQuH2fmw9MEF9rftzG+o1GVNWpjrjz0wSI5rKZDBUUE8QJxSluDuQhA6FuiV2DObZOVci4IwEdVaiPxiweqgSARYfGg5CFW46+apO4En6R5ieSTpu8CQsqtij5qcs3x8VcC/2', 1)
const['c14'] = c14

c15 = elements.load_element('eJwtjksOwjAMRK9iZZ1F7ebjcBWEooK66y6AhBB3Z1xnE808T8b+ht4fxzZG7+FC4f557iNEAn1vx2s/6TW1SFkjVYnEnCKVDFBghEEhaoVZFnswrs2EYZ0ZZqCaTMgMZZlf1LDYX14RMrJ62FthMoyixg6xThVntqidW000v8UXWmFSb1dMSrn9/kEQMCI=', 1)
const['c15'] = c15

c16 = elements.load_element('eJw1jjEOwzAIRa+CPDOYyBjcq1SVlVbZsjmpVFW9e8GOByR48D//G2p97WtrtYYbhOfn2FpAMPpe93Pr9J4KAitCzgi0RBusKC4IYjQJgpIDp2STWKN2WyZwYdJrINKx9jNJ5malLuvL+aPI1PCloZgH9m9eLCMB8zAqM1bpTm7vl5Y+8+P3B+jiL9Q=', 1)
const['c16'] = c16

c17 = elements.load_element('eJwtjkEOAyEIRa9CXLvAKQr2Ks3ETJvZzc62SdP07v2MLlB4/A98Q2uPY+u9tXClcP889x4igb6347Wf9CY1UrZIRSMlzv4skQTEBMXCTjxLwHZBFIjRzg4ZQOAUb+iUGjzZfcmmb2AfgAUZWsWvqAu2m0caw4c6nRmw8ryn+o46b2IbYj+5Apay/v4REi/3', 1)
const['c17'] = c17

c18 = elements.load_element('eJwtTksOAiEMvQphzYIibcGrmAkZzexmh5oY4919BRZteb+Wr2/tce69t+avzt8/z6P74MC+9/N1DPaWa3BcghNMihdrObhiBVYHywBDGYjQEppCL2wgYgUCilmLWXRZGCmBhVFiCkEpqKwzQhQnUJpzHkuwi6n2DVlbUzI5rYNEdcXHS3j7/QHckzCs', 1)
const['c18'] = c18

c19 = elements.load_element('eJw9TrsOwjAQ+5VT5gwJzT3Cr6AqKqhbtwASQvw7vqYwxHJsy753aO22Lb23Fs4Urq/72kMkqM9le6y7eik1Elsk4UimkRTPSqScJwdxQKS6jEhOu4Ifw2cZDsNRc7c6gPGvQuvRYCcnPIggouC1HiMFgnmjp1KC4PNpX5yG7ReqjGHR/yloEJk/X18HMEw=', 1)
const['c19'] = c19

t = elements.load_element('eJxVVcuO2zAM/BUjZx9ESxSl/kqxCLbF3vaWtkBR9N+rIYdKetisLfMxHA6pP7f7/fvn++Nxv9++HLdvv398PG7nsU5/vX/+/PDTryrnoeM8up6HlLZervOY60DEzsPKepnn0dbBaDhcX8c6GH19XK59GfUO12XR4HHBarkNBB0vsWA2BKYwufxnvQ6NiH3ywOBQ3HCGu2kk9OyApMBZwscN3KUyEZ9gaxlKWuYUoL8CPb7jGbFEltcs/Jv0wQPSu+UIL6ep0VUEcXq8AE9PBJbuwuJgqXUX5yA7MY/Co1ZJplyFP22SOJm7QiPbLQgZll6S5Kp3pTClsGIlWlU+a1h6+50kj+8NXNmUVWYjGzWBXnrrR+QGajQF/5PUwX4bVWE1O46PlaKSrA2VzGDfy0NPx2DVjV/UsoOdgnSWnBgUHR3Z34QIC5FMot9RLF5gYEmulaQi+iTsfA1MMShKGltkUAJ+9TMqxbMrAaLmadn5QqSWYbwLGi8vop6Jo2c7G3m3aJ/t4Ul9+vBwyq4whncbNFSi8v+Vc3vlePoSKNRWj76ChDGJ2nn3mQRCYLKUa/SItAeZF8O2SU16SahaNacvV0ZOigf2Nj7HuVNdNYsEV0p9+Uq6yDwcUV7bYDpHQpJjjwshz5yoSPkcJU0Ftsjb0x+tcSa9qOfekVBEsJQiaxTPViJLdhVepJ86Fv7Ax0md4Qs/lDI5FKgTaNrOVFhj29quCdgCUe4i65SflZeuuUIlBe8Cj7qVyyljjk2i3xa5BuHlAWV/Nkbse6ModflslRB62xwU3gXYTjPpqqllvzuEk45WWU7WyA5M6jS42YiNm0hzu2vIHDWFAnpIcpfjmHXfWnlHCVeycrv48qe6RoqjvvBM5JVgJXnx7TNZ1B5OvFhL9nNSc3MN5nlhwHWRWnKtY0UZtagMN7KgWCS7LSx4UJyag5S6j5XEKekksPPq4Y363MOak1o4gv+Nv/N+5V3rGtZI3/aFF8IbtOnPSbLA4sxW6rzo299/rfmbpg==', 3)
const['t'] = t
pis = [
    UnamedArray([
        [
            elements.load_element('eJxNUMsOAiEM/BXCmQPlVfBXzIasZm97WzUxxn+3Q9nEQ6F0pjMtH9v7fV+Po3d7Mfb2fmyHdUaqr3V/bqN6zd6ZXJ0p2ZlKcktOPjjDSIKgqQmSJAIQ0ARhKeSCAhLQJRIL6NEmQk3aiMKfIlECBjJIFHHAXtpYHtw0h34GlfBARCUoW7RrmShMatNRGk8JfxoMz6bzFdZNUlRx7AuphOmoTAOP3rFWO19JeUxTbPwJBuA5Km7smKOqki/6YXm2Dus4Vx9eoI2g5fsDoixRCg==', 2),
            elements.load_element('eJxNUMsOwjAM+5Vq5x6aro+MX0GoArTbbgMkhPh34iQgDuvq2ImdvqYxrtt538eYDmG6PG/rPsUg1cd5u69aPdYUQ+UYWo+BlxiImgC9JEdEsxxJBCqWf4dYmnoFIezCkJF0ir5nKaA5S4HBQt6MhEcl90rN27qiDFSNYxnQZWqZXUI5m7leME6dlWMyE81WXEbl54CoZGshQ0Ge7oshDD519gzlj8cCiNequ5KAwt/ZOZm9ImZ/N84WRCfYK2Hv2Rt68sWwgaai0/sDl8FSqw==', 2),
        ],
        [
            elements.load_element('eJw1UEEOAiEM/ArhzKFFKOBXjCGr2Zu3VRNj/LsdCgfSdjqdTvn63u+P7Th692fnb5/nfvjgFH1vj9c+0Eum4HINrmhkOmmiRc4a0wRyRMLB1aIPgACQSYnarnENFyQKV1Vh1koykmi6TFpVSJFNg4Y6LxazLE1afHBkyjWaSRkmtCXNnLVicTiDTWZ4TdO3CskYUemELtGkJLSTKWIpqNgH3OwMKmmZJ33cOmSr3Txmon0NSAUPRzTrwYZMDu5lbgYIX39/RIdRew==', 2),
            elements.load_element('eJxFUEGOAjEM+0o15x4mpWlSvoJWI0DcuA0gIcTfsZthObRpncR28pqW5Xw9ruuyTPs0nZ63yzrlBPRxvN4vAz3onJN6TiaIBbHlVHtODqzhqObUGZGXuQSgKBIp2+W7aDGcircUcDaUOICGctf4W2WH8wKb18h2VPceWbeg8ZlqKDI+BKTNwptIDTW2UFnmTSEM0eLQ5DxGwGIYAjYAEHQLAg5j/tMmoX4ZxnybbQK6izWJaADfnf2rDz/MDu/DS6VkkShuI8VpuBn5e38A1B5QmQ==', 2),
        ],
    ]),
]
thetas = [
    UnamedArray([
        [
            elements.load_element('eJwtTkEOwyAM+0rEmQNpSQj7yjShbuqtt26Tpml/nwMcDNjYib+htcexnWdr4ULh/nnuZ4gE9b0dr72r11wjiUXSEolTilQAAZhxqILkSFb9F6RCrLAbu2OFHTABWTyTwPLqjzzHyTLhKts09q24DSPVBi8ylhuaiLobsdxrlcmYZfQRHrmKnMrt9wfXBS+o', 1),
            elements.load_element('eJw1jsEOAiEMRH+l4cyhdaEFf8UYspq97Q01McZ/d7rgoaGdPqbzCa3d97X31sKZwu392HqIBPW17s/tUC+pRsolknEkxSvig6DhNNQKIlmkwr49oZmlEA3LArDkUcJOMTwUk4GqEIr7yfQqOgnn0zLM/aL7HAcyCJsxsrm4+Bf5J+QZhiGrXr8/ji4vZw==', 1),
        ],
        [
            elements.load_element('eJwtjkEOAyEIRa9CXLMQB0V7laYx02Z2s7Nt0jS9e0FcoOF//oNv6P1x7mP0Hi4Q7p/nMQKCqu/9fB1TvXJDyBWhCALFjFCjFq2GN3WK/0Q6WhlBmrnRlG3NUjFpIsgRlOZAsic6RJLns/bZOHVBWYNZHCVara6UrZ0JFe3QuVDYjWapZOjb7w/a2C+m', 1),
            elements.load_element('eJwtjksOwzAIRK+CvPbCOP7gXqWKrDTKLjunlaqqdy9jujCGYXjwcb3v5zZG7+5G7vG+juE8qfrazucx1XtqnrJ4KtVTXTxxqAhF1fBX9WeOGiKyICjRV7fMiaQJEM0QAgKDG60BZ81Gk4wJbWQtCgoGNbItkmIcYTug6cOJ05UWE2uycWZA8/r9Abe0L4s=', 1),
        ],
    ]),
]

eq = Equation([c10, c11, c12, c13, c14, c15, c16, c17, c18, c19], [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9], [[elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()]], t, 3)
eqs.append(eq)
v=verify(crs, eqs, c, c_prime, d, d_prime, pis, thetas)
print(v)
