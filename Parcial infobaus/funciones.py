import re
from functools import reduce
import json
from random import *

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



def validar_entero()->int:
    while True:
        try:
            numero = int(input("ingrese el numero: "))
            if numero > 0:
                break
        except ValueError:
            print("eso no es un numero")
    return numero
        


def maximo_diccionario(lista:list, parame:str)->int:
    for el in lista:
        bandera = True
        if bandera == True or el[parame] > maximo:
            maximo = el[parame]
            bandera = False
    return maximo


def minimo_diccionario(lista:list, parame:str)->int:
    for el in lista:
        bandera = True
        if bandera == True or el[parame] < minimo:
            minimo = el[parame]
            bandera = False
    return minimo


def filtrar_por(lista:list, key:str, value:any)->list:
    """
    Filtra una lista segun el parametro que le pasemos
    Necesita: lista, key y un value
    Devuelve: La lista ya filtrada para usar
    """
    if Validar_lista(lista):
        lista_filtrada = []
        for item in lista:
            if item[key] == value:
                lista_filtrada.append(item)
    return lista_filtrada

def normalizar_datos(lista:list):
    """
    Funciona para verificar si los datos numéricos están casteado correctamente.
    Si no es asi los cambia.
    
    """
    bandera_casteo = False
    for diccionario in lista:
        if 'edad' in diccionario:
            diccionario['edad'] = int(diccionario['edad'])
            bandera_casteo = True

        if 'altura' in diccionario:
            diccionario['altura'] = float(diccionario['altura'])
            bandera_casteo = True

        if 'peso' in diccionario:
            diccionario['peso'] = float(diccionario['peso'])
            bandera_casteo = True
        if 'fuerza' in diccionario:
            diccionario['fuerza'] = int(diccionario['fuerza'])
    
    if bandera_casteo:
        print('Datos normalizados')
    
    return lista


def obtener_nombre(diccionario:dict)->str:
    """"
    recibirá por parámetro un
    diccionario el cual representara a un héroe y devolverá un string el cual
    contenga su nombre formateado de la siguiente manera:
    Nombre: Howard the Duck
    """
    for el in diccionario:
        if el == 'nombre':
            nombre = diccionario[el]
            nombre = f'Nombre: {nombre}'
            return nombre

def imprimir_dato(string:str):
    print(string)

def obtener_nombre_y_dato(diccionario:dict, key:str):
    """"
    recibirá por parámetro un
    diccionario el cual representara a un héroe y una key (string) la cual
    representará el dato que se desea obtener.
    La función deberá devolver un string el cual contenga el nombre y dato
    (key) del héroe a imprimir.
    """
    nombre = obtener_nombre(diccionario)
    for i in diccionario:
        if i == key:
            dato = diccionario[key]
            return print(f'{nombre} | {key}: {dato}')
        

def calcular_max(lista:list, key:str):
    """
    recibe una lista y un key y devuelve el maximo
    """
    bandera = True
    for persona in lista:
        for el in persona:
            if el == key:
                if bandera == True or persona[key] >= maximo:
                    maximo = persona[key]
                    item = persona
                    bandera = False
        return obtener_nombre_y_dato(item, key)


def calcular_min(lista:list, key:str):
    bandera = True
    for persona in lista:
        for el in persona:
            if el == key:
                if bandera == True or persona[key] < minimo:
                    minimo = persona[key]
                    item = persona
                    bandera = False
        return obtener_nombre_y_dato(item, key)

def calcular_max_min_dato(lista:list, operacion:str, key:str):
    if operacion == 'maximo':
        calcular_max(lista, key)
    elif operacion == 'minimo':
        calcular_min(lista, key)
    else:
        print(-1)


def Validar_lista(lista:any):
    validacion = True
    if not  type(lista) == list:
        print("Esto no es una lista")
        validacion = False
    if len(lista) == 0:
        validacion = False
    return validacion


def Validar_diccionario(diccionario:any):
    validacion = True
    if not  type(diccionario) == dict:
        print("Esto no es un diccionario")
        validacion = False
    return validacion

