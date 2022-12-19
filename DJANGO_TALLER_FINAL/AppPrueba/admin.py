from django.contrib import admin
from AppPrueba.models import Institucion
# Register your models here.

class InstitucionADM (admin.ModelAdmin):
    list_display = ['institucion']

admin.site.register(Institucion, InstitucionADM)
