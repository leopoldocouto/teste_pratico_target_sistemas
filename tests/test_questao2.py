from teste_pratico_target_sistemas.questao2 import questao2

# given (dado quem, cenário) Arrange
# when  (quando algo acontecer) Act
# then  (então algo deve ser verificado) Assert


def test_deve_retornar_true_para_questao2() -> None:
    numero: int = 8
    quest2: bool = questao2(numero)
    resp2: bool = True
    assert quest2 == resp2


def test_deve_retornar_false_para_questao2() -> None:
    numero: int = 7
    quest2: bool = questao2(numero)
    resp2: bool = False
    assert quest2 == resp2
