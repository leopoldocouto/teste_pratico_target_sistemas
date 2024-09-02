from teste_pratico_target_sistemas.questao1 import questao1

# given (dado quem, cenário) Arrange
# when  (quando algo acontecer) Act
# then  (então algo deve ser verificado) Assert


def test_deve_retornar_true():
    quest1 = questao1()
    resp = True
    assert quest1 == resp
