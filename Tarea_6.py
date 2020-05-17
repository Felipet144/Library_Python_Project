import csv
from collections import Counter


# Menu
def menu():
    print(
        'Bienvenidos al menú de la biblioteca, \n 1. Solicitar un prestamo. \n 2. Consultar día con más solicitudes. \n 3. Consultar autor más solicitado. \n 4. Consultar libro más solicitado. \n 5. Consultar todos los libros prestados de un autor determinado')
    choice = input()
    if choice == '1':
        prestamo()
        menu()
    if choice == '2':
        dia_mas_prestamos()
        menu()
    if choice == '3':
        autor_mas_prestamos()
        menu()
    if choice == '4':
        libro_mas_prestamos()
        menu()
    if choice == '5':
        libros_autor()
        menu()


# Leer el archivo con los titulos
def lector_titulos():
    with open('libros.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        titulos = [row for row in csvreader]
        flat_titulos = [item for sublist in titulos for item in sublist]
        return flat_titulos


# Leer el archivo con los autores
def lector_autores():
    with open('autores.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        autores = [row for row in csvreader]
        flat_autores = [item for sublist in autores for item in sublist]
        return flat_autores


# Unir los archivos para crear lista de titulo, autor
def zipper():
    titulos = lector_titulos()
    autores = lector_autores()
    zipped = zip(titulos, autores)
    libros = list(zipped)
    return libros


# Solicitar un libro prestado (utilizado en el menu)
def prestamo():
    lista_libros = zipper()
    nombre = input('Ingrese el nombre del libro a solicitar: ')
    autor = input('Ingrese el nombre del autor del libro a solicitar: ')
    if (nombre, autor) in lista_libros:
        dia = input('Ingrese el día en que se está haciendo la solicitud: ')
        fecha = input('Ingrese la fecha en la que se está haciendo la solicitud con el formato año-día-mes: ')
        rows = [[nombre, autor, dia, fecha]]
        filename = 'prestamos.csv'
        with open(filename, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(rows)
        print(f'\nSe solicitó el libro {nombre} por {autor}\nVolviendo al menu principal...\n')
    else:
        print(
            f'\nNo se encontró el libro {nombre} por {autor}.\nPor favor, verifique la lista de libros y los datos digitados.\nVolviendo al menu principal...\n')


# Todos los libros prestados de un autor (utilizado en el menu)
def libros_autor():
    with open('prestamos.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        prestamos = [row for row in csvreader]
        autor = input('Ingrese el nombre del autor a consultar: ')
        if any(elemento[1] == autor for elemento in prestamos):
            lista_de_autor = [item for item in prestamos if item[1] == autor]
            libros_de_autor = [item[0] for item in lista_de_autor]
            print(f'\nLos libros prestados del autor {autor} son: {libros_de_autor}\nVolviendo al menu principal...\n')
        else:
            print(f'\nNo existen prestamos de libros del autor: {autor}\nVolviendo al menu principal...\n')


# Día de la semana en que llegan más personas a pedir préstamos (utilizado en el menu)
def dia_mas_prestamos():
    with open('prestamos.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        prestamos = [row for row in csvreader]
        dias = [item[2] for item in prestamos]
        counter = Counter(dias)
        dias_comunes = counter.most_common(2)
        solo_dias = [elemento[0] for elemento in dias_comunes]
        print(
            f'\nEl día con más prestamos es: {solo_dias[0]}, seguido de {solo_dias[1]}.\nVolviendo al menu principal...\n')


# Autor más solicitado (utilizado en el menu)
def autor_mas_prestamos():
    with open('prestamos.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        prestamos = [row for row in csvreader]
        autores = [item[1] for item in prestamos]
        counter = Counter(autores)
        autores_comunes = counter.most_common(2)
        solo_autores = [elemento[0] for elemento in autores_comunes]
        print(
            f'\nEl autor con más prestamos es: {solo_autores[0]}, seguido de {solo_autores[1]}.\nVolviendo al menu principal...\n')


# Libro más solicitado (utilizado en el menu)
def libro_mas_prestamos():
    with open('prestamos.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        prestamos = [row for row in csvreader]
        titulos = [item[0] for item in prestamos]
        counter = Counter(titulos)
        titulos_comunes = counter.most_common(2)
        solo_titulos = [elemento[0] for elemento in titulos_comunes]
        print(
            f'\nEl libro con más prestamos es: {solo_titulos[0]}, seguido de {solo_titulos[1]}.\nVolviendo al menu principal...\n')
