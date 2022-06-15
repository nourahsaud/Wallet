from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#class Source(models.Model):
#    Source = models.CharField(max_length=100)

class Income(models.Model):

    SOURCE_OPTIONS = [
        ('SALARY', 'SALARY'),
        ('BUSINESS', 'BUSINESS'),
        ('SAVING', 'SAVING'),
        ('BONUS', 'BONUS'),
        ('OTHERS', 'OTHERS')
    ]

    amount = models.DecimalField(max_digits=11, decimal_places=2)
    source = models.CharField(choices=SOURCE_OPTIONS, max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True)
    recurring = models.BooleanField(default=False)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)



#class Category(models.Model):
#    Category  = models.CharField(max_length=100)

class Expense(models.Model):

    CATEGORY_OPTIONS = [
        ('FOOD', 'FOOD'),
        ('COFFEE', 'COFFEE'),
        ('RENT', 'RENT'),
        ('BILLS', 'BILLS'),
        ('GROCERY', 'GROCERY'),
        ('OTHERS', 'OTHERS')
    ]

    amount = models.DecimalField(max_digits=11, decimal_places=2)
    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True)
    recurring = models.BooleanField(default=False)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)


class Plan(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.TextField(blank=True)
    start_date = models.DateField(auto_now_add=True, blank=True)
    estemated_date = models.DateField()
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Calculate the time in months 


class Consult(models.Model):
    consult = models.BooleanField()

    