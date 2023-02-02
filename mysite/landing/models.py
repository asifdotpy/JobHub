from django.db import models


"""
This model has five fields: name, email, subject, date_time, and source. The CharField and EmailField are used for the character-based data, such as name and email. The DateTimeField is used for the date_time field, and the auto_now_add argument is set to True to automatically set the date and time when the form is submitted. The source field uses CharField to store a short description of where the form was submitted from. The __str__ method returns the subject field, which can be used to identify the form in the Django admin interface.
"""
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=50, default="website")

    def __str__(self):
        return self.subject


