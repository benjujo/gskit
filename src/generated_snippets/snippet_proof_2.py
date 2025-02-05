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

v0 = elements.load_element('eJwtjsEOAiEMRH+FcOZAl0LBXzGGrGZve0NNjPHfnVIOLc3w2pmv7/1x7mP07i/O3z/PY/jgoL7383VM9cotuFyDKyU42ghDxkCzibZqEuOlGLXxkiXZmmBLwIqiqFqsJl6T0sl+pgkBr3BtcWFqpjcobsjCK8fkiAAK25kMj9Ysil5T1DLcfn8dOzAG', 1)
X = X.append('v0', v0)

v1 = elements.load_element('eJw1jbEOwzAIRH8FefZgEoNJf6WKrLTKls1tparqv/eI3QWO4x18Qq33Y2ut1nChcHs/9hYiwX1tx3M/3WteIolF0oLOkUwiFegyYU6RMnaclg6UDAOaefbiavLMySiEHwNjWMvceZkGatwvmhspeQGinmX1CQ8U3218dd6wEPlnxFG/UIYQ9cj6/QG9ui+V', 1)
X = X.append('v1', v1)

v2 = elements.load_element('eJxNTkEOwjAM+0rUcw/t1rQpX0FTNdBuuxWQEOLv2CtIHGIltuPk5Vq77mvvrbmTuMvztnXnBexj3e/bwZ5T9aLmJWeUeolTBITADpAglYkDwGZ4KUeyUBVEKSSSl4okw1D+ySNOkVtY6C2MUtxTHqh0zmOV12KkE41xPcJWvzbGWP59F/IIybq8P7IcL5A=', 1)
X = X.append('v2', v2)

v3 = elements.load_element('eJwtTkEOAiEM/ErDuQeKlIJfMRuymr3tDTUxxr/bUg4NM8PMtN/Q++Pcx+g9XCHcP89jBARV3/v5OqZ6yw2BK0IRHUbIijkiECkREwtC1aGY3SX6UkoKLqaSA2bPmYONi3PrpygOzGhdQh6YaYraVefKVSrWpZhtU2zrN6m3TVte9cWu235/Vw8vJQ==', 1)
X = X.append('v3', v3)

v4 = elements.load_element('eJxFjbEOwyAMRH/FYmYIBLDpr1QVSqps2WgrVVX/vWeTKoPFcfd8/rjW7vvSe2vuQm59P7buPMF9LftzM/eaqqcsnjh4CqF4EgjOmAnGBIORhqhxhMUz+Hiw9mHlIIoJhUNSxSec59FbkUr9Nx3dAp3tmBI8rhcZI9hO2oJM8FYD0wDH2XL7/gCzXi+P', 1)
X = X.append('v4', v4)

v5 = elements.load_element('eJxFTkEOAiEM/ErDmQNlgbZ+xRiymr3tDTUxxr87LBgPQ2em05a3q/W2r63V6k7krq/71pwnuM91f2yHe07mKasniZ40gQMiqAUaPWVPZn9eUJkDnoiJDJKkCxBZAIwVGVCsNf01Jzj0g3Ek+7HDGBsDbOuE8/hQ0pExmVlepkCz5I7L5ws32y8d', 1)
X = X.append('v5', v5)

v6 = elements.load_element('eJw1TkEOwjAM+0rUcw9N1zQZX0GoGmi33QZICPF3nLU7WHVsx+k3tPbYln1vLVwo3D/PdQ+RoL6X7bUe6rXMkcQiVY3EmTuRDICbABOAEKcSqUxOKhSkFAmFo5gldc7siZw8drDsGmrKqDVYhnsKV/HaWOaUzw9Irxy78GZzck7iXkKdcUeV2+8PFV0v4A==', 1)
X = X.append('v6', v6)

v7 = elements.load_element('eJw1jsEOAiEMRH+l4cyBshS6/ooxZDV72xtqYoz/7hTYAw3MmynzdbU+jq21Wt2F3P3z3JvzBPW9Ha+9q9e0ehL1VBZPHNhGwOAESe2CVwJT+HL2tK5mEdBidBlUTnuIsOCSjYZzp8QRFOQ42v4IVaNhS+IIAsITa5kVmHl2yIhrGr/1it3Ms0iW2+8PnXcwWg==', 1)
X = X.append('v7', v7)

