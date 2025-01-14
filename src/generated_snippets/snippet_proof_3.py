from gskit.framework import CRS, Equation, equations, proof
from gskit.utils import NamedArray
import gskit.elements as elements

crs = CRS.from_json({'u1': ['eJw9jT0OwyAMha+CmBnsBBvoVaoKJVW2bLSVqqp373OgGcDW93788bXe96W1Wv3F+fX92JoPDvS17M/toNdYgpMcnGpwBTNhMvP5xY4SJCbTCFgIZDxNXS2YOY8IE2oz2WIF1kRz98rU8wKoMqxM1mIq7BlULY9zcbbGaeSZjwP6Tw6jyu37A0eOMCE=', 'eJw1TkEOwyAM+0rEOQdoCYR9ZapQN/XWG9ukadrf5wC7OInj2Pm4Wu/n3lqt7kLu9n4czTGBfe3n8+jsNRYmUaa8MKlnCl4wJKaSMYQVTWcBGowxPVYax0aXOedRg8etpKn2pl7tDBFxxgQfR1bRqc9okv5vAIIn1BZlmNkzEqdhN1Nz9YAk2/cHvwgvsQ=='], 'u2': ['eJw1jrEOwjAMRH/FypzBbrHj8CsIRQV161ZAQoh/59yEIVbu+c72J7V235Z9by2dKd3ej3VPmUBfy/ZcD3o51UzqmUwzlSmTiEaRTLWAxGM4OKBHKd3rMwQDW40Pkna0gVWCWChglzGYYxaExwLWEZcJvTL3dc7/A1g6detHKFwKXawf49jqI2l2/f4ADbEv2w==', 'eJw1jEsOwyAMRK+CWLOwKWDoVaoIpVV22ZFUqqrevWMIi/Hn2TNfW+trX1ur1d6NfX6OrVlnQN/rfm6dPkJxJmZnhCF0Zg+AJd8gnZMzBU8S9CgY/PhmAimkVH0UtaSrRBlxIgrKpHCEvtAkUI6jM5dp0EvP02SP5+hHXoDy5WHyWmBIafn9AXvqMF4='], 'v1': ['eJxFUEEOAjEI/Eqz5x5Kty3UrxjTrGZve1s1Mca/O9CuHqB0YGDgPbV225Z9b206uen6uq/75B3Q57I9VkPPOXiXxTuevUt4iao6BlK8EyAZGY4wSyCQogF4SZFIKEkwoCXDrAwA88GpvRHFqG4Qi3SeDqYAJ9wV1NpjTeoopv9LQRlqWRvDCSzHo3lQOMhwkg6NyJXRXhBXaKj4yzw0cy/WRlIHKVAXKXirXcaUhjFGa3jsq71Mmm1nu9JQ/LuAqbXDWM4wm02XzxcfNVIH', 'eJxNUMtuwzAM+xUjZx+s+CGrv1IUQVfkllu6AcPQfy9pq8AOtiWKEin/Ldv2OO7nuW3LJSxfv8/9XGIA+nM/vveBXmuKofYYVGKQVHgpEKAdqPE1gIKrr6wi0BxDUaLgNwRq8xVp6EVVKxNcFT2mDiRWABTSOxlIOvvWoQ6O2SwPOyJTvYrbEkmuvNIYxFTnSPIVecluj+NTYgui1ph130Mku9WhYD5qMM0+tmwmw292xbE9ndfiqyHuMh3SF218PqTnf/9Gn2N/F1evNR65vd6geFJB'], 'v2': ['eJxNUEEOAjEI/ErTcw9tt6XUrxjTrGZve1s1Mca/O7Ss7gECA8wAb9vabZ23rTV7Mvb6ui+bdQboc14fS0fP2TuT2RkiZ1JBnJ0pyPPkDAcY8BClKQ2rFYAHmtHNPREXpDdLALiIRQBFyiwOpYoggZaKAsRjpreykoSILCGrQgJhqmOE/UEh7SpqotS5SbmDl8q07xCP7JTHKcEnhaVRLh6HdTSqiP+LjMJPRe+Xh8in+nxgXbAz6Wv0dhnnuG/jp7EIhcvnCxYjUeo=', 'eJxFUDuuAjEMvEq09RZxEscJV0FPK0B0dAtICHF3ZhI/Ufg3/o39Xrbtcjvt+7Yth7CcX/frvqwB6PN0e1wHetS4Bm1rMFhJCSraGnqn43ADWs0BSUSQrhVZ2NKmr5DmHUbLOMMqamzWVPhWgKOmcoVgtEFU5zCRPqe3ERQqpFr9RwZBpSoOjYhtJpgjv+USCSSvlUjebOKqPDmYTb4K23hhEr+QbzH19eoUeCrLenMqJc8Znc+L2T/Iazl9lJCj5il8JFcNuvxFlb/PF9QaUTI=']})

X = NamedArray([])
Y = NamedArray([])
x = NamedArray([])
y = NamedArray([])

eqs = equations()
const = {}

v0 = elements.load_element('eJwtjrEOwjAMRH/FypzBbmMn4VcQigrq1q2AhBD/zrnukOT8zmfnm8Z4bMu+j5EulO6f57qnTKDvZXutB72WnklbJtNMDbpBC6tfJVOtQbpTYQA4ilNhNvEuDrcjW6FlwqUzgBeMvKK1zJ6fYoXitXOwa2GLjuZD+dwk4p+QGnvUvCgRPHwf69Ts9vsDw7Uvmw==', 1)
X = X.append('v0', v0)

