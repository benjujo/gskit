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

v0 = elements.load_element('eJwtjkEOQjEIRK9CumbR1raAVzGm+Zq/+7uqiTHeXaZ2Q2YeMPAJvd+PbYzew5nC7f3YR2By+tqO5z7ppRhTVSbJTHpiMnGfmFJ0YNEbDlPKKFDZe2pwiiGo2FAErP0DzHu1MrUK6CGGK8XDCgBonDd0HVoZrpqLMvHcxXzOy0oE8kU8rboMPhfB5vX7A2aRMSc=', 1)
X = X.append('v0', v0)

v1 = elements.load_element('eJwtjbEOwjAMRH/FypwhLnbs8iuoigrq1i2AhBD/zrnpYvtOz3ff1NpjX3tvLV0p3T/PradMcN/r/toO9yZzJvVMVjJVbJ8yMUMYDrtAFAsHWKDGwBXbwwwEJk8cqo6EGc+uA6vwJNCiZ8U8KtwGGHmCFo9siZSIKnXQWkLEYDk7Cw7Bs4KrR8Py+wOLkS9i', 1)
X = X.append('v1', v1)

v2 = elements.load_element('eJxNjksOQiEMRbdCGDNoBUpxK8aQp3mzN0NNjHHv3gIDB/2d29/Ht3Y/tt5b82fnb+/H3n1woK/teO6DXlINLmtwgsgsSGCKohigZJTREkGg5GKUplxHsVRmModMTyuxAcmQEcuA4wiuKf9dVIBKc4uKrURvpjnLBJfieqOg0DjbbYc9KnL9/gDu+i/M', 1)
X = X.append('v2', v2)

v3 = elements.load_element('eJw9TkkOwjAM/IqVcw7Z7fAVhKIW9dZbAAkh/s44Db1Y49nsj2ntvi+9t2YuZNb3Y+vGEtjXsj+3wV5TtZTFUimWGNi7iBE8hg+g8gTZWZKgOoMVBUgUPhRmtWkVgmk0OLXAxwOMmjg37ZN49BUNKa5/R5pBH8Y59eKSyFwy9IpF/Nlb9f3b9wfNITCa', 1)
X = X.append('v3', v3)

v4 = elements.load_element('eJxFTrsOwjAM/BUrswe7JHHKr6AqKqhbtwASQvw7vhqJwa/z3dnv1PttX8foPZ0pXV/3bSQmR5/r/tgO9JJnptKY7MTUJibMGb1XKx7KpDoh+aTSfusa1YRptuiLR/Z9cXaFrUXABhxgqvlPgvgASoW1X2qwxkXJoTFcFkOSEKq2+BIf1rp8vi+pLxs=', 1)
X = X.append('v4', v4)

v5 = elements.load_element('eJw9UMsOAjEI/BWy5x5Kn6y/YsxGjTdvqybG+O8yQDzQFoYZhn6Wbbvez/u+bcuBlsv7cduXRFp9ne/Pm1WPPSfqkmjWRJxnoqbREQrMkWhMAOhqiVbtZMaRweFE0vUGWlDUQzRGDw6XEhA3h5gxqLCzTGs2n2jQOkMTQIlBXX2I3kPcl/HxQKdU9wU3CJMRBdsKulmpMc4y4B3WVbVV31CCY+o5xmCNMfwb0PwHoWyOc41F4e6/bLMk1HwJdjX8AEZK5INP3x/LLFDz', 2)
Y = Y.append('v5', v5)

v6 = elements.load_element('eJw9UEEOAjEI/Eqz5z0ULYX1K8ZsVuPN26qJMf7dmZbdA9AyAwx8h3m+PZZ1nefhlIbr53lfhzEh+14er3vLnjWPSX1MdhiT5ExX4QSuwrwAmhCPTMIVmLbPzs0THXNZwC6dbYYOirgVge+tNSZNLDng4cYM5jvgug+iIA1BSlpQtUZz77JEMNG1a1VEla1n2fq0xQA5Ie+mpQNmIYi1nEig+KbSY2m10NIWyHGbMu1zpK9kiMW6AkbeQkM635IpRjTuxX2rXH5/jWxRmg==', 2)
Y = Y.append('v6', v6)

