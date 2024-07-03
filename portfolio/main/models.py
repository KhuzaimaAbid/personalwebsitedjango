from django.db import models

# Create your models here.
class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.degree

class Skill(models.Model):
    name = models.CharField(max_length=200)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.name

class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.job_title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name