v8 = elements.load_element('eJw1jssOAiEMRX+lYd3F8GrBXzETMprZzQ41McZ/95bBBW049wEf19r92HpvzV3I3d6PvTsm0Nd2PPdBr6ky5cIkwuT9ghE8U4k4ypRsJ8Cl2gjw2s3DLAhV+HM8YfEm1KkqaEJBVQOQtMyIwbnNlNGp2UyARc4uM8pIhn9FnO0yn9bxq2hg/f4AwUkvvg==', 1)
X = X.append('v8', v8)

v9 = elements.load_element('eJw1TssOwzAI+xWUM4eQQh77lWmKuqq33tJNmqb9+yBJD0aWjQ1fV+t2rK3V6m7gnp9zbw5B1fd6vPau3rkgSEaIEYFCQOAFISmyiqwgoouoGxNCUcgyIuLNsKxPxooxMcaXQZrNYcR6OdmOOplmabYidVOYgliDN4fH7STjoV42Rz+lI4rh8fsDqHQwiQ==', 1)
X = X.append('v9', v9)

v10 = elements.load_element('eJxVkE1uAzEIha9izdoLmDHYzlWqaJRW2WU3baUoyt37+JlFF2D8gA/s17LvX4/bcez7cinL5/P7fiy1QP29PX7urn4I1SKjFu21dJjOWpi4ltHDmBQZwQXnwNkgNnTwuiJA+YQNb9vgWMwhErsRZaFwzOAVSjehB8r509vNcQPM6WjoSEkzVWPE4OAKhoha4hRt/XHiIbYtGa74Q5ijcVoJ0p0SQuMMWlJsf9WkkP1Ey/fNEfx4Ga0ZqXe5Q/Xssbvmh/Z/uC0KVNL4+v4DWB9SDg==', 2)
Y = Y.append('v10', v10)

v11 = elements.load_element('eJw9UEEOwjAM+0q1cw9JadqGryA0DbTbbgMkhPg7cbNyaBZ5tuPkM83zfVv2fZ6nc5hu78e6TzEY+lq259rRi1AM0mIo9kTs5RiYTlZY0ClKjaFZ0zgGtb4CZOOoiSpEyX4WN6lGqgUq6Dk5ixMo8Gnuga+YRcWoROCnYxRT8xwCHnR0OOWTA6pOKOpmWb1nhpxppEenHe9bFV+j1v+KjKI+qYdmPZLk4eRs8vRM4wTNzyAmErhQdgA3wl4yJvYkI2jXY+VuxkfswtfvDxEqUok=', 2)
Y = Y.append('v11', v11)

v12 = elements.load_element('eJxNUEsOAiEMvQphzYJigeJVjCFqZje7URNjvLt9lDEuoND36efte7+tl23r3R+dv77uy+aD0+zzsj6WkT3lGFyW4OohOIo1ONEPUQmuZM1qbE1jA0pAEl6DAzziodJhA4jEVKxJ4ali9c1lRrhE3qvpL2vkZh4olOHHxpbBVkBQKcVfcTadtN0NjcmsxWJuRHqVYsCYIYFVgDQzQKFxxlw6Uot/DEoQqpvsutgmj6Kmyt6LbQ3SOoeYmzMb9Awueqk0+8CCx6Hz5wt3NlIb', 2)
Y = Y.append('v12', v12)

v13 = elements.load_element('eJw9UEEOgzAM+wrizKEpJG33lWlCbOLGjW3SNO3vs9vAwWowsZ3k28/zY1v2fZ77S9ffP89174cO7HvZXmtlrxqGTvPQGZAigDcrUFADEliA0BHkBEAwJQiAwgZRduGPRn4ZaHpqkxkwjQ3MkACiMExamHkgBRRWzwgrQ6Fwy2jURGXwtOTRfEU4dGjaNJ7zRB+fv7O1frqwrvudZocuIKcciwVfNrdLsObSyYfn1eq1zDXZZ+VE0Ter9uYO1V6ktIuY3H5/uF1QLQ==', 2)
Y = Y.append('v13', v13)

