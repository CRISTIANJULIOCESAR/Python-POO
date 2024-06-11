class Persona: # clase padre
    def __init__(self, nombre, apellido_pat, apellido_mat,fecha_nacimiento):
        self.nombre = nombre
        self.apellido_paterno= apellido_pat
        self.apellido_materno = apellido_mat
        self.fecha_nacimiento = fecha_nacimiento

    def nombre_completo(self):
        return self.apellido_paterno + ' ' + self.apellido_materno + ', ' + self.nombre
    
    def __repr__(self):
        return self.nombre_completo()



#