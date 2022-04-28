from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    picture=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name