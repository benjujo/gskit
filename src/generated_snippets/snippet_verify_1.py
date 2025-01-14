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

v0 = [elements.load_element('eJw9jTsOAjEMRK9ipU4R5+M4XAWtogVtt10ACSHujp0PRSaaNx77Y2q9n3trtZoLmNv7cTRjQehrP59Hp9dYLCS2QEn+KM9bKOJTsMCaCUdEEa/icFqWuchq3MJO61lwWRX0k4SxHF0aFzjOFJ0K0mhRXktVHKmU/1AYYe4DglmWlR5LjWj7/gD3FTDF', 1), elements.load_element('eJw1jj0OwyAMha9iMXsASozpVaoIpVW2bCSVqqp3r18gAxi+9wNfV+trW1qr1d3JPT/72hyT0feyHetJH6kwTcqUg80bU/DJLjiEyKQRZDLiLxm+zCQGRcbUHikehjJcIfjRkqCjKaJFrn7pihpU85cMaOlkquKJE2DzKMj9F1BRhgiWyPz7A6muL38=', 1)]
c = c.append('v0', v0, True)

v1 = [elements.load_element('eJxNjjEOwyAMRa9iMTNggnHoVaoKpVG2bKSVqqp37weClAFjP9v/+2tyXvellJzNjczzc2zFWAJ9L/tra/QekiWZLamzxA5FUgC2NEf8yNn72pkQmGuYrkwbCkjwBBraBmW0U62goo24U74VWIgwDjrGYBj1dBDfL+h2nPpN9R6Jo3MBUR6/P53wMHA=', 1), elements.load_element('eJwljsEOAjEIRH+F9NwDdLuU+ivGNKvZ296qJsb47w7LgUDfzFC+aYzHsc05RrpQun+e+0yZQN/b8dpPeq0902qZdEVvmTpnas7QRQoeKHWgAEUwSLiFzS2QGrzGoTQo6kJBznqUMGizWOTbRSqUJRapRswNp1sWjxSf/FPGWYbBqhOO2wwB80v09vsDkqkvgw==', 1)]
c = c.append('v1', v1, True)

v2 = [elements.load_element('eJxNjksOwjAMRK9iZZ1FHPJxuAqqooK66y6AhBB3Z6ZUFQtbnucZJ2/X+22dx+jdncVdX/dlOC+gz3l9LBu9pOYlm5d68qIaIJKXRpABQtypwVZASiVoXGEykrL7qnE4mpLHQEkXI4pIxfmCfVYU3wzpP0aUEWqoBHuOP62qbJuXpyJ4soMr/zF9vjj2MO8=', 1), elements.load_element('eJw9jksKwzAMBa8ivNbC8j+9SgkmDdll57RQSu/eJ9t0YYxG0jx9TK37ubVWq7mRebyvoxkm0Nd2Po9O72FhioUpW6YSmMQ6phRRAKYygYgfVcZfMoDDfADQfXECik5286k06W6cElE9SNYIUaO1I0dEtX0G/QgSvBZxKEX6UX4c9G8lTYCmLGpZvz8ZCS/4', 1)]
c = c.append('v2', v2, True)

v3 = [elements.load_element('eJw1jkEOwyAMBL9iceaAkxpDv1JVKI1yy420UlX17/Wa9ACC2fXIn9Daui+9txauFB7vY+shktHXsj83p7dLjSQlUtZIPE2RqgFAzQYYqUG1k8VAsqvgYyMyo6ED+Kz3mfFK9R8mhDykcIieHjUolgqjCjvjlSyvpxV9bFbc5huVkWA9V6cZtfv3B34sMFc=', 1), elements.load_element('eJw1TksOAiEMvUrDugtAaItXMYaMZnazQ02M8e62FBc079vyCb3fj22M3sMZwu392EdAUPW1Hc99qpfSEKog8AkhxagjZwQpf5aaoWRIE6TJWpfHbKqNqJJorZZlp1mozhq7I83fdFkXiBlaY6snN4k87O3sQTI8r8X1G2N20WpE1+8PDCsv3A==', 1)]
c = c.append('v3', v3, True)