v7 = elements.load_element('eJxNUEEOwjAM+0rVcw9NaZqMryBUDbTbbgMkhPg7SRoGly6J7djZK/Z+Xedt6z0eQ7w8b8sWU5DpY17vi01PmFNAToFKCgCYAjcpsnXyNO0KaDdpVb5MEplISXAWhL02MGel6gOmVAsrDvpU6aRotPuIa+WhN5nCRMOchU55fG0TCZNFhkpQ1cFT6nYbokcwpq5gT47FaUwDJU+GmkCuwDZmAM1PYyfYT5GCpl8syLo4V3fJw9qosCP0J7ZzNSLVwW26Dc7vD7r5UaU=', 2)
Y = Y.append('v7', v7)

v8 = elements.load_element('eJxVUDEOwjAQ+0rUuUMuNLmEryAUFdStWwEJIf6OfZeFIZLjsx1fPlPv9309jt6nc5hu78d2THMA+1r352bsJcc55DqHUuZQBQdYBCArQQKTAWLhDahBrzgFY3o1OTaFqssLQpSOGB20NsKapXKUIud1oAWCeuKFL4KoiWMwGV0WTqJ4S2vHmq2OTv72Msozk24aJWavaUTyJG7GyiqjoSmZass1T6baFKJO2raIU+aTQ1RpY+nod/5g/jORLOM3k3isSHNrkev3B5R6UQI=', 2)
Y = Y.append('v8', v8)

v9 = elements.load_element('eJxNUEEOwjAM+0q1cw/NaJuUryA0DbTbbgMkhPg7cZIDlzZ1HNfOZ1qW+74ex7JM5zTd3o/tmHJS9LXuz83QSys5NcmJKScqJz1o5FQFRdeWIlUBrjn1BlCLVoNPHAf4Q2/RWzqU5n/KrK/OATeV6RJSGKCiREbHJiFT0cZ3ZfgAkVkDcQSRZn+wDrBxYU3jVI4uleL/WsjmVHQbdIApSUZENRtDwi78WGGysNm7Z+SgQZTFa8t+8lxsEsV3RkV8X7YZ8WVCSVSlo6br9weX+VG0', 2)
Y = Y.append('v9', v9)

c0 = elements.load_element('eJxNUEFuAzEI/Iq1Zx8gMWD3K1W1SqPcctu0UlX1750xjtqDMWZgZvD3tu/X++U49n17Kdv71+N2bLWg+nm5f9xm9dWkFuu1uNUycOtJEXTUEg0I0GBVT4QQzGtpQNsZCE7HGSNvFWMXZrpwxpNANZCQQBpfCLH4VRaU8F8AUcwEbhw9faTckMVAzSkVQANd9s/QJGFrn4JzIw6KrJVo2BKmVbLPFbsmoZGQy+gzhKVJjswcY+7LB3l7pD59eM/b2vPXYvnxJSbn/HLXt59fIC5RPQ==', 2)
const['c0'] = c0

c1 = elements.load_element('eJw9UEFuBDEI+0o05xzCJCSkX6lWo221t71NW6mq+vfahOkBRAw2xD/bcbw/7+d5HNtL2t6+Px7nlhPQr/vz8+Hoq5ac1HLqPacxcmoIkYlUgE4USqQI2oWtfaG28+HDgI0BBdmvGXMWUnetYE1uUkg1gnrp2YrBEKpIkIeTkbrLVRTGgqukB2vEAnW9GhqCl6Kwea3aMTPqmuMxPMQ1+bE1VklssXwR/J8SfhgF0adr3vYrmsVd7pvU/wqTQ5dGAzpL+FZaWKqX27yly+33D0GNU5o=', 2)
const['c1'] = c1

