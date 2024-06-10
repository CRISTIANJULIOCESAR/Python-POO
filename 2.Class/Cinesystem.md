
# Cine System

Este proyecto es una simulación de un sistema de cine utilizando Programación Orientada a Objetos (POO). Aquí se explicarán los conceptos fundamentales de POO utilizados en este proyecto: clases, objetos, atributos, instancias y métodos, así como la integración de clases en un archivo principal (`main.py`).

## Conceptos de POO

### Clases
Una **clase** es un plano o plantilla para crear objetos. Define un conjunto de atributos y métodos que los objetos de esa clase compartirán. Por ejemplo, en este proyecto, tenemos las siguientes clases:

- `Asiento`: Representa un asiento en el cine.
- `Sala`: Representa una sala de cine que contiene asientos.
- `Pelicula`: Representa una película con sus características.
- `Funcion`: Representa una función de cine que incluye una película, una sala y un horario.
- `Cine`: Representa un cine con un nombre, dirección y funciones del día.

### Objetos
Un **objeto** es una instancia de una clase. Es una entidad que tiene estado y comportamiento. Por ejemplo, `asientoA1`, `sala1`, `pelicula1`, `funcion1` y `cine` son objetos creados a partir de sus respectivas clases.

### Atributos
Los **atributos** son variables que pertenecen a una clase y definen las propiedades de los objetos de esa clase. Por ejemplo:
- La clase `Asiento` tiene los atributos `fila`, `numero` y `ocupado`.
- La clase `Sala` tiene los atributos `nombre`, `tipo` y `asientos`.
- La clase `Pelicula` tiene los atributos `nombre`, `descripcion`, `genero` y `duracion`.
- La clase `Funcion` tiene los atributos `pelicula`, `sala`, `horario`, `started` y `finished`.
- La clase `Cine` tiene los atributos `cine`, `direccion` y `funciones`.

### Métodos
Los **métodos** son funciones definidas dentro de una clase que describen los comportamientos de los objetos de esa clase. Por ejemplo:
- La clase `Asiento` tiene el método `marcarOcupado()`.
- La clase `Pelicula` tiene el método `info()`.
- La clase `Funcion` tiene los métodos `info()`, `ocuparAsiento()`, `iniciarFuncion()` y `finalizarFuncion()`.
- La clase `Cine` tiene los métodos `info()`, `mostrarFunciones()` y `obtenerLugares()`.

### Instancias
Una **instancia** es un objeto particular de una clase. Crear una instancia de una clase se llama instanciar la clase. Por ejemplo:
```python
asientoA1 = Asiento("A", 1)
```
Esto crea una instancia de la clase `Asiento` con la fila "A" y el número 1.

## Código de las Clases

### Clase Asiento

```python
class Asiento:
    
    def __init__(self, fila, numero):
        self.fila = fila
        self.numero = numero
        self.ocupado = False
 
    def marcarOcupado(self):
        self.ocupado = True
```

### Clase Sala

```python
class Sala:
    
    def __init__(self, nombre, tipo, lista_asientos):
        self.nombre = nombre
        self.tipo = tipo
        self.asientos = lista_asientos
```

### Clase Pelicula

```python
class Pelicula:
    
    def __init__(self, nombre, descripcion, genero, duracion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.genero = genero
        self.duracion = duracion
        
    def info(self):
        print(f"Película: {self.nombre} \nDescripción: {self.descripcion} \nGénero:({self.genero}) \nDuración:{self.duracion}")
```

### Clase Funcion

```python
class Funcion:
    
    def __init__(self, pelicula, sala, horario):
        self.pelicula = pelicula
        self.sala = sala
        self.horario = horario
        self.started = False
        self.finished = False

        
    def info(self):
        print(f"Pelicula: {self.pelicula.nombre}, Sala: {self.sala.nombre}, Tipo: {self.sala.tipo}, Horario: {self.horario}")
    
    def ocuparAsiento(self, lugar):
        self.sala.asientos[lugar].ocupado = True
        
    def iniciarFuncion(self):
        self.started = True
        
    def finalizarFuncion(self):
        self.finished = True
```

### Clase Cine

```python
class Cine:
    
    def __init__(self, cine, direccion, funciones):
        self.cine = cine
        self.direccion = direccion
        self.funciones = funciones
        self.open = True

        
    def info(self):
        print(f"Cine: {self.cine} \nDirección: {self.direccion}")
        
    def mostrarFunciones(self):
        print("\nFunciones disponibles del día de hoy:\n")
        for funcion in self.funciones:
            if not funcion.finished:
                funcion.info()
           
               
    def obtenerLugares(self, funcion):
        self.funciones[funcion].pelicula.info()
        for asiento in self.funciones[funcion].sala.asientos:
            estado = "Ocupado" if asiento.ocupado else "Disponible"
            print(f"{asiento.numero}{asiento.fila} Estado: {estado}")
```

## Integración de Clases

Para utilizar las clases de manera independiente en archivos de código, podemos importarlas en el archivo principal (`main.py`). Aquí está el código completo con comentarios que explican la importación y uso de las clases:

```python
# Importando clases desde archivos separados
from AsientoClass import Asiento  # Importando la clase Asiento
from SalaClass import Sala  # Importando la clase Sala
from PeliculaClass import Pelicula  # Importando la clase Pelicula
from FuncionClass import Funcion  # Importando la clase Funcion
from CineClass import Cine  # Importando la clase Cine

# Creando instancias de la clase Asiento
asientoA1 = Asiento("A", 1)
asientoA2 = Asiento("A", 2)
asientoA3 = Asiento("A", 3)
asientoB1 = Asiento("B", 1)
asientoB2 = Asiento("B", 2)
asientoB3 = Asiento("B", 3)

# Creando una lista de asientos
lista_asientos = [asientoA1, asientoA2, asientoA3, asientoB1, asientoB2, asientoB3]

# Creando instancias de la clase Sala
sala1 = Sala("Sala A1", "Regular", lista_asientos)
sala2 = Sala("Sala A2", "VIP", lista_asientos)
sala3 = Sala("Sala A3", "3D", lista_asientos)

# Creando instancias de la clase Pelicula
pelicula1 = Pelicula("Inception", "Un ladrón habilidoso ingresa a los sueños de las personas para robar información valiosa.", "Ciencia ficción, Acción, Suspense", "2 horas 28 minutos")
pelicula2 = Pelicula("Jurassic Park", "Un parque temático de dinosaurios se convierte en un caos cuando los dinosaurios escapan y comienzan a causar estragos.", "Ciencia ficción, Acción, Aventura", "2 horas 7 minutos")

# Creando instancias de la clase Funcion
funcion1 = Funcion(pelicula1, sala1, "12:00PM")
funcion2 = Funcion(pelicula2, sala2, "12:00PM")
funcion3 = Funcion(pelicula1, sala3, "12:00PM")
funcion4 = Funcion(pelicula2, sala3, "02:00PM")

# Creando una lista de funciones
lista_funciones = [funcion1, funcion2, funcion3, funcion4]

# Creando instancia de la clase Cine
cine = Cine("Cinépolis Diana", "Paseo Reforma", lista_funciones)

# Uso de métodos de la clase Cine
cine.obtenerLugares(0)
cine.funciones[0].ocuparAsiento(0)
cine.funciones[0].ocuparAsiento(2)
cine.funciones[0].ocuparAsiento(4)
cine.obtenerLugares(0)
```

Este archivo `main.py` muestra cómo se integran las distintas clases y se utilizan sus métodos para simular el funcionamiento de un cine.
