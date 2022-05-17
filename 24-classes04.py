# Classes y POO en Python //TODO prueba
class Restaurante:
    # Definir los constructores en Python
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Propiedades del constructor que estan publicos
        self.categoria = categoria
        self.__precio = precio # agregando _ al inicio se declara PROTECTED y agregando dobre __ se declara como Privada

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')

    # Usando los GETTERS Y SETTERS en las clases en Python
    def get_precio(self):
        print(f'Precio {self.__precio} usando GETTERS')

    # Usando el SETTER
    def set_precio(self, precio):
        self.__precio = precio

# Usar la HERENCIA en Python
class Hotel(Restaurante):
    def __init__(self, nombre, categoria, precio): # Usar el constructor de la clase Heredada
        super().__init__(nombre, categoria, precio) # Usar el constructor de la clase Heredada

hotel = Hotel('Antigua Guatemala', 'Hotel de Invierno', 1500)

hotel.mostrar_informacion()