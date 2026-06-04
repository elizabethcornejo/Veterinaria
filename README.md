# Veterinaria
## Realizado por:
# 1 Camilo Diaz
# 2 Elizabeth cornejo
# 3 Martin Acevedo
# 4 Randy Cortinez 
# 🐾 Sistema de Gestión Veterinaria

¡Bienvenido al **Sistema de Gestión Veterinaria**! Este es un sistema de consola desarrollado en **Python** y conectado a una base de datos **MySQL**. El proyecto está estructurado bajo el paradigma de **Programación Orientada a Objetos (POO)** y sigue una arquitectura modular limpia, ideal como proyecto de estudio o gestión inicial.

---

## 📌 Características Principales

* **Registro Completo en un Flujo:** Permite registrar de manera secuencial y ordenada un Dueño, su Mascota y la Consulta médica correspondiente en una sola operación (Opción 4 del menú).
* **Arquitectura Modular:** El código está inteligentemente dividido por responsabilidades (Conexión, Entidades y Flujo Principal), facilitando su lectura y escalabilidad.
* **Seguridad contra Inyección SQL:** Implementación de marcadores de posición (`%s`) en todas las consultas para proteger la integridad de los datos frente a manipulaciones maliciosas.
* **Borrado Lógico:** Los registros no se eliminan permanentemente de la base de datos; en su lugar, se utiliza una bandera (`deleted = 1`) para conservar el historial clínico y la integridad referencial.
* **Persistencia de Datos:** Conexión robusta a MySQL mediante el conector oficial de Python, garantizando que la información se guarde mediante transacciones seguras (`commit`).

---

## 📂 Estructura del Proyecto

El sistema está compuesto por los siguientes archivos clave:

* `main.py`: **El cerebro del programa.** Contiene el menú interactivo de consola, captura los datos del usuario mediante inputs y coordina las llamadas a los métodos de cada clase.
* `conexion.py`: **El puente de datos.** Configura y establece la conexión con el servidor MySQL local y expone el `cursor` para ejecutar sentencias SQL.
* `persona.py`: **Módulo de Clientes.** Define la clase `persona` (Dueños) junto con sus operaciones de inserción, búsqueda por nombre, listado y borrado lógico.
* `mascota.py`: **Módulo de Pacientes.** Define la clase `mascota` asociada a un dueño, administrando campos críticos como peso, sexo, fecha de nacimiento, especie y raza.
* `consulta.py`: **Módulo de Fichas Clínicas.** Define la clase `consulta` para registrar los motivos de atención, anamnesis y tipos de consulta vinculados a una mascota.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Base de Datos:** MySQL
* **Librería Principal:** `mysql-connector-python`

---




