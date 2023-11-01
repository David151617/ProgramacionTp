import pytest
from funciones import document_verify

# Define una lista de casos de prueba con la estructura (entrada, resultado_esperado)
test_cases = [
    (1234567, True),  # Número válido
    (98765432, True),  # Número válido
    (1, False),  # Número inválido
    (123456, False),  # Número inválido
    (123456789, False),  # Número inválido
    (0, False),  # Número inválido
    (1000000, True),  # Número válido (límite inferior)
    (99999999, True),  # Número válido (límite superior)
    (100000000, False)  # Número inválido
]

@pytest.mark.parametrize("input, expected", test_cases)
def test_document_verify(input, expected):
    result = document_verify(input)
    assert result == expected
