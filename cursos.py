# Diseña una clase Estudiante que tenga un nombre, apellido y
# una lista de cursos en los que está inscrito. Además, crea una clase Curso que tenga un nombre,
# una descripción y una lista de estudiantes inscritos. Ambas clases deben permitir agregar y
# eliminar elementos de sus listas respectivas (cursos para estudiantes, estudiantes para cursos).


class Estudiante:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.cursos_inscritos = []

    def inscribir_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            curso.agregar_estudiante(self)

    def retirar_curso(self, curso):
        if curso in self.cursos_inscritos:
            self.cursos_inscritos.remove(curso)
            curso.eliminar_estudiante(self)

class Curso:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estudiantes_inscritos = []

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes_inscritos:
            self.estudiantes_inscritos.append(estudiante)

    def eliminar_estudiante(self, estudiante):
        if estudiante in self.estudiantes_inscritos:
            self.estudiantes_inscritos.remove(estudiante)

estudiante1 = Estudiante("Cristiano", "Ronaldo")
estudiante2 = Estudiante("Cesar", "Cortes")

curso1 = Curso("Programación en Python", "Aprende a programar en Python desde cero")
curso2 = Curso("Introducción a la Matemática", "Fundamentos matemáticos para principiantes")

estudiante1.inscribir_curso(curso1)
estudiante1.inscribir_curso(curso2)
estudiante2.inscribir_curso(curso1)

estudiante1.retirar_curso(curso2)
estudiante2.retirar_curso(curso1)

print("Cursos y estudiantes inscritos:")
for curso in [curso1, curso2]:
    print(f"Curso: {curso.nombre}")
    print(f"Descripción: {curso.descripcion}")
    print("Estudiantes inscritos:")
    for estudiante in curso.estudiantes_inscritos:
        print(f"- {estudiante.nombre} {estudiante.apellido}")
 
