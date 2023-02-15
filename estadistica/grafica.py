"""
  _clase para graficar depende la data ingresada
  _dateCreated: 10/Febrero/2023
===================================

  _script: 'grafica'
  _Prueba técnica INGEODATA
  _summary: Realiza proceso de graficar depende del conjunto de datos
  _information: la grafica ingresada es depende de la lista ingresada, si es una moda, media o mediana
                
  _CreatedBy:: Edison Moreno Capera.

  _Available functions:
    - __init__: inicializa y recibe la data para ser procesada por el resto de funciones
    - grafica: lleva a cabo el grafico correspondiente a la lista ingresada

"""
from matplotlib import pyplot as plt
import os


class Grafica():
    def __init__(self, data, tipo, name_file, tituloGrafica):
        """funcion que inicializa y recibe la data, nombre del eje x, nombre del eje y y el nombre del la grafica a guardar como png

        Args:
            data (lista): lista de números
        """
        self._data = data  # lista de data para graficar
        self._tipo = tipo  # ingresa un arrego con los tipos 'media', 'mediana' y 'moda'
        self._name_file = name_file  # nombre del archivo
        self._tituloGrafica = tituloGrafica  # nombre titulo de la grafica

    def grafica(self):
        """Funcion que muestra un grafico de la información suministrada
        """
        # definimos el eje x
        x = [self._tipo[0], self._tipo[1]]
        # definimos el eje y
        y = [self._data[0], self._data[1]]

        # Valida si hay mas de 1 moda para agregarlo al eje
        if len(self._data[2]) > 1:
            for i in range(len(self._data[2])):
                x.append('{}-{}'.format('Moda', i))
                y.append(self._data[2][i])
        else:
            x.append('Moda')
            y.append(self._data[2][0])

        # define la longitud de los ejes x y y dependiendo de la data ingresada
        plt.subplots()
        plt.bar(x, y)
        plt.title(self._tituloGrafica)  # nombre del titulo
        plt.xlabel('Eje x')  # nombre del eje x
        plt.ylabel('Eje y')  # nombre del eje y

    def guardarGrafica(self):
        # Valida si existe la carpeta para despues guardar, en caso de no estar la crea
        if os.path.exists('media//graficas//{}'.format(self._name_file)):
            plt.savefig(
                'media\\graficas\\{}\\{}.png'.format(self._name_file, 'grafica'))
        else:
            os.makedirs('media//graficas//{}'.format(self._name_file))
            plt.savefig(
                'media\\graficas\\{}\\{}.png'.format(self._name_file, 'grafica'))
