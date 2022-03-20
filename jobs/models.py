from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Applicant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    email = models.EmailField()
    resume = models.FileField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    company = models.CharField(max_length=200)
    manager_email = models.EmailField()
    description = models.CharField(max_length=600)
    time = models.DateField(auto_now_add=False, auto_now=True)
    location = models.CharField(max_length=200)
    industries = models.CharField(max_length=600)
    employment_type = models.CharField(max_length=100)
    applicants = models.ManyToManyField(Applicant, blank=True)

    def __str__(self):
        return self.title







    