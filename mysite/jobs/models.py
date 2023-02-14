# models.py

from django.db import models


class JobOpening(models.Model):
    """
    A model representing a job opening for the company.
    """
    # Fields for the job opening
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    requirements = models.TextField()

    # Timestamps to track when the job opening was created and modified
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return a string representation of the job opening.
        """
        return self.title


class FullStackDeveloper(models.Model):
    """
    Model for Full Stack Developer
    """
    name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    resume = models.FileField(upload_to='resumes/full_stack_developers/')
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    cover_letter = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name


class DigitalMarketingManager(models.Model):
    """
    Model for Digital Marketing Manager
    """
    name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    resume = models.FileField(upload_to='resumes/digital_marketing_managers/')
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    cover_letter = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name
