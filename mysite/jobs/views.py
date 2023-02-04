#views.py

from django.shortcuts import render, get_object_or_404
from .models import JobOpening

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

