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

v1_0 = elements.load_element('eJw9TrsOwyAM/BWL2QMQDE5/pYpQGmXLRlqpqvrvtQ3p4sfd+c4fV+t2rK3V6m7gHu9zbw5B0Nd6PHdD72lGIEbI0kPICCUhcBBQe1SQLkYks8o8a8laShdl0fA0ZiHISFlIHaLZpHGp2jL9EY2SjejyjL7z9pG3cN9d2ZDxX6F+RBa/fH975DBI', 1)
X = X.append('v1_0', v1_0)

v1_1 = elements.load_element('eJwtTksOAjEIvQrpuouhlsJ4FTNpRjO72VVNjPHuPtouCLwP8L6h1se5t1ZruFK4f55HC5HAvvfzdXT2ltdIYpFKiZQvkQyYEwPYKFlQEJgTBrgKHMXGrMusboBgeQ5ZwboDp1ZgFXRwovO0jn/M5g/TUNzZU/gmBPU0rDOSR7Fu90xYKbL9/goLLwM=', 1)
X = X.append('v1_1', v1_1)

v1_2 = elements.load_element('eJwtjrEOwyAMRH/FYmawCWDor1QVSqNs2UgrVVX/vefAcMh65zv8da1tx9p7a+5G7vk59+48gb7X47Vf9B6rp1Q85eRJRDxVxcARFFIA2zCJAOQMIwAsmA0GsXWE1QoYtuaJNY6gFYlc/Ys9POLCMpcZJBkJaC46v0psFk4rddgWKlCFoTwuNS+nx+8PDnAv3Q==', 1)
X = X.append('v1_2', v1_2)

v1_3 = elements.load_element('eJw1jsEOwjAMQ38l6rmHpSxtw68gVA20224FJIT4d+zRXSL32XHzCa3dt6X31sJZwu39WHuIAvpatue608vsUaxGKSmKpgljAqkzhBpEiZKdFMROFMxopYLnDBsfaeCaEUQm7xGMXOhgNcPJNipYWuCY/qHzhqOIx9Dc00epqo/dgrKaxufO2PX7A08tMEI=', 1)
X = X.append('v1_3', v1_3)

v1_4 = elements.load_element('eJwtjbEOwjAMRH/FypwhDnWc8Cuoigrq1i2AhBD/zjnu5PPdPfsben8c2xi9hyuF++e5jxAJ7ns7Xvt0b0uLJDWS5kgNWlOkgskMUfkUKp4WTFmwgxCERhfTimLC0pKfUDuRISR7a/4BUY0urtUotsIFgTrNbG110sya7bZV88nPisFF1t8fBhIu9w==', 1)
X = X.append('v1_4', v1_4)

v1_5 = elements.load_element('eJw1TssOAiEM/JWGMwdACsVfMYasZm97Q02M8d+dWdZDm3m0035c7/dtGaN3dxZ3ez/W4bxAfS3bc93VS25e1LzUk5cYEkghiF4aHCNJAQCCwrVGt7JhQQMBZjKUwtmIqLLb+gdoFaQao9KMKm0KRjEeV0l4IwbEKtYMa5ZnzZfCcYbpluaPRa/fH+tvL9c=', 1)
X = X.append('v1_5', v1_5)

v1_6 = elements.load_element('eJw1TrsOwyAM/BWLmSEkYEx/papQGmXLRlqpqvrvPTuw4HtwZ39drduxtlaru5F7fs69OU9Q3+vx2k29x+IpiSfGzNlTCAHPxGDqLKqApORJYJeiQuqqfRYLaMWIKyiTEq3IPWFdM+wIIIMoYLh2hzUt1yY7aFYBRORqjDL2cY9gMj9+fyD9MAY=', 1)
X = X.append('v1_6', v1_6)

v1_7 = elements.load_element('eJxFTkEOwyAM+0rEOQfCgMC+MlWorXrrjW3SNO3vcxjSDpjEcWK/XWv7ufbemruS2173ozsmsM/1fByDvcXKlAqTXpiKZ4qokzJV4yKTyABBl/Dw5wzCQ66QpYA1naQYhGCAS7WaDktRZxPEROiGqUxD/RmOAGaa/0FKnVctSRlBMFE/Y9k45+XzBZIlL4M=', 1)
X = X.append('v1_7', v1_7)

v1_8 = elements.load_element('eJxVTkEOwjAM+0rUcw9NWduUr6Cp2tBuuxWQEOLvOCkg7ZDGdWLHL9fadV96b82dya3P29adJ7CPZb9vxl6m6imJp4wqwMzBkxRPVYkErMOMQeQBfsVBvqzpYlDxgbIF/iN9pA73DOeKLtgVmJUJPY0YGkn1et2OacQT/lHt0jDgoIw5ze8P2S0v6Q==', 1)
X = X.append('v1_8', v1_8)

v1_9 = elements.load_element('eJw1jsEOAiEMRH+l4cwBWKCtv2I2ZDV72xtqYoz/7pTFAwPMdB58XGv3Y+u9NXchd3s/9u48wX1tx3Mf7jWrpyKeOHiKMZkskFBMsidlO0TzYZWKhV2thTSP2VHlWaiIRM9RMV5CzLgwIBXditdkcgZZAGFMCgwxVuD/fwZUTepZiilNi5GJ/Sssxl2/P6BHMHQ=', 1)
X = X.append('v1_9', v1_9)

