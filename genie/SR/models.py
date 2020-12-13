from django.db import models
# Create your models here.
class INVTN_IGNORE_KEY_LIST(models.Model):
    IGNORE_KEY = models.CharField(max_length=4000)


class INVTN_LOGIC_KEY_LIST(models.Model):
    LOGIC_KEY = models.CharField(max_length=4000)
    LOGIC_NAME = models.CharField(max_length=4000)


class INVTN_OBJECT_KEY_LIST(models.Model):
    OBJECT_KEY = models.CharField(max_length=4000)
    OBJECT_NAME = models.CharField(max_length=4000)
    OBJECT_MASTER = models.CharField(max_length=4000)

class INVTN_EMPL(models.Model):
    EMPL_ID = models.CharField(max_length=4000)
    EMPL_NAME = models.CharField(max_length=4000)
    COUNTRY_CD = models.CharField(max_length=4000)

class INVTN_EMPL_PAY(models.Model):
    EMPL_ID = models.CharField(max_length=4000)
    SAL = models.IntegerField()
    PAY_PERIOD = models.DateField()

class test(models.Model):
    name = models.CharField(max_length=100)

class employee(models.Model):
    # gender_choice = (('M'),('F'))
    emp_no = models.IntegerField(primary_key=True, null=False)
    birth_date = models.DateField(null=False)
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False)
    gender = models.CharField(max_length=1, null=False)
    hire_date = models.DateField(null=False)

class departments(models.Model):
    dept_no = models.CharField(primary_key=True, null=False, max_length=4)
    dept_name = models.CharField(null=False, max_length=40, unique=True)

class dept_manager(models.Model):
    emp_no = models.IntegerField(null=False)
    dept_no = models.CharField(max_length=40,null=False)
    from_date = models.DateField(null=False)
    to_date = models.DateField(null=False)

class titles(models.Model):
    emp_no = models.IntegerField(null=False)
    title = models.CharField(max_length=40,null=False)
    from_date = models.DateField(null=False)
    to_date = models.DateField(null=False)

class salaries(models.Model):
    emp_no = models.IntegerField(null=False)
    salary = models.IntegerField(null=False)
    from_date = models.DateField(null=False)
    to_date = models.DateField(null=False)