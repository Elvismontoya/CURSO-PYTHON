import logging
from dueno import Dueno
from mascota import Mascota
from consulta import Consulta
from utilidades import buscar_mascota

def registrar_mascota(lista_mascotas, lista_duenos):
    try:
        nombre = input("Nombre de la mascota: ")
        especie = input("Especie de la mascota: ")
        raza = input("Raza de la mascota: ")            # <-- nuevo input
        edad = int(input("Edad de la mascota: "))
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")

        rut = input("RUT del dueño: ")
        dueno = next((d for d in lista_duenos if d.rut == rut), None)
        if not dueno:
            print("Dueño no encontrado. Registrando nuevo dueño.")
            nombre_dueno = input("Nombre del dueño: ")
            telefono_dueno = input("Teléfono del dueño: ")
            direccion_dueno = input("Dirección del dueño: ")
            dueno = Dueno(nombre_dueno, telefono_dueno, direccion_dueno, rut)
            lista_duenos.append(dueno)

        mascota = Mascota(nombre, especie, raza, edad, dueno)   # <-- pasar raza aquí
        lista_mascotas.append(mascota)
        logging.info(f"Usuario registró una mascota: {nombre}, especie: {especie}, raza: {raza}")
        print("Mascota registrada exitosamente.")
    except ValueError as ve:
        logging.warning(f"Error de valor al registrar mascota: {ve}")
        print(f"Error: {ve}")
    except Exception as e:
        logging.error(f"Error inesperado al registrar mascota: {e}")
        print(f"Error inesperado: {e}")

def registrar_consulta(lista_consultas, lista_mascotas):
    try:
        nombre = input("Nombre de la mascota: ")
        mascota = next((m for m in lista_mascotas if m.nombre == nombre), None)
        if not mascota:
            raise Exception("Mascota no encontrada.")

        diagnostico = input("Diagnóstico de la consulta: ")
        consulta = Consulta(diagnostico, mascota)
        lista_consultas.append(consulta)
        mascota.agregar_consulta(consulta)  # si quieres también agregarla al historial de la mascota
        logging.info(f"Consulta registrada para: {mascota.nombre} - Diagnóstico: {diagnostico}")
        print("Consulta registrada exitosamente.")
    except Exception as e:
        print("Error:", e)
        logging.error(f"Error al registrar consulta: {e}")


def listar_mascotas(lista_mascotas):
    print("\n--- Lista de Mascotas ---")
    if not lista_mascotas:
        print("No hay mascotas registradas.")
    else:
        for mascota in lista_mascotas:
            print(f"{mascota} - Dueño: {mascota.dueno}")

def ver_historial(lista_consultas, lista_mascotas):
    print("\n--- Historial de Consultas ---")
    nombre = input("Nombre de la mascota: ")
    mascota = next((m for m in lista_mascotas if m.nombre == nombre), None)

    if mascota:
        historial = [c for c in lista_consultas if c.mascota == mascota]
        if historial:
            for c in historial:
                print(f"- {c}")
        else:
            print("No hay consultas registradas para esta mascota.")
    else:
        print("⚠️ Mascota no encontrada.")
