from django.db import models

from phone_field import PhoneField

# Create your models here.
class Contact(models.Model):

    fname = models.CharField(max_length=120)
    lname = models.CharField(max_length=120)
    phone = PhoneField(blank=False)
    email = models.EmailField(unique=True)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.fname + " " + self.lname
