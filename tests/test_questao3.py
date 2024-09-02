import json

import pytest

from teste_pratico_target_sistemas.questao3 import Faturamento

# given (dado quem, cenário) Arrange
# when  (quando algo acontecer) Act
# then  (então algo deve ser verificado) Assert

type_json = list[dict[str, int | float]]


@pytest.fixture
def setup() -> Faturamento:
    faturamento = Faturamento()
    return faturamento


@pytest.fixture
def faturamento_json() -> type_json:
    return [
        {'dia': 1, 'valor': 1000.0},
        {'dia': 2, 'valor': 1200.0},
        {'dia': 3, 'valor': 0.0},  # Fim de semana
        {'dia': 4, 'valor': 0.0},  # Fim de semana
        {'dia': 5, 'valor': 1500.0},
        {'dia': 6, 'valor': 1300.0},
        {'dia': 7, 'valor': 0.0},  # Feriado
        {'dia': 8, 'valor': 1100.0},
        {'dia': 9, 'valor': 0.0},  # Fim de semana
        {'dia': 10, 'valor': 0.0},  # Fim de semana
        {'dia': 11, 'valor': 1700.0},
        {'dia': 12, 'valor': 1600.0},
        {'dia': 13, 'valor': 900.0},
        {'dia': 14, 'valor': 0.0},  # Feriado
        {'dia': 15, 'valor': 2000.0},
        {'dia': 16, 'valor': 0.0},  # Fim de semana
        {'dia': 17, 'valor': 0.0},  # Fim de semana
        {'dia': 18, 'valor': 1800.0},
        {'dia': 19, 'valor': 1550.0},
        {'dia': 20, 'valor': 1400.0},
        {'dia': 21, 'valor': 0.0},  # Feriado
        {'dia': 22, 'valor': 1500.0},
        {'dia': 23, 'valor': 0.0},  # Fim de semana
        {'dia': 24, 'valor': 0.0},  # Fim de semana
        {'dia': 25, 'valor': 1600.0},
        {'dia': 26, 'valor': 1900.0},
        {'dia': 27, 'valor': 0.0},  # Feriado
        {'dia': 28, 'valor': 2100.0},
        {'dia': 29, 'valor': 2200.0},
        {'dia': 30, 'valor': 0.0},  # Fim de semana
        {'dia': 31, 'valor': 0.0},  # Fim de semana
    ]


def test_deve_comparar_true_para_menor_valor_faturamento(
    setup: Faturamento, faturamento_json: type_json
) -> None:
    dados: str = json.dumps(faturamento_json)
    quest3: float = setup.menor_faturamento(dados)
    resp3: float = 900.0
    assert quest3 == resp3


def test_deve_comparar_true_para_maior_valor_faturamento(
    setup: Faturamento, faturamento_json: type_json
) -> None:
    dados: str = json.dumps(faturamento_json)
    quest3: float = setup.maior_faturamento(dados)
    resp3: float = 2200.0
    assert quest3 == resp3


def test_deve_comparar_true_para_media_faturamento(
    setup: Faturamento, faturamento_json: type_json
) -> None:
    dados: str = json.dumps(faturamento_json)
    quest3: float = setup.media_faturamento(dados)
    resp3: float = 1550.0
    assert quest3 == resp3


def test_deve_comparar_true_para_dias_acima_media(
    setup: Faturamento, faturamento_json: type_json
) -> None:
    dados: str = json.dumps(faturamento_json)
    quest3: int = setup.dias_acima_media(dados)
    resp3: int = 8
    assert quest3 == resp3
