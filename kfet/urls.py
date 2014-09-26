from django.conf.urls import patterns, include, url

urlpatterns = patterns('kfet.views',
		url(r'^$', "index", name = 'index_kfet'),
		url(r'^products/$', "products", name = 'products'),
		url(r'^statistics/$', "statistics", name = 'statistics'),
		url(r'^print_pg/$', "print_pg", name = 'pg'),
)
