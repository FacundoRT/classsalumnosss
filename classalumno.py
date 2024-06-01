class Alumno:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, tutor):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.tutor = tutor
        self.notas = []
        self.faltas = 0
        self.amonestaciones = 0

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def asignar_falta(self):
        self.faltas += 1

    def asignar_amonestacion(self):
        self.amonestaciones += 1

    def cambiar_domicilio(self, nuevo_domicilio):
        self.domicilio = nuevo_domicilio

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("DNI:", self.dni)
        print("Fecha de nacimiento:", self.fecha_nacimiento)
        print("Tutor:", self.tutor)
        print("Notas:", self.notas)
        print("Faltas:", self.faltas)
        print("Amonestaciones:", self.amonestaciones)


# Ejemplo de uso
datos_escuela = {"Alumnos": []}

while True:
    comando = input("Ingrese el comando (agregar, mostrar, modificar, expulsar, salir): ").lower()

    if comando == "agregar":
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        dni = input("Ingrese el DNI del alumno: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (YYYY-MM-DD): ")
        tutor = input("Ingrese el nombre del tutor del alumno: ")
        nuevo_alumno = Alumno(nombre, apellido, dni, fecha_nacimiento, tutor)
        datos_escuela["Alumnos"].append(nuevo_alumno)
        print("Alumno agregado correctamente.")
    
    elif comando == "mostrar":
        dni = input("Ingrese el DNI del alumno a mostrar: ")
        for alumno in datos_escuela["Alumnos"]:
            if alumno.dni == dni:
                print("Datos del alumno:")
                alumno.mostrar_datos()
                break
        else:
            print("No se encontró ningún alumno con ese DNI.")

    elif comando == "modificar":
        dni = input("Ingrese el DNI del alumno a modificar: ")
        for alumno in datos_escuela["Alumnos"]:
            if alumno.dni == dni:
                print("Datos actuales del alumno:")
                alumno.mostrar_datos()
                nombre = input("Ingrese el nuevo nombre del alumno (deje en blanco para mantener el actual): ")
                apellido = input("Ingrese el nuevo apellido del alumno (deje en blanco para mantener el actual): ")
                nueva_fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento del alumno (YYYY-MM-DD) (deje en blanco para mantener la actual): ")
                tutor = input("Ingrese el nuevo tutor del alumno (deje en blanco para mantener el actual): ")
                if nombre:
                    alumno.nombre = nombre
                if apellido:
                    alumno.apellido = apellido
                if nueva_fecha_nacimiento:
                    alumno.fecha_nacimiento = nueva_fecha_nacimiento
                if tutor:
                    alumno.tutor = tutor
                print("Datos del alumno modificados correctamente.")
                break
        else:
            print("No se encontró ningún alumno con ese DNI.")

    elif comando == "expulsar":
        dni = input("Ingrese el DNI del alumno a expulsar: ")
        for i, alumno in enumerate(datos_escuela["Alumnos"]):
            if alumno.dni == dni:
                del datos_escuela["Alumnos"][i]
                print("Alumno expulsado correctamente.")
                break
        else:
            print("No se encontró ningún alumno con ese DNI.")

    elif comando == "salir":
        print("¡Hasta luego!")
        break

    else:
        print("Comando no válido.")