v4 = [elements.load_element('eJxFjcEOAiEMRH+l4cyBLhS6/orZkNXsbW+oiTH+u1Mg8dBSXmemH1fr/dxbq9VdyN3ej6M5T6Cv/XwenV7T6knUU84o8aTBEzOaRhRgYVQBDGiqEy4AC1rqGzVPGgF/LdZFBxCbs3nCOKFQF7wlmjrOwTIUGcLzwyEPrSV3MzOiFHtdR2yW7fsDvc4vlQ==', 1), elements.load_element('eJwtjsEOAiEMRH+l4cyhRSjgr5gNWc3e9oaaGOO/OwUOwOvM0PbrWnuce++tuSu5++d5dOcJ6ns/X8dQb7F6SsWTZk8FRxPe6EnEhAuADWSBFgP4RS3DgKGwVYOCXaAcFwhbFwmzb7VumFEtAkOrmZYIPBNJViEMLyOb8CfmycJpbZDCGhdtfd1+f+DBMLE=', 1)]
c = c.append('v4', v4, True)

v5 = [elements.load_element('eJxFUEEOwjAM+0q18w5N1zYpX0FoAsSN2wAJIf6O3RQ4NMsc17Xzmtb1fD1u27pOuzCdnrfLNs0B6ON4vV86ui9xDsXmUHUOiiNSAOBIRMlArGHaCCSWTI6A3KGFf4AUTWsuY8uQ6YWo4hHDUTBLHV8KRftJkoZRxmUt7oXejAwxH1hyHYkssvi7CrQIUfpP6AodRDS5347DigKp9JXS323n6Z/HWKK+A40jrMQ6bFgZqonm8iD33eQ22IzGjXH8je05kucXQWkUEGdWObw/eoVSkg==', 2), elements.load_element('eJw9UEEOAjEI/ErTcw/QLaX1K8Y0q9nb3lZNjPHvQkEPhTAMw9B3HOO2r8cxRjyFeH3dtyOmIOhz3R/bRM8EKVBLgRd5OQUEKZoCRTIKkCU06VA2BkkDUcDiLNb8IyneTQFRtDtLIdpEkskldQfrYm2AMpUOLk5sdhDY1xd2jg4hkJPLnKpKAhttXRH1RKbTpjrb7kpm0Bj1t+UfcPFj3Eid+n5R7y6Pfp4KzMJDcRm9kNlNQ/crF/+KbN6UpHYqXj5fMJJRZA==', 2)]
d = d.append('v5', v5, True)

v6 = [elements.load_element('eJxFULsOwjAM/JWocwanzcPhVxCqAHXrVkBCiH/nLnHEYDv2ne1zPtO63vfrcazrdHLT7f3Yjsk7VF/X/bm16jmJd0m9K2KWYIt3QTIdkBDgMspVmMzeaQEHRf3zANVCGC7C1Gitj1TGisiBUslcRkuwAVytERG9mZIaivG58YFENWrbY+rSf1uvUFEZk2PrrdZHGRoMFiSZWsUSVslPS39TRGw3RjpDOSNI6FDiMBoYaR4yaz9CxxGzdEYZf6pN0NL/J4fL9weu+1JC', 2), elements.load_element('eJw9UEEOwyAM+wrizIEACWFfmSbUTb311m3SNO3vSwjtIdAY23H69b0/tmXfe/cX5++f57r74AR9L9trHegVY3DIwdUcXJO7zGqCcxEcpZr0VW4KjvRdeoTgIOoBoqzF1JAE4ahPaJ4AzcwwiVi+S56GykonlUzHVSVyIJleZWMERJmBeU5VJ4jZ8mkWVl6k6alpTTBiCrnyHNtOvzY5Nc3gaqo7j+b4GQBg++nmrAPgoHA2P6K559h8iKvZauFYKR6ZRyCxIjSE4Pb7A/z6Udk=', 2)]
d = d.append('v6', v6, True)

