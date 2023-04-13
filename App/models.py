from django.db import models

# Create your models here.

class Civilservants(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    ministry = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    appointment_date = models.DateField()

    def __str__(self):
        return self.firstname

    class Meta:
        verbose_name = 'civilservants'
        verbose_name_plural = 'civilservants'


class csdetails(models.Model):
    name = (models.ForeignKey(Civilservants, on_delete=models.CASCADE))
    minist = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    cs_age = models.IntegerField()
    cs_years = models.IntegerField()

    def __str__(self):
        return self.dept

    class Meta:
        verbose_name = 'csdetails'
        verbose_name_plural = 'csdetails'


class Retirement(models.Model):
    retiree_name =  (models.ForeignKey(Civilservants, on_delete=models.CASCADE))
    dob = models.DateField()
    appointment_date = models.DateField()
    age = models.IntegerField()
    years_of_work = models.IntegerField()
    retirement_status = models.CharField(max_length=50)

    def __str__(self):
        return self.retiree_name

    class Meta:
        verbose_name = 'retirement'
        verbose_name_plural = 'retirement'
class Reports(models.Model):
    Retname =  (models.ForeignKey(Civilservants, on_delete=models.CASCADE))
    Minist = models.CharField(max_length=100)
    Dept = models.CharField(max_length=100)
    Apt_date = models.DateField()
    Dob = models.DateField()
    Age = models.IntegerField()
    Duration = models.IntegerField()
    Status = models.CharField(max_length=50)

    def __str__(self):
        return self.retname

    class Meta:
        verbose_name = 'reports'
        verbose_name_plural = 'reports'
