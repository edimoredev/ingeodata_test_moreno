"""
  _clase para calcula la mediana de una sección de numeros
  _dateCreated: 10/Febrero/2023
===================================

  _script: 'mediana'
  _Prueba técnica INGEODATA
  _summary: Realiza proceso de calcular la mediana de un conjunto de datos
  _information: La mediana es el valor obtenido depende de 2 reglas como:

      * Regla 1
        Conjunto de numero de datos impar: Se debe ordenar el conjunto de numeros de menor a mayor y se selecciona el del centro
        ejemplo: [10, 12 , 8, 24, 32], ordenado [8, 10, 12, 24, 32] y se selecciona el centro en este caso es el numero 12
      
      * Regla 2
        Conjunto de numero de datos par: Se debe ordenar el conjunto de numeros de menor a mayor y se halla el promedio de los 2 datos centrales
        ejemplo: [10, 12, 32, 24], ordenado [10, 12, 24, 32] y se se selecciona los dos medios y se saca el promedio  en este caso 
        es 12 y 24 y su promedio es (12 + 24) / 2 = 18

  _CreatedBy:: Edison Moreno Capera.

  _Available functions:
    - __init__: inicializa y recibe la data para ser procesada por el resto de funciones
    - calcularMediana: lleva a cabo el calculo de la mediana y retorna numero.

"""


class Mediana():
    def __init__(self, x):
        """funcion que inicializa y recibe la data

        Args:
            data (lista): lista de numeros
        """
        self._x = x

    def calcularMediana(self):
        """Realiza proceso de calcular la mediana de un conjunto de datos

        Returns:
            float: total del calculo
        """
        ordenada = sorted(self._x)
        longitud = len(self._x)
        mitad = int(longitud / 2)
        if longitud % 2 == 0:
            mediana = (ordenada[mitad - 1] + ordenada[mitad]) / 2
        else:
            mediana = ordenada[mitad]

        return mediana
