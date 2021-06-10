from ClaseCapitulo import Capitulo
from ClaseLibro import Libro
import csv

class ManejadorLibro:
    __lista=[]
    def __init__(self):
        self.__lista = []

    def agregarLibro(self,unLibro):
        if isinstance(unLibro,Libro):
            self.__lista.append(unLibro)

    def agregarCapitulo(self,titCap,catCap):
         unCapitulo=Capitulo(titCap,catCap)
         self.__lista.append(unCapitulo)
 
    def cargarDatos(self):
         archivo= open ("libros.csv")
         reader= csv.reader(archivo,delimiter=',')
         for fila in reader:
            if fila[0].isdigit():
                 idLibro= int(fila[0])
                 titulo=fila[1]
                 autor=fila[2]
                 editorial=fila[3]
                 isbn=int(fila[4])
                 cantidadCapitulos=int(fila[5])
                 libro=Libro(idLibro,titulo,autor,editorial,isbn,cantidadCapitulos)
                 self.agregarLibro(libro)
                 for fila1 in reader:
                         libro.agregarCapitulo(fila1[0],fila1[1])
                         cantidadCapitulos-=1
                         if cantidadCapitulos==0:
                             break
                  

         archivo.close()
    def mostrarTityCap(self,id):
        band=True
        i=0
        assert isinstance(id,int)
        while  band and i<len(self.__lista):
            if self.__lista[i].getID() == id:
                 print (self.__lista[i].getID())
                 titulo = self.__lista[i].getTitulo()
                 band = False
                 print(f'Titulo: {titulo}')                 
                 self.__lista[i].mostrarNombreCapitulos() 
                 print ("El total de Paginas que tiene el libro es de:")
                 print( f"{self.__lista[i].getTotalPaginas()}")  
            else:
                i=i+1
        if band == True:
                print('ID No encontrada') 
    
    def mostrarTitulos(self, palabra):
            assert isinstance(palabra,str)
            band = False
            for Libro in self.__lista:
                if Libro.getTitulo().find(palabra) != -1:
                    titulo=Libro.getTitulo()
                    autor=Libro.getAutor()
                    print(f'Titulo: {titulo}')
                    print(f'Autor: {autor}')    
                    band = True
            for Capitulo in Libro.retornaLista():
                if Capitulo.getTitulo().find(palabra) != -1:
                    print(f'Titulo: {Capitulo.getTitulo()}' )
                    band = True
            if band == False:
                       print('La palabra buscada no fue encontrada en ningun Titulo')             

    def __str__(self):
        s=''
        unLibro=Libro()      
        for unLibro in self.__lista:
               s+=unLibro.__str__() + '\n' 
        return s