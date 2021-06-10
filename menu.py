import os
from ClaseCapitulo import Capitulo
from ClaseLibro import Libro
from ManejaLibro import ManejadorLibro

class Menu:
      __op = 0
      def __init__(self,opcion=0):
        self.__op = opcion
      def Ejecutar(self,otroManejadorLibro):
          os.system('cls')
          salir = False

          while salir == False:
              print('1-\tIngresar el identificador de un libro y mostrar título del libro, nombre de cada uno de sus capítulos y cantidad total de páginas de un libro.')
              print('2-\tDada una palabra, mostrar título y autor de los libros que contienen la palabra dada en su título o en el título de alguno de sus capítulos. ')
              print('0-\tSalir')
              self.__op = int(input('Ingrese la opcion: '))
              if self.__op == 1:  
                 id=int(input('Ingrese el identificador de un libro: '))
                 otroManejadorLibro.mostrarTityCap(id)
                 print('\n')
              elif self.__op == 2: 
                 x=input("Ingresar una Palabra para que sea buscada en los titulos: ")
                 otroManejadorLibro.mostrarTitulos(x)
                 print('\n')
              elif self.__op == 0: #Salir
                  salir = True
              else:
                 print('Opcion ingresada incorrecta')
                 input('Presiona ENTER para continuar...')


          print('Cerrando Menú..')   