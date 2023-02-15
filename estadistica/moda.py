"""
  _clase para calcula la moda de una sección de números
  _dateCreated: 10/Febrero/2023
===================================

  _script: 'moda'
  _Prueba técnica INGEODATA
  _summary: Realiza proceso de calcular la moda de un conjunto de datos
  _information: La moda es el valor obtenido depende de 3 reglas como:

        * Regla 1: 
                  Conjunto de números similar: Se debe ordenar el conjunto de números de menor a mayor y se selecciona el número que mas se repite 
                    - ejemplo: [10, 12 , 8, 24, 8, 1, 7, 8, 32], ordenado [1, 7, 8, 8, 8, 10, 12, 24, 32], la moda(Mo) es el número 8
        
        * Regla 2:
                  2 Conjuntos de números similar: Se debe ordenar el conjunto de números de menor a mayor y se selecciona los números que mas se repiten y 
                  que tengan el mismo número de moda
                  
                    - ejemplo [10, 7, 12 ,7, 8, 24, 8, 1, 7, 8, 32], ordenado [1, 7, 7, 7, 8, 8, 8, 10, 12, 24, 32], en este caso los números de moda(Mo) = 7, 8 
                    en este caso se llama "Distribución bimodal"

        * Regla 3:
                  3 o mas conjuntos de numeros similar: Se debe ordenar el conjunto de números de menor a mayor y se selecciona los números que mas se repiten y 
                  que tengan el mismo número de moda
                  
                    - ejemplo [10, 7, 1, 12 ,1, 7, 8, 24, 8, 1, 7, 8, 32], ordenado [1, 1, 1, 7, 7, 7, 8, 8, 8, 10, 12, 24, 32], en este caso los números de moda(Mo) =1, 7, 8 
                    en este caso se llama "Distribución multimodal"
                
  _CreatedBy:: Edison Moreno Capera.

  _Available functions:
    - __init__: inicializa y recibe la data para ser procesada por el resto de funciones
    - calcularModa: lleva a cabo el calculo de la media.

"""


class Moda():
    def __init__(self, x):
        """funcion que inicializa y recibe la data

        Args:
            data (lista): lista de números
        """
        self._x = x

    def calcularModa(self):
        """Realiza proceso de calcular la moda de un conjunto de datos

        Returns:
            float: total del calculo
        """
        ordenada = sorted(self._x)
        repeticiones = 0

        for i in ordenada:
            n = ordenada.count(i)
            if n > repeticiones:
                repeticiones = n

        moda = []  # Arreglo donde se guardara el o los valores de mayor frecuencia

        for i in ordenada:
            # Devuelve el número de veces que x aparece enla lista.
            n = ordenada.count(i)
            if n == repeticiones and i not in moda:
                moda.append(i)

        if len(moda) != len(ordenada):
            return moda
        else:
            return [0]
