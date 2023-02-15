import pytest
from estadistica import media

"""
    Parametrización de los datos para su respectivas pruebas
"""


@pytest.mark.parametrize(
    "data, expected",
    [
        ([10, 5, 7, 9, 20, 35, 40, 10], 17),
        ([30, 5, 2, 19, 30, 24, 5], 16.43),
        ([18, 20, 7, 9, 20, 35, 18, 10, 35], 19.11),
        (['hola', 1, 8, 10, 1, 8, 34, 10], 9.12)

    ]
)
def test_media(data, expected):
    """ Test a la clase media, compara el calculo realizado con lo que
        se espera obtener

    Args:
        data (list): Contiene la información recibida desde el archivo
        expected (float): Contiene el resultado esperado
    """
    assert media.Media(data).calcularMedia() == expected
