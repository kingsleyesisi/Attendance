from django.db import models

class Attendance(models.Model):
    name = models.CharField(max_length=100, unique=True)
    Matric_No = models.CharField(max_length=100, unique=True)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return super().__str__()