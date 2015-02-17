from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('thuysses.views',
    # Examples:
    # url(r'^$', 'Thuysses.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', "index"),
	url(r'^get_page/(?P<annee>\w{1,9})/(?P<matiere>\w{1,50})/$', "get_page"),
    url(r'^third/(?P<matiere>\w{1,50})/$', "third"),
    url(r'^other/(?P<matiere>\w{1,50})/$', "other"),
    url(r'^creer_thuysse/$', "save_thuysse"),
    url(r'^action_change/', "action_change"),
    url(r'^download/(?P<id_dl>\d+)', "download"),
)