v1_10 = elements.load_element('eJw1jsEOAiEMRH+l4dwDVaDFXzEbsm72tjdWE2P8d6cQD6TTN2XaT2htO9beWws3Co/3uffABPpaj+c+6D1VpmxMGpkkJiYDUGUqbqjDC6CgwUtXGNmhj8uw68Qi4AahDupMHKlSIBCiqIZaberBMGDo83+9G/7bYUG+xZmovlXivMlNiX5kXr4/LvAvIw==', 1)
X = X.append('v1_10', v1_10)

v1_11 = elements.load_element('eJwtTkEOwyAM+0rEmQNpCQn7yjShbuqtN7ZJ07S/zykcMMQ2jr+htcex9d5auFC4f557D5HAvrfjtZ/sNddIYpGUIzEvDgmQSiSTSFlxw2KQFXPxo26A1eCs54CHQJE8VdZBqE3VVmcBBcHiG1jmQsMnWedirWNwi1cyGNRbJS/iaYszeTRirp54+/0B4GUvsQ==', 1)
X = X.append('v1_11', v1_11)

v1_12 = elements.load_element('eJxNjsEKAjEMRH8l9NxD0m26rb8iUlbZ296qgoj/7qSt4CGQTDJv8na13o6ttVrdidz1dd+b8wT1uR2PvavnWDxp9pTUk7B4WiMqoSCUPEp4hbCgCTK3bEOAD34R3OZgd3Yj3WHM6cqmsg52+m0VGOURFDubZ1IHi2DMYs3y94Hlda4RsC026+XzBU13MCs=', 1)
X = X.append('v1_12', v1_12)

v1_13 = elements.load_element('eJw1jjkOAjEMRa9ipXaRn8FZuApC0YCmmy6AhBB3xx6Hwkr8/Lx8Qu/3fR2j93CmcHs/thGYlL7W/bkd9HJqTFKZsoYkjayxMAGRqYpDxDKrcSZF9Vos0U9RLYu/h2WCtSE5bGYCTgXWFn0lklHzs88Aqh9gGwD508V9U63a2pyY5fr9AYbeL2w=', 1)
X = X.append('v1_13', v1_13)

v1_14 = elements.load_element('eJxNTkEOAiEQ+8qEMwdmgZlZv2IMWc3e9oaaGOPfLSCJh0JpOx3erpTbsdVaijuRu77ue3WeoD6347F39ZxWT9k8afDEywKCBwccWRqBbYBMZE9JkWp3RIDzSDaBeY6I/ggzmgyydAvyqqNFEwxA9W8NBxnxTuYSi7OfQeL4iWHOuBVfPl/TGC/a', 1)
X = X.append('v1_14', v1_14)

v2_15 = elements.load_element('eJxNUEEKwzAM+0roOYckjR1nXxkjdKO33roNxtjfZyUu9GBaybIs5zu19tiWfW9turjp/nmu++Sdsu9le62dvVLwjsQ71opxVpC8q1VBYO8yflICUp1EaFRYtAggaD9jMhhDBZKsEpQC0m9W25JsVuhkK9VYbCTtIA6XMTLW1WGMEcnYpN0qthsbevKQbMUIS0ZJR3H02Px74J4xYOC4A+41mH68AFg5xWUeF8psx8XjhGiRYZ1gEsnCl3kUk70pF3tp3Meq4Hj7/QGTrFIo', 2)
Y = Y.append('v2_15', v2_15)

v2_16 = elements.load_element('eJxFUEEOwjAM+0q18w7J1iYtX0FoGogbtwESQvwdp8ng0Kz1bMfJe1iWy23dtmUZDmk4v+7XbRgT0Od6e1w7eiw0plLHpPjmeUwVh6kBZFw4o0yT3YCrAAaSjW8nB6WUEFVQG5yqiQmozv7XpEzZGUxkBRzFSzsXPGkOME07r/uKy6UG719a8w5VQ8AmYI2ouossJ1VHf+16G54ihe2BWWLcYqZQterTdk9P0nltl9MeyppZFEGCbGSOJfUHqSul57MlASgSVja48OnzBfcfUuE=', 2)
Y = Y.append('v2_16', v2_16)

v2_17 = elements.load_element('eJw1kDEOwzAIRa9iZfZgEtvgXqWqrLTKli1tparq3csHZ8AK8Pj88J16f+zrcfQ+XcJ0/zy3Y4pBq+91f21WvZYUQ5EYqgbRjKfGwBpFk1q0kCgGQTs1rWYgmkn1dsP34iOszbyAZG0o3VSdEwrVSW4eRCqasZd9JLOHQdiRxBMzBZe21R4oYwYOpQy2wjI5KirEPDYlELQMjCi7b2OVEWMWV5R5LMxt2DGvfF4CxmZjcLbiCnYXojZ+092nU9V6xe8FP1lGxx7IVrr9/rvIUkY=', 2)
Y = Y.append('v2_17', v2_17)

