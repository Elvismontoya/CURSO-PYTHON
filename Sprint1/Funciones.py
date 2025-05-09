import re

#para almacenar los correos
correos = []

#coleccion para almacenar los nombres
def CorreoValido(Correo):
    #expresion regular simple para validar el formato
    Patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(Patron, Correo)

#Funcion para clasificar el correo según su dominio
def ClasificarCorreo(Correo):
    if Correo.endswith("@estudiante.utv.edu.co"):
        return "Estudiante"
    elif Correo.endswith("@utv.edu.co"):
        return "Docente"
    else:
        return None

#funcion para registrar un nuevo correo
def RegistrarCorreo():
    Correo = input("Ingrese un correo electronico: ").strip()
    if not CorreoValido(Correo):
        print("❌ extension no valida")
        return
    Tipo = ClasificarCorreo(Correo)
    if Tipo:
        correos.append({"Correo": Correo, "Tipo": Tipo})
        print(f"✅ Correo registrado como {Tipo}.")
        print("---------------------")
    else:
        print("❌ El dominio del correo no es valido para estudiantes o docentes")

#Funcion para ver los correos registrados
def VerCorreos():
    if not correos:
        print("❌no hay correos registrados")
        print("---------------------")
        return
    for i, c in enumerate(correos, 1):
        print(f"{i}. {c['Correo']} ({c['Tipo']})")

#Funcion para buscar correos
def BuscarCorreo():
    consulta = input("Ingrese parte del correo que desea buscar: ").strip()
    encontrados = [c for c in correos if consulta in c["Correo"]]
    if encontrados:
        for i, c in enumerate(encontrados, 1):
            print(f"{i}. {c['Correo']} ({c['Tipo']})")
            print("---------------------")
    else:
        print("❌No se encontraron coincidencias")