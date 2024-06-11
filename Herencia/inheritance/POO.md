
# OOP Example Project

This project demonstrates basic concepts of Object-Oriented Programming (OOP) in Python, including inheritance, parent classes, and child classes. The project includes classes for `Persona`, `Estudiante`, and `Profesor`, showcasing how to structure and relate different classes.

## Files Overview

### persona.py
Defines the `Persona` class, which serves as a base (parent) class for other classes.

```python
class Persona:
    def __init__(self, nombre, edad):
        # Constructor method: Initializes the class attributes
        self.nombre = nombre  # Attribute 'nombre'
        self.edad = edad      # Attribute 'edad'

    def mostrar_informacion(self):
        # Method that returns a string with the person's information
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# This file defines the 'Persona' class with two attributes: 'nombre' and 'edad'.
# The class also has a method 'mostrar_informacion' that returns a string with the attribute values.
# Vocabulary:
# - Class: A blueprint for creating objects (instances of a class) that encapsulates data and behaviors.
# - Attribute: A variable within a class.
# - Method: A function within a class.
# - Constructor (__init__): A special method that is executed when a new instance of the class is created.
# - Parent Class (Superclass): A class that is inherited from. In this case, 'Persona' is the parent class.
```

### estudiante.py
Defines the `Estudiante` class, which inherits from the `Persona` class.

```python
class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        # Call to the constructor of the base class (Persona)
        super().__init__(nombre, edad)
        self.matricula = matricula  # Attribute specific to the Estudiante class

    def mostrar_informacion(self):
        # Method that returns a string with the student's information, including the matricula
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Matrícula: {self.matricula}"

# This file defines the 'Estudiante' class that inherits from 'Persona'.
# In addition to 'nombre' and 'edad', it adds the attribute 'matricula'.
# Vocabulary:
# - Inheritance: A mechanism where a class (child class) derives from another class (parent class), inheriting its attributes and methods.
# - super(): A function that allows calling methods of the base class within the child class.
# - Child Class (Subclass): A class that inherits from another class. In this case, 'Estudiante' is the child class.
```

### profesor.py
Defines the `Profesor` class, which also inherits from the `Persona` class.

```python
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        # Call to the constructor of the base class (Persona)
        super().__init__(nombre, edad)
        self.materia = materia  # Attribute specific to the Profesor class

    def mostrar_informacion(self):
        # Method that returns a string with the professor's information, including the subject they teach
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Materia: {self.materia}"

# This file defines the 'Profesor' class that inherits from 'Persona'.
# In addition to 'nombre' and 'edad', it adds the attribute 'materia'.
# Vocabulary:
# - Child Class (Subclass): A class that inherits from another class. In this case, 'Profesor' is the child class.
# - Method overriding: A method in a child class that has the same name as a method in the parent class but with a different implementation.
```

### main.py
Contains the main script that creates instances of `Estudiante` and `Profesor`, and displays their information.

```python
from estudiante import Estudiante
from profesor import Profesor

def main():
    # Creating an instance of the Estudiante class
    estudiante = Estudiante("Ana", 20, "A12345")
    # Creating an instance of the Profesor class
    profesor = Profesor("Dr. Smith", 45, "Matemáticas")

    # Print the student's information
    print(estudiante.mostrar_informacion())
    # Print the professor's information
    print(profesor.mostrar_informacion())

if __name__ == "__main__":
    main()

# This file is the main script that creates instances of 'Estudiante' and 'Profesor',
# and displays their information on the console.
# Vocabulary:
# - Instance: An object created from a class.
# - __name__: A special variable in Python that indicates the name of the current module.
# - "__main__": The value of __name__ when the module is executed as the main script.
# - if __name__ == "__main__": A construct that allows the code block to run only if the script is executed directly, not if it is imported as a module.
```

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

### Summary of Expected Outputs

1. **persona.py**: The `Persona` class initializes with a name and age, and the `mostrar_informacion` method returns these details in a formatted string.
   - Example Output: `"Nombre: Juan, Edad: 30"`

2. **estudiante.py**: The `Estudiante` class inherits from `Persona` and adds an attribute for matricula. The `mostrar_informacion` method includes the matricula in the returned string.
   - Example Output: `"Nombre: Ana, Edad: 20, Matrícula: A12345"`

3. **profesor.py**: The `Profesor` class inherits from `Persona` and adds an attribute for materia. The `mostrar_informacion` method includes the materia in the returned string.
   - Example Output: `"Nombre: Dr. Smith, Edad: 45, Materia: Matemáticas"`

4. **main.py**: This script creates instances of `Estudiante` and `Profesor`, then prints their information using the `mostrar_informacion` method of each class.
   - Expected Output:
     ```
     Nombre: Ana, Edad: 20, Matrícula: A12345
     Nombre: Dr. Smith, Edad: 45, Materia: Matemáticas
     ```

