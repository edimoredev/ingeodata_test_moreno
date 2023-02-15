import pytest
from estadistica import grafica

"""
    Parametrización de los datos para su respectivas pruebas
"""


@pytest.mark.parametrize(
    "data, tipo, name_file, title_grafica",
    [
        # : data es un arreglo donde esta la media(numero), mediana(numero) y moda(lista)
        ([10, 20, [30]], ['Me_Aritmetica', 'Media', 'Moda'], 'prueba1', 'prueba1'),
        ([10, 20, [30]], ['Me_Aritmetica'], 'prueba10', 'prueba10')

    ]
)
def test_grafica(data, tipo, name_file, title_grafica):
    """ Test de la clase Grafica

    Args:
        data (list): Lista que contiene el valor de la media, mediana y moda
        tipo (list): Lista que contiene los nombres tipos calculados
        name_file (string): nombre del archivo cargado
    """
    gf = grafica.Grafica(data, tipo, name_file, title_grafica)
    gf.grafica()
    resul = gf.guardarGrafica
    assert resul
