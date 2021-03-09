from django.db import models

# Create your models here.


class Project(models.Model):
    id_project  = models.AutoField(primary_key=True,
                                    auto_created=True, unique=True) 
    name         = models.CharField('Nombre de Proyecto', max_length=300)
    description  = models.TextField('Descripcion del Proyecto')
    picture_head = models.CharField('Imagen', max_length=500)

    def __str__(self):
        return self.name




class Picture(models.Model):
    id_img    = models.AutoField( primary_key=True, 
                                auto_created=True, unique=True)
    name_pict =  models.CharField('Nombre de Imagen', max_length=200)
    url       = models.ImageField(upload_to='pictures/')
    project   = models.ForeignKey(Project, on_delete=models.CASCADE, to_field='id_project')

    def __str__(self):
        return self.name_pict


