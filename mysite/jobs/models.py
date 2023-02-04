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

