from django.db import models
from users.models import User

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duración en horas")
    created_at = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
 
    def __str__(self):
        return self.title

 

class Inscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.PositiveIntegerField(
        default=0, help_text="Progreso en porcentaje"
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
 
    def __str__(self):
        return f"{self.user.username} inscrito en {self.course.title}"



