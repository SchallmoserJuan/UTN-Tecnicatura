# Creacion de la clase pelicula
class pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Pelicula: {self._nombre}'
    
    # metodo get
    @property
    def nombre(self):
        return self._nombre

    # motodo set
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre # Para modificar el nombre