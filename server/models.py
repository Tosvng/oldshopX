
from django.db import models


class Member(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    first_name = models.CharField(max_length=200, default="No name")
    user_name = models.CharField(max_length=200, default="No name")
    email = models.EmailField(max_length=200)
    pwd = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, choices=GENDER, default='O')

    def __str__(self):
        return self.first_name + " : " + self.user_name
