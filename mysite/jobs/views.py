# views.py

import logging
from django.conf import settings
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.core.files.storage import FileSystemStorage
from .models import FullStackDeveloper, DigitalMarketingManager, JobApplication
from django.shortcuts import render, redirect
from .forms import FullStackDeveloperForm, DigitalMarketingManagerForm
from django.shortcuts import render, get_object_or_404
from .models import JobOpening
from django.contrib import messages


# Added logger
logger = logging.getLogger(__name__)


def job_list(request):
    """
    A view to display a list of all job openings.
    """

    # Render the template with the list of jobs and return the response to the user
    return render(request, 'jobs/job_list.html')


def success(request, activation_key):
    return render(request, 'jobs/success.html', {'activation_key': activation_key})


def apply_job(request, job_title):
    if job_title == 'full_stack_developer':
        form = FullStackDeveloperForm(
            request.POST or None, request.FILES or None)
    else:
        form = DigitalMarketingManagerForm(
            request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            job_application = form.save(commit=False)
            activation_key = get_random_string(length=32)

            # Save the job application in the database
            job_application.activation_key = activation_key
            job_application.job_title = job_title
            job_application.save()

            logger.info('Job application submitted for %s', job_title)

            # Send activation email to the user
            subject = 'Activate your job application'
            message = f'Hi {job_application.name},<br><br>Thank you for applying for the {job_title} position at DotPot IT.<br><br>Please click the button below to activate your job application:<br><br><a href="https://dotpotit.com/jobs/activate/{activation_key}" style="background-color: #eb5d1e; color: #fef8f5; padding: 10px 20px; border-radius: 5px; text-decoration: none;">Activate</a><br><br>Best regards,<br>The DotPot IT Team'

            send_mail(subject, message, 'career@dotpotit.com',
                      [job_application.email], fail_silently=False, html_message=message)

            logger.info('Activation email sent to %s', job_application.email)

            messages.success(
                request, 'Your job application has been submitted!')
            return redirect('jobs:apply_job', job_title=job_title)

    return render(request, 'jobs/apply_job.html', {'job_title': job_title})


# Activate job application function will save the data after the apply_job
# function triggered.
def activate_job_application(request, activation_key):
    """
    Activates a job application for the given activation key.

    When a user clicks the activation link sent to their email after submitting
    a job application, this function is called to activate the application.

    Args:
        request: The HTTP request.
        activation_key (str): The activation key to use to activate the application.

    Returns:
        A redirect to the success page for the job title of the activated application.
    """
    logger.info(
        'Activating job application for activation key: %s', activation_key)

    # Look up the job application using the activation key
    try:
        job_application_data = JobApplication.objects.get(
            activation_key=activation_key)
    except JobApplication.DoesNotExist:
        logger.warning('Invalid activation link: %s', activation_key)
        messages.error(
            request, 'Invalid activation link. Please contact us if you need further assistance.')
        return redirect('jobs:job_list')

    if job_application_data:
        if job_application_data.job_title == 'full_stack_developer':
            # Create a FullStackDeveloper object and save it to the database
            fs_developer = FullStackDeveloper.objects.create(
                name=job_application_data.name,
                email=job_application_data.email,
                address=job_application_data.address,
                resume=job_application_data.resume_url,
                phone_number=job_application_data.phone_number,
                cover_letter=job_application_data.cover_letter
            )
            fs_developer.save()
        elif job_application_data.job_title == 'digital_marketing_manager':
            # Create a DigitalMarketingManager object and save it to the database
            dm_manager = DigitalMarketingManager.objects.create(
                name=job_application_data.name,
                email=job_application_data.email,
                address=job_application_data.address,
                resume=job_application_data.resume_url,
                phone_number=job_application_data.phone_number,
                cover_letter=job_application_data.cover_letter
            )
            dm_manager.save()

        messages.success(
            request, 'Your job application has been activated! Thank you for applying.')
        logger.info('Job application activated for %s',
                    job_application_data.email)

        job_title = job_application_data.job_title

        # Delete the job application data from the database
        job_application_data.delete()
        logger.info('Job application data deleted for %s',
                    job_application_data.email)

    else:
        logger.warning('Invalid activation link: %s', activation_key)
        messages.error(
            request, 'Invalid activation link. Please contact us if you need further assistance.')
        job_title = None

    return redirect('jobs:success', job_title=job_title)
