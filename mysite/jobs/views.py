# views.py

from django.conf import settings
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.core.files.storage import FileSystemStorage
from .models import FullStackDeveloper, DigitalMarketingManager
from django.shortcuts import render, redirect
from .forms import FullStackDeveloperForm, DigitalMarketingManagerForm
from django.shortcuts import render, get_object_or_404
from .models import JobOpening
from django.contrib import messages


def job_list(request):
    """
    A view to display a list of all job openings.
    """
    # Get a list of all job openings
    jobs = JobOpening.objects.all()

    # Render the template with the list of jobs and return the response to the user
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def success(request, activation_key):
    return render(request, 'jobs/success.html', {'activation_key': activation_key})


def apply_job(request, job_title):
    if job_title == 'full_stack_developer':
        form = FullStackDeveloperForm(
            request.POST or None, request.FILES or None)
        if request.method == 'POST':
            if form.is_valid():
                name = form.cleaned_data['name']
                address = form.cleaned_data['address']
                phone_number = form.cleaned_data['phone_number']
                email = form.cleaned_data['email']
                cover_letter = form.cleaned_data['cover_letter']
                resume = request.FILES['resume']
                fs = FileSystemStorage(location='resumes/full_stack_developer')
                filename = fs.save(resume.name, resume)
                uploaded_file_url = fs.url(filename)
                activation_key = get_random_string(length=32)

                # Set session data to indicate that the application is pending activation
                request.session['job_application'] = {
                    'name': name,
                    'address': address,
                    'phone_number': phone_number,
                    'email': email,
                    'cover_letter': cover_letter,
                    'resume_url': uploaded_file_url,
                    'activation_key': activation_key,
                }

                # Send activation email to the user
                subject = 'Activate your job application'
                message = f'Hi {name}, please click the following link to activate your job application: https://dotpotit.com/jobs/activate/{activation_key}'
                send_mail(subject, message, 'career@dotpotit.com',
                          [email], fail_silently=False)

                messages.success(
                    request, 'Your job application has been submitted!')
                return redirect('jobs:apply_job', job_title=job_title)
    else:
        form = DigitalMarketingManagerForm(
            request.POST or None, request.FILES or None)
        if request.method == 'POST':
            if form.is_valid():
                name = form.cleaned_data['name']
                address = form.cleaned_data['address']
                phone_number = form.cleaned_data['phone_number']
                email = form.cleaned_data['email']
                cover_letter = form.cleaned_data['cover_letter']
                resume = request.FILES['resume']
                fs = FileSystemStorage(
                    location='resumes/digital_marketing_manager')
                filename = fs.save(resume.name, resume)
                uploaded_file_url = fs.url(filename)
                activation_key = get_random_string(length=32)

                # Set session data to indicate that the application is pending activation
                request.session['job_application'] = {
                    'name': name,
                    'address': address,
                    'phone_number': phone_number,
                    'email': email,
                    'cover_letter': cover_letter,
                    'resume_url': uploaded_file_url,
                    'activation_key': activation_key,
                }

                # Send activation email to the user
                subject = 'Activate your job application'
                message = f'Hi {name}, please click the following link to activate your job application: https://dotpotit.com/jobs/activate/{activation_key}'
                send_mail(subject, message, 'career@dotpotit.com',
                          [email], fail_silently=False)

                messages.success(
                    request, 'Your job application has been submitted!')
                return redirect('jobs:apply_job', job_title=job_title)
    return render(request, 'jobs/apply_job.html', {'form': form, 'job_title': job_title})


def activate_job_application(request, activation_key):
    job_application_data = request.session.get('job_application')

    if job_application_data and job_application_data.get('activation_key') == activation_key:
        if job_application_data.get('job_title') == 'full_stack_developer':
            fs_developer = FullStackDeveloper.objects.create(
                name=job_application_data.get('name'),
                email=job_application_data.get('email'),
                address=job_application_data.get('address'),
                resume=job_application_data.get('resume_url'),
                phone_number=job_application_data.get('phone_number'),
                cover_letter=job_application_data.get('cover_letter')
            )
            fs_developer.save()
        elif job_application_data.get('job_title') == 'digital_marketing_manager':
            dm_manager = DigitalMarketingManager.objects.create(
                name=job_application_data.get('name'),
                email=job_application_data.get('email'),
                address=job_application_data.get('address'),
                resume=job_application_data.get('resume_url'),
                phone_number=job_application_data.get('phone_number'),
                cover_letter=job_application_data.get('cover_letter')
            )
            dm_manager.save()

        messages.success(
            request, 'Your job application has been activated! Thank you for applying.')

        job_title = job_application_data.get('job_title')

        # Delete the job application data from the session
        del request.session['job_application']

    else:
        messages.error(
            request, 'Invalid activation link. Please contact us if you need further assistance.')
        job_title = None

    return redirect('jobs:success', activation_key=activation_key)
