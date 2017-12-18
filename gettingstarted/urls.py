from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^FP_Home/', hello.views.FP_Home, name = 'FP_Home'),
	url(r'^Gene_Alignments/', hello.views.Gene_Alignments, name = 'Gene_Alignments'),
	url(r'^Protein_Structure/', hello.views.Protein_Structure, name = 'Protein_Structure'),
	url(r'^Cell_and_Molecular/', hello.views.Cell_and_Molecular, name = 'Cell_and_Molecular'),
	url(r'^Refferences_and_Resources/', hello.views.Refferences_and_Resources, name = 'Refferences_and_Resources'),
	url(r'^Clinical_Study/', hello.views.Clinical_Study, name = 'Clinical_Study'),
]
