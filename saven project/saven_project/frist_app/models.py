from django.db import models

class StudentModel(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    father_name= models.CharField(max_length=30)
    adresss = models.TextField()
    
    def __str__(self):
        return f"{self.roll}-{self.name}--{self.father_name}--{self.adresss}"