v1 = elements.load_element('eJxNTkEOAiEM/ErDuQeKQMGvGENWs7e9oSbG+Hc7wMFDS2emneHjWrsfW++tuTO52/uxd8dk7Gs7nvtgL7EypcKkJybxaiDZIAUoLBQCqIhmU7QlXJXMVD1Ttjf5yRe4iLVoVXUKWNCwBEWWAugKHPSwr0gVvxq854KPf/8rAh2WabKonK7fH6B3MGo=', 1)
X = X.append('v1', v1)

v2 = elements.load_element('eJw1TksOAiEMvUrDuguKQItXMYaMZnazQ02M8e6+Ds6Cpn1fPqH3+7aM0Xs4U7i9H+sITEBfy/Zcd/SSG1MxplqZJEYMKUz55ItipMRkgBsOg1bBFJn7TkrMQPHMFWkqPa0ixzxVPDXBk9Gj8Hnn7HLUvSLyF+rh8Dj1fLH5g4Jm1YMFWFDQmpddvz8YRi/4', 1)
X = X.append('v2', v2)

v3 = elements.load_element('eJw1jksOAjEMQ68Sdd1FPdP0w1UQqgY0u9kVkBDi7ji0bKz02XXydq3djq331txJ3PV137vzQvrcjsf+o+dYvWjxkoMXYPWSlICPQiNlwqDmUIrF6ohGc0DR5KUWi0UOdKsVLRhRgFSng2C1y6hPaQLAJLCi5lmDsE7JOlZlptVO+P8yAHBLLHby5fMFTKUwIQ==', 1)
X = X.append('v3', v3)

v4 = elements.load_element('eJxNTssKAjEM/JXScw9J7NNfESmr7G1vVUHEf3eS7YKHKZ1HJvn43u/bMkbv/uz87f1Yhw8O6mvZnqupl9iCSzW4wsExnUCAAtSmApxYppNBEoGwWaI/mSELMEXMguV8ECRLnGkt0vl29IjtRKQmKEbwVEX5K2nIVi2T/TImvUjsEtqHc7p+f55FMGA=', 1)
X = X.append('v4', v4)

v5 = elements.load_element('eJw1js0OAiEMhF+l4cyBAuXHVzGGrGZve0NNjPHdncJyoHQ+Zlq+prXHsfXemrmQuX+eezeWQN/b8doHvcZqSYqlJDh13hU6y+wLWHGWmAOKi6DZkqaqUhdW8ZApnR5JUxR94UWZxyCPbF3KM9xZVV2TOM4FohGHcATN+JOoN5whXZ9GkHXX7fcHqkAwbA==', 1)
X = X.append('v5', v5)

v6 = elements.load_element('eJwtTksOwiAQvQphzaKDHQa8imlINd11h5oY4919D1gwMO/L19f6OPfWavVX5++f59F8cEDf+/k6OnpbS3Cag7MlOBHFg8ewLCsHtgy6ZNIJWqCKu9AXqehGgQmozSS9DIuVaWNNyiM9MZPiXiBzZCiMi8QhIW3I0WnpxPgQUIm9l7Fp+/0B8yov1g==', 1)
X = X.append('v6', v6)

v7 = elements.load_element('eJw1jsEOAiEMRH+l4cyBskCLv2IMWTd72xuriTH+u1PQQ0v7ZjLl7VrbjrX31tyF3P117t15An2ux2Mf9Jqqp6yeSvGkEZU9iaAYMzSOGAQiB1PTj9SARY0OAkkWBEUjhhkRGVLCq8uczS+ItJMjjRkpBbSKLbBpmYv9YNgYTYKdsBby9I9N/nrJt88XIZswEQ==', 1)
X = X.append('v7', v7)

v8 = elements.load_element('eJw1jksOwjAMRK9iZZ1F3PwcroKqqKDuugsgIcTdGbth4YzzZiz743q/H9sYvbsLudv7sQ/nCfS1Hc/d6DU1T1k81cVTgnJInkpGw9WTgFaAXKAoUW3/AMOIAFDRsEEFMhuLwy1weeETMCf96b6o+8K5RkBrnIMNsKIyoIQ5bKfZIzKPZbtl/f4A60Mvvw==', 1)
X = X.append('v8', v8)

v9 = elements.load_element('eJw1jrEOwyAMRH/FYvaACWDTX6kilEbZspFWqqr+e22gi/E93R3+uFr3c2utVncD93hfR3MISl/b+Tw6vceCkASBCYGIdVEg+lIw4j1CMeWjLipSNh+NgPk4Dwcnc8m0RplhomBjMfkfYh1BuVjPMjp6rDd3qiTrJdzTxfzzkhRGgci8Vf/Naf3+AHX3MFY=', 1)
X = X.append('v9', v9)

v10 = elements.load_element('eJwtjbEOwjAMRH/FyuyhbmPH5VcQigrq1i2AhBD/zrnJ4Ojsu3v5plofx9ZarelC6f557i0x4frejtd+Xq95ZVJnKguTQ5fYDVqgMZqZMrx1YhLB4yEmja3AxqalT8R9xuSuy6iaR9iiNtwOWjpMwbKBEInvhxFdkTMOguuIzBIk4AxZ09vvD1YTLzA=', 1)
X = X.append('v10', v10)

v11 = elements.load_element('eJw1jksOwzAIRK+CvPbCODaQXqWqrDTKLjunlaqqdy/4swDheQyerytlP7daS3E3cM/PdVTnQdX3dr6Opt7T6iGLB148IJIH0WKyR9YWUBUZCDEqW21gbTHaQrIpdF2MBRlmuyRKMk6Co9FcIZq/mrvhpWPWkpYpDTVJj2KJJY005mO2Q4/fH+DgMMw=', 1)
X = X.append('v11', v11)

