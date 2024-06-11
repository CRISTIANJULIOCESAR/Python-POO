
# OOP Example Project

This project demonstrates basic concepts of Object-Oriented Programming (OOP) in Python, including inheritance, parent classes, and child classes. The project includes classes for `Persona`, `Estudiante`, and `Profesor`, showcasing how to structure and relate different classes.

## Files Overview

### persona.py
Defines the `Persona` class, which serves as a base (parent) class for other classes.

### estudiante.py
Defines the `Estudiante` class, which inherits from the `Persona` class.

### profesor.py
Defines the `Profesor` class, which also inherits from the `Persona` class.

### main.py
Contains the main script that creates instances of `Estudiante` and `Profesor`, and displays their information.

## Key Concepts

### Classes and Objects
- **Class**: A blueprint for creating objects (a particular data structure), containing methods (functions) and attributes (variables).
- **Object**: An instance of a class.

### Inheritance
Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).

- **Parent Class**: The class being inherited from (e.g., `Persona`).
- **Child Class**: The class that inherits from the parent class (e.g., `Estudiante` and `Profesor`).

### Super Function
The `super()` function allows a child class to call methods from the parent class. It's often used to initialize the parent class's attributes.

### Example

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Matrícula: {self.matricula}"

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Materia: {self.materia}"
```

### Main Script

The `main.py` script creates instances of `Estudiante` and `Profesor` and displays their information using the `mostrar_informacion` method.

```python
from estudiante import Estudiante
from profesor import Profesor

def main():
    estudiante = Estudiante("Ana", 20, "A12345")
    profesor = Profesor("Dr. Smith", 45, "Matemáticas")

    print(estudiante.mostrar_informacion())
    print(profesor.mostrar_informacion())

if __name__ == "__main__":
    main()
```

### The `if __name__ == "__main__":` Construct

In Python, the `if __name__ == "__main__":` construct is used to determine whether the script is being run directly or being imported as a module in another script. When the script is run directly, the code block under this condition will execute. If the script is imported as a module in another script, the code block will not execute.

- `__name__`: A special built-in variable in Python that represents the name of the current module.
- `"__main__"`: The value of `__name__` when the script is run directly.

This construct is useful for organizing code and ensuring that certain blocks of code only run when intended.

```python
if __name__ == "__main__":
    main()
```

In this project, the construct ensures that the `main()` function is called only when `main.py` is executed directly, not when it is imported as a module in another script.

## Running the Project

To run the project, execute the `main.py` script:

```bash
python main.py
```

This will create an instance of `Estudiante` and `Profesor` and print their information to the console.
