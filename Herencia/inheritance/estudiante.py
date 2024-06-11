from persona import Persona
class Estudiante(Persona):
    def __init__(self, nombre, apellido_pat, apellido_mat,fecha_nacimiento, matricula):
        super().__init__(nombre, apellido_pat, apellido_mat,fecha_nacimiento)
        self.matricula= matricula

    def __repr__(self):
        return "[{}] {}".format(self.matricula, self.nombre_completo())




