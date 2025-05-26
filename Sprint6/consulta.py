class Consulta:
    def __init__(self, diagnostico, mascota):
        self.diagnostico = diagnostico
        self.mascota = mascota

    def __str__(self):
        return f"Diagnóstico: {self.diagnostico}"

