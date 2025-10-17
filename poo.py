class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."    
    

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        return f"{self.nombre} está estudiando {self.carrera}."
    

class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def enseñar(self):
        return f"{self.nombre} está enseñando {self.asignatura}."


# Ejemplo de uso
persona = Persona("Ana", 30)
print(persona.saludar())
estudiante = Estudiante("Luis", 20, "Ingeniería")
print(estudiante.saludar())
print(estudiante.estudiar())
profesor = Profesor("Carlos", 45, "Matemáticas")
print(profesor.saludar())
print(profesor.enseñar())