def Validar_set(sett:any):
    validacion = True
    if not  type(sett) == set:
        print("Esto no es un set")
        validacion = False
    return validacion

def Validar_float(flotante:any):
    validacion = True
    if not  type(flotante) == float:
        print("Esto no es un float")
        validacion = False
    return validacion












def normalizar_datos(lista:list)->list:
    """
    Funciona para verificar si los datos numéricos están casteado correctamente.
    Si no es asi los cambia.

    Args:
        lista (list): Lista con diccionarios

    Returns:
        list: lista con casteo.
    """
    bandera_casteo = False
    if Validar_lista(lista):
        for diccionario in lista:
            if 'id' in diccionario:
                diccionario['id'] = int(diccionario['id'])
                bandera_casteo = True

            if 'precio' in diccionario:
                diccionario['precio'] = float(diccionario['precio'])
                bandera_casteo = True

            if 'peso' in diccionario:
                diccionario['peso'] = float(diccionario['peso'])
                bandera_casteo = True
            if 'fuerza' in diccionario:
                diccionario['fuerza'] = int(diccionario['fuerza'])
    
    if bandera_casteo:
        print('Datos normalizados')
    
    return lista



def Filtrar_lista(lista_general:list, clave:str):
    """
    Filtra una lista segun un parametro

    Args:
        lista_general (list): lista con diccionarios
        clave (str): key por el cual quiero filtrar la lista.

    Returns:
        list: lista filtrada
    """
    if Validar_lista(lista_general):
        lista_con_repeticiones = []
        for el in lista_general:
            lista_con_repeticiones.append(el[clave]) 
    return lista_con_repeticiones


def Contar_segun_parametro(lista_set:set, lista:list, nombre_1:str, nombre_2:str):
    """
    Su funcion es tomar una lista sin filtrar y una lista ya filtrada,
    luego comparar cuantas veces se repite ese elemento y lo cuenta

    Args:
        lista_set (set): lista sin repeticiones.
        lista (list): lista con repeteciones.
        nombre_1 (str): el key por el cual estamos contando.
        nombre_2 (str): La palabra que usamos para mostrar 
        la cantidad de repeteciones(contador).
    
    """
    if Validar_lista(lista) and Validar_set(lista_set):
        for el in lista_set:
            lista_aux = []
            diccionario = {}
            contador = lista.count(el)
            diccionario[nombre_1] = el
            diccionario[nombre_2] = contador
            lista_aux.append(diccionario)
            print(f"   {nombre_1}                {nombre_2} ")
            for el in lista_aux:
                print(f"   {el[nombre_1]:<15}       {el[nombre_2]:<10}")
                print("------------------------------------------")


def Traer_datos_csv_a_diccionario(key_archivo: str):
    listado = []
    with open(key_archivo, "r", encoding="utf-8") as file:
        data = file.read()
    datos = data.split("\n")
    for persona in datos:
        item = persona.split(",")
        diccionario = {}
        diccionario['id'] = item[0]
        diccionario['nombre'] = item[1]
        diccionario['marca'] = item[2]
        diccionario['precio'] = item[3]
        diccionario['caracteristicas'] = item[4]
        diccionario['id'] = diccionario['id'].replace('"', '')
        diccionario['caracteristicas'] = diccionario['caracteristicas'].replace('"', '')
        diccionario["precio"] = diccionario["precio"].replace("$", '')
        listado.append(diccionario)
    return listado


def listar_por_key(lista:list, lista_filtrada:set, key:str, key_2:str, key_3:str):
    if Validar_lista(lista) and Validar_set(lista_filtrada):
        for item in lista:
            for el in lista_filtrada:
                if el == item[key]:
                    print(f' {item["marca"]}: || {item["nombre"]}  || {item["precio"]}')
#Falta darle una mano de tuerca.


