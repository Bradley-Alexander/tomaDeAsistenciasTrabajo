from django.db import models
class Persona(models.Model):
    nombre = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre

    class Meta:
        abstract = True

class Estudiante(Persona):
    ciclo = models.PositiveIntegerField()
    paralelo = models.CharField(max_length=10)

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Profesor(Persona):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)


class Asistencia(models.Model):
    fechaAsistencia = models.DateField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name="asistencia_list")
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    asistio = models.BooleanField()

    def __str__(self):
        return f"{self.estudiante} - {self.fechaAsistencia}"
    def registrarAsistencia(self, fecha, profesor, estudiante, materia, asistio):
        self.fechaAsistencia = fecha
        self.profesor = profesor
        self.estudiante = estudiante
        self.materia = materia
        self.asistio = asistio
        self.save()
        return self