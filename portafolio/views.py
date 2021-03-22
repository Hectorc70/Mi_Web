from django.shortcuts import render, redirect

from portafolio.forms import ProjectForm
from portafolio.models import Project, Picture, Profile
# Create your views here.



def projects_view(request):
    last_picture = dict()

    projects = Project.objects.all()
    profiles = Profile.objects.all()

    

    return render (request, 'index.html', {'projects': projects,
                                            'profile': profiles,})