v2_18 = elements.load_element('eJw9UEEOwyAM+wrizIEwILCvTBPqpt566zZpmvb3xQndIS2yje3w8WPct2Xfx/Bn52/vx7r74AR9LdtzVfRSYnClBcen4Ig4uNblELOgMp2N6aKAshXDuUGNK0nQDJVcK+pR8IEGZiT/alNScLXCvBgAslSbBoKmEl5EyeK1D6K6FkvIlIt9tlGkHm4EAE2EaXHmoSLFf+MIUUqHYbQIbKgUk63YRNFUfzLz3O0NMAySJ0mEABKDynN3rJSVormXNY/6OGLEx6Fi6Pr9Ae5cUkY=', 2)
Y = Y.append('v2_18', v2_18)

v2_19 = elements.load_element('eJxFUEEOAiEM/ArZM4fOLoXiV4whq9mbt1UTY/y7LWXjodCWmemUz9Ta7b7ue2vTKUzX92Pbpxi0+1rvz613z0wxsMSQi945BlCNIS0xCGuB6okoKlte/QYUKnMMRZFVH0syqrhG1mDVSxpldiDIxGdySiEPhjOqaRIfB2ykTVCBKkfDeGO+WJMWL3hxg30+kHwZkB6ihcAhrC5S/etYpOHS9kpy/IBNHWEOAAz/nAa1w+BbAjQw3UgezgBxummWsWP/1O5bk4zL9wc9V1D+', 2)
Y = Y.append('v2_19', v2_19)

v2_20 = elements.load_element('eJw1UDsOwjAMvUrUOUOcJrbLVRCqCmJjKyAhxN3xs9OhaWy/X/yd1vX22PZ9XadTmq6f532fcrLue3u87t4995JT15zYPu05EXFObc5pWVCIdQ2h1VD2XwzVOYZiMyolaF4caKJmGuBXVEWDwCARxn10iSpuKCsc7KLQAMGZZqXQKW1UHo8N09xwCWVFXmuImxtbeqh5LITAFOERjw9n5gilHEhpAy310EIq68o80BJ7kGFIlca73dYPLA/P5B5LwHqgoW2E9bfMYc10+f0BgNFRsA==', 2)
Y = Y.append('v2_20', v2_20)

v2_21 = elements.load_element('eJw9UMsOAiEM/BXCmQNdKRR/xRiymr3tbdXEGP/dvvAA9DEznfKJY9z39TjGiOcQb+/HdsQUuPpa9+em1QvmFJBSaAufxofj0vktKVSOIWcr4kkSkKvyBXJlTIGkBw4GZhJ3kNmIglAW/SNwRQChqBAPLrPXuwnhVBdbClGfAlvE6MlhxSmMLGQ6JObBpxI6vblwy8aQ9QDIqDoJZdICBpGFejOHqHbRivI1tgpwmViFmiRTTlUsyz4VzY9tUuey8nNg3QrX7w93FFH4', 2)
Y = Y.append('v2_21', v2_21)

v2_22 = elements.load_element('eJw9UEkOwjAM/EqUcw92msXhKwhFBfXWWwEJIf7OOE57SJ2MZ7H79a09tmXfW/MX5++f57r7yQF9L9tr7eg10eSSTK4w6oyaJ8cccQkAyCoTUAEoYERlywCZ4uAzoScFIjhJUhT9CDDBQSBIeFfShn4CWaB2mXsIOFWNQ7CU7qvKjCMV3GTWwhZlmWDnYlEl2tGY1CfrNmVMY3toOsGl0Ji/W/NB1FY9OLnr+RxxsJnruftsYnWz7VRfx4WpjClqsWgdN50/TX2yHr79/rcIUr4=', 2)
Y = Y.append('v2_22', v2_22)

v2_23 = elements.load_element('eJw1UEEOwjAM+0q18w5NaZeUryA0AeLGbYCEEH/HTrNDtNSzEzvfaV1vj8u2ret0TNP187xv05yAvi+P193RU8tzajanZUE19PhKETz6nAwlGagIYOUvIQy+HYJfCHLIgQ2EVikCoo4Eb59doVcjIx4NkqbB9O0ZSCdFSoys7oNKLvL5UBiNZS7JIPY+VB2UrqOnUfbaw30B0TSGMR3jVxtel2DSBMt2vI1dfg1PWMZ4t8VbcSdjk60RkLmk5HFZz0SkatyQ513k/PsDdxJRHw==', 2)
Y = Y.append('v2_23', v2_23)

v2_24 = elements.load_element('eJxFkMFuwzAIhl/FytkHk9gB71WqKuqm3HrLWmma9u79f0y6AxZg+Pjhd9q2r/vtOLZt+kjT58/3fkw5Ifu83R+7Zy+t5NQsp7XlpPTXnAwmpeIReG1mBEeFDuvwZchq/DKuYJiCg1zvKJxRvcKpSg4e6zFhGVNESoBF8GWIjBPEogam7AO9+ehl0BqJxQbeW+YQ4ab/LCWmDkHdQgcV+nwq9OXYTu1jU4qXFiNI6xrFejre4aeQIoPo9yLgxFuLoy7nTvW9c+im/lWufy+dPlGb', 2)
Y = Y.append('v2_24', v2_24)

