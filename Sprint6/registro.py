import logging
from dueno import Dueno
from mascota import Mascota
from consulta import Consulta

def registrar_mascota(lista_mascotas, lista_duenos):
    try:
        nombre = input("Nombre de la mascota: ")
        especie = input("Especie de la mascota: ")
        raza = input("Raza de la mascota: ")
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

        mascota = Mascota(nombre, especie, raza, edad, dueno)
        lista_mascotas.append(mascota)
        logging.info(f"Se registró una mascota: {nombre}")
        print("Mascota registrada exitosamente.")
    except ValueError as ve:
        logging.warning(f"Error: {ve}")
        print(f"Error: {ve}")
    except Exception as e:
        logging.error(f"Error inesperado: {e}")
        print(f"Error inesperado: {e}")

def registrar_consulta(lista_consultas, lista_mascotas):
    try:
        nombre = input("Nombre de la mascota: ")
        mascota = next((m for m in lista_mascotas if m.nombre.lower() == nombre.lower()), None)
        if not mascota:
            raise Exception("Mascota no encontrada.")

        diagnostico = input("Diagnóstico: ")
        consulta = Consulta(diagnostico, mascota)
        lista_consultas.append(consulta)
        mascota.agregar_consulta(consulta)
        print("Consulta registrada exitosamente.")
    except Exception as e:
        print("Error:", e)

def listar_mascotas(mascotas):
    print("\n🐶 Lista de Mascotas Registradas")
    if not mascotas:
        print("No hay mascotas registradas.")
        return
    for mascota in mascotas:
        print(mascota)
