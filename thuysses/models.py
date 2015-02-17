# -*- coding: utf8 -*-
from django.db import models
import os

from thuysses.matieres import type_matiere, nom_annee, choix_matieres, choix_ss_matieres

def get_path (instance, filename):
	""" Function doc """
	path = os.path.join(os.path.split(instance.fichier.path)[0])
	try:
		path = os.path.join(path, "data", instance.annee, instance.matiere, instance.sous_matiere, instance.genre)
		os.mkdir(path)
	except os.error:
		pass
	return os.path.join(path, filename)
	

class Thuysse(models.Model):
	annee = models.CharField(max_length = 32, choices = nom_annee, verbose_name = "Année")
	matiere = models.CharField(max_length = 32, choices = choix_matieres, verbose_name = "Matière")
	sous_matiere = models.CharField(max_length = 32, choices = choix_ss_matieres, verbose_name = "Sous matière", blank = True)
	genre = models.CharField(max_length = 32, choices = type_matiere, verbose_name = "Genre")
	date_DL =  models.DateTimeField(auto_now_add=True, auto_now=False)
	name = models.CharField(max_length = 255, verbose_name = "Nom de la thuysse")
	auteur = models.CharField(max_length = 32)
	commentaire = models.TextField(blank = True)
	fichier = models.FileField(upload_to =get_path)
	DL_Thuysse = models.IntegerField(default = 0)
	publisher = models.ForeignKey("users.Client")