v2_25 = elements.load_element('eJxNUMsOAiEM/BXCmUPL0gL+ijFEzd72tmpijP9uH2g8FOh02pnyimNct/O+jxEPIV6et3WPKQj6OG/31dAjQQrUUqhLCk0CgVLoArYuYBYABaisD6E1SQgljKp9NEGa1K4siaK3tJHMKFWKGb21FhcgAcviN7FjLG/uOmlxjdIdoOKNJpPVFgi11emV/1Fdxe00H2DSP/0GWupeqiZma86dycrKsyaYX4KQ3R6iHsBu3jLWfwBf22zU72rsrs0WAnimn6nDdS/G0/sDUyBRZw==', 2)
Y = Y.append('v2_25', v2_25)

v2_26 = elements.load_element('eJw1kEEOAiEMRa9CWLOgDFDqVYwho5nd7EZNjPHu9lNm0QTa8vro1/f+2Nfj6N1fnL9/ntvhg9Pse91f28heSwyutOCYgqNY9aJBlIKrmm1ZE6yJFOchaoVFAxcqweXFWhnv4pkdD1AStqgyAQQSYkE/SNpelNoaqkqpbIMbG6JkFMjUCtkoXuYkyGSogjl90JSHLZkckMBgKCw4QjEBIeY3Jo8lEKy1zslAgBLl00OALYYAqulZZC5vUFo1iyZzM/lUpfnLiJ1potLt9weh2VEP', 2)
Y = Y.append('v2_26', v2_26)

v2_27 = elements.load_element('eJw9ULsOwjAM/JUocwY7xYnDryAUFdSNrYCEEP+OH0mHWs71fHf2N/Z+f6z73ns8h3j7PLc9piDoe328NkMvBCkQp1BqCohZC2opKVRt4KQvK00gUkhKkf8kIyzjlb1H1GZKFBozmPN4gZBIpBoMlVan1URIUR5GGaeo8TTp4tw6BxGsLJ7I/CyaAE29AX0PKmM9slg0lzIL0M3kYxwIK7B4EssI4HrKOtKzyDHNi8FxIx6Qkq0xkmZUc8KZWuP4BZofqOD19wdj71O0', 2)
Y = Y.append('v2_27', v2_27)

v2_28 = elements.load_element('eJw9UEEOwjAM+0rVcw/JWJuWryBUDbTbbgMkhPg7TpNxiJS4jh33E3u/b8u+9x7PId7ej3WPKQB9LdtzHeglUwq5plByCswnNA0NzUAxCKMKelIQL7OgQK8g8MSKktGYh4JysJjBqwMAWVS/+mAmKqGoOBUipaga2ymSzaehMvo66SYbaFYEndpMgynbkdKcSyPGZNOwG4BmYfMeciNplUOFnaPk7FGZxJbMcfaU/6t0SchS2oliQ/M/OO5iLsas5GL614Wv3x/0ZFHV', 2)
Y = Y.append('v2_28', v2_28)

v2_29 = elements.load_element('eJw1ULsOwjAM/JWocwZfGqcJv4JQVRAbWwEJIf4dX+IOTZ2z7+F8p3W9PbZ9X9fpFKbr53nfpxgMfW+P172jZ5UYtMZQSgx1iQFQuxgAmQcKISycYZFSDM2Kmo2Y2TEgG6AwcB4fQKAX1E/OlcaDc1bk2S+tDSO6Lj2CdZq4F1VaPTKVYQ7QORlZDVl6DCMU6oObkKgeW42QDzYNOFZlGDMbNZrT+a/qG0CyezEsRQG4RV+GD8BwlcrGWsRjjVkdXSAdT5KOp+wWbXgWXH5/7X1SZg==', 2)
Y = Y.append('v2_29', v2_29)

c0_v1_0 = elements.load_element('eJxNUEEOAjEI/Eqz5x5KtxTqV4xpVrM3b6smxvh3gdLEw25mGKYDfJbeb/ftOHpfTmG5vh/7scQg1dd2f+5WPWOKATkGyjFwjQESCSlCRICsVRxEiygfKV4FT63F0MTEpG4hAKt3FK0IqKxAf5BHVG3+IE4VVSV3Q8qK0nxDu0RrOhOASyTjEo2xEaY9C6pSKeykqFEIr74lutDmrLpdI0812aZJdabl5KPbQSxnBJaRZUbCP8DWx+MqXKZdj2Fr1xFUcZyiwuX7A3QWUo8=', 2)
const['c0_v1_0'] = c0_v1_0

c0_v1_1 = elements.load_element('eJw9UEsOAiEMvQqZNYsWKR+vYsxEjTt3oybGeHffo+iiBdr3aXkv63q5nbZtXZd9WM6v+3VbYkD1ebo9rqN6MInBWgwVZ8HZLIZe8dYYVISpIymTFPR3CPRaRqDdyMU9A5DBa4loFAzATMFBh2qjKorFnF2BNPUao4sHSQanDqJVd1RVJ9BGE5lpesssqGTiKGbTccxPWwLHUJ0XAYZrD9Fis1W7z2o/O00y5bXMtrg4p7U/Is1Vin+canJ5/gbPWn2X0ci7+Zn0LXr8fAFch1DV', 2)
const['c0_v1_1'] = c0_v1_1

