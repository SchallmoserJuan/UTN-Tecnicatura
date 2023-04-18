import os
class CatalogoPeliculas:

    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregar_peliculas(cls, pelicula): # cls -> contexto de clase
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    
    # Metodo para listar las peliculas
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print(f'Catalogo de peliculas'.center(50, '-'))
            print(archivo.read())

    
    # Metodo para eliminar peliculas
    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')