from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import JobFilter


# Create your views here.

def index(request):
    return render(request, 'jobs/index.html')

def jobs(request):
    jobs = Job.objects.all()
    myFilter = JobFilter(request.GET, queryset=jobs)
    jobs = myFilter.qs
    context = {'jobs': jobs, 'myFilter': myFilter}
    return render(request, 'jobs/jobs.html', context)
    
def details(request, job_slug):
    job = Job.objects.get(slug=job_slug)
    context = {'job': job, 'industries': job.industries.split(", "), 'industries_index': range(len(job.industries.split(", ")))
    , 'industries_len': len(job.industries.split(", ")) - 1}
    return render(request, 'jobs/details.html', context)


def register(request, job_slug):
    job = Job.objects.get(slug=job_slug)
    form = ApplicantForm()
    if request.method == 'GET':
        form = ApplicantForm()
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicants,_ = Applicant.objects.get_or_create(name=form.cleaned_data['name'], location=form.cleaned_data['location'], email=form.cleaned_data['email'])
            job.applicants.add(applicants)
            return redirect('success', job_slug)
    context = {'job': job, 'form': form}
    return render(request, 'jobs/register.html', context)


def success(request, job_slug):
    job = Job.objects.get(slug=job_slug)
    context = {'manager_email': job.manager_email, 'company': job.company, 'position': job.title}
    return render(request, 'jobs/success.html', context)