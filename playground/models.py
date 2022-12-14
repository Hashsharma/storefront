# import the standard Django Model
# from built-in library
from django.db import models
  
# declare a new model with a name "GeeksModel"
class Employee(models.Model):  
    e_id  = models.CharField(max_length=20)  
    e_name  = models.CharField(max_length=100)  
    email  = models.EmailField()  
    e_contact  = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"  