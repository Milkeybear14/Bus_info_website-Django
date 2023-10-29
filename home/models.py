from django.db import models

# Create your models here.

class busCatagory(models.Model):
    pass
    Name = models.CharField(max_length=255)
    Image = models.ImageField(upload_to='bus_images')    
    Description = models.TextField()

    def __str__(self):
        return self.Name

class Bus(models.Model):

    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Catagory = models.ForeignKey(busCatagory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Name} ==== {self.Catagory}'
