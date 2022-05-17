# Leer el contenido de un archivo

def app():
    with open('archivo.txt') as archivo:
        for c in archivo:
            print(c.rstrip()) # rstrip() -- Remover los saltos de linea

app()