c2 = elements.load_element('eJw9UMFOxTAM+5Vq5x7ibV1TfgWh6YHe7d0GSAjx79hp4JC0cR076fdynm+P23Wd5/JUltev9/u11EL08/b4uAf63KyW5rUcvRbYwYKXvmVAIF+9MXhiJeJrLTtfd7WAaFd/U7EpmZJKI8H3WoYlrAKGeVF00lpQpUmZEZoxC+HepxNs+2tWAqbnyFE9bKnQpDIIMpos6Dk8B/sfN8z0JFrsjDVXAlj5MbukNueR9JZSq+U3ACO1RITZlIhCG0hGv3J4GsQUQh3pFBLBwcvPL3pkUpk=', 2)
const['c2'] = c2

c3 = elements.load_element('eJxVUNEOwiAM/BXCMw+UwVr8FWPINHvb29TEGP/dlhbNHsbo3fV69O1bu23LvrfmT85fX/d198Ex+ly2x9rRc4nBFQpuLsEh/yFBcFQMmIPLpEThuoo4M8c4AB/IBVYmkIkkIGo3RGapy7gi8ZxUDnEadL9UqwCyQcBHZZiiqVEuQDYTgN0y8xJdZuGkaecxN6OmoqyxtTeSBUhJBxUUlM1QksdoYbsGqvpRtnYs44VZpxb4hUqHnNNxZ39jWYe8S7Y6Ntw/uHy+ojNSLg==', 2)
const['c3'] = c3

c4 = elements.load_element('eJxNUEFuAyEM/AraMwcbFoz7lShaJdHe9rZtpKjq3zO2adUDYA/jmYHvZdsex+08t235SMv99bmfS05An7fja3f00iinNnLqWG3F2XNiamgERWEUNafRYilYzLiRYgX4Dfyu1pR/g2J8cBX1qIENsAXs1TV864EwWUc2p8HvZk5kHAqUqYescERpOHubF04bKAb9IRocs/Yn6K+tuSk6qRFKfabaVmYEdwYiY5qwT5t1iYQikd2kZS6zW2u82rV0kiyzfexqKsUUZvjO1583H8RRYw==', 2)
const['c4'] = c4

c5 = elements.load_element('eJw9TkEOwjAM+0rUcw/JWNuEr6CpGmi33QpICPF3nLVwcOLYiZV3qPW2r63VGs4Urq/71kIkqM91f2yHepktUtJIGV1LJJGEwuU3CcgUqUiHcAaBk04Aw0TPuC/QDbpBS/LPgSsTO4Nm2qG+z/3ORobI5AUpCsXwTXEczjxiMah5oK+yjT9zWj5f8Acv2g==', 1)
const['c5'] = c5

c6 = elements.load_element('eJw1TMsOAiEM/BXCmQNFaKm/YgxZzd72xq6JMf67U1gP7bwy8/GtPbel99b81fnHe1+7Dw7ua9mOdbi3rMGVGhwDK4MXoGmgWhanppghEgiByMUIniIWuEXMsBeLPcvj8NLcGjWK9VxL6ClyUYvgSP53LaqEk3Mo42qayFYmpDIIz3Hm+/cHgI8wWg==', 1)
const['c6'] = c6

c7 = elements.load_element('eJw1TTkOAjEM/IqV2oVnyclXEIoWtN12ASSE+Dt2vBTJ2HN4PqH3+76O0Xs4U7i9H9sITMq+1v25TfYSG1OqTAVMVXRO+gwXJiz2QZV4UrUwNXOqA6JLUTIXtyZDmFD9ThNPQNRexAZ4fmaB5rSF7Ej9kykeoVkMWLx6ycSpHG1Z/Tldvz+wVC+P', 1)
const['c7'] = c7

