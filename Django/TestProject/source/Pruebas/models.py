from django.db import models

# Create your models here.
class prueba(models.Model):
	campo1 = models.CharField(max_length=100, blank=True, null=True)
	campo2 = models.EmailField()
	campo3 = models.TextField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return self.campo1

	def __str__(self):
		return self.campo1

