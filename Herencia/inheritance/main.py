from estudiante import Estudiante
from profesor import Profesor
from persona import Persona

#estud1 = Estudiante('Gerardo','Mathus','Gomez Snadoval', '1994-01-24','gaymatrix')
#prof1 = Profesor('Isacc',     'Newton','PEREZ',          '1643-01-04','P1')
 
persona = Persona('Maria',' Gonza','Perez','1994-01-01')
#print(persona)

estud1 = Estudiante('Gerardo','Mathus','Gomez Snadoval', '1994-01-24','gaymatrix')
prof1 = Profesor('Isacc',     'Newton','PEREZ',          '1643-01-04','P1')

print(prof1.nombre_completo()) #herencia en accion explicame en el readme que hiciste


print(estud1.nombre_completo()) #herencia en accion explicame en el readme que hiciste


print(estud1) # como tiene __repr__ lo imprime como  estud1.nombre_completo() también



"""

hijos padres de clases que heredan 

lcase madre 
"""
