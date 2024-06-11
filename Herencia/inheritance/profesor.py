from persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido_pat, apellido_mat, fech_nac,id_emp):
        super().__init__(nombre, apellido_pat, apellido_mat, fech_nac) 

        self.id_empleado = id_emp