v12 = elements.load_element('eJw1jkEOAiEMRa/SsGbRAqXgVYwho5nd7FATY7y7LTCLkvL6PvTrWnscW++tuQu4++e5d+dB6Xs7Xvug11Q9cPGQswcK6KGQNmTUGlRcdcyiCs9edFiUczSTzYorQzjSQWUNCM0iLEbjaQbjeP5gD5DYoVdOGq0zPryRkLycpFVk7cU4d+Bsu91+f9XHMJk=', 1)
X = X.append('v12', v12)

v13 = elements.load_element('eJw1TssOwjAM+5Wo5xyaro+UX0FTNdBuuxWQEOLfcdZysBzZjpOPa+1+bL235i7kbu/H3h0T1Nd2PPdTvcbKlJSpeKZcmNQQmMRjMPMcRCCljBhYEa2A6kCpw1NwSZixkGdWgkDwE2JNi3Va3Jw4I3EZ542rXQ22LH48k9P8w3Yk+H/vaa3fH46yL1o=', 1)
X = X.append('v13', v13)

v14 = elements.load_element('eJwtTkEOAjEI/ErTcw9lLYX6FbNpVrO3vVVNjPHvDmUPMMPAAN/Y++PYxug9XkO8f577iClAfW/Ha5/qrbQUWFOQBchABBEEyoK0ZGNTA6vVKhCFSwqQEBc4yzlhAhEqhlvQ0eqi3fGVluoZROKtBlRcLYZmxzsNtWbvM1ZI80NlblH/ovL6+wOKni+F', 1)
X = X.append('v14', v14)

v15 = elements.load_element('eJxNULsOwjAM/JWoc4a4iR2XX0EoKqhbtwISQvw7duwghrzu7Ltz3lNrt309jtamU5iur/t2TDEI+lz3x9bRM6YYkGOoOYZlkVMWAMqWSgwkDM+yQNikDCujtXqZwUoqKSpNFRwFqA4V5dHasYOdTv82XZbTkE4Wh9CU1bxkrVp+6rKxUFgc5mrRtV77eSRiBQUgOXG2hFWKqdq8iMapGWd7M49JIXvW7p/IORUGUP8xKmYLw27TQ2FvYpfQT6AxMftcChBcPl+XqFIt', 2)
Y = Y.append('v15', v15)

v16 = elements.load_element('eJw1UMtuwzAM+xUjZx+kxPKjv1IMQVfkllu6AcPQfy8pJQc5MkXSVP6ndX3uj+NY1+mWpu+/13ZMOQH9few/m6N3k5ys51QrquU0UG3JSRWgznp1CrwaZuANAAV3FVysXLxZyLsgNt2RGc1Mtoa0j3McMuFV2nmQ0CBrjpYIY+B1o4ppoSxLpFFZAhgYdOYUi9fo414kLJGJqnK+4dndz1ejB6s6yqAjuL1EYNfSB/4GvPR4sPJ7rkqMJszv23ZUsyB4MlX+GpFIX+Fb9ev9AarrUaw=', 2)
Y = Y.append('v16', v16)

v17 = elements.load_element('eJw9UEkOwjAM/EqUcw5xUmfhKwhVBfXGrYCEEH/HEzscUjUzziz++HW93bfjWFd/cv76fuyHD07Q13Z/7gM9cwyOW3CVgiMqwZUe3FLlEuXTBOgNTAYis5Ti5Bb8CM54GuW2ZEMay4l6YACZYtpESd1qsmcMjQLGHDHGDLabzTAlWHQN1JCQcMGICBRW2y5EHxHLjE2kdM3mNduNrKUq2rJlowh9UrRmkxolaayCNXtDmZhsQXG2GVuCWEtaGlHHlvk/sVhu0q6FLt8fzr9SPQ==', 2)
Y = Y.append('v17', v17)

v18 = elements.load_element('eJw1UEEOwjAM+0q1cw9NWZqUryA0DbTbbgMkhPg7cRMuXebYjpPPtCz3fT2OZZnOabq9H9sx5WToa92f20AvXHJizUkoJ7Vaqn17TrNhjHrOicgaVPEUNogAdTxiAoP1ZAIDVELUHG/sOJGGrKLLQCrcDJIxwAzaIFpP2MdTmUNVzK+JB2OrewkHp0Gj4YSUAqp6LB+GLOpaKtWDYlM2RtdgIc1gYT4I/b869hzRMa9LRBthYYkb4n7DqUe01nwlpmBq9Z9xIPLjNLp+f/DCUTo=', 2)
Y = Y.append('v18', v18)

v19 = elements.load_element('eJw1UEEOwjAM+0q1cw/NaJqUryBUDbQbtwESQvyduE0Py5rYtZ1+l9buj+04WlvOYbl9nvuxxGDT9/Z47X164RQDawyFY6CVrCQrcooh2ydiqP2J1hi0ALWOVxxyDFVwsCJ2WxMa8EyOIUdQIufCoFZDxD0GRVG6sPpcaXgTsY+LXSmdiEimpXCp7gA+gox4VjQDgQ0hEhlR+3Y9dhp6uTrE0xyeNY3dRySaezLNOOTOBddTHZuX4g1ySfKmP4zO9SscZMDCLqfOwNsUuv7+WXJTIA==', 2)
Y = Y.append('v19', v19)

