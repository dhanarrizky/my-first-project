from django.db import models

# Create your models here.
class Members(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    
    def __str__(self): #untuk mengganti tampilan di halaman admin
        return f"{self.firstname} {self.lastname}"  #mengeluarkan isi dari data nama members dalam halaman admin