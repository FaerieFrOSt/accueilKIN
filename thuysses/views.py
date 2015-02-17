# -*- coding: utf8 -*-
from django.shortcuts import render, HttpResponse, get_object_or_404
from thuysses.forms import ThuysseForm
from thuysses.models import Thuysse
import json
from users.models import Client
from django.db.models import Count

from thuysses.matieres import matieres as mats
from thuysses.matieres import choix_matieres, choix_ss_matieres, type_matiere

# Create your views here.

def index (request):
	""" Function doc """
	thuysses_plus_DL = Thuysse.objects.all().order_by('DL_Thuysse').reverse()[:10]
	name_last_thuysse = Thuysse.objects.all().order_by('date_DL').reverse()[:10]
	thuysseurs = Client.objects.annotate(num_Thuysse=Count('thuysse'))[:10]
	return render(request, 'thuysses/index.html', {'thuysses_plus_DL' : thuysses_plus_DL, 'name_last_thuysse' : name_last_thuysse, 'thuysseurs' : thuysseurs})

def get_page(request, annee = None, matiere = None):
	if annee == None:
		return redirect(index, request)
	ss_mat = []
	try:
		ss_mat = mats[annee][matiere]
	except KeyError:
		return redirect(index, request)
	dico = {}
	if not len(ss_mat):
		for i in type_matiere:
			dico[i[0]] = Thuysse.objects.filter(annee=annee, matiere=matiere, genre=i[0])
	for i in ss_mat:
		dico[i] = {}
		for j in type_matiere:
			dico[i][j[0]] = Thuysse.objects.filter(annee=annee, matiere=matiere,
												genre=j[0], sous_matiere=i)
	return render(request, 'thuysses/matiere_page.html', {'annee' : annee, 'matiere' : matiere, 'dico' : dico, 'ss_mat' : len(ss_mat) != 0})

def third (request, matiere = None):
	""" Function doc """
	return index(request)
	
def other (request, matiere = None):
	""" Function doc """
	return index(request)

def action_change(request):
	""" Function doc """
	action_list = []
	annee = request.GET.get("annee")
	annee = str(annee)
	if annee in mats:
		choices = [i for i in choix_matieres if i[0] == '' or i[0] in mats[annee]]
	else:
		choices = []
		matiere = str(request.GET.get("matiere"))
		try:
			annee = ''
			for i in mats:
				j = mats[i]
				if matiere in j:
					annee = i
					break
			if annee == '':
				raise KeyError
			choices = [i for i in choix_ss_matieres if i[0] == '' or i[0] in mats[annee][matiere]]
		except KeyError:
			choices = []
	if len(choices) == 1 and choices[0][0] == '':
		choices = []
	j = json.dumps(choices)
	return HttpResponse(j, content_type = 'application/javascript')

def save_thuysse (request):
	""" Function doc"""
	envoi = False
	if request.method == 'POST':
		form = ThuysseForm(request.POST.copy(), request.FILES)
		if form.is_valid():
			form = form.save(commit = False)
			gadz = Client.objects.get(username = request.user.username)
			form.publisher = gadz
			form.save()
			form = ThuysseForm()
			envoi = True
	else:
		form = ThuysseForm()
	return render(request, 'thuysses/creer_thuysse.html', {'form' : form, 'envoi' : envoi})		

def download (request, id_dl):
	""" Function doc """
	obj = get_object_or_404(Thuysse, id = id_dl)
	return HttpResponse(obj.name)