def Buscar_insumo_por(lista_con_diccionario:list, key:str):
    """"
    El usuario ingresa un patron y
    la funcion se escarga de buscar que elementos
    puede llegar a tener relacion, si es asi los muestra.
    """ 
    if Validar_lista(lista_con_diccionario):
        lista = []
        busqueda = input("Que marca desea buscar: ")
        for dicc in lista_con_diccionario:
            for i in dicc:
                if i == key:
                    if re.search(busqueda, dicc[key]):
                        lista.append(dicc)

        if type(lista) == None:
            return print("Ocurrio un error.")
        else:
            return lista


def encontrar_insumo(lista:list, key:str, value:any):
    if Validar_lista(lista):
        for diccionario in lista:
            for clave in diccionario:
                if clave == key and diccionario[key] == value:
                    insumo = diccionario
                    return insumo




def Buscar_insumo_por_caracteristica_con_lista(lista_con_diccionario:list, key:str):
    """
    El usuario ingresa un patron y
    la funcion se escarga de buscar que elementos
    puede llegar a tener relacion, si es asi los muestra.

    Args:
        lista_con_diccionario (list): lista con diccionarios.
        key (str): clave donde vamos a buscar. Ejemplo(caracteristicas).

    """
    if Validar_lista(lista_con_diccionario):
        busqueda = input("Que desea buscar: ")
        diccionarios_final = []
        for diccionarios in lista_con_diccionario:
            for item in diccionarios:
                if item == key:
                    for caracteristica in diccionarios[key]:
                        if re.search(busqueda, caracteristica, re.IGNORECASE):
                            diccionarios_final.append(diccionarios)
    if  len(diccionarios_final) == 0:
        return print("No se encontro nada.")
    else:
        return Imprimir_lista_dicc(diccionarios_final)

import re
def Buscar_insumo_por_nombre_con_lista(lista_con_diccionario:list, key:str, patron:str):
    """ El usuario ingresa un patron y
    la funcion se escarga de buscar que elementos
    puede llegar a tener relacion, si es asi los muestra.

    Args:
        lista_con_diccionario (list): Lista con diccionarios.
        key (str): parametro para buscar.
        patron (str): cadena str.

    Returns:
        _type_: _description_
    """
    if Validar_lista(lista_con_diccionario):
        lista = []
        for diccionario in lista_con_diccionario:
            if key in diccionario:
                nombre = diccionario[key]
                if re.search(patron, nombre, re.IGNORECASE):
                    lista.append(diccionario)
    return lista



def OrdenarLista_2(lista:list, key:str, key_2:str):
    """Ordena una lista con diccionarios,
    segun por 2 parametros.

    Args:
        lista (list): Lista con diccionarios.
        key (str): parametro para ordenar la lista.
        key_2 (str): Segundo parametro para ordenar la lista.

    Returns:
        list: lista ordenada.
    """
    if Validar_lista(lista):
        tam = len(lista)
        for i in range(0, tam - 1):
            for j in range(i + 1, tam):
                if lista[i][key] == lista[j][key]:
                    if lista[i][key_2] < lista[j][key_2]:
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux
                elif lista[i][key] > lista[j][key]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    return lista
                


def Imprimir_diccionario_1_caract(diccionario:dict):
    """
    Imprime un diccionarios mostrando,
    todo este y en el caracteristicas solo 1.
    """
    if Validar_diccionario(diccionario):
        imprimir_dato(f""" {diccionario['id']:<2} || {diccionario['nombre']:<52} || {diccionario['marca']:<20} || {diccionario['precio']:<5} || {diccionario['caracteristicas'][0]}
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------""")

def Imprimir_diccionario_completo(diccionario:dict):
    """
    Printea un diccionario.
    """
    if Validar_diccionario(diccionario):
        imprimir_dato(f""" {diccionario['id']:<2} || {diccionario['nombre']:<52} || {diccionario['marca']:<20} || {diccionario['precio']:<5} || {diccionario['caracteristicas']}
    ------------------------------------------------------------------------------------------------------------------------------------------------------------""")


