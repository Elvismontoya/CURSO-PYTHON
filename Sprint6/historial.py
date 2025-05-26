def ver_historial(lista_consultas, lista_mascotas):
    print("\n--- Historial de Consultas ---")
    nombre = input("Nombre de la mascota: ")
    mascota = next((m for m in lista_mascotas if m.nombre.lower() == nombre.lower()), None)

    if mascota:
        historial = [c for c in lista_consultas if c.mascota == mascota]
        if historial:
            for c in historial:
                print(f"- {c}")
        else:
            print("No hay consultas registradas para esta mascota.")
    else:
        print("⚠️ Mascota no encontrada.")

