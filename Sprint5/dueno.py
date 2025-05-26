class Dueno:
    def __init__(self, nombre, telefono, direccion, rut):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.rut = rut

    def __str__(self):
        return f"{self.nombre}, Tel: {self.telefono}, Dir: {self.direccion}, RUT: {self.rut}"
