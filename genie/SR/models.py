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