c0_v1_2 = elements.load_element('eJxFULsOwjAM/JWoc4ekje2UX0EoKqhbtwISQvw75wdicBKf73x23kPvt309jt6HUxqur/t2DGMC+lz3x2bomfKYqI2JaUwlVxxTAYJoCFm80nBXsJoRIClFkAERRlRnMzDrp6xcXCaQLwDbpKocLk6h6IqS4K5zdFeN2aM5IViNzLVFEyIfTK1VZqwl5C0kNgOzMykKJeuDIim/1XVr44s9JIafY1TbeZr8Z6y3Ju5WfYPa/kbOz0v8JIeBSPhzjM/l8vkC4sRRDw==', 2)
const['c0_v1_2'] = c0_v1_2

c0_v1_3 = elements.load_element('eJw1kE0OAiEMha9CWLOgDD/FqxhDRjO72Y2aGOPd7aOdRQvte3wFvn6Mx74exxj+4vz989wOH5x03+v+2mb3WmJwhYOrNbgsa2sSJTiWmiJrUSQaW5OapZJUoUQiLcogEmBnhRHNDnAdm4wk5tbVAyYIPSpgOopEqyqw7KuZshhYRnagUlQmTk4hqwgiDrTFBqOgiAtibkSBlBJ0ewAXnTgbeOP8lGR+6qZQlEd3C3xLn+xF2WV6MRp3bqfCqlb7Yoq40xl0+/0BgU9RBw==', 2)
const['c0_v1_3'] = c0_v1_3

c0_v1_4 = elements.load_element('eJw1UMsOwjAM+5Vq5x6a0bQpv4LQNNBuuw2QEOLfiZNwSB+2Gzv9TMty39fjWJbpnKbb+7EdU06Kvtb9uRl64ZITS079pNW15pyIOKc2chpKVC1RcAwQTQ+qomI3UhmkijT0QBWwFYsyTK7HTsUo7SAjkNng7h2QBF1gSlTDGbFqAJ0hFw9qnSypBIWHEiyfPA6miLDFjcU850C4xM2oGFW6GzP+Y/jowv43UtxQwoyKCqsKK4aa/WyDjf+UpCjjefNMRMODNbp+f403UTI=', 2)
const['c0_v1_4'] = c0_v1_4

c0_v1_5 = elements.load_element('eJxNUEEOwjAM+8q08w5N1zUpX0FoGmi33QZICPF37LSgHZI4idO4effzfNuWfZ/n/tT119d93fuhQ/W5bI/Vq+cpDN1kQ6cjYkZELgGJKmxCMbIAl0YCtqXQsR8bkECmEHgGQiltbkoA0Xt0kons+FbWuka5HxzjYzClLvataZIARs6VbRg3bhNQbazS+R2OZz1uoTLz5dBSrLYVOBG3cQrmBTxqVeNqXU5qJKuyLNbr+I7k9yDQan5E+V8ztpnUVITy+zhNLp8v1RhR1w==', 2)
const['c0_v1_5'] = c0_v1_5

c0_v1_6 = elements.load_element('eJw9kEsOwyAMRK+CsmaBAWPoVaoqSqvssktbqap6947ByQJkjT3Pn+80z49t2fd5ni5uun+e6z55B/W9bK+1q1cO3nH1rrB3tXlHMXqXBUFApuER4ROolVVF0FAnaYiiHsr6Rf14yBTIWKUcuZAsUm9DT8nWUzvUesCO5kbMhiUCKWtFUGRgM/YuiqkwMtAcR52gooDKGIU7RWeiZCgKqJdqgY2oCB4b9qK+IrxC5tc7UaRzxHQu1sYOfTA9YL9oMpveTrPVVm9im7IYoMBf6Pb7A6MNU9I=', 2)
const['c0_v1_6'] = c0_v1_6

c0_v1_7 = elements.load_element('eJxFUEEOAiEM/ArhzGEHKXT9ijFkNXvb26qJMf7dtnTjARim7UzbT+z9vi373ns8h3h7P9Y9piDsa9meq7EXmlIgTqGSvIIxzXrlFBgpFPmQYGQ40HBpKTTNkPxZa1kDdhVhFYBHsTGAFNDJAfI0frPEm9hy8XLVM111xdBu8rIkcxv8aG12i6oSB6v9FeuChrCacPa5UN1Fla0HQIzJzOsByFtuemwQuDpg28ExhWYVX9y/zoafTPzkvI5p3fOYpFYPEI0lq0LF9fsD0BZSyA==', 2)
const['c0_v1_7'] = c0_v1_7

c0_v1_8 = elements.load_element('eJxFUMsOwjAM+5Wq5x7qbemDX0GoGmi33QZICPHvxE0Rh6pp7Dh23761274eR2v+5Pz1dd8OH5x2n+v+2Hr3LDE4KcFlBIeoRal6Jm0qgEmLnAYiokgObilsLNpQtCS7CZLJsawkWYyc478WPcCsj74MNo1IXY4prfatnKGWMpKYNiaYeKocmc0oYrS1hRRE43Y+DQJjcy8AMS9dK5UBUasyEhh2pK8d6e7qMC+DyxSkmAmMH8tmmUL8jlx+cYdtM0f2bKGYI+Hy+QKVN1EC', 2)
const['c0_v1_8'] = c0_v1_8

