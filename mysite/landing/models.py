from django.db import models


"""
This model has five fields: name, email, subject, date_time, and source. The CharField and EmailField are used for the character-based data, such as name and email. The DateTimeField is used for the date_time field, and the auto_now_add argument is set to True to automatically set the date and time when the form is submitted. The source field uses CharField to store a short description of where the form was submitted from. The __str__ method returns the subject field, which can be used to identify the form in the Django admin interface.
"""

from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
