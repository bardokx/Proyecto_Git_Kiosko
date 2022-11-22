from django.contrib import admin
from .models import  Usuarios, Tiendas, Productos

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Tiendas)
admin.site.register(Productos)