from django.db import models

# Create your models here.

class Manager(models.Model):
    name=models.CharField(max_length=150)
    def __str__(self):
        return self.name 
    
class AddDepartment(models.Model):
    PARENT_DEPARTMENT_CHOICES = (
        ('Main Department', 'Main Department'),
        ('Admin $ HR', 'Admin $ HR'),
        ('Account', 'Account'),
        ('Development', 'Development'),
        ('Software', 'Software'),
        ('Ui&Ux', 'Ui&Ux'),
        )
    WORK_SHIFT_CHOICES=(
        ('Regular work shift', 'Regular work shift'),
        ('demo working shift regular', 'demo working shift regular'),
        ('demo working shift scheduled', 'demo working shift scheduled'),
        
    )
    
    name = models.CharField(max_length=100,unique=True,null=True,blank=True)
    manager=models.ForeignKey(Manager,on_delete=models.CASCADE)                              
    Parent_department=models.CharField(max_length=150,choices=PARENT_DEPARTMENT_CHOICES)
    Location=models.CharField(max_length=100)
    Work_Shift=models.CharField(max_length=150,choices=WORK_SHIFT_CHOICES)
    Description=models.TextField(max_length=150)
    is_active = models.BooleanField(default=True,null=True,blank=True)
    
    
class AddDesignation(models.Model):
    
    name = models.CharField(max_length=100,unique=True,null=True,blank=True)
    Description=models.TextField(null=True,blank=True)
    No_of_Employees=models.IntegerField(null=True,blank=True)

    