def Imprimir_lista_dicc(lista:list):
    """Imprime toda una lista de diccionarios,
    pero es caracteristicas, solo una.

    Args:
        lista (list): Lista con diccionarios
    """
    if Validar_lista(lista):
        for dicc in lista:
            Imprimir_diccionario_1_caract(dicc)


# def Carrito_compras(lista:list, key:str):
#     """
#     Su funcion es interactuar con el cliente y almacenar algun producto,
#     Tambien si el usuario ingresa algo dentro del carro. Muestra Factura.
#     """
#     if Validar_lista(lista):
#         carrito = []
#         principio = 'Si'
#         while principio == 'Si':
         

def Total_compra(lista_diccionario: list):
    """
    Muestra un subtotal, para saber cuanto va a gastar.
    Usa Reduce 
    """
    if Validar_lista(lista_diccionario):
        lista_sub_totales = []
        for diccionario in lista_diccionario:
            nombre = diccionario['producto'][0]
            precio = diccionario['producto'][1]
            cantidad = diccionario['cantidad']
            sub_total = precio * cantidad
            lista_sub_totales.append(sub_total)
        Total = reduce(lambda ant, desp: ant + desp, lista_sub_totales)
        print(f'''           CANT.    DESCRIPCION    PRECIO.U    IMPORTE
        {cantidad} || {nombre} || {precio}:  {Total}
        --------------------------------------------------------''')


def Crear_diccionario(lista_key:list, lista:list):
    """Crea un diccionario.

    Args:
        lista_key (list): Lista con strings
        lista (list): lista con cadenas de string.

    Returns:
        dict: Retorna un diccionario con las keys,
        pasadas por el parametro.
    """
    if Validar_lista(lista) and Validar_lista(lista_key):
        diccionario = {}
        for i in range(len(lista_key)):
            diccionario[lista_key[i]] = lista[i]
    return diccionario


#lista_key = ['id' ,"nombre", "marca", "precio", "caracteristicas"]

def Retocar_diccionario_(lista:list):
    """Su funcion es factorizar y hacer utilizable el documento.
    

    Args:
        lista (list): Lista.
    """
    if Validar_lista(lista):
        for diccionario in lista:
            diccionario['id'] = diccionario['id'].replace('"', '')
            diccionario['caracteristicas'] = diccionario['caracteristicas'].replace('"', '')
            diccionario["caracteristicas"] = diccionario["caracteristicas"].replace("|!*|", "||")
            diccionario["caracteristicas"] = lista_caracteristicas = diccionario["caracteristicas"].split("||")
            diccionario["precio"] = diccionario["precio"].replace("$", '')


def Traer_datos_csv_a_diccionario_2(archivo:str, lista_key:list)->list:
    """Abre un archivo csv y lo refactoriza para usarlo
    como diccionario

    Args:
        archivo (str): Nombre del archivo.
        lista_key (list): Lista con los keys 
        para crear el diccionario.

    Returns:
        list: Lista con diccionarios.
    """
    
    if Validar_lista(lista_key):
        listado = []
        with open(archivo, "r", encoding="utf-8") as file:
            data = file.read()
        datos = data.split("\n")
        for persona in datos:
            item = persona.split(",")
            diccionario = Crear_diccionario(lista_key, item)
            listado.append(diccionario)
        eliminar_lista = listado.pop(0)
        Retocar_diccionario_(listado)
        return listado

def crear_factura(ruta_archivo:str, lista_diccionarios:list):
    """
    Su funcion es crear un factura mostrando cantidad,
    descripcion, precio.U, importe.
    """
    if Validar_lista(lista_diccionarios):
        lista_sub_totales = []
        for diccionario in lista_diccionarios:
            nombre = diccionario['producto'][0]
            precio = diccionario['producto'][1]
            cantidad = diccionario['cantidad']
            sub_total = precio * cantidad
            lista_sub_totales.append(sub_total)
            Total = reduce(lambda ant, desp: ant + desp, lista_sub_totales)
            contenido = (f'''           CANT.    DESCRIPCION    PRECIO.U    IMPORTE
            {cantidad} || {nombre} || {precio}:  {sub_total}
            -----------------------------------------------------------
                    TOTAL                                   {Total}''')
        archivo = open(ruta_archivo, 'w')
        archivo.write(contenido)
        archivo.close()
        print("Archivo de factura creado exitosamente.")


