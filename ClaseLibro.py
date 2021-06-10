from ClaseCapitulo import Capitulo


class Libro:
    __idLibro=0
    __titulo=''
    __autor=''
    __editorial=''
    __isbn=0
    __cantidadCapitulos=0
    __capitulo=[]
    def __init__(self,idLibro='',titulo='',autor='',editorial='',isbn='',cantidadCapitulos=0 ):
         self.__idLibro=idLibro
         self.__titulo=titulo
         self.__autor=autor
         self.__editorial=editorial
         self.__isbn=isbn
         self.__cantidadCapitulos=cantidadCapitulos
         self.__capitulo=[]

    def agregarCapitulo(self,titCap,catCap):
         unCapitulo=Capitulo(titCap,catCap)
         self.__capitulo.append(unCapitulo)
    def getLista(self):
      return self.__capitulo
    def getID(self):
      return self.__idLibro
    def getTitulo(self):
      return self.__titulo
    def mostrarNombreCapitulos(self):
        k=1
        for Capitulo in self.__capitulo:
            print (f"El capitulo {k} se llama:",)
            print(f'Titulo: {Capitulo.getTitulo()}')
            k=k+1

    def getTotalPaginas(self):
        acumulador = 0
        for Capitulo in self.__capitulo:
            acumulador+=int(Capitulo.getPag())
        return acumulador   
    def getAutor(self):
      return self.__autor
    def retornaLista(self):
        return self.__capitulo
    def __str__(self):
        s=  f'ID Libro: {self.__idLibro},Titulo: {self.__titulo},Autor: {self.__autor},Editorial: {self.__editorial},Isbn: {self.__isbn},Cantidad Capitulos: {self.__cantidadCapitulos}'
        d = '\n Los capitulos son:\n'
        for Capitulo in self.__capitulo:
            d+= Capitulo.__str__()+'\n'
            
        s+=d    
        return s
            