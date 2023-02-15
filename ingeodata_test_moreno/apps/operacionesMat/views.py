from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import pandas as pd
import time
from os import listdir, remove
from shutil import rmtree
from os.path import isfile, join
from django.conf import settings
from estadistica import media, mediana, moda, grafica


# Create your views here.

def home(request):
    data_list = []
    # : Asignamos a media_path la ruta y acceso a la carpeta Media, donde esta guardado el archivo .xls o .csv
    media_path = settings.MEDIA_ROOT
    print(media_path)
    # : Recorremos los archivos guardados en la carpeta para extraer la información
    for f in listdir(media_path):
        fs = FileSystemStorage()
        uploaded_file_url = fs.url(f)
        """ 
        : Variables 
        """
        name = f
        # : variable lista_calcular, para ingresar la data en una lista para su respectivo calculo
        lista_calcular = []
        # : variable imaganes
        imagenes = []
        # : variable data
        data = []
        """ : End Variables"""

        """ 
        : Valida el archivo para extraer la data correspondiente 
        """
        if (f).endswith('.xls'):
            # : A la variable xls le asignamos el archivo
            xls = pd.ExcelFile('media//{}'.format(f))
            # : seleccionamos la hoja 'estadistica y que empiece desde la fila 1, ya que la fila 0 contiene el encabezado
            df = xls.parse('espeni', header=0)
            # : ingresamos a la información de la columna data
            data = df['POWER_ESPENI_MW']
        elif (f).endswith('.csv'):
            # : A la variable csv le asignamos el archivo
            csv = pd.read_csv('media//{}'.format(f),
                              encoding='latin-1', header=0)
            # : ingresamos a la información de la columna data
            data = csv['POWER_ESPENI_MW']
        """ : End validación """

        """ 
        : Valida si hay data, realiza los calculos correspondientes 
        """
        if len(data) > 0:
            # : recorremos cada dato para ingresarlos en la lista
            for i in data:
                lista_calcular.append(i)
            """
            : importamos la libreria 'estadistica' que calcula, la media, mediana y moda
            """
            # : Media
            me_aritmetica = media.Media(lista_calcular)
            resul_me_aritmetica = me_aritmetica.calcularMedia()

            # : Mediana
            me = mediana.Mediana(lista_calcular)
            result_me = me.calcularMediana()

            # : Moda
            mo = moda.Moda(lista_calcular)
            resul_mo = mo.calcularModa()
            resul_mo_f = str(resul_mo)[1:-1]
            resul_mo_f = resul_mo_f.replace(",", " - ")

            """ : Estadistica End """

            """ 
            : Grafica
            """
            tituloGrafica = 'Demanda total de electricidad en el Reino Unido'
            type_name = ['Me_Aritmetica', 'Media', 'Moda']
            result_data = [resul_me_aritmetica, result_me, resul_mo]

            grafica_est = grafica.Grafica(
                result_data, type_name, '{}'.format(f), tituloGrafica)
            grafica_est.grafica()
            grafica_est.guardarGrafica()

            """ : End Grafica """

            """ 
            : Listar img de las graficas
            """
            img = listdir('media\\graficas\\{}\\'.format(f))
            for a in img:
                imagenes.append('./media/graficas/{}/{}'.format(f, a))
            """ : End Listar img """

            """ 
            : Guardar resultado final
            """
            data_list.append(
                (f, uploaded_file_url, resul_me_aritmetica, result_me, resul_mo_f, imagenes))

            """ : End Resultado Final"""

    # : diccionario contexto para retornar al template
    contexto = {'myfiles': data_list}
    return render(request, 'operacionesMat/operacionesMat.html', contexto)


def adjuntarFile(request):
    """ : Función que adjunta el archivo 

    Args:
        request (Post): petición Post

    Returns:
        redirect: pagina
    """
    # : validamos petición method POST
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        # : si es .xls o .csv realiza el proceso de guardar el archivo en caso
        if (myfile.name).endswith('.xls') or (myfile.name).endswith('.csv'):
            fs = FileSystemStorage()
            fs.save(myfile.name, myfile)
            """Valida el archivo ingresado, revisando cada dato para posteriomente saber si se guarda o no

            Returns:
                redirect: pagina
            """
            validar = False
            if (myfile.name).endswith('.xls'):
                # : A la variable xls le asignamos el archivo
                xls = pd.ExcelFile('media//{}'.format((myfile.name)))
                # : seleccionamos la hoja 'estadistica y que empiece desde la fila 1, ya que la fila 0 contiene el encabezado
                df = xls.parse('espeni', header=0)
                # : ingresamos a la información de la columna data
                data = df['POWER_ESPENI_MW']
                for i in data:
                    if isinstance(i, int) or isinstance(i, float):
                        pass
                    else:
                        validar = True
                        xls.close()
                        break
            elif (myfile.name).endswith('.csv'):
                # : A la variable csv le asignamos el archivo
                csv = pd.read_csv('media//{}'.format((myfile.name)),
                                  encoding='latin-1', header=0)
                # : ingresamos a la información de la columna data
                data = csv['POWER_ESPENI_MW']
                for i in data:
                    if isinstance(i, int) or isinstance(i, float):
                        pass
                    else:
                        validar = True
                        xls.close()
                        break
            """End validación"""

            if validar != True:
                messages.success(
                    request, '¡El Archivo fue Cargado Exitosamente!')
                return redirect('/')
            else:
                messages.info(
                    request, "El archivo no se adjunto, ya que hay un dato no calculable")
                rutaFile = 'media\\{}'.format(myfile.name)
                remove(rutaFile)
                return redirect('/')

        else:
            messages.info(
                request, "El archivo cargado no es de extensión .csv o .xls")
            return redirect('/')


def fileDelete(request, file):
    """Eliminar toda la información visualizada

    Args:
        request (_type_): pagina
        file (file): .xls o .csv

    Returns:
        redirect: pagina
    """
    media_path = settings.MEDIA_ROOT
    for f in listdir(media_path):
        if f.count(file) == 1:
            rutaFile = 'media\\{}'.format(f)
            rutaFolder = 'media\\graficas\\{}'.format(f)
            remove(rutaFile)
            rmtree(rutaFolder)

    messages.success(request, '¡Se elimino el archivo satisfactoriamente!')
    return redirect('/')
