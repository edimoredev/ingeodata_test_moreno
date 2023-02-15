import pytest
from estadistica import moda

"""
    Parametrización de los datos para su respectivas pruebas
"""


@pytest.mark.parametrize(
    "data, expected",
    [
        ([10, 5, 7, 9, 20, 35, 40, 10], [10]),
        ([30, 5, 2, 19, 30, 24, 5], [5, 30]),
        ([18, 20, 7, 9, 20, 35, 18, 10, 35], [18, 20, 35]),
        ([1, 1, 8, 10, 1, 8, 34, 10], [1, 8])

    ]
)
def test_moda(data, expected):
    """ Test a la clase moda,compara el calculo realizado con lo que
        se espera obtener

    Args:
        data (list): Contiene la información recibida desde el archivo
        expected (float): Contiene el resultado esperado
    """
    assert moda.Moda(data).calcularModa() == expected
