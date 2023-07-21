
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Work_Shift(models.Model):
    BREAK_CHOICES = (
        ('Tea Break', 'Tea Break'),
        ('Lunch Break', 'Lunch Break'),
    )


    WEEKEND_DAYS = (
        ('Sunday', 'Sunday'),
        ('monday','Monday'),
        ('tuesday','Tuesday'),
        ('wednesday','Wednesday'),
        ('thursday','Thursday'),
        ('friday','Friday'),
        ('Saturday', 'Saturday'),

    )

    SHIFT_TYPES = (
        ("Regular", "Regular"),
        ("sheduled","sheduled")
    )

    Name = models.CharField(max_length=250,unique=True,null=True,blank=True)
    Start_date = models.DateTimeField()
    End_date = models.DateTimeField()
    shift_type = models.CharField(max_length=100,choices=SHIFT_TYPES, default=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    weekend_day = models.CharField(max_length=10, choices=WEEKEND_DAYS)
    Break_time = models.CharField(max_length=20, choices=BREAK_CHOICES)
    Description =  models.TextField(blank=True)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


    def __str__(self):
        return self.Name
    

class Designation(models.Model):
    name= models.CharField(max_length=250)
    discription=models.TextField(blank=True)
    No_of_Employee= models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
