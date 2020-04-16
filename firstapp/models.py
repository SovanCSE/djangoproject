from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    total_employees = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Language(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

# class SalaryHistory(models.Model):
#     salary = models.IntegerField()

class Programmer(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    language = models.ManyToManyField(Language, related_name='programmer_language_mapper')
    # salary = models.OneToOneField(SalaryHistory, on_delete=models.CASCADE())
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