v20 = elements.load_element('eJw9UEEOAiEM/ArhzIHiQsGvGLNZzd72tmpijH+303Y9UMow7Uz7ifN835Z9n+d4DvH2fqx7TEHQ17I9V0UvNadQewpNDhfJKQXKSFoKfZIHSTIN+WUBT/gVgEr5Z1pRhS1QY1QM78HVSiAyujGAUQaDstPaMIWR7YZsx61qCNStAZGINVFlcvlOh004qOZAAdWArzoZzbqwTUJ0hMpO5maSejBZJh8Pi5nY25m0BoyUvVoTNTGOBM6Lwid3AZXhlboIrKrBNV2/P9aaUuc=', 2)
Y = Y.append('v20', v20)

v21 = elements.load_element('eJw9UMsOwjAM+5Vq5x36TFp+BaFpoN24DZAQ4t+x24zDMtd1HSefaVlu93Xfl2U6uen6fmz7NDuwr/X+3Dp7Ln52pc5OE/5ldiEoikfJlQCU4mueV9GYiuuayASABonwkA8LsCFCXIuBEL0JKpSa7UWEsAAIuzDE0UD/nuiitAtixl0TIG4M0a+KAV9MyMQ1W2I+yOnIl8eoqoMkprJHAid14B4tI0VJY1SKRY4mXqxwnKxjbvUjqzRrRiOuisujOTc1Ftl3nMbgEi7fHy53Uew=', 2)
Y = Y.append('v21', v21)

v22 = elements.load_element('eJw9UEFuwzAM+4qRsw+RY0tyvzIUQTf01lu2AUXRv4+M5R1kSCJFSn4t+/71uB3Hvi+XtHw+v+/HkhO6v7fHz/3sfrQ1p+Y5qeVUEdZyklVQbEhEWHU+NaeOxBENkILnSgDDUsgrBRDkKimVkMWj4FQfBqccJzudodI95KWgY2skNGiF0DZ4IhbEZmMHTvZzOfC8DneCp4iwgI/qEBOhkXBnqXGkb5OMwspM9J9NfI65z5NZ2PDnf9g2z4qILytxuY3NlGicyHGXsZjK9f0HhcVSLQ==', 2)
Y = Y.append('v22', v22)

v23 = elements.load_element('eJxFUMtuwzAM+xUjZx8sN5Ls/cpQBG3RW2/pBhTF/n2kFaOHxBIpUo/3sm23x2Xft235Ssv19bzvS05Afy+Pn/tAv7XkpC0ns5z8hFgRI28Wb3dgK3LEjtg8MBESELQOokSxSEUiOa09iIa4ESNZSUDRe9j1QgUCBSGFJUXDjBQ7SYVYZyeM4TTDaz2MpXT+hoFPS48hvB/+UgcsB2caqw691ENP6eoTEfRQ9tLoO84xFzodBSIWx+C6H72FNQG32Z3TcTPemwOMT85//4XDUPc=', 2)
Y = Y.append('v23', v23)

v24 = elements.load_element('eJw9UEEOwyAM+wrquQdCCYR9ZZpQN/XWW7dJ07S/LybQA8E4xNh8p1of+3octU4XN90/z+2YZqfse91fW2Ov7GfHMrvEsxPdoy5WnJUnIi1eULJSCrLuvFi7lLOrRZQVZVPHEM7FRDFFPioZ9JCgDLAYgYnUtNjEizcpyEQ0iI0k3wwNawKfwWYYqr6YSyI/3kj9ZQlgFpTYb5NYjjjctfnmAtGKnPGixaEwMuX+Qb5/hxlDO6URBCAE0+HYfUdcDvCOASqWPNHt9wct/FJh', 2)
Y = Y.append('v24', v24)

v25 = elements.load_element('eJw1UEEOwjAM+0q1cw/N1jQpX0GoGmi33QZICPF34qY7dFocO3bynVp77OtxtDZdwnT/PLdjisHQ97q/to5eOcXAGkPhGGimGMQAShKDGqqEAggJ/hYjKqoFVTFCNYU9nkebMaKr1LlVxzyWExVH1TQVWrMW2CceRpwRxmxl8QxSXNKf4bp4UGXvlxFBiz8im5AHCWJK2Q1VnI1JMrsaRCIdG/SwRPUU2idXXwppYYkBcmaEL3ar4qfwU804CBXnwQit3NvpvKRVhW6/P2VzUZ8=', 2)
Y = Y.append('v25', v25)

v26 = elements.load_element('eJxFUM0OwiAMfhXCmQMdFDpfxRgyzW7epibG+O5+pcwdoLTfT1s+vrXbfdm21vzJ+ev7sW4+OFRfy/259uqZY3AswVXEuSIWHOQ0UXB5xiNGvUgv4IWDE+XgzShyMt18UNWxWKVHVYm5qipXJQHgrG0m+NXRj5EUIII4y47CR/IYRgtqSCRGl94SsLAtUcm0vQ0hqZNptR3rhvyftCilDqOym+2QJHPR4SnCIafDraahzX3OODboX0j2Nf1LKJvOuMn6EAEqeujy/QENVlFQ', 2)
Y = Y.append('v26', v26)

v27 = elements.load_element('eJxNUEEOwjAM+0q1cw9NtyQtX0GoGmg3bgMkhPg7cZtJHBrZlmun/Uyt3e7rvrc2ncJ0fT+2fYrB1Nd6f25dPXOKgUsMUmMgslEyAMegZCDxIc8A2RkbYAFZMCxDyvCw49rzZs+iZLJ2MP9VjAiMZJIYKAehpN6ldSRiQ6SDU87DW5Jb4ejbVFhQUn1hEW8TsxX2p6BD0ZPpeGpP6AN57Ez8Bs6iXl19l1JcRJHq6FAZmC2VeXAYe/+xleK/aMQLXb4/5MNSbw==', 2)
Y = Y.append('v27', v27)

