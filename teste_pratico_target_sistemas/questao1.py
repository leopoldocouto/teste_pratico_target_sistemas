"""
1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
"""


def questao1() -> int:
    indice: int = 13
    soma: int = 0
    k: int = 0
    while k < indice:
        k += 1
        soma += k
    return soma  # 91
