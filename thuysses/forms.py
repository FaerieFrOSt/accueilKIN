from django import forms
from thuysses.models import Thuysse

class ThuysseForm(forms.ModelForm):
	class Meta:
		model = Thuysse
		exclude = ["DL_Thuysse", "publisher"]
		widgets = {
			"annee" : forms.Select(attrs = {'onchange' : 'annee_change();'}),
			"matiere" : forms.Select(attrs = {'onchange' : 'matiere_change();'}),
			"sous_matiere" : forms.Select(attrs = {'onchange' : 'sous_matiere_change();'}),
			}
