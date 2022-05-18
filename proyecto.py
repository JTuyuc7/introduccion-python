# Proyecto Agenda de telefonos en Python

import os
CARPETA = 'contactos/'
EXTENSION = '.txt'

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria
def app():
    # Crear el directorio donde se guardaran los contactos
    crear_directorio()
    # Crear las opciones de menu
    mostrar_menu()
    # Preguntar la accion a realizar
    preguntar = True
    while preguntar:
        opcion = input('Selecciona una opcion a realizar \r\n')
        opcion = int(opcion)

        if( opcion == 0):
            print('Bye -*-*-*-*-*-*-*-*-*-* :)')
            preguntar = False
        elif(opcion == 1):
            agregar_contacto()
            preguntar = False
        elif(opcion == 2):
            editar_contacto()
            preguntar = False
        elif(opcion == 3):
            ver_contacto()
            preguntar = False
        elif(opcion == 4):
            buscar_contacto()
            preguntar = False
        elif(opcion == 5 ):
            eliminar_contacto()
            preguntar = False
        else:
            print('Por favor selecciona una opcion valida')

def eliminar_contacto():
    nombre_contacto = input('Ingresa el contacto a eliminar \r\n')
    
    try:
        os.remove(CARPETA+nombre_contacto+EXTENSION)
        print('Contacto eliminado correctamente -*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    except:
        print(f'El contacto {nombre_contacto} no existe *-*-*-*-*-*-*-*-*-*-*')
    # Reiniciar la pp
    app()

def buscar_contacto():
    nombre_contacto = input('Ingresa el nombre del contacto a buscar: \r\n')
    # Revisar si el contacto existe
    existe = existe_contacto(nombre_contacto)
    if(existe):
        with open(CARPETA+nombre_contacto+EXTENSION) as contacto:
            for linea in contacto:
                print(linea.rstrip())
    else:
        print(f'El contacto {nombre_contacto} no existe -*-*-*-*-*-*-*-*-*')
    # Reiniciar la app
    app()

def ver_contacto():
    print('La lista de tus contactos: \r\n')
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    
    for archivo in archivos_txt:
        with open(CARPETA+archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    # Reiniciar la app
    app()

def editar_contacto():
    nombre_anterior = input('Ingresa el nombre del contacto a editar \r\n')
    # Revisar que el archivo exista
    existe = existe_contacto(nombre_anterior)

    if (existe):
        with open(CARPETA+nombre_anterior+EXTENSION, 'w') as archivo:
            nuevo_nombre = input('Ingresa el nuevo nombre: \r\n')
            telefono_contacto = input('Ingresa el nuevo numero de contacto: \r\n')
            print('Selecciona la categoria de contacto \r\n')
            print('1 - Amigos')
            print('2 - Negocio')
            print('3 - Escuela')
            seleccionar = True
            categoria_seleccionada = input('Selecciona tu una opcion \r\n')
            categoria_seleccionada = int(categoria_seleccionada)
            categoria_contacto = ''
            while seleccionar:
                if(categoria_seleccionada == 1):
                    categoria_contacto = 'Amigos'
                    seleccionar = False
                elif (categoria_seleccionada == 2 ):
                    categoria_contacto = 'Negocio'
                    seleccionar = False
                elif( categoria_seleccionada == 3):
                    categoria_contacto = 'Escuela'
                    seleccionar = False
                else:
                    print('Seleccion no valida, Agregado como Amigo')
                    categoria_contacto = 'Amigos'
                    seleccionar = False
            
            contacto = Contacto(nuevo_nombre, telefono_contacto, categoria_contacto)
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')
            archivo.close()
            os.rename(CARPETA+nombre_anterior+EXTENSION, CARPETA+nuevo_nombre+EXTENSION)
            print('\r\n Contacto Editado correctamente -*-*-*-*-*-*-*')
    else:
        print('El contacto no existe')
    # Reiniciar la app
    app()

def agregar_contacto():
    print('Escribe los datos para agregar el contacto')
    nombre_contacto = input('Ingresa el nombre del contacto \r\n')
    
    # Validar que el archivo ya exista
    existe = os.path.isfile(CARPETA+nombre_contacto+EXTENSION)

    if not (existe):
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            # Crear los valores restantes
            telefono_contacto = input('Ingresa el numero de contacto \r\n')

            print('Selecciona la categoria de contacto \r\n')
            print('1 - Amigos')
            print('2 - Negocio')
            print('3 - Escuela')
            seleccionar = True
            categoria_seleccionada = input('Selecciona tu una opcion \r\n')
            categoria_seleccionada = int(categoria_seleccionada)
            categoria_contacto = ''
            while seleccionar:
                if(categoria_seleccionada == 1):
                    categoria_contacto = 'Amigos'
                    seleccionar = False
                elif (categoria_seleccionada == 2 ):
                    categoria_contacto = 'Negocio'
                    seleccionar = False
                elif( categoria_seleccionada == 3):
                    categoria_contacto = 'Escuela'
                    seleccionar = False
                else:
                    print('Seleccion no valida, Agregado como Amigo')
                    categoria_contacto = 'Amigos'
                    seleccionar = False

            # Crear la instancia de la clase Contacto
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            print('\r\n Contacto agregado correctamente*-*-*-*-*-*-*-*-*')
    else:
        print('El contacto ya existe \r\n')
    # Reiniciar la app
    app()

def mostrar_menu():
    #print('Selecciona una opcion a usar')
    print('1 - Agregar nuevo contacto')
    print('2 - Editar contacto')
    print('3 - Ver Contacto')
    print('4 - Buscar contacto')
    print('5 - Eliminar contacto')
    print('0 - Salir')

def crear_directorio():
    if not os.path.exists(CARPETA):
        # Si la carpeta no existe crearla
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    return os.path.isfile(CARPETA+nombre+EXTENSION)
app()