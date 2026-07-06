from conexion import conexion, cursor

class persona:

    def __init__(self, nombre, email, telefono, rut, comuna, calle, numero_residencia):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono    
        self.rut = rut
        self.comuna = comuna
        self.calle = calle
        self.numero_residencia = numero_residencia

    def mostrar_datos_personas(self):
        print(f"{self.nombre}")
        print(f"{self.email}")
        print(f"{self.telefono}")
        print(f"{self.rut}")
        print(f"{self.comuna}")
        print(f"{self.calle}")
        print(f"{self.numero_residencia}")

    def actualizar_informacion_persona(self, nuevo_email, nuevo_telefono,
    nueva_comuna, nueva_calle, nuevo_numero_residencia ):
        
        self.email = nuevo_email
        self.telefono = nuevo_telefono
        self.comuna = nueva_comuna
        self.calle = nueva_calle
        self.numero_residencia = nuevo_numero_residencia

        print("Información actualizada correctamente")

    def guardar(self):

        sql = """
        INSERT INTO duenos
        (nombre_dueno, email, telefono, rut)
        VALUES (%s, %s, %s, %s)
        """

        valores = (
            self.nombre,
            self.email,
            self.telefono,
            self.rut
        )

        cursor.execute(sql, valores)
        conexion.commit()

        print("Dueño registrado")
        return cursor.lastrowid

    @staticmethod
    def listar():

        cursor.execute("""
            SELECT
                id_dueno,
                nombre_dueno,
                email,
                telefono,
                rut
            FROM duenos
            WHERE deleted = 0
        """)

        duenos = cursor.fetchall()

        print("\n===== DUEÑOS =====\n")

        for dueno in duenos:
            print(
                f"ID: {dueno[0]} | "
                f"Nombre: {dueno[1]} | "
                f"Email: {dueno[2]} | "
                f"Teléfono: {dueno[3]} | "
                f"RUT: {dueno[4]}"
            )

    @staticmethod
    def buscar():

        nombre = input("Nombre dueño: ")

        cursor.execute("""
            SELECT
                id_dueno,
                nombre_dueno,
                email,
                telefono,
                rut
            FROM duenos
            WHERE nombre_dueno LIKE %s
            AND deleted = 0
        """, ('%' + nombre + '%',))

        duenos = cursor.fetchall()

        if len(duenos) == 0:
            print("No se encontraron dueños.")

        else:
            for dueno in duenos:
                print(
                    f"ID: {dueno[0]} | "
                    f"Nombre: {dueno[1]} | "
                    f"Email: {dueno[2]} | "
                    f"Teléfono: {dueno[3]} | "
                    f"RUT: {dueno[4]}"
                )

    @staticmethod
    def eliminar():

        id_dueno = int(input("ID dueño: "))

        cursor.execute("""
            UPDATE duenos
            SET deleted = 1
            WHERE id_dueno = %s
        """, (id_dueno,))

        conexion.commit()

        print("Dueño eliminado")