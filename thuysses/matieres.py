# coding: utf-8
matieres = {
	'first' : {"CEE" : [], "CM" : [], "CPD" : [], "MAT" : [], "MDS" :[], "PMP" :[], "SIM" : [], "TDE" :[] , "IMP" :[] , "HSE" :[] , "HSM" :[], "Anglais" :[] },
	'secondGM' : {"ESM" : ["Moraru", "Kubler", "Pernot-Gomand"], "IND" : ["Usinage", "Fonderie", "Assemblage", "Roucoule"], "TCM" : ["Masse" , "Barral'ss"], "TDP" :["Hydraulique" , " Elec" , " Mécanique"] , "Anglais" : [], "OPM" : ["Kubler" , "Fabre", "Gomand" , "Martin" , "Fonderie" , "Assemblage" , "Usinage", "Gras" , "Malburet", "Pons"]},
	'secondGI' : {"CSI" : ["Rosin", "Favarel", "Salgado"], "CM2" : [], "MSP" : [] , "MSE" :[] , "CMS" :[] , "Anglais" :[]},
	#'other' : {"CAMIP" : [], "TOEIC" :[] ,"Calcul_moy " : ["1A" , "2A" ] },
}

nom_annee = [("first", "Première année"), ("secondGM", "Deuxième année GM"), ("secondGI", "Deuxième année GI")]

type_matiere = [("Cours Amphi", "Cours Amphi"), ("ED", "ED"), ("TP", "TP"), ("Test", "Test"), ("Projet", "Projet"), ("Fiche", "Fiche")]

choix_matieres = []
for i in matieres.items():
	for j in i[1]:
		choix_matieres.append(j)

choix_matieres = list(set(choix_matieres))
choix_matieres.sort(reverse = True)
choix_matieres = [(i, i) for i in choix_matieres]
choix_matieres.append(("", "----------"))
choix_matieres.reverse()

choix_ss_matieres = []
for i in matieres.items():
	for j in i[1].items():
		for k in j[1]:
			choix_ss_matieres.append(k)

choix_ss_matieres = list(set(choix_ss_matieres))
choix_ss_matieres.sort(reverse = True)
choix_ss_matieres = [(i, i) for i in choix_ss_matieres]
choix_ss_matieres.append(("", "----------"))
choix_ss_matieres.reverse()

if __name__ == "__main__":
	print(choix_matieres)
	print()
	print(choix_ss_matieres)
	print()
