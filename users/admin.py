# -*- coding: utf8 -*-
from django.contrib import admin
from users.models import Client

class   AdminClient(admin.ModelAdmin):
	list_display = ('__str__', 'is_active', 'has_rezal', 'kgibss', 'phone', 'email')
	list_filter = ('is_active', 'has_rezal')
	search_fields = ('first_name', 'last_name', 'kgibss', 'phone', 'email')
	fieldsets = (
				(u"Utilisateur", {
						'classes' : ('gr-collapse grp-closed'),
						'fields' : ('username', 'first_name', 'last_name', 'phone', 'kgibss', 'email', 'is_active', 'has_rezal')
						}),)
	actions = ['delete_selected', 'set_rezal', 'remove_rezal', 'set_active', 'remove_active']

	def delete_selected(self, request, queryset):
		for item in queryset:
			item.delete()
	delete_selected.short_description = u"Supprimer les utilisateurs sélectionnés"	

	def set_rezal(self, request, queryset):
		for item in queryset:
			item.has_rezal = True
			item.save()
	set_rezal.short_description = u"Activer le rézal pour les utilisateurs sélectionnés"

	def remove_rezal(self, request, queryset):
		for item in queryset:
			item.has_rezal = False
			item.save()
	remove_rezal.short_description = u"Désactiver le rézal pour les utilisateurs sélectionnés"

	def set_active(self, request, queryset):
		for item in queryset:
			item.is_active = True
			item.save()
	set_active.short_description = u"Activer les utilisateurs sélectionnés"

	def remove_active(self, request, queryset):
		for item in queryset:
			item.is_active = False 
			item.save()
	remove_active.short_description = u"Désactiver les utilisateurs sélectionnés"

admin.site.register(Client, AdminClient)
