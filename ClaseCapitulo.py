
class Capitulo:
    __tituloCapitulo=''
    __cantidadPaginas=0
  
  #  @classmethod    
 #   def getTituloCapitulo (cls):
  #      return cls.__tituloCapitulo
  #  @classmethod    

  #  def getCantidadPaginas(cls):
   #     return cls.__cantidadPaginas

    def __init__(self,tituloCapitulo,cantidadPaginas):
        self.__tituloCapitulo=tituloCapitulo
        self.__cantidadPaginas=cantidadPaginas
    def getTitulo(self):
        return self.__tituloCapitulo

    def getPag(self):
        return self.__cantidadPaginas
    def __str__(self):
         return f'Titulo: {self.__tituloCapitulo}y tiene un total de paginas de: {self.__cantidadPaginas}'