v28 = elements.load_element('eJw1UEEOwjAM+0q1cw9NadqOryA0DbQbtwESQvwdO80ObVInset8p2W5P9Z9X5bpHKbb57ntUwxA3+vjtRl60RSD9hgaYpljmBvexGoMkgCIJGYnZoo6emcgXR1QVhKmKh4V1V4AZkQMN5xyjKqwk5cYBIXGfnHGTJBX4jQZ7Q86KIYg/yIoSUaPFmduTLLRc0TKYB2QVJfVNmzRHunNXp1Hr/mlOgF6aqbHzVT30V3WGLmr5tHavGS8LkBHrA+xwxl5uCeuw3bGI9ffH2wGUpc=', 2)
Y = Y.append('v28', v28)

v29 = elements.load_element('eJw9UMsOwjAM+5Vq5x6Wro+EX0GoGmg3bgMkhPh3nKTjYC1zY8fJZ+r9dl/3vffpFKbr+7HtUwxgX+v9uRl7LnMMhWOoLQZKKYZGMWQQrYCYBa9LDIwvkTHo5zJYoAEF2pJRq8eMx1q1wF8Td27ZIc1VDJeMOos72DD114LVhnQOYhRYcVI7yKu2JTpiiJtm67eRi4djcoi4AdEyhOqvITSqHGsTDa1l5rGhWv+nq9bn8OgVW7aOLHaCdDB0yAgBuPp19GIm90Ivo6DL9wezQFG1', 2)
Y = Y.append('v29', v29)

c0 = elements.load_element('eJxNUEFuBCEM+wqaM4eEIQT6lWo12lZ729u0laqqf69NGKkHTGIHJ+RnO4735/08j2N7Sdvb98fj3HIC+3V/fj4m+2qSk/WcWstJVQg7YQCEqVAQVuAM0MNzqrhtFk+1IMOr5mQApmHo02VfzmPKcOmdQUWgy5t+XldzQ50XKmC74cgqU6nXlEWipwr7lTB1o8IExyUmolD7svO2qqZdmcZI6x5/m9PzgbWVcLIh178krDvI6nE3DujXOgCusYDoaVdjBgpwLqD+3zMdmt5+/wDZ11Lo', 2)
const['c0'] = c0

c1 = elements.load_element('eJxNUEEOAiEM/ArZMwe6C7T4FWM2q/HmbdXEGP9upwXjgULLzHTa97Sul9u27+s6HcJ0ft2v+xSDVp/b7XG16rGkGIrEUDkGSgWBEGYNlGNoDY9FQZpUBYLAemf9YD2if9nIChBxEM3JEy5dGhJECcEUtc5az+LKUDEFY9MIaCKpwxa/68+R8kV1WvIebrXbQ+Nh0YrShscMf+QQS2CGiHuWsBGMP9sO6lgEe5eizCa9SDQyrA4PBinx3zRmC6IeMJaUzhDyeSqdPl+jg1LR', 2)
const['c1'] = c1

c2 = elements.load_element('eJw9UMsOAiEM/BXCmQNlgYK/YgxZzd68rZoY47/bKV0PwNDOTB8fP8btvu77GP7k/PX92HYfnERf6/25afRcYnClBVdLcERytQxQg8sMsATXu1AoOJZT5E9xObhJhGz8CWAT9RJVl1A1q7zYkWJZcpRgV4+C6fCNbYYpRgMkoFkPmsYHh43aVJxMY16S4zRLMk+szRPE1UZjqFGHp9N/PAQwENbD3V7rgwjLyOalW0FApTyHQ2e6AeXCCLRudIqHGFuvdPn+AC2HUeY=', 2)
const['c2'] = c2

c3 = elements.load_element('eJw9UDEOwzAI/IqV2QMQE+x+paqitMqWLW2lqurfC4ZksA0H3J35DvP82JZ9n+fhkob757nuQ06KvpfttXb0ypAT15wmzqmO+k4es+SEqAWpESA0u+SAMKeiiIyRIOqokNL0pOTUlLsZd/NWBBskCnbQlkrWy+cl7kIsAeWrxflOSSYfEgiRjlq/oa5ibejy/Us1nEoQI4UNJDjNk5tvXWj0wA6HmJSDvnsj99Y3Y0II4HU+jHFxgiq+0enYqHlqxoQtKnj7/QHl9VJX', 2)
const['c3'] = c3

c4 = elements.load_element('eJw9ULsOwzAI/BUrswfjF7i/UlVRWmXLlrZSVfXfexgngzE6juPgO83zY1v2fZ6ni5vun+e6T94BfS/ba+3otQTvinhXq3eN8ZBL9o6oakA1NyColAIWfgZGEaGCyhEEtrw27egB1EKookKhCyVIh4MzlASU1gxUuk5iMpyiKicrKliSapF54WydPLrUvXRpMqN9YKdTCENN0uEmyFiQ8fQCxtSliMRk9RDcbFTtiur4lNFqGUlHIp1TxdZRQwVNWcy9rlWPE5OpVrr9/mOPUYI=', 2)
const['c4'] = c4

c5 = elements.load_element('eJw1UMsOwyAM+xXEuQfCI8B+ZZpQN/XWW7dJ07R/X5yUA22wHSfm68d47OtxjOEvzt8/z+3wixP0ve6vTdFrCYsrbXE1Lo5CsaJmOSynAcQnioy7FASY5ExpMCl8iATMFYXcmshZGG4nY25CF8iSKJRJdmEQ1f4UyaboXKBN7bP1VL1gOBiGK5CoEeArnS3NnfrMAFHBqsm6crdMGke4LKLe5+B4ioslwQIqmitib32n6d+bTdUXyWcIjRgwIKGAabYFWYyZbr8/m2JQ/w==', 2)
const['c5'] = c5

