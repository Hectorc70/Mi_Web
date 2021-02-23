from django.forms import ModelForm

from portafolio.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = (
            'name',
            'description',
        )



