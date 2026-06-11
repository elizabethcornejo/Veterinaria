from conexion import conexion, cursor

class consulta:

    def __init__(self, motivo, anamnesis, tipo_consulta, mascota, dueno):
        self.motivo = motivo
        self.anamnesis = anamnesis
        self.tipo_consulta = tipo_consulta
        self.mascota = mascota
        self.dueno = dueno

    def mostrar_datos_consulta(self):
        print(f"{self.motivo}")
        print(f"{self.anamnesis}")
        print(f"{self.tipo_consulta}")
        print(f"{self.mascota}")

    def actualizar_anamnesis(self, nueva_anamnesis):
        self.anamnesis = nueva_anamnesis
        print("Información actualizada correctamente")

    def guardar(self):

        sql = """
        INSERT INTO consultas
        (motivo_consulta, anamnesis, id_tipo_consulta, id_mascota, id_dueno)
        VALUES (%s, %s, %s, %s, %s)
        """

        valores = (
            self.motivo,
            self.anamnesis,
            self.tipo_consulta,
            self.mascota,
            self.dueno
        )

        cursor.execute(sql, valores)
        conexion.commit()

        print("Consulta registrada")

    @staticmethod
    def listar():

        cursor.execute("""
            SELECT
                id_consulta,
                motivo_consulta,
                anamnesis,
                id_tipo_consulta,
                id_mascota
            FROM consultas
            WHERE deleted = 0
        """)

        consultas = cursor.fetchall()

        print("\n===== CONSULTAS =====\n")

        for consulta in consultas:
            print(
                f"ID: {consulta[0]} | "
                f"Motivo: {consulta[1]} | "
                f"Anamnesis: {consulta[2]} | "
                f"Tipo: {consulta[3]} | "
                f"Mascota: {consulta[4]}"
            )

    @staticmethod
    def buscar():

        id_consulta = int(input("ID consulta: "))

        cursor.execute("""
            SELECT
                id_consulta,
                motivo_consulta,
                anamnesis,
                id_tipo_consulta,
                id_mascota
            FROM consultas
            WHERE id_consulta = %s
            AND deleted = 0
        """, (id_consulta,))

        consultas = cursor.fetchall()

        if len(consultas) == 0:
            print("No se encontró la consulta.")

        else:
            for consulta in consultas:
                print(
                    f"ID: {consulta[0]} | "
                    f"Motivo: {consulta[1]} | "
                    f"Anamnesis: {consulta[2]} | "
                    f"Tipo: {consulta[3]} | "
                    f"Mascota: {consulta[4]}"
                )

    @staticmethod
    def eliminar():

        id_consulta = int(input("ID consulta: "))

        cursor.execute("""
            UPDATE consultas
            SET deleted = 1
            WHERE id_consulta = %s
        """, (id_consulta,))

        conexion.commit()

        print("Consulta eliminada")
