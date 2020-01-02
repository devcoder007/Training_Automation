from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class TrainerInfo(models.Model):
    trainerName = models.CharField(max_length=50,unique=False)
    trainingName = models.CharField(max_length=50, unique=False)
    startDate = models.CharField(max_length=50, unique=False)
    

    def __str__(self):
        return self.trainerName


class Trainer(models.Model):
    name = models.CharField(max_length=50,unique=True)
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender'),
        ('N', 'Not Known')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    speciality = models.CharField(max_length=50,unique=False)
    summary = models.CharField(max_length=500,unique=False)
    trainerImage = models.ImageField(upload_to = 'pro_pic', default = 'pic_folder/None/no-img.jpg')
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.name


class EmailSend(models.Model):
    toEmailList = models.CharField(max_length=1000,unique=False)
    fromEmail = models.CharField(max_length=50,unique = False)
    subject = models.CharField(max_length=250, unique=False)
    bodyEmail = models.CharField(max_length=2500,unique=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Myy(User):
    tokenn = models.CharField(max_length=10,unique=True)
    def __str__():
        return self.username




