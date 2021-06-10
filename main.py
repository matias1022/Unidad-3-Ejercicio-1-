


from ClaseLibro import Libro
from ManejaLibro import ManejadorLibro
from menu import Menu
def test():
    unoslibros=ManejadorLibro()
    libro=Libro(10001, "Python 3 Object oriented Programming", "Dusty Phillips", "Packt Publishing", 1849511268, 5)
    unoslibros.agregarLibro(libro)
    libro.agregarCapitulo("Objects in Python", 31)
    print(unoslibros)


if __name__ == '__main__':
   test()
   input()
   libros=ManejadorLibro()
   libros.cargarDatos()
   unLibro=Libro
   print (libros)
   menu = Menu()
   menu.Ejecutar(libros)