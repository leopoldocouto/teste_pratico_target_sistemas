"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à
média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados.
Estes dias devem ser ignorados no cálculo da média;
"""

import json

type_json = list[dict[str, int | float]]


class Faturamento:
    def __init__(self) -> None:
        pass

    @staticmethod
    def menor_faturamento(dados_faturamento: str) -> float:
        faturamento_json: type_json = json.loads(dados_faturamento)
        menor_valor: float = float('inf')
        for faturamento_dia in faturamento_json:
            valor_dia: float = faturamento_dia['valor']
            if valor_dia < menor_valor and valor_dia > 0:
                menor_valor = valor_dia
        return menor_valor

    @staticmethod
    def maior_faturamento(dados_faturamento: str) -> float:
        faturamento_json: type_json = json.loads(dados_faturamento)
        maior_valor: float = 0
        for faturamento_dia in faturamento_json:
            valor_dia: float = faturamento_dia['valor']
            maior_valor = max(valor_dia, maior_valor)
        return maior_valor

    @staticmethod
    def media_faturamento(dados_faturamento: str) -> float:
        faturamento_json: type_json = json.loads(dados_faturamento)
        soma_faturamento: float = 0
        dias_com_faturamento: int = 0
        for faturamento_dia in faturamento_json:
            valor_dia: float = faturamento_dia['valor']
            if valor_dia > 0:
                soma_faturamento += valor_dia
                dias_com_faturamento += 1
        return soma_faturamento / dias_com_faturamento

    def dias_acima_media(self, dados_faturamento: str) -> int:
        faturamento_json: type_json = json.loads(dados_faturamento)
        media_faturamento: float = self.media_faturamento(dados_faturamento)
        dias_acima_media: int = 0
        for faturamento_dia in faturamento_json:
            valor_dia: float = faturamento_dia['valor']
            if valor_dia > media_faturamento:
                dias_acima_media += 1
        return dias_acima_media
