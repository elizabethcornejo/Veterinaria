from persona import persona
from mascota import mascota
from consulta import consulta

while True:

    print("\n===================================")
    print("      SISTEMA VETERINARIA")
    print("===================================")

    print("1. Mostrar consultas")
    print("2. Mostrar mascotas")
    print("3. Mostrar dueños")
    print("4. REGISTRAR ATENCIÓN COMPLETA")
    print("5. Buscar mascota")
    print("6. Eliminar mascota")
    print("7. Buscar consulta")
    print("8. Eliminar consulta")
    print("9. Buscar dueño")
    print("10. Eliminar dueño")
    print("11. Salir")

    opcion = input("\nSeleccione una opción: ")

    # MOSTRAR LISTAS
    if opcion == "1":
        consulta.listar()

    elif opcion == "2":
        mascota.listar()

    elif opcion == "3":
        persona.listar()

    # REGISTRO COMPLETO
    elif opcion == "4":

        print("\n--- PASO 1: DATOS DEL DUEÑO ---")
        nombre = input("Nombre dueño: ")
        email = input("Email: ")
        telefono = input("Telefono: ")
        rut = input("Rut: ")
        comuna = input("Comuna: ")
        calle = input("Calle: ")
        numero = input("Numero residencia: ")

        nuevo_dueno = persona(
            nombre,
            email,
            telefono,
            rut,
            comuna,
            calle,
            numero
        )

        # Guarda el dueño y obtiene su ID automáticamente
        id_dueno = nuevo_dueno.guardar()

        print("\n--- PASO 2: DATOS DE LA MASCOTA ---")
        nombre_m = input("Nombre mascota: ")
        especie = int(input("ID especie: "))
        raza = int(input("ID raza: "))
        sexo = input("Sexo: ")
        fecha_nac = input("Fecha nacimiento (AAAA-MM-DD): ")
        peso = float(input("Peso: "))

        nueva_mascota = mascota(
            nombre_m,
            especie,
            raza,
            sexo,
            fecha_nac,
            peso,
            id_dueno
        )

        # Guarda la mascota y obtiene su ID automáticamente
        id_mascota = nueva_mascota.guardar()

        print("\n--- PASO 3: DATOS DE LA CONSULTA ---")
        motivo = input("Motivo consulta: ")
        anamnesis = input("Anamnesis: ")
        tipo_consulta = int(input("ID tipo consulta: "))

        nueva_consulta = consulta(
            motivo,
            anamnesis,
            tipo_consulta,
            id_mascota,
            id_dueno
        )

        nueva_consulta.guardar()

        print("\n=== ¡Proceso terminado exitosamente! ===")

    # BÚSQUEDAS Y ELIMINACIONES
    elif opcion == "5":
        mascota.buscar()

    elif opcion == "6":
        mascota.eliminar()

    elif opcion == "7":
        consulta.buscar()

    elif opcion == "8":
        consulta.eliminar()

    elif opcion == "9":
        persona.buscar()

    elif opcion == "10":
        persona.eliminar()

    # SALIR
    elif opcion == "11":
        print("\nPrograma finalizado.")
        break

    else:
        print("\nOpción inválida.")