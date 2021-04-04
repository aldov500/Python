from django.shortcuts import render
from .forms import RegForm

# Create your views here.
# Las vistas son el front de la pagina
def inicio(request):	
	# Forma
	form = RegForm()
	context = {
		"el_form" : form, # Variable de tipo form
	}	
	return render(request,"inicio.html",context)

def pagina(request):
	# Forma
	form =  RegForm()
	context = {
		"el_pagina" : form,
	}
	return render(request,"pagina.html",context)
	