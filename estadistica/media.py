"""
  _clase para calcula la media de una sección de numeros
  _dateCreated: 10/Febrero/2023
===================================

  _script: 'media'
  _Prueba técnica INGEODATA
  _summary: Realiza proceso de calcular la media aritmetica(promedio) de un conjunto de datos
  _information: La media es el valor obtenido al sumar todos los datos y dividir el resultado entre el numero total de datos
  _CreatedBy:: Edison Moreno Capera.

  _Available functions:
    - __init__: inicializa y recibe la data para ser procesada por el resto de funciones
    - calcularMedia: lleva a cabo el calculo de la media.

"""


class Media():
    def __init__(self, x):
        """funcion que inicializa y recibe la data

        Args:
            data (lista): lista de numeros
        """
        self._x = x

    def calcularMedia(self):
        """calcula la media de un conjunto de numeros y retorna el numero total de la media

        Returns:
            float: total del calculo
        """
        suma = sum(self._x)
        n = len(self._x)
        x = suma/n
        return round(x, 2)
