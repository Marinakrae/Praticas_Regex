'''Validador de comentarios em py'''

import re

comentarios = "'''" \
               "Comentário de várias " \
               "linhas" \
               "'''"\
             + "String normal" \
             + "#Comentario de uma linha" \
             + "//Comentário " \
               "//com barras " \
             + """"" \
             "Aspas duplas" \
             """"" \
             + 'String normal2'

regex = re.compile(r"(#.+|//.+|'''.*?'''|\"\"\".*?\"\"\")", re.DOTALL)
comentarios = regex.findall(comentarios)

print(comentarios if comentarios else 'nok')

'''Validar endereço IP'''

regex = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

print('ok' if regex.search('190.0.00.255') else 'nok')

'''Regex para validação de dicionários em python'''

dicionario = {"nome": "Marina", "idade": 21, "telefone": 51982432302, "endereco": "Rua dos Andradas"}

r="r{((\w+):(\d+))"

# print('ok' if r.search then 1)

'''Exemplos aula'''

regex = r"^Py"
string = "PyPy"

m = re.search(regex, string)
print(m.group())

##

regex = r"(..)/(..)/(....)"
string = "20/03/2023"

m = re.search(regex, string) #O search encerra quando encontrar a primeira correspondencia
print(m.span())

##

string = "Bom dia! Hoje é 20 de 03 de 2023"
print(re.findall(r'\d+', string))
print ("\n")

string = "Nascer do sol: 06:52 e pôr-do-sol: 18:22."
print(re.findall(r'(\d\d):(\d\d)', string))

##finditer

for m in re.finditer(r'(\d\d):(\d\d)', string):
    hora = m.group(1)
    min = m.group(2)
    print("%s horas e %s minutos" % (hora, min))

print("OU")
for m in re.finditer(r'(\d\d):(\d\d)', string):
    print(m.expand(r"\2 horas, \2 minutos."))

##

print(re.sub(r"(Py).*", r"\g<1>3", "Python"))

##

print (re.split(r"[/.]", "20/03/2023"))

# compilar a regex antes

regex_h = re.compile(r'(\d\d):(\d\d)')
regex_sep = re.compile(r'[/.:]')

if regex_h.search('23:59'):
    print ('ok')

print(regex_sep.split('1.23'))


