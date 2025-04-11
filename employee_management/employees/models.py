from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name