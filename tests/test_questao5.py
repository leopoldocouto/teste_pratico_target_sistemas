from teste_pratico_target_sistemas.questao5 import (
    questao5_maneira1,
    questao5_maneira2,
)

# given (dado quem, cenário) Arrange
# when  (quando algo acontecer) Act
# then  (então algo deve ser verificado) Assert


def test_deve_comparar_true_string_invertida_maneira1():
    palavra: str = 'Target Sistemas'
    quest5: str = questao5_maneira1(palavra)
    resp5 = 'sametsiS tegraT'
    assert quest5 == resp5


def test_deve_comparar_true_string_invertida_maneira2():
    palavra: str = 'Target Sistemas'
    quest5: str = questao5_maneira2(palavra)
    resp5 = 'sametsiS tegraT'
    assert quest5 == resp5
