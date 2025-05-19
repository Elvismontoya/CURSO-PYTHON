# Funciones para registrar mascotas y consultas

from clases.dueno import Dueno
from clases.mascota import Mascota
from clases.consulta import Consulta
from funciones.utilidades import buscar_mascota

# Listas globales de objetos
mascotas = []
duenos = []

def registrar_mascota():
    print("\n--- Registro de Mascota ---")
    nombre_mascota = input("Nombre: ")
    especie = input("Especie: ")
    raza = input("Raza: ")
    edad = input("Edad: ")

    nombre_dueno = input("Nombre del dueño: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")

    dueno = Dueno(nombre_dueno, telefono, direccion)
    mascota = Mascota(nombre_mascota, especie, raza, edad, dueno)

    duenos.append(dueno)
    mascotas.append(mascota)

    print(f"✅ Mascota '{nombre_mascota}' registrada.")

def registrar_consulta():
    print("\n--- Registro de Consulta ---")
    nombre = input("Nombre de la mascota: ")
    mascota = buscar_mascota(nombre, mascotas)

    if mascota:
        fecha = input("Fecha (DD/MM/AAAA): ")
        motivo = input("Motivo: ")
        diagnostico = input("Diagnóstico: ")

        consulta = Consulta(fecha, motivo, diagnostico, mascota)
        mascota.agregar_consulta(consulta)

        print("✅ Consulta registrada.")
    else:
        print("⚠️ Mascota no encontrada.")

def listar_mascotas():
    print("\n--- Lista de Mascotas ---")
    if not mascotas:
        print("No hay mascotas registradas.")
    else:
        for mascota in mascotas:
            print(f"{mascota} - Dueño: {mascota.dueno}")

def ver_historial():
    print("\n--- Historial de Consultas ---")
    nombre = input("Nombre de la mascota: ")
    mascota = buscar_mascota(nombre, mascotas)

    if mascota:
        print(mascota.mostrar_historial())
    else:
        print("⚠️ Mascota no encontrada.")