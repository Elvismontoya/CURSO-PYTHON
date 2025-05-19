# Clase que representa una consulta veterinaria

class Consulta:
    def __init__(self, fecha, motivo, diagnostico, mascota):
        self.fecha = fecha
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.mascota = mascota

    def __str__(self):
        return f"[{self.fecha}] Motivo: {self.motivo}, Diagnóstico: {self.diagnostico}"