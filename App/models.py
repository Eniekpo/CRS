from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.ensemble import RandomForestClassifier
import joblib

# Create your models here.
DEPARTMENT = (
    ('', 'Department'),
    ('ICT', 'ICT'),
    ('ICT', 'ICT'),
    ('ICT', 'ICT'),
    ('ICT', 'ICT'),
)

MINISTRY = (
    ('', 'Ministry'),
    ('Agriculture', 'Agriculture'),
    ('Agriculture', 'Agriculture'),
    ('Agriculture', 'Agriculture'),
    ('Agriculture', 'Agriculture'),
    ('Agriculture', 'Agriculture'),
)



class Civilservants(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    ministry = models.CharField(max_length=100, choices=MINISTRY)
    department = models.CharField(max_length=50, choices=DEPARTMENT)
    marital_status = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    appointment_date = models.DateField()

    def __str__(self):
        return self.firstname

    class Meta:
        ordering = ['firstname']
        verbose_name = 'civilservants'
        verbose_name_plural = 'civilservants'

class Retirement(models.Model):
    retiree_name =  (models.ForeignKey(Civilservants, on_delete=models.CASCADE))
    retiree_ministry = models.CharField(max_length=100, choices=MINISTRY)
    retiree_department = models.CharField(max_length=100, choices=DEPARTMENT)
    appointment_date = models.DateField()
    dob = models.DateField()
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(75)], null=True)
    years_of_work = models.IntegerField()
    retirement_status = models.CharField(max_length=50, blank=True)

     # FUNCTION TO MAKE PREDICTIONS
    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/retirement_processor.joblib')
        self.Predictions = ml_model.predict(
            [[self.age]])
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.retiree_department

    class Meta:
        ordering = ['-appointment_date']
        verbose_name = 'retirement'
        verbose_name_plural = 'retirement'
class Reports(models.Model):
    Retname =  (models.ForeignKey(Civilservants, on_delete=models.CASCADE))
    Minist = models.CharField(max_length=100, choices=MINISTRY)
    Dept = models.CharField(max_length=100, choices=DEPARTMENT)
    Apt_date = models.DateField()
    Dob = models.DateField()
    Age = models.IntegerField()
    Duration = models.IntegerField()
    Status = models.CharField(max_length=50)

    def __str__(self):
        return self.Minist

    class Meta:
        ordering = ['-Apt_date']
        verbose_name = 'reports'
        verbose_name_plural = 'reports'
