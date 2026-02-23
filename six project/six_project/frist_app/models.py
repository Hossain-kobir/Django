from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)
    adress = models.TextField()
    father_name = models.TextField(default="f_name")
    
    def __str__(self):
        return f"ID:{self.id}--{self.name}"