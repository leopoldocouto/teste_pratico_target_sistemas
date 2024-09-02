from teste_pratico_target_sistemas.questao1 import questao1

# given (dado quem, cenário) Arrange
# when  (quando algo acontecer) Act
# then  (então algo deve ser verificado) Assert


def test_deve_comparar_true_para_resultado_correto_questao1() -> None:
    quest1: int = questao1()
    resp1: int = 91
    assert quest1 == resp1


def test_deve_diferenciar_true_para_resultado_errado_questao1() -> None:
    quest1: int = questao1()
    resp1: int = 92
    assert quest1 != resp1
