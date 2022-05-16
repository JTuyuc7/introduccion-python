# Arreglos o listas en python
lenguajes = ['Python', 'Kotlin', 'Javascript', 'Java']

print(lenguajes, 'lenguajes de programacion en python')

#Forma de acceder a los arreglos en python
print(lenguajes[0], 'primera posicion en la list')

#Ordenar una lista alfabeticamente en python usando el metodo SORT
lenguajes.sort()
print(lenguajes, 'Ordenados alfabeticamente')

#Acceder a un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

# Modificar valores dentro de una lista en Python
lenguajes[1] = 'PHP'
print(lenguajes)

# Agregar un nuevo elemento a la lista
lenguajes.append('Ruby')
print(lenguajes)

# Eliminar un elemento de la lista
del lenguajes[0]
print(lenguajes)

# Eliminar el ultimo elemento usando POP
lenguajes.pop()
print(lenguajes)

# Elñiminar un elemento pasando un argumento a POP
lenguajes.pop(0)
print(lenguajes)

# Eliminar un elemento por nombre
lenguajes.remove('Kotlin')
print(lenguajes)