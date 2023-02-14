# views.py

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


def job_detail(request, pk):
    """
    A view to display the details of a specific job opening.
    """
    # Get a specific job opening based on its primary key
    job = get_object_or_404(JobOpening, pk=pk)

    # Render the template with the details of the job and return the response to the user
    return render(request, 'jobs/job_detail.html', {'job': job})


def apply_job(request, job_title):
    if job_title == 'full_stack_developer':
        form = FullStackDeveloperForm(
            request.POST or None, request.FILES or None)
        if request.method == 'POST':
            if form.is_valid():
                name = form.cleaned_data['name']
                address = form.cleaned_data['address']
                phone_number = form.cleaned_data['phone_number']
                cover_letter = form.cleaned_data['cover_letter']
                resume = request.FILES['resume']
                fs = FileSystemStorage(location='jobs/resumes')
                filename = fs.save(resume.name, resume)
                uploaded_file_url = fs.url(filename)
                FullStackDeveloper.objects.create(
                    name=name,
                    address=address,
                    phone_number=phone_number,
                    cover_letter=cover_letter,
                    resume=uploaded_file_url
                )
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
                cover_letter = form.cleaned_data['cover_letter']
                resume = request.FILES['resume']
                fs = FileSystemStorage(location='jobs/resumes')
                filename = fs.save(resume.name, resume)
                uploaded_file_url = fs.url(filename)
                DigitalMarketingManager.objects.create(
                    name=name,
                    address=address,
                    phone_number=phone_number,
                    cover_letter=cover_letter,
                    resume=uploaded_file_url
                )
                messages.success(
                    request, 'Your job application has been submitted!')
                return redirect('jobs:apply_job', job_title=job_title)
    return render(request, 'jobs/apply_job.html', {'form': form, 'job_title': job_title})
