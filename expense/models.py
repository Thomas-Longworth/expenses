from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField
from datetime import datetime, date
# Create your models here.

class Expense(models.Model):
    name = models.CharField( max_length=50, null = False, blank = False)
    number = models.PositiveIntegerField(default=0,  validators=[MinValueValidator(1), MaxValueValidator(100000)])
    date_field = models.DateField(default=date.today)
    featured_image = CloudinaryField('image', default='placeholder')


    def __str__(self):
        return self.name
    


