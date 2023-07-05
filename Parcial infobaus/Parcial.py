# Consignas a desarrollar

# Realizar un menú que permita al usuario trabajar con las siguientes opciones:

# 1 Traer datos desde archivo: guardará el contenido del archivo Insumos.csv en una colección. Tener en cuenta que las características de los insumos deben estar en un tipo de colección integrada.
# 2 Listar cantidad por marca: mostrará todos las marcas indicando la cantidad de insumos que corresponden a esa marca.
# 3 Listar insumos por marca: mostrará cada marca indicando el nombre del insumo, y precio de cada uno de los insumos que correspondan a esa marca. 
# 4 Buscar insumo por característica: el usuario ingresa una característica (Por ejemplo, “Compatible con Windows”). La opción deberá listar todos los insumos que poseen dicha característica.
# 5 Listar insumos ordenados: mostrará id, descripción, precio, marca y la primera característica de todos los productos, ordenados por marca de la A-Z y ante de marca por precio descendente.
# 6 Realizar compras: A partir del ingreso de una marca, el programa mostrará todos los productos de esa marca. El usuario elegirá un producto y la cantidad y se agrega al carrito de compras. Esta acción se repetirá mientras el usuario lo desee (con distintas marcas). Al finalizar mostrar el total de la compra. Si el usuario acepta la misma se deberá generar un archivo txt con la factura de la compra. Indicando cantidad, producto, subtotal y total de la compra. 
# 7 Guardar Json: Generará un archivo de tipo Json con todos los productos cuyo nombre contenga “Disco Duro”
# 8 Leer Json: permitirá mostrar un listado con los insumos guardados en el archivo Json de la opción 7.
# 9 Actualizar precios: Dada la inflación del mes de Mayo, es necesario aplicar un aumento del 8.4% a todos los productos (utilizar la función map). Guardar en el archivo Insumos.csv todos los productos actualizados.
# 10 Salir del programa



# Requerimientos extra

#1 El programa deberá permitir agregar un nuevo producto a la lista (mediante una nueva opción de menú). 
# Al momento de ingresar la marca del producto se deberá mostrar por pantalla un listado con todas las marcas disponibles. Las mismas serán cargadas al programa desde el archivo marcas.txt. 
# En cuanto a las características, se podrán agregar un mínimo de una y un máximo de 3.

#2 Agregar una opción para guardar todos los datos actualizados (incluyendo las altas). El usuario elegirá el tipo de formato de exportación: csv o json.   
def menu_Info_Baus():
    print("""
    1- Traer datos de archivo.
    2- Listar cantidad por marca.
    3- Listar insumos por marca.
    4- Buscar insumo por caracteristica.
    5- listar insumos ordenados.
    6- Realizar compras.
    7- Guardar Json.
    8- Leer Json.
    9- Acturalizar precios.
    10- Agregar nuevo producto.
    11- Guardar en json o csv.
    SALIDA- Salir del programa.
    """)

    opcion = input('ingrese lo que quiere hacer: ')
    return opcion
from funciones import *
import os
import re

bandera_json = False
datos = None
lista_marcas = []
set_marca = {()}
bandera_datos = False
bandera_set = False
bandera_actualizacion = False
bandera_lista_completa = False


while True:
    os.system("cls")
    match menu_Info_Baus():
        case "1":
            datos = Traer_datos_csv_a_diccionario_2("Insumos.csv", ["id", "nombre", "marca", "precio", "caracteristicas"])
            normalizar_datos(datos)
            datos = importar_stock(datos)
            bandera_datos = True
        case "2":
            if bandera_datos:
                lista_marcas = Filtrar_lista(datos, 'marca')
                set_marca = set(lista_marcas)
                Contar_segun_parametro(set_marca, lista_marcas, 'Marca', 'Contador')
                bandera_set = True
            else:
                print("Primero se debe cargar el archivo")
        case "3":
            if bandera_datos and bandera_set:
                Listar_por_key(datos, set_marca, 'marca')
            else:
                print("Primero se debe cargar el archivo o la lista de marcas")
        case "4":
            if bandera_datos:
                Buscar_insumo_por_caracteristica_con_lista(datos, 'caracteristicas')
            else:
                print("Primero se debe cargar el archivo")
        case "5":
            if bandera_datos:
                lista_ordenada = OrdenarLista_2(datos, 'marca', 'precio')
                Imprimir_lista_dicc(lista_ordenada)
            else:
                print("Primero se debe cargar el archivo")
        case "6":
            if bandera_datos:
                carrito_compras, carrito_cantidad = realizar_compra(datos)
                factura(carrito_compras, carrito_cantidad, "factura.txt")
            else:
                print("Primero se debe cargar el archivo")
        case "7":
            if bandera_datos:
                lista_filtrada = Buscar_insumo_por_nombre_con_lista(datos, 'nombre', 'Disco Duro')
                Crear_json_escribir('Discos_Duros.json', lista_filtrada)
                bandera_json = True
            else:
                print("Primero se debe cargar el archivo")
        case "8":
            if bandera_datos and bandera_json:
                Mostrar_json('Discos_Duros.json')
            else:
                print("No se puede.")
        case "9":
            if bandera_datos:
                lista_nueva = Crear_nueva_lista_impuesto(datos, 'precio', 1.084)
                datos_actualizados = actualizar_diccionarios(datos, 'precio', lista_nueva)
                Diccionaro_a_csv(datos_actualizados)
                Csv_nuevo(Diccionaro_a_csv(datos_actualizados), "Insumos_copia.csv")
                bandera_actualizacion = True
            else:
                print("Primero se debe cargar el archivo")
        
        case "10":
            if bandera_datos and bandera_actualizacion:
                marcas = Traer_dato_csv("marcas.txt")
                diccionario_nuevo = agregar_nuevo_diccionario(marcas, ["id", "nombre", "marca", "precio", "caracteristicas", "stock"], ((datos[-1]["id"]) + 1))
                if len(diccionario_nuevo) != 0:
                    datos_actualizados.append(diccionario_nuevo)
                    print(diccionario_nuevo)
                else:
                    print("No se agrego ningun insumo.")
                bandera_lista_completa = True
            else:
                print("primero se debe actualizar los precios.")
        case "11":
            if bandera_lista_completa:
                Eleccion_csv_json(datos_actualizados)
            else:
                print("Todavia no se puede")

        case "SALIDA":
            print("Hasta luego... !!!")
            break
    os.system("pause")