c6 = elements.load_element('eJw9UEFuwzAM+4qRsw+mY1lxvzIUQTf01lu2AUXRv0+0lB1kyxJNkXot+/71uB3Hvi+XtHw+v+/HkpNVf2+Pn/usfkjJSbacutrdLZCTjpwa35ITarWmNdRiWHEzMAqT1aIHAuDLuJq1RyFEHCJs1Cg4thhGSQPw2ByI0iwRn4YC1zTBfTAJIW31CY1FiP+ZikSdlz60BiP/UvM4yQDC1MWPWRjnUWIDKOvp6V9i89FhIbYBVLfI0BaE06CEZ9WwM+Wwr6vvidydhnF9/wH8b1Jz', 2)
const['c6'] = c6

c7 = elements.load_element('eJw1ULsOwyAM/BXEnAETwKa/UlUorbJlS1upqvrv9YshYO7O53O+cYzHsZ3nGPES4v3z3M+4BEbf2/HaFb3WtIRKS2htCQBcEHKRuiEkaMpOoXxM1yoA8EOLIhpt5wNZ3FlX+aaVXbiGnITt7kXFJ0CS/sSOjV91GqraqOz+RNYmaVHbi4llVO92eyNaCAmry63GNs06FZqG8lxXkWqJaU5uOLP6/yndhiFYWgJLpmmkQLVP0wzmVO4p4pw8pBVOy+4Nbr8/nwVSuw==', 2)
const['c7'] = c7

c8 = elements.load_element('eJw1UEEOAiEM/ArhzIGulIJfMYasZm/eVk2M8e92WvZQaIfpdMo3jnF/rPs+RjyHePs8tz2moOh7fbw2Qy+cU+CWQtUgOumRBRkj6ykUhaoW4BnQ8gwFi1Jb1dBbmmO8KHHRo1bo5CkrhyrgLq4h7P1E3UHRPqnupnRMVFaHvT6n4LYHWCVSBIFisVHN7VojUZlM5rmYTabDjibtsMsYCzQ3F8Vy2F5gobsGTBd973nqoUCYNxCKLwGCfRk+AGpmyizmadGCrr8/DV1RSA==', 2)
const['c8'] = c8

c9 = elements.load_element('eJxFUMsOAiEM/BXCmQNdKA9/xRiymr3tbdXEGP/dKRQ9UJrpdDrt27Z229fjaM2ejL2+7tthnQH6XPfH1tEze2e4OJMXZ4gqgo+SkWQSKCMsUvXJmcKSBAmsEJHgAtGPBcFC4zHkiuiS6PoyqkOjN9B/8mxFLYPNGJ3wMvCKn4EXL0S0xDpNw0hiNc48qMO2F07QsX2JTlygUf2wJeXRwLo2s+7E4DOAXMefkrrlNMcW3StXLcnGMfzmR72iOI/dg16ka4d5GYQkjy6fL11oU6M=', 2)
const['c9'] = c9

c10 = elements.load_element('eJxNUEkOwjAM/ErUcw5xGscOX0EoKqi33gpICPF3bMdFHLxkvMzE76n327bse+/TKUzX133dpxgEfS7bYzX0jCkG5BhIIkusFEORyC2GJhhkEAezuMSjBCAQVjFBS9NKlkQGbdk8BlmauI5GqqMGQO4IfAyS9GPRxGrZKZXfLHszwDGf2qBtKlt3lSFdWSj7kmZC00GA+jKoeVb1ldL4OeGfyJx/2rL3qAoUY82FstHA7KPomszxcSlI9Xc9I0bfZSdUDibXU9Xg8vkCFk1S8w==', 2)
const['c10'] = c10

c11 = elements.load_element('eJxNUMsOwjAM+5Vq5x6SrY+UX0GoGmg3bgMkhPh37LaTOCRtPcd29plqvd3Xfa91Ornp+n5s++Qd0Nd6f24NPUfxLpp3CaWq3lnCA6Wzss1s4JTiXV7IibgANZwWwM2DG5YBck5BD6gmr0O6wCOgsh3KAjRDwIjIsLBC/nIg0pUyK/yBzZhpVObDBLlj6vlU5x6wMAJOE4JsQhN+zV2JIy39sV8ZIQn0/ciKw0HVOr8tlZsxSHFUG166r0rLl7p7lKHPsPxNCfekl+8P5d9Rrw==', 2)
const['c11'] = c11

c12 = elements.load_element('eJw1UEEOAiEM/ArhzAF2KRS/YgxZzd72tmpijH+3U8qBpp3O0Gm/vvfHsZ1n7/7i/P3z3E8fnKDv7Xjtil4pBkccXGnBpRQRSEIsFkiTCpxHRSm4KhxejIwCYIqrFJKUCaIWaavz2wXaNl6KOnIFHOdwEGgmebVEqapZdChCFFYTSzWbQSSkRTZFg0ocM9xWc4wGlmWsIiAJyDKIs+3IPBqFTYW8jhX1WtlugMukNpV5XEfvCG/4U62oJ/AwCe2KaWDYqUq6/f6DjFIm', 2)
const['c12'] = c12

c13 = elements.load_element('eJxVUMsOAiEM/BXCmUO7LNvirxhDVrM3b6smxvjv9gGbeKAU2pnO9BNbu93XfW8tnkK8vh/bHlOQ39d6f272ey6QQuEUFkoBsWrIKdAykmmUsAcrTYqSw9T7qj6yPooAlG/c1Q+C4IqwEXgRQTkkKVKYlQcksLJD9UTZSTpY27G3I5iSP008eSOpAsgDMXc9JHy1epuNJe6js+PUYVkOWnOIbsjUseLYDbHqwKFFRtDYnDqzZZiBQ7C6L3SQk+uZc0fZovDy/QEoIVJ8', 2)
const['c13'] = c13