def Mostrar_archivo_txt(archivo:str):
    """
    Muestra un archivo.txt
    """
    archivo = open(archivo, "r")
    contenido = archivo.read()
    archivo.close()
    print(contenido)

def Listar_por_key(lista:list, set:set, key:str):
    """Mostrar todos los datos relacionados,
    a cada elemento del set.

    Args:
        lista (list): lista con diccionarios.
        set (set): lista sin repetecion.
        key (str): clave por el cual queremos identificar.
    """
    for marca in set:
        print(f"------------------------------------")
        print(f"--------------{marca}--------------")
        for diccionario in lista:
            for clave in diccionario:
                if clave == key:
                    if diccionario[clave] == marca:
                        print("  {:<52} || Precio: ${:<8}||".format(diccionario["nombre"], diccionario["precio"]))




def Crear_json_escribir(nombre: str, contenido:any):
    """Crea un archivo.josn y lo escribe.

    Args:
        nombre (str): nombre de archivo + .json.
        contenido (any): Contenido del archivo
    """
    contenido = json.dumps(contenido, indent=4, ensure_ascii=False)
    with open(f'{nombre}', "w") as file:
        file.write(contenido)
    print("Carga Completada.")

def Mostrar_json(archivo:str):
    """
    Muestra un archivo Json
    """
    with open(archivo, "r") as file:
        contenido = file.read()
    contenido = json.loads(contenido)
    Imprimir_lista_dicc(contenido)


def Crear_nueva_lista_impuesto(lista:list, key:str, impuesto:float):
    """Actualiza los precios.

    Args:
        lista (list): lista con diccionarios.
        key (str): 'precio'
        impuesto (float): cantidad a aumentar.

    Returns:
        list: lista precios actualizada.
    """
    if Validar_lista(lista) and Validar_float(impuesto):
        lista_aux = Filtrar_lista(lista, key)
        nueva_lista = list(map(lambda item: item * impuesto, lista_aux))
        return nueva_lista



def Csv_nuevo(lista_csv:list, archivo:str):
    """
    Agrego datos str a un archivo.csv.
    """
    if Validar_lista(lista_csv):
        with open(archivo, "w", encoding="utf-8") as file:
            for linea in lista_csv:
                file.write(f'{linea} \n')
        print("Todo normalizado")

def actualizar_diccionarios(lista:list, clave:str, lista_nueva:list):
    """ 
    Su funcion es actualizar un key de un diccionario


    Args:
        lista (list): lista diccionarios.
        clave (str): key a actualizar
        lista_nueva (list): una lista con la key actualiada.

    Returns:
        list: Lista de diccionarios Actualizados.
    """
    if Validar_lista(lista) and  Validar_lista(lista_nueva):
        for i in range(len(lista)):
            lista[i][clave] = lista_nueva[i]
        return lista

def Diccionaro_a_csv(lista_diccionarios:list)->str:
    """
    Su funcion es pasar una lista de diccionaros
    a un formato "parecido" a csv.
    """
    if Validar_lista(lista_diccionarios):
        csv = []
        for diccionario in lista_diccionarios:
            contenido = f"{diccionario['id']},{diccionario['nombre']},{diccionario['marca']},{diccionario['precio']},{diccionario['caracteristicas']},{diccionario['stock']}"
            csv.append(contenido)
        return(csv)