c8 = elements.load_element('eJwtjkEOAyEIRa9CXLuQGYWxV2kaM21mNzvbJk3Tu/cjLhD+Az98Q2uPc++9tXChcP88jx4igb7383UMes01UtkiCbJIJEXO0Jw00lZQ8IoCwiZ5WeZToTR5p0AXtlF2yGxuOskmTgvcFFEywkzzXFOtqX6D+XKq/ovTauvS9DA6jmA3Gm2R2+8Px+Qvug==', 1)
const['c8'] = c8

c9 = elements.load_element('eJw1TUEOAjEI/ArpmUOppbR+xZhmNXvbW9XEGP8utHhgwszAzCf0fj+2MXoPZwi392MfAUHV13Y896leckPgilB0KBoQI4iqlMhYViY6qnJCsHuK0RxlLM745ItkW3hZ8o8iWilEBkk/m91Wj5nlZmXxx+JxdtZk1ZYpKjQltXg7mcPX7w93IjBh', 1)
const['c9'] = c9

t = elements.load_element('eJxVVstuGzEM/JWFzz6Iu3qxv1IURlrkllvaAkXRf69mOFScg7G7EikOh0PKf2+Px4+3l/f3x+P25bh9//Pz9f12P9bq75e3X69c/drsfrR5P/r6tXo/zHy9lLUw1vO8H6Nos2FzLY7rfswug7XY1vtc79Pi3cqytnO5VlhccMOKrRUf2F8RZgsHKyvm5Pal84HIrGBvGQ2LH89wDzw0HkOxT5iuherhDHOcb2WZzhIu2Az4a6dzt8dHvYSJ6QM3EdC5x8d0Aeg9MuquzBC3DREAdKcopH/NdM0QLFM9LZLHRzDmihzcmcVBBFSGwGMfcacKQxKySoy93LxEQoNstthoYpXgTgW2cgZNQztwReFBMhK3s6hqYDpqWCw4gCCqVDOYn3JjhVywGYJlKiIf1SC7pwKiElHwLjFQXk1US1LIH1ltdzuT3OQUxMG1yZUAAlrmOeMQggGyKOApjcyAiszx7GNXQwVAPPj7FLUIxYOTHkBz1RScuwQRgXBwf1JAcNZChBtukLdsZlV6rFyJSobWa0iDYar8AYhiqBKAqSG6WpchS3I2tqI9qki9UogjixUvHvx8FMqCaDYl9DAvrSIUjhsaEqNmW6ORp2QjILsLm0qEPSYwohhk5hJNMEUc8vBpWlAmJQXgwRs1M6NVugvnFiDFBzgwhQhnqrrl4PDoKraCiXaERCVH+5gDpAeghiKxLld4TKmWolOoD+AivEeW/Vl+Z6x5zlF2ffJIl5BL2YOyBiTPvh5ZLTI/njs3zdjY4ojl40qMvaruHzmAKLOeClDjR8/Srj81UHaFxbiPAbcVaKlvl5y7sp6Zzcx22HOsjBzBZ9pIMDndQxMlWeXlc2WgDXdqBpegYUzBR2czZ8tbo6sbOQVoMhOU+jqFvk/GRvREJnXuoS7u43L5JFZTB+aQLNlMc89dqYoCAIVNkooBYTqN6YKBPY55aSdhTG3PFoYBz65b38fTGIpLeoislFwTUa56V09lKQ/PetRkRTcNK1vU2nBzV17BqiTPcSq186YqqVv+y6jf/v0H7+KYLA==', 3)
const['t'] = t

eq = Equation([c5, c6, c7, c8, c9], [c0, c1, c2, c3, c4], [[elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()]], t, 3)
eqs.append(eq)
p=proof(crs, eqs, X, Y, x, y)
p.consts=const
print(p.to_json())
