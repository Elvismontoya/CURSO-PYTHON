class Mascota:
    def __init__(self, nombre, especie, raza, edad, dueno):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.dueno = dueno
        self.consultas = []

    def agregar_consulta(self, consulta):
        self.consultas.append(consulta)

    def __str__(self):
        return f"{self.nombre}, {self.especie}, {self.raza}, {self.edad} años - Dueño: {self.dueno.nombre}"
