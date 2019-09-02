from django.shortcuts import render, get_object_or_404
from .models import Job, Education, Painting
from django.views import View
# Create your views here.

def home(request):
    return render(request,'jobs/home.html')

def shivangi(request):
    jobs = Job.objects
    return render(request, 'jobs/work.html',{'jobs':jobs})

def shivangi_education(request):
    educations = Education.objects
    return render(request, 'jobs/edu.html',{'educations':educations})

def shivangi_paintings(request):
    paintings = Painting.objects
    return render(request, 'jobs/paintings.html',{'paintings':paintings})

def detail(request,job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail})


