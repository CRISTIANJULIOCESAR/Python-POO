
# Project: Classes and Object-Oriented Programming in Python

This project is an introduction to Object-Oriented Programming (OOP) in Python by implementing a simple class called `Person`. OOP is a programming paradigm that uses "objects" and their interactions to design and program applications or systems.

## Project Description

The goal of this project is to demonstrate how to define a class, create instances of that class, and interact with its methods and attributes. In this case, we have created a `Person` class with some basic attributes and methods.

## Contents

The project contains the following file:

- `person.py`: Contains the definition of the `Person` class and examples of how to create and use instances of this class.

## `person.py` Overview

### Class Definition

```python
class Person:
    def __init__(self, name, age, city):
        # Constructor: called automatically when a new instance of the Person class is created
        # The 'self' parameter refers to the current instance of the class
        self.name = name  # Instance attribute: stores the person's name
        self.age = age    # Instance attribute: stores the person's age
        self.city = city  # Instance attribute: stores the person's city

    def sleep(self):
        # sleep method: prints a message indicating that the person is sleeping
        print(self.name + ' is sleeping')

    def walk(self, distance):
        # walk method: prints a message indicating how many kilometers the person has walked
        print(self.name + ' has walked ' + str(distance) + ' KM')
```

### Creating Instances

Here is an example of how to create instances of the `Person` class:

```python
# Example of how to create an instance of the Person class
person1 = Person("John", 24, "New York")
person2 = Person("Abigail", 34, "Los Angeles")

# Calling methods on the instances
person1.sleep()
person2.sleep()
```

### Running the Code

To run the code, simply execute the `person.py` file:

```sh
python person.py
```

This will create two instances of the `Person` class and call the `sleep` method on each of them, producing the following output:

```
John is sleeping
Abigail is sleeping
```

## Conclusion

This project serves as a basic introduction to OOP in Python, showing how to define a class, create objects, and use their methods. By understanding these fundamentals, you can start building more complex and modular programs using OOP principles.

Feel free to explore and modify the code to learn more about OOP in Python!

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