def agregar_nuevo_diccionario(lista:list, lista_key:list, id:int):
    lista_datos = []
    diccionario = {}
    if Validar_lista(lista) and Validar_lista(lista_key):
        lista_datos.append(id)
        while True:
            nombre = input("Ingrese el nombre: ")
            if nombre.isalpha() and len(nombre) != 0:
                lista_datos.append(nombre)
                break
            else:
                print("Error.Reingrese el dato: ")

        marca = Elija_marca(lista)
        lista_datos.append(marca)

        while True:    
            precio = (input("Ingrese el precio: "))
            if precio.isdigit() and int(precio) > 0:
                lista_datos.append(float(precio))
                break
            else:
                print("Error.Reingrese el dato: ")

        while True:
            cantidad_caracteristicas = input("Cuantas caracteristicas desea escribir, maximo 3: ")
            if int(cantidad_caracteristicas) > 0 and int(cantidad_caracteristicas) < 4 and  cantidad_caracteristicas.isdigit():
                cantidad_caracteristicas = int(cantidad_caracteristicas)
                break
            else:
                cantidad_caracteristicas = input("Reingrese el dato.")

        while True:
            caracteristicas = []
            for i in range(cantidad_caracteristicas):
                while True:
                    carateristica = input("Ingrese las caracteristicas del producto: ")
                    if len(carateristica) != 0:
                        caracteristicas.append(carateristica)
                        break
                    else:
                        print("Reingrese la caracteristica: ")
                        continue
            if len(caracteristicas) != 0:
                lista_datos.append(caracteristicas)
                break
            else:
                print("Ingrese caracteristicas.")
                continue
        
        while True:
            stock = input("Ingrese el stock: ")
            if stock.isdigit() and int(stock) > 0 and int(stock) < 11:
                stock = int(stock)
                lista_datos.append(stock)
                break
            else:
                print("Ingrese stock !!!!")
        
    for i in range(len(lista_key)):
        diccionario[lista_key[i]] = lista_datos[i]
        lista.append(diccionario)
    
    return diccionario

def Traer_dato_csv(archivo):
    """Traer a memoria datos de un archivo csv.

    Args:
        archivo (str): Nombre del archivo

    Returns:
        list: Retorna una lista con la informacion.
    """
    with open(archivo, "r", encoding="utf-8") as file:
        contenido = file.read()
    contenido = contenido.split("\n")
    contenido[0] = "Intel"   #Me salia el intel raro con errores y no supe resolverlo asi que meti mano.
    return contenido

def Elija_marca(lista:list):
    Validar_lista(lista)
    print(lista)
    while True:
        opcion = input("Que marca busca: ")
        if opcion.isalpha() and opcion in lista:
            print("Marca encontrada.")
            break
        else:
            print("ERROR, Marca no encotrada.")
            continue
    return opcion

def Eleccion_csv_json(lista:list):
    """Crea un archivo csv o json.

    Args:
        lista (list): Lista con diccionarios.
    """
    while True:
        if Validar_lista(lista):
            eleccion = input("Quiere exportar en csv o json: ")
            if eleccion == "csv":
                nombre_archivo = input("Que nombre va a llevar: ")
                lista = Diccionaro_a_csv(lista)
                Csv_nuevo(lista, nombre_archivo)
                break
            elif eleccion == "json":
                nombre_archivo = input("Que nombre va a llevar: ")
                Crear_json_escribir(nombre_archivo, lista)
                break
            else:
                print("Reingrese la eleccion.")
                continue

def seleccion_marca(lista:list, key:str):
    """Se encarga de seleccion de marca.

    Args:
        lista (list): lista de diccionarios
        key (str): clave de un diccionario.

    Returns:
        list: lista de id.
    """
    lista_marcas = []
    lista_id = []
    if Validar_lista(lista):
        for diccionario in lista:
            for clave in diccionario:
                if clave == key:
                    lista_marcas.append(diccionario[key])

        set_marcas = set(lista_marcas)

        for marca in set_marcas:
            print(f"|{marca}|")

        while True:
            input_marca = input("Selecciona que marca queres comprar: ")
            if input_marca in set_marcas:
                print(f"||---------------{input_marca}-----------||")
                break
            else:
                print("ERROR.")
                continue

        for dicc in lista:
            for clave in dicc:
                if clave == key and dicc[clave] == input_marca:
                    print(f'''
                    --------------------------------
                    Nombre: {dicc["nombre"]}
                    --------------------------------
                    ID: {dicc["id"]}
                    -------------------------------- 
                    Marca:  {dicc["marca"]}|| 
                    --------------------------------
                    Precio:  {dicc["precio"]}
                    --------------------------------
                    Stock:  {dicc["stock"]}''')
                    lista_id.append(dicc["id"])

    return lista_id

