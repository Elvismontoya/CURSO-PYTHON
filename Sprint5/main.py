# Menú principal de la aplicación veterinaria
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("clinica_veterinaria.log"),
        logging.StreamHandler()
    ]
)

logging.info("Aplicación iniciada")

from registro import registrar_mascota, registrar_consulta, listar_mascotas, ver_historial

# Listas globales para almacenar mascotas y consultas
lista_mascotas = []
lista_duenos = []
lista_consultas = []

def menu():
    while True:
        print("\n🐾 Clínica Veterinaria 'Amigos Peludos'")
        print("1. Registrar Mascota")
        print("2. Registrar Consulta")
        print("3. Listar Mascotas")
        print("4. Ver Historial de Consultas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_mascota(lista_mascotas, lista_duenos)
            logging.info("Usuario registro una mascota.")
        elif opcion == "2":
            registrar_consulta(lista_consultas, lista_mascotas)
            logging.info("Usuario registro una consulta.")
        elif opcion == "3":
            listar_mascotas(lista_mascotas)
            logging.info("Usuario listo las mascotas registradas.")
        elif opcion == "4":
            ver_historial(lista_consultas, lista_mascotas)
            logging.info("Usuario consulto el historial de consultas.")
        elif opcion == "5":
            print("¡Hasta luego!")
            logging.info("Usuario salio de la aplicación.")
            break
        else:
            print("Opción no válida.")
            logging.warning("Usuario ingresó una opción no válida.")

if __name__ == "__main__":
    menu()
    logging.info("Aplicación finalizada")

