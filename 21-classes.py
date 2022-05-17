# Classes y POO en Python //TODO prueba

class Restaurante:
    def agregar_restaurante(self, nombre): # Definir metodos de la clase
        self.nombre = nombre

    def mostrar_informacion(self):
        print(f'Mostrando informacion {self.nombre}')

# Instanciar la clase
restaurante = Restaurante()

# Ejecutar los metodos de la instancia de la clase
restaurante.agregar_restaurante('Pizzeria Napoli XD')
restaurante.mostrar_informacion()

restaurante2 = Restaurante()
restaurante2.agregar_restaurante('Bongorotondo XD')
restaurante2.mostrar_informacion()

# Mostrar la informacion de diferento forma de la clase
print(f'Nombre restaurantte: {restaurante.nombre}')
print(f'Nombre restaurantte: {restaurante2.nombre}')