c0_v1_9 = elements.load_element('eJxNkEEOAjEIRa/SzLqLMpZCvYoxk9G4czdqYox39wOdxEVJ+YXHp59pWa73dduWZTqm6fJ+3LYpJ6iv9f68uXrikhNrTjLnVCUnxenI6yEnmvHYcahA0TouRIweyLVbggbGaRK1stcL22uPMlOZY4yLDgmu0SCLoQuHDSqYLxSJmBeyUPzJGAVAxYXbIEh4VrC5DoDSQLqpIPjYugdCUCCajnXNrHG8Yy7/dV1iBz2ELf8iM2M9XQbcLmYiiL7uHD3qvluUtH3JZrV0/v4AIHtSaQ==', 2)
const['c0_v1_9'] = c0_v1_9

c0_v1_10 = elements.load_element('eJxNUMsOwjAM+5Vq5x2aro+UX0FoArQbtwESQvw7dpYhDlMW23Gcvod5vt7O6zrPwyEMl9d9WYcxAH2eb4/F0GOJYyg6hoaqeQySBA2A3kAkgKgSqQBBdSv4OkGyaDothAB+MuWSvSPFOUmRSCU3QaTuWQyBmRIRiGpzxPhuHQwykALXVj1q20JwP0c0bcskwl65dWKz57CsIhCXyR077BW16jZNJ7qbILJpf5YioNQo8YAU2135N1H9ov0h1JOpPUHyMy3ifnjlAXL6fAHD8lIx', 2)
const['c0_v1_10'] = c0_v1_10

c0_v1_11 = elements.load_element('eJw9UEEOwyAM+wrqmQOhBMK+Mk1VN/XWW7dJ07S/zwa2CyTGsR3e07Lc9vU4lmU6uen6um/H5B3Q57o/toaeNXin5l3O3kmM3tXAQrwrFUXAoYkFEfDI523oEx6N9IDhysf5x0SRCxpRNCg0dkGqc9RAUCWb4vKnNqvQlbIxSeieWfsww9CzNF+wShyhUndpqlyk/OS5GlHjiiIjs9SeQoJ1q4QmlbE8uVoGn8MKwCKBeWSlKZeuECp8Bd3an+lYon2J9tsISh5f2pJzpSyXzxckyFFT', 2)
const['c0_v1_11'] = c0_v1_11

c0_v1_12 = elements.load_element('eJxdT7sOAjEM+5Wqc4em10fKryBUHeg2tgMkhPh34jS3MLRKHNtxPn6M233d9zH8yfnr+7HtPjhBX+v9uSl6LjG4wsHVHhzLIyJ8VVC8HFxbBIjHqCR0UrQSXGc0i6EQ5WZjihlfMoiEWaTgf2WrUw1w+kogVokUDWuTjLmYSUMGo0GHzBzngwdSq6IKmaXpQqh2DuMUkmC9zc0tzfvgqC55CpiMqAHoyKapye7NSCMUtlrPwUbl63Q5xNBQimbOc0GVSaXL9wc6blFq', 2)
const['c0_v1_12'] = c0_v1_12

c0_v1_13 = elements.load_element('eJxFkLEOwjAMRH8l6pwhThvb5VcQqgpiYysgIcS/43NcmOxcz8/nvodludzWbVuW4ZCG8+t+3YacTH2ut8fV1WMrOTXNiSUnojknMUE4J51MKAWqfVZr1KpAJfPOJkxWG0Mga2KOCmhzQKy2Ckezx2hjEMCoBBVU6buUO9Rhk+7Lq0036SQizzT2zd44GFB/CZTC4RQE4d2DI2oAu3n+MaY9Ie+rTVaKO+LaRuHy3+TpcAmiIIBG5TgZHNa4lmoPB4M4h/8LmE6fL5myUj0=', 2)
const['c0_v1_13'] = c0_v1_13

c0_v1_14 = elements.load_element('eJxNkE0KAjEMha8Suu6iqf31KiJllNnNblQQ8e7mpRlw0zYvL/mSftwY923Z9zHcmdzt/Vh350nU17I9V1UvOXjKzVPJnlr1xCwCh+gpdU8dSowzXYpYWBJtvjk0+CWTUYxb1QSVcWjY8TqJQRo3ySWlaKlEvRuhhjkACCpwgDFkG6dqRbfHoWBAUCtQbOVJaEUp4spsLnMqtR6Tw661gacVQWVbDqPW/ufgyHOJ3iYGf4FmNRoOtUDpB0GwXeRoB73F2RJw/Vi+fn/ll1JQ', 2)
const['c0_v1_14'] = c0_v1_14

c0_v2_15 = elements.load_element('eJxNTksOAjEIvQrpmkWppWW8ipk0o5nd7Komxnh3H01N3ACP94F3aO12bL23Fs4Urq/73gMTts/teOxje8kLkxpTUfQTkxUmiZUpA4hgKIsP4mvzacAMNThJEZb445KrJE19hcDUOUQVgApNHnab+X5oINUZJhL/BIZu7ogoFUzx90Snwd+YR8W59fMFmLIxWA==', 1)
const['c0_v2_15'] = c0_v2_15

c0_v2_16 = elements.load_element('eJw9jksOQiEMRbfSMGbQIi3gVowhT/Nmb4aaGOPevXzioHB7e/r5uFrvx9Zare5M7vZ+7M15gvvajuc+3EssnjR7SidPBb9wgmCIwCsTSbMuYoAF0V0GrYOxPxg9GUREqM0Ys7isgQaRMCGiOfd1EiBkJh3PcRUYC3NYhIiib1zVWVtHzaevNr1+f9kCMK4=', 1)
const['c0_v2_16'] = c0_v2_16

