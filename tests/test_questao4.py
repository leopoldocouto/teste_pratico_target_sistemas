import pytest

from teste_pratico_target_sistemas.questao4 import Faturamento

# given (dado quem, cenário) Arrange
# when  (quando algo acontecer) Act
# then  (então algo deve ser verificado) Assert

dict_type = dict[str, str | float]
type_json = list[dict_type]


@pytest.fixture
def setup() -> Faturamento:
    faturamento = Faturamento()
    return faturamento


@pytest.fixture
def faturamento_str() -> str:
    return """
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53"""


def test_deve_retornar_true(setup: Faturamento, faturamento_str: str) -> None:
    quest4: type_json = setup.questao4(faturamento_str)
    resp4: dict_type = {
        'estado': 'SP',
        'valor': 67836.43,
        'percentual_sobre_media': 187.6422812173358,
    }
    assert resp4 in quest4


def test_deve_comparar_true_em_tratamento_dados(
    setup: Faturamento, faturamento_str: str
) -> None:
    quest4: type_json = setup.tratamento_dados(faturamento_str)
    resp4: dict_type = {'estado': 'SP', 'valor': 67836.43}
    assert resp4 in quest4


def test_deve_comparar_true_para_media_faturamento(
    setup: Faturamento, faturamento_str: str
) -> None:
    dados_json: type_json = setup.tratamento_dados(faturamento_str)
    quest3: float = setup.media_faturamento(dados_json)
    resp3: float = 36151.996
    assert quest3 == resp3