c14 = elements.load_element('eJw1ULsOwjAM/JWocwZfSWKXX0GoKqgbWwEJIf4dP5LBSXxn3zn+Tut6f2zHsa7TOU23z3M/ppwUfW+P1+7opVJOVXLiOSfRe1k0LzmBWjxqJ8RuVgInBREAUDXp4S0gBM1dtKkgo0eL3HWsEBhCpDBmjIO4q5gujCOxQ73F/DWalkiNWChkWHplkdEXzQhjN59DGqSNrEILd1djiwJl+DUZc1qtlPiRz+pNVmOj2H5sT8HafDzWAd8lxbjs//O9UR+tqXDD9fcH4m9SSQ==', 2)
const['c14'] = c14

c15 = elements.load_element('eJw1TkEOwyAM+wrizIG0AZp9ZapQV/XWG92kadrfFxN2cDCOE+fja93PrbVa/c35x/s6mg9O1dd2Po+u3lmCS0twuShScKJ8IUPKiqGjT1GbRMmUIvhEJbDP+ipnjAMZ9gmFdQnDChuUiUbpOWwLOsTyCo9lYqOMGxAdZxP+B+a0fn8Eii7i', 1)
const['c15'] = c15

c16 = elements.load_element('eJxNjjEOwyAMRa9iMXvAaWxDr1JFKImyZaOtVFW9e22gUgf4/g9/43coZT/XWksJVwjb637UgGD0uZ6Po9HbnBE4IegFQUwpOiAvjOiMkNVNRPBWIkFIdtQpUTcUrWAjzB0kU5qoZ3LuD67Z57SoTU76MxZhGaD9wj0i+reRjBlEk19x7Ci8fL71zy/k', 1)
const['c16'] = c16

c17 = elements.load_element('eJwtjsEOAiEMRH+l4dwDZWlh/RVjyGr2tjfUxBj/3enCgU46zLz0G1p7HFvvrYULhfvnuffABPe9Ha/9dK95ZdLKVBJUmKoyWWESqXOs2OqCJYo7hhycDEe9E0cil9HVDAWzQg3ZAtVl8EXSCIp4A2zz5xfYSHhDYpoIhEwnJnoLnBrnjefH7fcH2NEuzw==', 1)
const['c17'] = c17

c18 = elements.load_element('eJwtjkEOAyEIRa9CXLsQFWF6laYx02Z2s7Nt0jS9e0FZiPz384Fv6P1x7mP0Hi4Q7p/nMUIEpe/9fB2TXusWgSQCF332J9XW5wiIzUqyolYTV6Ieaw5TWUFzWDzA7E4jbTJGsB3btNEsxWJ0kmJkzqomyVeQTxXt2QLkccorjWkeWJdqdPv9AaVzMGg=', 1)
const['c18'] = c18

c19 = elements.load_element('eJw1jrEOwyAMRH/FYmaIQ4xNf6WqUFply0Zbqar67z0HMgCn57sz31DrY19bqzVcKNw/z62FSKDvdX9tB70uJZJYpIyXee7CpkgKyJPTmX2k8AEXYMORpetjkLN7xS8oGy2KXFaH8BXtGUkYeD2M6lFPMQwqo0PPLXCb9K2aBkv+HwDTM377/QFu4y9v', 1)
const['c19'] = c19

c20 = elements.load_element('eJw1TkkOwyAM/IrFmQNmNf1KFaE0yi030kpV1b93HOjFHs/C8DGtbcfae2vmRubxPvduLIF9rcdzv9h7rJaSWMrY7LIOtlSuC0MKDhApAEONsApw4ok99IR4Ht4YNBgGyU7mqCppk4ONlURO/pUlTqAvV9jL3Mx+/Ezrsgp+1DJrD1ctXr4/l8Evjg==', 1)
const['c20'] = c20

c21 = elements.load_element('eJw1jsEOAiEMRH+l4dwDxYWCv2IMWc3e9sauiTH+u1OQC6VvZtp+XK3PfW2tVncl93gfW3NMoK91P7dOb0thipkpJSbxnikDKJq4GFA8IYBE6y5MBV6FVKAoerWImAsf1QHEw6EYJBLGtJ4X0Bj+FoGcQUv3lxHOfi4VnSfAk+I80BbksbHXLt6/P+1UL9k=', 1)
const['c21'] = c21

c22 = elements.load_element('eJw9TTsOwjAMvYqVOUPcJrHNVRCKCurWLYCEEHfnJW06+Pd+/rpSHttSaynuQu7+ea7VeQL6XrbX2tFrNE9JPWVM5oBDPBkAjQAmHgy3hk37lRsHMQc7ms6e5MxBhqISJALAwpHX5WynESZNqMlTlGFuSXgQx1+BIs17cQBgYAQzzvue0+33B1x1ME0=', 1)
const['c22'] = c22

c23 = elements.load_element('eJw9TcsOAiEM/JWGMweKlIe/YgxZzd72hpoY47877bIeOpTpPD6u9/u2jNG7O5O7vR/rcJ7AvpbtuRp7Sc2TVE/l5KnhFfFUwTUMcwJRsARAxiVV/cgBHHaTLQkJNcIQldAoEIKEcki1wy7McaZzDLMrMuzWVfcsDqygymhymSrzJJP+jZicr98fa/4xHA==', 1)
const['c23'] = c23