def realizar_compra(lista:list):
    """Funcion funcion que valida que puedas comprar el objeto y que tenga stock disponible

    Args:
        lista (list): lista de id.

    Returns:
        tuple: lista con los diccionarios seleccionadios y 
        otras lista con la cantidad.
    """
    carrito_compras = []
    carrito_cantidad = []
    stock_producto = 0
    respuesta = "no"

    while respuesta == "no":

        validacion_id = seleccion_marca(lista, "marca")
        while True:

            id_seleccionado = input("Ingrese el numero de ID que desea Comprar: ")

            if id_seleccionado.isdigit() and int(id_seleccionado) > 0: 
                if int(id_seleccionado) in validacion_id:
                    id_seleccionado = int(id_seleccionado)
                    break
                else:
                    print("ingreso un id incorrecto.")
                    continue
            else:
                print("Error.Reingrese el dato.")
                continue

        for dicc in lista:

            for clave in dicc:

                if clave == "id":

                    if dicc[clave] == id_seleccionado: 
                        
                            stock_producto = dicc["stock"]

                            while True:
                                cantidad = input("Cual es la cantidad del producto que desea comprar?: ")
                                if cantidad.isdigit() and int(cantidad) > 0 and int(cantidad) < 11:
                                    if (int(cantidad) <= stock_producto):

                                        cantidad = int(cantidad)
                                        stock_producto -= cantidad
                                        print(f"STOCK: {stock_producto}")
                                        carrito_compras.append(dicc)
                                        carrito_cantidad.append(cantidad)
                                        dicc["stock"] = stock_producto
                                        break
                                    else:
                                        print("Pruebe de con menos cantidad")
                                else:
                                    print("Cantidad puede ser de 1-10.")
                    
        print("Producto agregado al carrito.")

        respuesta = input("Se agrego correctamente al carrito:?(si/no):  ")
        while respuesta != "si" and respuesta != "no":
            respuesta = input("ERROR, Desea comprar otro producto?(si/no):  ")

        print(carrito_compras)

    return carrito_compras, carrito_cantidad


def factura(lista_diccionarios:list, lista_cantidad:list, nombre_archivo:str):
    """
    Se encarga de hacer la factura.

    Args:
        lista_diccionarios(list): Es una lista con diccionarios.
        lista_cantidad(list): Lista con la cantidades pedidas.
        nombre_archivo(str): Nombre de el archivo.txt.

    """
    if Validar_lista(lista_diccionarios) and Validar_lista(lista_cantidad):
        total = 0

        for insumo, numero in zip(lista_diccionarios, lista_cantidad):
            subtotal = float(insumo["precio"]) * numero
            total += subtotal
            contenido = f"""             PRODUCTO     PRECIO     CANTIDAD     SUBTOTAL
                {insumo['nombre']}   {insumo['precio']}         {numero}            {subtotal}
                ---------------------------------------------------------------------------------------
                        Total                                                           $$${total}"""
        archivo = open(nombre_archivo, 'w')
        archivo.write(contenido)
        archivo.close()
        print(f"El diccionario se guardo correctamente en {nombre_archivo}.")





def agregar_stock(diccionario):
    diccionario["stock"] = randrange(1, 10)
    return diccionario

def importar_stock(lista):
    """Agrega la key "stock" a los diccionarios
    de la lista y le declara un numero random.

    Args:
        lista (list): lista con diccionarios

    Returns:
        lista(list): lista con diccionarios con la key "stock"
    """
    lista_final = list(map(agregar_stock,lista))
    return lista_final