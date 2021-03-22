from django.db import models

# Create your models here.

class Profile(models.Model):
    id_profile = models.AutoField(primary_key=True,
                                    auto_created=True, unique=True) 
    name         = models.CharField('Nombre', max_length=300)
    description  = models.TextField('Descripcion', blank=True)    
    photo_profile = models.CharField('Imagen de perfil', blank=True, max_length=500)
    link_cv      = models.CharField('Path CV', max_length= 500, blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    id_project   = models.AutoField(primary_key=True,
                                    auto_created=True, unique=True) 
    name         = models.CharField('Nombre de Proyecto', max_length=300)
    description  = models.TextField('Descripcion del Proyecto')
    picture_head = models.CharField('Imagen', max_length=500)
    code_link    = models.CharField('link codigo', max_length=500,blank=True) 
    demo_link    = models.CharField('link demo', max_length=500,blank=True) 

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


