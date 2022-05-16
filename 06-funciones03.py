def informacion(nombre, puesto = 'sin asignar puesto'):
    print(f'Soy {nombre} y soy {puesto}')
informacion('James', 'fullstack dev')
informacion('Frida', 'Diseñadora')
informacion('Cristian', 'React native front')

#funcones que retornan un valor
def mifuncion(nombre = 'Sin asignar nombre'):
    return nombre
empleado = mifuncion('James')

print(empleado)