from django.contrib import admin

# Register your models here.
from .models import prueba

class DisplayPrueba(admin.ModelAdmin):
	list_display = ["campo1","campo2","campo3"]
	class Meta:
		model = prueba


admin.site.register(prueba, DisplayPrueba)
