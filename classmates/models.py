from django.db import models
from django.urls import reverse
# Create your models here.

class Classmate(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    address = models.CharField(max_length=255) 
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)  
    age = models.IntegerField()

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('classmate_edit', kwargs={'pk': self.pk})
