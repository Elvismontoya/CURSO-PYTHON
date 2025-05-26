import logging
from registro import registrar_mascota, registrar_consulta, listar_mascotas
from historial import ver_historial
from persistencia import guardar_mascotas_y_duenos_csv, cargar_mascotas_y_duenos_csv, guardar_consultas_json, cargar_consultas_json
from mascota import Mascota
from dueno import Dueno

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("clinica_veterinaria.log"),
        logging.StreamHandler()
    ]
)

# Cargar datos al iniciar
lista_mascotas, lista_duenos = cargar_mascotas_y_duenos_csv()
lista_consultas = cargar_consultas_json(lista_mascotas)

def importar_mascotas_por_defecto():
    if not lista_mascotas:
        print("No se encontraron mascotas. Importando mascotas por defecto...")
        dueno1 = Dueno("Carlos Pérez", "3001234567", "Cra 1 #10-20", "12345678")
        dueno2 = Dueno("Ana Gómez", "3017654321", "Calle 5 #22-30", "87654321")

        mascota1 = Mascota("Firulais", "Perro", "Labrador", 5, dueno1)
        mascota2 = Mascota("Misu", "Gato", "Persa", 3, dueno2)

        lista_duenos.extend([dueno1, dueno2])
        lista_mascotas.extend([mascota1, mascota2])

        print("Mascotas por defecto importadas:")
        for m in lista_mascotas:
            print(f"- {m.nombre} ({m.especie}) del dueño {m.dueno.nombre}")

def menu():
    while True:
        print("\n🐾 Clínica Veterinaria 'Amigos Peludos'")
        print("1. Registrar Mascota")
        print("2. Registrar Consulta")
        print("3. Listar Mascotas")
        print("4. Ver Historial de Consultas")
        print("5. Exportar Información")
        print("6. Importar Información")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_mascota(lista_mascotas, lista_duenos)
        elif opcion == "2":
            registrar_consulta(lista_consultas, lista_mascotas)
        elif opcion == "3":
            listar_mascotas(lista_mascotas)
        elif opcion == "4":
            ver_historial(lista_consultas, lista_mascotas)
        elif opcion == "5":
            guardar_mascotas_y_duenos_csv(lista_mascotas, lista_duenos)
            guardar_consultas_json(lista_consultas)
            print("Información exportada exitosamente.")
        elif opcion == "6":
            lista_mascotas[:], lista_duenos[:] = cargar_mascotas_y_duenos_csv()
            lista_consultas[:] = cargar_consultas_json(lista_mascotas)
            importar_mascotas_por_defecto()
        elif opcion == "7":
            guardar_mascotas_y_duenos_csv(lista_mascotas, lista_duenos)
            guardar_consultas_json(lista_consultas)
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
