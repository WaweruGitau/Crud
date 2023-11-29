from django.db import models

class Student(models.Model):
    name = models.CharField(max_length= 30, blank= False,null= False)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, blank= False, null= False)

# Function to create a database
def __str__(self):
    return self.name
