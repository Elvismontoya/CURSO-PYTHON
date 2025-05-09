import re
from Funciones import RegistrarCorreo, VerCorreos, BuscarCorreo

  
#funcion principal del menu
def Menu():
    while True:
        print("\n1.Registrar un correo")
        print("2.Ver correos")
        print("3.Buscar correo")
        print("4.Salir♿")
        opcion = input("---------------------\n🔺Seleccione una opcion🔻 ").strip()
        print("---------------------")
        if opcion == "1":
            RegistrarCorreo()
        elif opcion == "2":
            VerCorreos()
        elif opcion == "3":
            BuscarCorreo()
        elif opcion == "4":
            print("♿Saliendo de la aplicacion♿")
            break
        else:
            print("❌ Opcion no valida.")
            
#iniciar el menu
Menu()