c0_v2_17 = elements.load_element('eJw1TbsOwyAM/BWL2UNMAJP+SlWhNMqWjbRSVfXfeway2Pfwnb+ulO1Yay3F3cg9P+deHRPU93q89qbew8IUM1NSpjxhR6YwM4kIxrQMZiCrATDNQ4kJBEL0JjQbKfWXYpb1zuM09HMRI3ikLWJtEm0EG+gVL/1LuEjr6xaQIp99/9SiKT1+f6RtMHg=', 1)
const['c0_v2_17'] = c0_v2_17

c0_v2_18 = elements.load_element('eJxFTkEOAiEQ+wrhzIFhGWD9itmQ1extb6iJMf7dFlY90OmUlvKytV73tbVa7cnYy/O2NesM1Me637eunuPsjBZnEmYWZyJ4nKB57PHPRSgoSBBuiZAJMIkvh0MCYKY1jVmQL2GcnuqFmIVv+a6y+qhNuNEwvqNf90QTWjPdPv1y7PMM6fL+ADjQL/o=', 1)
const['c0_v2_18'] = c0_v2_18

c0_v2_19 = elements.load_element('eJwtjrEOwyAMRH/FYvYACWDcX6kqlEbZspFWqqr+e33AYIzu3p38dbXu59Zare5G7vm5juaYTH1v5+vo6j0qUypMsjKVbH+bKEzBLyaYUWwnbyMDytiACiAAcdIhlNEBRWGHdZSJuaozn0YeGx0A4SUc4BHqj85SiaNTlmmB6fegIz9+fw3DLv0=', 1)
const['c0_v2_19'] = c0_v2_19

c0_v2_20 = elements.load_element('eJw9jkEOAiEMRa/SsO6CAi3gVcyEjGZ2s0NNjPHuttOJKz7vP0o/YYz7vs45RrhAuL0f2wwISl/r/twOei0dgRuCVASKGog0FQ2VENoBWC/Jam1aUT8j9Gige9Pt/KvaCtslu06U3DetkQE6XbYQtS7ZiDosGlLyhWo5l2rVPzDI+k5skvhEkeX7A/D2L+M=', 1)
const['c0_v2_20'] = c0_v2_20

c0_v2_21 = elements.load_element('eJw1TkkKwzAM/Irx2QfLm6J+pQSThtxyc1oopX/vKEoPAs1oFn187+u+jNG7vzn/eB/b8MGBfS37czvZe5Hg6hQcx+AoAkyMyQBUlMFWm41eSv7LRCVAnC8QyYwqY3ir7moDL5pOpyqZXLQTlwYFY29am4wXsQTGjVK8silWs1hbsadam78/mcovlQ==', 1)
const['c0_v2_21'] = c0_v2_21

c0_v2_22 = elements.load_element('eJw1TkEOAiEM/ErDmUO7QgG/YgxZzd72hpoY49+dLvUwA8xMp3xC7/d9HaP3cKZwez+2ESJBfa37czvUS2qRco2kgPApUgJEQK3AYWAxQXCBUM1lMWXxARE2glmsJ+MEqg1kDyc3hEFZPa7WB6eIL1Cd0VT+qWYzOqPzD+yri86H1apevz85iDAE', 1)
const['c0_v2_22'] = c0_v2_22

c0_v2_23 = elements.load_element('eJwtTssOwjAM+5Wo5x7arXmUX0GoGmi33QpICPHvOGsPSSzHdvINrT2OrffWwoXC/fPce4gE9r0dr/1kr6VGYoskEiknb3mJVFYw7AyaLQ7UV9UbkEHI65iiU4+loVSmj5MDbBQBjDLc0TTUOUNRbaQzsMJaPNrPLnnk+A/uYBkpavMBAajV3779/mCjL1s=', 1)
const['c0_v2_23'] = c0_v2_23

c0_v2_24 = elements.load_element('eJw9jbEOwjAMRH/FyuwhKXHs8CsIRQV16xZAQoh/59ymDBc7Z9/zJ7R2X+feWwtnCrf3Y+mBCe5rXp/L5l5yZRJjKrIrxchkMOzEpDIqlOGlpP8HI03ITkwVhuEvGbVA1TmDkaJfAFSwbR6dvMnOGHnHixzrPoUUeSk7UDAowOhxedtyp8j1+wNjFS9N', 1)
const['c0_v2_24'] = c0_v2_24

c0_v2_25 = elements.load_element('eJw1jrEOwyAMRH/FYvZgkwBOf6WqUFply0Zbqar67z1DMlgc744z31DrY19bqzVcKNw/z60FJtD3ur+2Tq/zwpSMKWecGI3CVGYmi0xuWgIUgALXMGVCUh0ikaKLAjGNuCqI6XC8x4vzaahAFfHbdOxSgTI5QoKXBpHLOHukbwVYeo2dNWl8Lqfb7w/lPi/R', 1)
const['c0_v2_25'] = c0_v2_25

c0_v2_26 = elements.load_element('eJw1TkEOwyAM+0rEmQN0BMK+Mk2om3rrjXbSNO3vs8t6wbEdYn9ca8917r01dxX3eG9Ld16gvuZ1Xw71lqoXNS8ZGIPxKWDZSwEp6sUSOLAe5mUYBrRMQc8hjiN0c6EwwYGoWK0BBmamxYiDpkOsDLNhELnE31b+YUwnSZjjFM4KbJ3Z8/79AUPLL0A=', 1)
const['c0_v2_26'] = c0_v2_26

