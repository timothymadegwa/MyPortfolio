from django.db import models
from django.utils import timezone
# Create your models here.

class Contact(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.first_name + ' ' + self.last_name
