from django.shortcuts import render, redirect
from .models import Education, Skill, Experience, Project, Contact
from .forms import ContactForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('home')
    else:
        form = ContactForm()

    education = Education.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    context = {
        'education': education,
        'skills': skills,
        'experiences': experiences,
        'projects': projects,
        'form': form,
    }
    return render(request, 'main/home.html', context)