c0_v2_27 = elements.load_element('eJw9TkEOAiEM/ErDmQPFQsGvmA1Zzd72hpoY49+dguuh6XQ6nc7btXbb195bc2dy19d9684T2Oe6P7bBXqR6SsVTRqXoSRO6euIAoNlAAMC2QskRkgRWTxiYMaBUPAluCpbZVIGPO53ORYwwW66HN/8AxzAFUmbZ+9GhKCOK/D3xugDkNPNY4pyXzxfqDi/G', 1)
const['c0_v2_27'] = c0_v2_27

c0_v2_28 = elements.load_element('eJw1jbEOwyAMRH/FYmbAIWCnv1JFKI2yZSOtVFX9956BDka+493540rZz63WUtyN3ON9HdV5gvvazufR3Pu8eErqKWOUsU+eeMIjAhE8NQA7B4gUbZmHUnxpGI4kCOQ0A4PW2PMCKCOfs4HWHkBK7KTovxQYszmYxUpZewFzOzECquOUVVp1Wr8/hO0vbw==', 1)
const['c0_v2_28'] = c0_v2_28

c0_v2_29 = elements.load_element('eJxNjcEOAiEMRH+l4cwBWGiLv2I2ZDV72xtqYoz/7hQ08TCTdqY8Xq6167H13po7kbs8b3t3npA+tuO+j/Scq6einmTxFFOEBbNYEFkVPKlamj1lDCXZUs0wiZ2NR3YHMZpqwlzFQOAqxOWLlvxbYMog5n+ipglgma2MUzYSUgmTFsMy/xgp8/r+AEP5MCU=', 1)
const['c0_v2_29'] = c0_v2_29

t0 = elements.load_element('eJxVVUuu1DAQvEo06yzcie22uQpCowd6O3YPkBDi7riqqzNhkZkk7m91deXP4/n89v3t4+P5fHzaHl9//3j/eOzbevvr7fvPd7793Gzf2ti33vZtrn87jn2rc9/c8VDWDR76vg1cy6qtq65DX55+yAiHZnWdrhtHrPWylfAYZ4SbuhAREZAbdmbIZbxr4eJDiVeCMaKABpcTRvxZzgMl5JsmVysVPx7HrFTBwrnKPhw9TFCilTO7sWgCBY4aFlZGlDCmqi4WFiyFkQCiJ2TrGtlcn4EMKuioCEitq3fFsTIDm+FRGWdRjkjH3OOIGPDBy64ZsBkkiGBnxDBT0zBtHJMpIhKPhNDrhVhXInSO4Oicx/BEW3jZ2g1pjKx1lQDSxPzOQBBXzzmOcCO9iLGVFniyddj1kWDYjCh1CBRT20kYRGHoI1jmTR2jU3ZbhDZpzNaYObBWH+QCDXAzNAH2wJrPpMyUp4vpBBj1D7GLRTb5okIOaAYjclDs4FCSkpQfdwxzx2IZDgUKgmF0JFeNdYgQpQTyvWn4sVDlKjsfvciFltbv66esRLMFskMMZZuoHpUP7UN4yT042F6n6KjPZG4VM3DDCaMrjii66q8lJ+FKjJ1rw2K6rHDaky+hNfLjMZyqmOSqkULkudmwmlOEmdIVu+lMzrzfk1waGIpzJI8tQ/9nGFPM+kOFrnKb4Iw5+auSeianXTrh0R2RKJfCVRVwBDHh1oosutzGSBrP20pFBkspOcOW8l1Sd126O0whie+ZdCL/JIaE6qUcksqWa4aHoMWRP/DmKJnJUz6lgazTtFAAoUo3JBXqbwgeF5pTyoJ1YIfshSuR+samx31BODGvLyHmqAjZkQ7BQOlXS4UIwczWLXcQkVsiGaT3q3eLKvnZ09eh3Ra5+u3rQjTnvEY+kzN2W/RYZr9e+x0k1N1SzMmseVHxkvfszbNl19cTY4tdPfID1GKdWa6+P55FhCQmp7QDOXVSe4QQsBNPTBCY/Gm5ICl8mdX08aE5laQLJcvZFPvy9x9or5qW', 3)
const['t0'] = t0

eq = Equation([c0_v2_15, c0_v2_16, c0_v2_17, c0_v2_18, c0_v2_19, c0_v2_20, c0_v2_21, c0_v2_22, c0_v2_23, c0_v2_24, c0_v2_25, c0_v2_26, c0_v2_27, c0_v2_28, c0_v2_29], [c0_v1_0, c0_v1_1, c0_v1_2, c0_v1_3, c0_v1_4, c0_v1_5, c0_v1_6, c0_v1_7, c0_v1_8, c0_v1_9, c0_v1_10, c0_v1_11, c0_v1_12, c0_v1_13, c0_v1_14], [[elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()], [elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero(), elements.ZpElement.zero()]], t0, 3)
eqs.append(eq)
p=proof(crs, eqs, X, Y, x, y)
p.consts=const
print(p.to_json())
