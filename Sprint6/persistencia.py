import csv
import json
from dueno import Dueno
from mascota import Mascota
from consulta import Consulta

def guardar_mascotas_y_duenos_csv(mascotas, duenos):
    with open("mascotas.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for m in mascotas:
            writer.writerow([m.nombre, m.especie, m.raza, m.edad, m.dueno.nombre, m.dueno.telefono, m.dueno.direccion, m.dueno.rut])

def cargar_mascotas_y_duenos_csv():
    mascotas = []
    duenos = []
    try:
        with open("mascotas.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                nombre, especie, raza, edad, nombre_dueno, tel, dir, rut = row
                edad = int(edad)
                dueno = next((d for d in duenos if d.rut == rut), None)
                if not dueno:
                    dueno = Dueno(nombre_dueno, tel, dir, rut)
                    duenos.append(dueno)
                mascota = Mascota(nombre, especie, raza, edad, dueno)
                mascotas.append(mascota)
    except FileNotFoundError:
        pass
    return mascotas, duenos

def guardar_consultas_json(consultas):
    data = []
    for c in consultas:
        data.append({"diagnostico": c.diagnostico, "mascota": c.mascota.nombre})
    with open("consultas.json", "w") as f:
        json.dump(data, f)

def cargar_consultas_json(lista_mascotas):
    consultas = []
    try:
        with open("consultas.json", "r") as f:
            data = json.load(f)
            for c in data:
                mascota = next((m for m in lista_mascotas if m.nombre == c["mascota"]), None)
                if mascota:
                    consultas.append(Consulta(c["diagnostico"], mascota))
    except FileNotFoundError:
        pass
    return consultas


