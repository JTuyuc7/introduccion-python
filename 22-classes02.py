# Classes y POO en Python //TODO prueba

class Restaurante:
    # Definir los constructores en Python
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')

# Instanciar la clase
restaurante = Restaurante('Pizzeria Napoli XD', 'Comida italiana', 55)
restaurante.mostrar_informacion() # Ejecutar los metodos de la instancia de la clase

restaurante2 = Restaurante('Bongorotondo XD', 'Comida china', 100)
restaurante2.mostrar_informacion()