c24 = elements.load_element('eJw1TUsKAjEMvUrouotmbJrGq4iUUWY3u6og4t19meCivL5vPmmM+77OOUY6U7q9H9tMmaC+1v25HeqlWibpmZQzNaCVTFxA5IQnMBQCLyDsDmzt4fICpbvKGmWVwApuGPZxRUN8o/yHmH26RFwbNiyQuYLA6D060YNox8c8UiLPjMMVuSbX7w+24y+i', 1)
const['c24'] = c24

c25 = elements.load_element('eJwtjksOwyAMRK9isWaBKebTq1QRSqvssiOpVFW9ez3ECyzmMcz463p/7esYvbs7uefn2IbzpPS97uc26SM1T1I9leipBT2qc/bEDKiCIygEqwjFLqxDIp51iFqKQPD1XJNCWIPB6UcKOphRgshZlM0zP6AxqCeLZacbiObVdm1Zku0hwXKzLL8/RxYwEg==', 1)
const['c25'] = c25

c26 = elements.load_element('eJwtjk0OwiAQha8yYc0CKGUGr2IMqaa77lATY7y770EXwPC9n8zXtfY4tt5bcxdx989z784L6Hs7Xvug11y9rOal8M04ixcyDV5iigDqxSBUwBhJQ4Js/OUpMWewKbJWmEtUOYUznZdpG5XKDJqMtoShKK0rFKojF3nl6dV6Eoa4IJdTNoOVcvv9AbdhL4I=', 1)
const['c26'] = c26

c27 = elements.load_element('eJw1TcsOwjAM+5Wq5x6Srk9+BaFqoN12KyAhxL9jd90hsuPYzte29tjX3luzF2Pvn+fWrTNQ3+v+2oZ6DdWZWJxJQFUQlQQlOpMFGDDKC89eTo+SiYdp4YZEWKZMe5QjXiBm7GlkloPExCqWyniX4UF7DrOgDOLnSaXO/PmOD4iVIWiFhnj7/QGXzjBk', 1)
const['c27'] = c27

c28 = elements.load_element('eJw1jsEOAiEMRH+FcOZAkULxV4whq9nb3tg1McZ/d8rWQ0n7OjPl43t/bssYvfur84/3vg4fHOhr2Y510ltuwbEEV1BEGU+k4Gr7N1UbYI6256Rk4miihiZfdECIkAr1SWRKwU7vzBsJ/jo3IILAwqh6nhI+03SeVcCjZekX1EAEZ1WlOQrfvz84hDAU', 1)
const['c28'] = c28

c29 = elements.load_element('eJw1jUsOwjAMRK9iZZ1FnSaxw1UQigrqrrsAEkLcnZlSFlU9bz55h95v2zJG7+Ek4fq6ryNEAX0u22Pd6Tm3KMWj1IJ/juL4mkXRCcBmiEYBqpp4IVvgu1JUFOE7HWVQQdx+LZtwU7MyMc7dhKIxmoAqifKlfXv+TzkVLoNvtDlRjogmOJkRzUe9lsvnC7Y/MJM=', 1)
const['c29'] = c29

t = elements.load_element('eJxNVUGO2zAQ+0qQcw6SLWnkfqUogm2xt71tW6Ao+veaHFLOIYEtj0YcDof6e38+f3y8fX4+n/cvt/v3Pz/fP++P27n6++3j1ztXv/b6uPX5uI143GrZH7e546Hp74j81XrG1K08bm068NwZFS/HmWLgM1bOL525zpfRz7CmL9h4HE5Vt/NTxwOXzu0ND9u5HENHIU878w1vYB7umIipkRlxZpzPUTIeefHDvpgu6XxoZ9AMnYeKAbsRrfMBcgcIYCuRDzFd3SZeugoi1rIpC9DXumtnrUVHHSjm4hVwDxHHQgmwdi9v+TCLyS36Ag6OKYCbENdSEiF75Q4llJab5xSRkUShbDAIgrsKJh1oCn6HWlvF5KH0bDMgkVp3jux1lFZrEjxFDwVwNa6oT1PhWKXw2NJQWwtF1ZWOx7ZkA5iORcZ0WLEqRhe8cFKwDllMdXKxjBekjUUWmRax1Glx17NRZRcidnEsfcSC0SViNmRk5WAuGdhEFHjBb1ppa7L2DOcLEJAavOQf8aAoIMT5bV8oi5Q7suFEBizjyGZQlSCDuFM2TXA5irtU4S84H9LgyBzKyLaGWOSk4dzxMi1Hse7LZrqowngpJy1kCHyX3HMOral0Cuk3z4wcO1RBnYDRORUGJAgdHspq18qZld306gHbvdE4rjp259XusNt1yTDyHCQLk2bDIvrpPCQ3RFu3KeTszuUTQ/YAWqW4Tb0rdhTUw300jKUOzwpsFh0JTwU6GrabFHcoF0XGs+hcdqEhUbKpGqK2JFiXiKsOb6anJDVoWbvKMO3dQ7u9IMv2dgEiOcWNK6kJxo540aS7T9bwAhrsDW23hMJR9iiQ1K+7RtR2d4SXk+PyTpIuQCo5BCYfQgV4XHaPVxXjyxG8Ks/XFYFsQ1dVelFTGZs01V4EwYWioN1TbMOxpJI1lT/dbbrQsqq0Cjk5q9CwLsPhQBLasnVKWj7Gzdd1GaoudHHPzbO1J9cx7UT7NTRdTQw55Tyuu4jtmiqcd8e0Duycicp2xQIxp1G//fsP2bWciQ==', 3)
const['t'] = t

eq = Equation([c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29], [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14], [[elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()]], t, 3)
eqs.append(eq)
p=proof(crs, eqs, X, Y, x, y)
p.consts=const
print(p.to_json())
