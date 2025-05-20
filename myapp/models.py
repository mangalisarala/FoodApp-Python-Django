from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.name} - {self.age}"
class FoodMenu(models.Model):
    item_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100) 
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    image = models.URLField(max_length=100)  

    def __str__(self):
        return f"{self.id} - {self.item_name} - {self.price}"

