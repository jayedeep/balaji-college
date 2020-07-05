from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser


# Create your models here.
GENDER=(
    ('male','Male'),
    ('female','Female'),
    ('lgbt','LBGT')
)
SEM=(
    ('1','1st'),
    ('2','2st'),
    ('3','3st'),
    ('4','4st'),
    ('5','5st'),
    ('6','6st'),
    ('7','7st'),
    ('8','8st')
)
DEPT=(
    ('comp','COMPUTER ENGINEERING'),
    ('mech',"MECHANICAL ENGINEERING"),
    ('ele','ELECTRICAL ENGINEERING'),
    ('civil','CIVIL ENGINEERING')
)
class Students(AbstractUser):
    profile=models.ImageField(upload_to='')
    fullname=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    gender=models.CharField(max_length=20,choices=GENDER,default='male')
    birthdate=models.DateTimeField(auto_now_add=True)
    semester=models.CharField(max_length=20,choices=SEM,default='1')
    department=models.CharField(max_length=20,choices=DEPT,default='comp')
    enrollment=models.CharField(max_length=50)
    lastsemspi=models.CharField(max_length=20)
    lastsemcpi=models.CharField(max_length=20)
    def __str__(self):
        return self.fullname

class PreviousMarks(models.Model):
    user=models.ForeignKey(Students,on_delete=models.CASCADE)
    spi = ArrayField(models.FloatField(),size=8)
    cpi = ArrayField(models.FloatField(),size=8)

    def __str__(self):
        return self.user