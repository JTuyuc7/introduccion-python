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

# Instanciar la clase
restaurante = Restaurante('Pizzeria Napoli XD', 'Comida italiana', 55)
#print(restaurante.__precio)
restaurante.mostrar_informacion() # Ejecutar los metodos de la instancia de la clase
# Usar el metodo para cambiar el precio
restaurante.set_precio(190)
restaurante.get_precio()

restaurante2 = Restaurante('Bongorotondo XD', 'Comida china', 100)
restaurante2.mostrar_informacion()

# Mostrar el precio
restaurante2.set_precio(90)
restaurante2.get_precio()

