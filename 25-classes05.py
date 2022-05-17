# Classes y POO en Python //TODO prueba
class Restaurante:
    # Definir los constructores en Python
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Propiedades del constructor que estan publicos
        self.categoria = categoria
        self.precio = precio # agregando _ al inicio se declara PROTECTED y agregando dobre __ se declara como Privada

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')

    # Usando los GETTERS Y SETTERS en las clases en Python
    def get_precio(self):
        print(f'Precio {self.precio} usando GETTERS')

    # Usando el SETTER
    def set_precio(self, precio):
        self.precio = precio

# Usar la HERENCIA en Python
class Hotel(Restaurante):
    def __init__(self, nombre, categoria, precio, alberca ): # Usar el constructor de la clase Heredada
        super().__init__(nombre, categoria, precio) # Usar el constructor de la clase Heredada
        self.alberca = alberca

    # Reescribir un metodo en una clase heredada -- (EL METODO DEBE DE LLAMARSE IGUAL)
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Alberca: {self.alberca}')

    # Agregar nuevos metodos solo para la clase heredada
    def get_alberca(self):
        return self.alberca

hotel = Hotel('Antigua Guatemala', 'Hotel de Invierno', 1500, 'Si')

hotel.mostrar_informacion()

# Mostrar la alberca
#alberca = hotel.get_alberca()
#print(f'Disponibilidad de alberca {alberca}')