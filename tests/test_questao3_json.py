import json

import pytest

from teste_pratico_target_sistemas.questao3_json import Faturamento

# given (dado quem, cenário) Arrange
# when  (quando algo acontecer) Act
# then  (então algo deve ser verificado) Assert

type_json = list[dict[str, int | float]]


@pytest.fixture
def setup() -> Faturamento:
    faturamento = Faturamento()
    return faturamento


@pytest.fixture
def faturamento_json(setup: Faturamento) -> type_json:
    caminho: str = './src/dados.json'
    return json.loads(setup.carregar_dados_json(caminho))


def test_deve_carregar_dados_json_com_sucesso(setup: Faturamento) -> None:
    caminho: str = './src/dados.json'
    dados_json: type_json = json.loads(setup.carregar_dados_json(caminho))
    assert len(dados_json) > 0


def test_nao_deve_carregar_dados_json_path_errado(setup: Faturamento) -> None:
    caminho_invalido: str = './src/dadoss.json'
    with pytest.raises(FileNotFoundError):
        setup.carregar_dados_json(caminho_invalido)


def test_deve_comparar_true_para_menor_valor_faturamento(
    setup: Faturamento, faturamento_json: type_json
) -> None:
    dados: type_json = faturamento_json
    quest3: float = setup.menor_faturamento(dados)
    resp3: float = 373.7838
    assert quest3 == resp3


def test_deve_comparar_true_para_maior_valor_faturamento(
    setup: Faturamento, faturamento_json: type_json
) -> None:
    dados: type_json = faturamento_json
    quest3: float = setup.maior_faturamento(dados)
    resp3: float = 48924.2448
    assert quest3 == resp3


def test_deve_comparar_true_para_media_faturamento(
    setup: Faturamento, faturamento_json: type_json
) -> None:
    dados: type_json = faturamento_json
    quest3: float = setup.media_faturamento(dados)
    resp3: float = 20865.370166666664
    assert quest3 == resp3


def test_deve_comparar_true_para_dias_acima_media(
    setup: Faturamento, faturamento_json: type_json
) -> None:
    dados: type_json = faturamento_json
    quest3: int = setup.dias_acima_media(dados)
    resp3: int = 10
    assert quest3 == resp3