v7 = [elements.load_element('eJw1UEEOwyAM+wrqmQOhhNB9ZZpQN/XWW7dJ07S/LybpIZA4joP5Tr0/9vU4ep8uYbp/ntsxxaDoe91f20CvnGLgFkNdYlg0KJMfolXRDtEcQ2NPFkVEg0XBDFBpVQyAGECMldlrTCcQoanBsxftTIjQT2JEERNcBlhUSTe0ag2uPpexOyFL7G240LsoTYBBQ2xchhaOjA3ZF4M+DOBNDIuJTAzLAUoxN/iecu6trghA2J9glth0hhaEKVXjtXIans9PU06l2+8P9YxRLg==', 2), elements.load_element('eJw1UEsOAiEMvQphzYIyFIpXMYaMZnazGzUxxrvbR5kFBPp+bb++98e+Hkfv/uL8/fPcDh+cVt/r/tpG9coxOJbgKgVH1PRTghM9uWoh6qMwHmRITcE10LXYVCpQgEmDzlPD2ehE6cRoUdUCXH88HkqSPGV5VKI1goQiRgOAFIp6lZFyUtEioAo4jaQycxPGYjvCJuQ004cV00xuWslwoDybgi+GI0KImFrIehojSTVbOXdjBtXS8UHb2BxOzWZRii1O4rQDTrffH5kyUZw=', 2)]
d = d.append('v7', v7, True)

v8 = [elements.load_element('eJxNULsOwjAM/JWoc4ZcGscJv4JQVVC3bgUkhPh37MRBDH7obN/Zfk/LctvX41iW6eSm6+u+HZN3gj7X/bE19EzBOyrescSSvKsS0+wdIE6LgLogLVWMsiEERaMMihHZMEvUAqS1CJhrL5RiHEA1btYkNPdrUEm2RJFUbSw3dGgjomshhq7BqZuKM1kBQW/RTWSQ82CI0Uq1ji3Ypufe22R1UU0Y1pHKWBh6GRkLAv71GiHSOFdvo9ip2Z7S/xc7fbYvZVw+XyOzUwI=', 2), elements.load_element('eJw1kLEOwjAMRH+l6twhV5rE5VcQqgrqxlZAQoh/585Oh6bO5dln+9svy/2x7vuy9Oeuv32e294PHdX3+nhtrl5yGrpsQ1dH/hnPNWLjh3SiYApmHpiIUKnESpXqRyY8BZcpWI4igIRCnI+T0rxGDTGTKjlojKl5AQdTyFjjKiIHyFHN0ChAUVK7atuCRUKDvcPwtXj3SUx+oJ9Z9C43ZVppY3qgZFlVr0SltD1h1IEx5vKbVmeq6GbpaOQoE4OltlfB09xUbaHg+vsDRxRShg==', 2)]
d = d.append('v8', v8, True)

