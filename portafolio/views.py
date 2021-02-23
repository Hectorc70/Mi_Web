from django.shortcuts import render, redirect

from portafolio.forms import ProjectForm
from portafolio.models import Project, Picture
# Create your views here.



def projects_view(request):
    
    projects = Project.objects.all()
    for project in projects:

        
        img = Picture.objects.filter(project = project.id_project)
        print(img)
    imgs = Picture.objects.all()[1]




    

    return render (request, 'index.html', {'projects': projects,
                                            'imgs':imgs})
