"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua
preferência
ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

def questao5_maneira1(palavra: str) ->str:
    palavra_invertida:str = ''
    for letra in range(len(palavra)-1, -1, -1):
        palavra_invertida += palavra[letra]
    return palavra_invertida


def questao5_maneira2(palavra: str) ->str:
    lista_palavra = list(palavra)
    palavra_invertida = ''.join(lista_palavra[::-1])
    return palavra_invertida
