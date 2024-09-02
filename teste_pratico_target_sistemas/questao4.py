import re

"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por
estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de
representação que cada estado teve dentro do valor total mensal da
distribuidora.
"""
dict_type = dict[str, str | float]
type_json = list[dict_type]


class Faturamento:
    def __init__(self) -> None:
        pass

    def questao4(self, lista_dados: str) -> type_json:
        dados_json: type_json = self.tratamento_dados(lista_dados)
        media_faturamento = self.media_faturamento(dados_json)
        lista_estado: type_json = []
        for dados_estado in dados_json:
            valor = float(dados_estado['valor'])
            percentual_estado = (valor / media_faturamento) * 100
            lista_estado.append({
                'estado': dados_estado['estado'],
                'valor': dados_estado['valor'],
                'percentual_sobre_media': percentual_estado,
            })
        return lista_estado

    @staticmethod
    def tratamento_dados(dados: str) -> type_json:
        pattern = r'•\s+(\w+)\s+–\s+R\$(\d+\.\d+,\d+)'
        regex = re.compile(pattern)
        dados_json: type_json = []

        for estado, valor in regex.findall(dados):
            dados_estado: dict_type = {
                'estado': estado,
                'valor': float(valor.replace('.', '').replace(',', '.')),
            }
            dados_json.append(dados_estado)
        return dados_json

    @staticmethod
    def media_faturamento(faturamento_json: type_json) -> float:
        soma_faturamento: float = 0
        dias_com_faturamento: int = 0
        for faturamento_dia in faturamento_json:
            valor_dia: float = float(faturamento_dia['valor'])
            if valor_dia > 0:
                soma_faturamento += valor_dia
                dias_com_faturamento += 1
        return soma_faturamento / dias_com_faturamento