v9 = [elements.load_element('eJw1UEEOwyAM+wrquQdCCQn7yjShbuqtt26Tpml/n0PKAeEE2zj5Tq099vU4WpsuYbp/ntsxzQHd97q/tt69cpwD6xyEcBZgnkNBTRGFAuTqjYrbyBmYQeYMQQIHd5ZTwMlAGXKj4BQ8Z9SU7BNxHUUzXE7D7KYKKeNoJ1gMMh+TResYpYPoRmWEk7OpRuczSIojjSHtU7HbKYTC/jmRur9U34GNo2MIojwMxMP1ohTn92cbkmXYV4/QC1mGf+eKL5rIctum6fb7A+qvUUA=', 2), elements.load_element('eJw9UEEOwyAM+wrqmQNpmxD2lWlC3dRbb90mTdP+vhjSHojASWzj71DrY1v2vdbhEob757nuQwyGvpfttTb0yikG1hikxKBkJ8dQ7J7ZcHtTUhRGsVEarejc+0Q2IOgT0MlQA9i7s7Hw1FmAZ7uXjOHGaFPCXQ+bRAbM6m0l1xNxCxkXmjq1li5zGNYRTek60jSyj7O4WDm4T8PtCwmrY5Mr515yOiKk4i5hjkdvQ93XjlR6wQYclPZAiIgCrCn7d8hIVHvMiADRC91+f9BCUtI=', 2)]
d = d.append('v9', v9, True)

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
pis = [
    UnamedArray([
        [
            elements.load_element('eJw1UEEOwzAI+0rVcw+hDYHuK9MUdVNvvXWbNE37+0wgh5BgjDH5jrU+ju08ax0vw3j/PPdznAag7+147Q29cpoG1mkQ3JQQyorHTAiEUKzElgAuYpzsaMbRYhXxbsnRw0B1wUGfAly7tILJsyWzM4hQFtDZKqlXKVRV7aFRAm1VV+XsLZTE56r0+TYXVlcAuTPMRFvCEnPD4UrId3CHEtOy/UAKEVNt26X4hBwe2mfMXYR7m1lOi9stHBrF6SVYdrdDt98fWNRRAg==', 2),
            elements.load_element('eJw1UMsOAiEM/BWyZw7AQin+ijFkNXvb26qJMf67HVoO0OdMp/0uvT+O7Tx7Xy5uuX+e+7l4J9n3drz2kb2W4F1h76iKjfKKd03iGJN3NYsTEqLVuyzpIpnWJJGC9bQKR9JlOIAGwCJ5x9LEEpD4GeUEUpnCbBQAYbROQRkCBrjyJG/zC1KrZI1aS6ZnzMRXaOJNUzUBNLYqqkj7oQDTUYKswRvDqnsybNAHAszJzazUqNlhlFA4OM7LQCmZCCwCVSq4KhDnQDt8irffH+VnUmo=', 2),
        ],
        [
            elements.load_element('eJxFUMsOAiEM/BXCmQNleforxpDV7G1vqybG+O92StFLaWf6mOFte7/t63H0bk/GXl/37bDOMPpc98cm6Dl5Z1J1pizOxOZM5Zx84oSBxiTRgtAQGC5p9JInhAI4cnfUKgLxbSSl6iiuyETOf0ZAKjMEGttbURUB0pLSSfoYydIblBcoBdUsFVxEVljDYPAOIWINjEjP0yxkwTBmJ4CBUfwSDEKIsnX6hyWoS1jYhgdVg0q08epW58f9fjjqWlzPdPl8ARrHUvY=', 2),
            elements.load_element('eJw9kEEPwiAMhf8K2XkHOoGCf8WYZZrddpuaGON/9z3aeYCWtny8x2eY5/u27Ps8D+cw3N6PdR/GgOpr2Z5rr15yHEOuY1DEmpFPiKcxSMRB1RoNSyZsmrAwUdAU4VU9RicmhXMkMIlIEvqFeCCLWrQmaY0UdrFKP+SDwrJEYdaPySUitmqKEmIVZ4Kdi9VJosCKqHJczi6NFgxMQ70nUf1Zyu2o6GL4Xv8OGz78dbeTW8i03zt/aqwmoTUH85/U/ZtlEqS5Wrl+fx6hUnY=', 2),
        ],
    ]),
]
thetas = [
    UnamedArray([
        [
            elements.load_element('eJw1TkEOwzAI+wrKOYfQJITuK1MVdVVvvaWbNE37+0zWHEDYGOOPq3U71tZqdTdyj/e5N+cJ7Gs9nntn72n2lNWToHhiT4oSkMwRIHlK0QCYgg2HvhIgDDOOcmcLtNDljMKck6lsmLAoA5S/vZ2akgOayvWLg15OHOKwiONBl4NSCwLT0vMGxLPwsnx/gKIwXQ==', 1),
            elements.load_element('eJwtTUEOwyAM+wrizIEwAum+MlWom3rrjXbSNO3vMySHBNvYzte39jq23lvzd+efn3PvPjio7+249qk+8hIcS3D1FtxSMeAUkxKiAoBfiXgxw01EENhAthwlssXJGtRs3UR5LEgy2chH1maBuYgFIk4yvLlqMRfFIpaYJQzAUY8VXn9/IOQwAQ==', 1),
        ],
        [
            elements.load_element('eJw1jrEOwjAMRH/FyuyhbpPY4VcQigrq1i2AhBD/zrlJB9vxO93F31DrY19bqzVcKNw/z60FJtD3ur+2g15jYUrGpAuTTIoloiamnJkKRBFv8+Sy4wQ596mzQxgjSssJpIcUczOIeaIOG6DBGg/xzJHxty3DktUfybE3QYKVniSCK0z7gSLiEbffHxbVL/Q=', 1),
            elements.load_element('eJwtjsEOAiEMRH+l4cyhXWkBf8VsyGr2trdVE2P8d6fABZg306Hf0Nrj2M6ztXClcP889zNEAn1vx2vv9JZqJC2R8gW3RnJtBo23CjS41eGLpEgFojBMdrBApOn0CGNGvWsZs8I68+qxTpCtPGIiGYPVaXHlpdwP7GBABT3q+/hPMqqyzagbZuvvD61ML3I=', 1),
        ],
    ]),
]

eq = Equation([c5, c6, c7, c8, c9], [c0, c1, c2, c3, c4], [[elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()]], t, 3)
eqs.append(eq)
v=verify(crs, eqs, c, c_prime, d, d_prime, pis, thetas)
print(v)
