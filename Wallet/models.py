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

    Amount = models.DecimalField(max_digits=11, decimal_places=2)
    Source = models.CharField(choices=SOURCE_OPTIONS, max_length=100)
    Descriptions = models.TextField(blank=True)
    Date = models.DateField(auto_now_add=True, blank=True)
    Recurring = models.BooleanField(default=False)
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

    Amount = models.DecimalField(max_digits=11, decimal_places=2)
    Category = models.CharField(choices=CATEGORY_OPTIONS, max_length=100)
    Descriptions = models.TextField(blank=True)
    Date = models.DateField(auto_now_add=True, blank=True)
    Recurring = models.BooleanField(default=False)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)




class Plan(models.Model):
    Name = models.CharField(max_length=100)
    Amount = models.DecimalField(max_digits=11, decimal_places=2)
    Descriptions = models.TextField(blank=True)
    Start_date = models.DateField(auto_now_add=True, blank=True)
    Estemated_date = models.DateField()
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Calculate the time in months 


#class Consult(models.Model):
#    Consultant_name = models.CharField()
    # it should be a foreign key
#    Date = models.DateField()

    