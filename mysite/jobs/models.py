# models.py

from __future__ import annotations
from django.db import models
from django.utils.translation import gettext_lazy as _

# Added work_types which is basically on-site or remote
WORK_TYPES = (
    ('on-site', 'On-Site'),
    ('remote', 'Remote'),
)


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


# The `JobApplication` model represents a job application submitted by a user. It stores information about the user, their resume, the job title, activation key, and whether the application has been activated.
# It also includes timestamps for when the application was created and last updated.
class JobApplication(models.Model):
    name: str = models.CharField(_("Name"), max_length=255)
    address: str = models.CharField(_("Address"), max_length=255)
    phone_number: str = models.CharField(_("Phone Number"), max_length=255)
    email: str = models.EmailField(_("Email"))
    cover_letter: str = models.TextField(_("Cover Letter"))
    resume: str = models.FileField(_("Resume"), upload_to='resumes/')
    job_title: str = models.CharField(_("Job Title"), max_length=255)
    work_type: str = models.CharField(
        _("Work Type"), max_length=20, choices=WORK_TYPES, default="on-site")
    activation_key: str = models.CharField(
        _("Activation Key"), max_length=32, unique=True)
    is_active: bool = models.BooleanField(_("Is Active"), default=False)
    created_at: datetime = models.DateTimeField(
        _("Created At"), auto_now_add=True)
    updated_at: datetime = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name: str = _("Job Application")
        verbose_name_plural: str = _("Job Applications")

    def __str__(self) -> str:
        return self.name


class FullStackDeveloper(models.Model):
    """
    Model for Full Stack Developer
    """
    WORK_TYPES = (
        ('on-site', 'On-Site'),
        ('remote', 'Remote'),
    )

    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    # resume folders will be full_stack_developer instead of full_stack_developers
    resume = models.FileField(upload_to='resumes/full_stack_developers/')
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    cover_letter = models.TextField(blank=False, null=False)
    work_type = models.CharField(
        max_length=20, choices=WORK_TYPES, default='On-Site')

    def __str__(self):
        return self.name


class DigitalMarketingManager(models.Model):
    """
    Model for Digital Marketing Manager
    """
    WORK_TYPES = (
        ('on-site', 'On-Site'),
        ('remote', 'Remote'),
    )

    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    # resume folders will be digital_marketing_manager instead of digital_marketing_managers
    resume = models.FileField(upload_to='resumes/digital_marketing_managers/')
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    cover_letter = models.TextField(blank=False, null=False)
    work_type = models.CharField(
        max_length=20, choices=WORK_TYPES, default='On-Site')

    def __str__(self):
        return self.name


class SeniorBackendEngineer(models.Model):
    """
    Model for Senior Backend Engineer
    """
    WORK_TYPES = (
        ('on-site', 'On-Site'),
        ('remote', 'Remote'),
    )

    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    # resume folders will be senior_backend_engineer instead of senior_backend_engineers
    resume = models.FileField(upload_to='resumes/senior_backend_engineers/')
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    cover_letter = models.TextField(blank=False, null=False)
    work_type = models.CharField(
        max_length=20, choices=WORK_TYPES, default='On-Site')

    def __str__(self):
        return self.name


class AIMLEngineer(models.Model):
    """
    Model for AI/ML Engineer
    """
    WORK_TYPES = (
        ('on-site', 'On-Site'),
        ('remote', 'Remote'),
    )

    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    # resume folders will be ai_ml_engineer instead of ai_ml_engineers
    resume = models.FileField(upload_to='resumes/ai_ml_engineers/')
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    cover_letter = models.TextField(blank=False, null=False)
    work_type = models.CharField(
        max_length=20, choices=WORK_TYPES, default='On-Site')

    def __str__(self):
        return self.name


class GameDeveloper(models.Model):
    """
    Model for Game Developer
    """
    WORK_TYPES = (
        ('on-site', 'On-Site'),
        ('remote', 'Remote'),
    )

    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    # resume folders will be game_developer instead of game_developers
    resume = models.FileField(upload_to='resumes/game_developers/')
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    cover_letter = models.TextField(blank=False, null=False)
    work_type = models.CharField(
        max_length=20, choices=WORK_TYPES, default='On-Site')

    def __str__(self):
        return self.name


class MobileAppDeveloper(models.Model):
    """
    Model for Mobile App Developer
    """
    WORK_TYPES = (
        ('on-site', 'On-Site'),
        ('remote', 'Remote'),
    )

    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    # resume folders will be mobile_app_developer instead of mobile_app_developers
    resume = models.FileField(upload_to='resumes/mobile_app_developers/')
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    cover_letter = models.TextField(blank=False, null=False)
    work_type = models.CharField(
        max_length=20, choices=WORK_TYPES, default='On-Site')

    def __str__(self):
        return self.name
