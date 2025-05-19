# Clase que representa a un dueño de mascota

class Dueno:
    def __init__(self, nombre, telefono, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"{self.nombre}, Tel: {self.telefono}, Dir: {self.direccion}"