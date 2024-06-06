
# Person Class Documentation

This is an example to demonstrate the concept of Object-Oriented Programming (OOP) in Python. The `Person` class represents a person with basic attributes and methods to interactively check their occupation.

## Class Definition

```python
class Person:
    def __init__(self, name):
        # Constructor method to initialize the name and occupation attributes
        self.name = name
        self.occupation = None

    def occupation_check(self):
        while True:
            # Ask the user for their occupation
            print('What is your occupation?')
            occupation_input = input()
            self.occupation = occupation_input
            
            # Ask if the occupation is acceptable
            print('Is it okay for you this? ' + occupation_input + ' YES or NOT?')
            response = input()
            
            # Check the user's response
            if response == 'NOT':
                print('Bye, pumpkin')
                break  # Exit the loop if the response is "NOT"
            elif response == 'YES':
                print('Ok, you can stay')
                break  # Exit the loop if the response is "YES"
            else:
                # If the response is neither "YES" nor "NOT"
                print('I just said YES or NOT')
```

## Example Usage

Here is an example of how to create an instance of the `Person` class and use its methods:

```python
# Example of how to use the class and method
person = Person("John")
person.occupation_check()
```

### Explanation

1. **Class Definition**:
    ```python
    class Person:
        def __init__(self, name):
            self.name = name
            self.occupation = None
    ```
    - The `Person` class is defined with an `__init__` method that initializes the `name` and `occupation` attributes. `__init__` is the constructor method that runs when a new instance of the class is created.

2. **Method `occupation_check`**:
    ```python
    def occupation_check(self):
        while True:
            print('What is your occupation?')
            occupation_input = input()
            self.occupation = occupation_input
            
            print('Is it okay for you this? ' + occupation_input + ' YES or NOT?')
            response = input()
            
            if response == 'NOT':
                print('Bye, pumpkin')
                break
            elif response == 'YES':
                print('Ok, you can stay')
                break
            else:
                print('I just said YES or NOT')
    ```
    - This method repeatedly asks the user for their occupation and checks if the entered occupation is acceptable by asking for a "YES" or "NOT" response.
    - The `while True` loop keeps running indefinitely until a valid response ("YES" or "NOT") is given.
    - If the response is "NOT", the method prints "Bye, pumpkin" and exits the loop using `break`.
    - If the response is "YES", the method prints "Ok, you can stay" and exits the loop using `break`.
    - If the response is neither "YES" nor "NOT", it prints a reminder to enter "YES" or "NOT", and the loop continues.

3. **Example Usage**:
    ```python
    person = Person("John")
    person.occupation_check()
    ```
    - An instance of the `Person` class is created with the name "John".
    - The `occupation_check` method is called on the `person` object, which starts the process of asking for the occupation and validating the response.

This code provides a basic example of how to use loops and conditionals within a class method to interact with the user until a specific condition is met.
