'''Validador de cpf'''

import re

regexCpf = r"^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.\-[0-9]{2}$"
'''Explicação: 
- Os caracteres ^ na frente e $ no final são para testar a string inteira
- O {3} atrás do [0-9] significa que ele repete 3 vezes
- Para testar um ponto ou hífen literal, usamos o \ (escape)
'''

cpf = input("Digite um cpf sem os dígitos verificadores:")

regexCpfCincoDigitos = r"^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}$"

validado = re.search(regexCpfCincoDigitos, str(cpf))
digito1 = 0
digito2 = 0

if (validado):
    indice = 0
    for i in range(10, 1, -1):
        digito1 += int(cpf[indice])*i
        indice += 1
    resto = digito1%11

    if (resto == 1 or resto == 0):
        digito1 = 0
    else:
        digito1 = 11 - resto

    #Concatenar o segundo digito ao final do cpf
    cpf = str(cpf) + str(digito1)

    indice = 0
    for i in range(11, 1, -1):
        print(cpf[indice], i)
        digito2 += int(cpf[indice]) * i
        indice += 1
    resto = digito2%11

    if (resto == 0 or resto == 1):
        digito2 = 0
    else:
        digito2 = 11 - resto

    print("Seu cpf eh: "+cpf+'-'+str(digito1)+str(digito2))
else:
    print("Cpf inserido inválido")