v14 = elements.load_element('eJw9UMtuwzAM+xUjZx9MvxT3V4Yi6Ibeess2oCj676MkewfFCiVSlF7bcXw9bud5HNslbJ/P7/u5xUD09/b4uRv60VIMbY+hSwyD7z4YPQZpMQAEO5OWCYAvoxY2kFTZjARnjaQ/pMrulVY8gEXVjpxdz4DmOmJU/aASKS4m1adqFzKmkBoD+hzcmIwxbQLmx0ZiKRox1TnZW7QqlpQFWTEtH5WSXa9Q3SCgIEfs+V+8T7vrICYm8xi6Q6seut0gV4rvo371tNL9Eha4vv8AXHZR2w==', 2)
Y = Y.append('v14', v14)

v15 = elements.load_element('eJxNkEsOwjAMRK8SZd1FHPJxuApCUUHddVdAQoi7M45d1IVTZzx2nvvxvd/Xedt692fnb+/HsvnJQX3N63MZ6iWHyWWeXMWXLYggtCqJ3AJupUjSNEkn+KsJjIQhcIYQCRVWgeJoFjlEqzHJ0HGIg4pJUQyUgFLNWVijFkXJ8JcdacDC3cTU9MlUdRZLk3AZG4WDeWxWgJSjikolI5Ot0gxOFq3WpthZaSiclDPtr0LM47c120K9/2motbA30oFiBF2/P/qCUeY=', 2)
Y = Y.append('v15', v15)

v16 = elements.load_element('eJw1UEEOgzAM+0rFmUMNTdPuK9OE2MSNG9ukadrfFzflENI4TuzwHZblsa/HsSzDJQz3z3M7hjEY+l7319bQq8QxSBmDWi7FI9cxAAbkbI9pMjRZIVZE+6ROz5ZF7V1IN0aarbBZ5QQsOAHbUaIXbCBW7zZ2crDWvp9ranECIroPKiR1ZUytRVTdhzsU3wZoFyaFvklRHoJzkPdRhKrJQhp9JoUG0e9rkCQPRF6b+z+BuAi3ZPWMSDF0C86X7pewnrvbSTyQPjJuvz+jzVGc', 2)
Y = Y.append('v16', v16)

v17 = elements.load_element('eJw1ULsOAjEM+5Xq5g5Jr4+UX0HoBIiN7QAJIf4duw1DWitxEjufZduu9/O+b9tyCMvl/bjtSwzIvs73521kj0ViKBZDrTHkhugx2IrICOCGXEGtN8cagwqAqvApfOrkNM5ByRIwC4kgkcEuZYlU/mg2UFrmuDz53K+C5YU9AmrFxE4q+vPKpE0ZmsTHmnqTmUvpnSBPLdV1qYgbpIkyzdEUzaqaAxlCuT6NuSBl1zB2F/HZ9r8FzzBWU+/0uE4exdMnsf2PVdZ54yG5AlQ9fX//tFHG', 2)
Y = Y.append('v17', v17)

v18 = elements.load_element('eJxFUMsOwjAM+5Wq5x6S0Se/glA10G67DZAQ4t9xHhKHdU3s2E4/cc77vh7HnPEc4u392I6YArqvdX9u2r0USqH0FGrBn1NgGnI0VDmFTlJUFICZwSsnuchB5GwhNeC5+yQzRocg4NVhUgUqHYwOZiPDzUcawwjM1S1IxRbwMcuLeqHfRGV4V2NwcQ81ZjP5GwzjZ9UEWiBZuxvIRbPJR6bTTp69WiTZKjtPZAWXbdvikeTlGnu07p6DbI+mIYqby0zVNYeZVb5+fwiKUWA=', 2)
Y = Y.append('v18', v18)

v19 = elements.load_element('eJxFUEEOAjEI/ErT8x5KtxTqV4xpVrO3va2aGOPfBcrqoQ3MDDDwjr3ftmXfe4+nEK+v+7rHKQj6XLbHaugZ0xSQp1DlQWr65Sk0yTg7glUSkQGAo1CkwFGkEUMqRweliTTTD9BJlFIWJRZHNWArEF2TXk0S8ok0axkOQlXEYxgLVq3xPFRVW2TzpZ7gN1OLsvs2UyxqtulCMQ0A8XCaYKykLdBjSk6ojWJmk+9D7NdiC/iY3bzCOJPbXvi/F4AwZPdS/7oQXD5f4pRSzA==', 2)
Y = Y.append('v19', v19)

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

eq = Equation([c10, c11, c12, c13, c14, c15, c16, c17, c18, c19], [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9], [[elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()]], t, 3)
eqs.append(eq)
p=proof(crs, eqs, X, Y, x, y)
p.consts=const
print(p.to_json())
