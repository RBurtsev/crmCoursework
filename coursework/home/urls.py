from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^parts/$', views.PartListView.as_view(), name='parts'),
    re_path(r'^clients/$', views.ClientsListView.as_view(), name='clients'),
    re_path(r'^fixes/$', views.fixesview, name='fixes_list'),
    re_path(r'^workers/$', views.WorkersListView.as_view(), name='workers'),
    re_path(r'^managedeck/$', views.managedeck, name='managedeck')
]

#update, create, delete parts
urlpatterns += [
    re_path(r'^part/create/$', views.PartCreate.as_view(), name='part_create'),
    re_path(r'^part/(?P<pk>\d+)/update/$', views.PartUpdate.as_view(), name='part_update'),
    re_path(r'^part/(?P<pk>\d+)/delete/$', views.PartDelete.as_view(), name='part_delete'),
]
#update, create, delete clients
urlpatterns += [
    re_path(r'^client/create/$', views.ClientCreate.as_view(), name='client_create'),
    re_path(r'^client/(?P<pk>\d+)/update/$', views.ClientUpdate.as_view(), name='client_update'),
    re_path(r'^client/(?P<pk>\d+)/delete/$', views.ClientDelete.as_view(), name='client_delete'),
]
#update, create, delete fixes
urlpatterns += [
    re_path(r'^fix/create/$', views.FixesCreate.as_view(), name='fix_create'),
    re_path(r'^fix/(?P<pk>\d+)/update/$', views.FixesUpdate.as_view(), name='fix_update'),
    re_path(r'^fix/(?P<pk>\d+)/delete/$', views.FixesDelete.as_view(), name='fix_delete'),
]

#update, create, delete workers
urlpatterns += [
    re_path(r'^worker/create/$', views.WorkersCreate.as_view(), name='worker_create'),
    re_path(r'^worker/(?P<pk>\d+)/update/$', views.WorkersUpdate.as_view(), name='worker_update'),
    re_path(r'^worker/(?P<pk>\d+)/delete/$', views.WorkersDelete.as_view(), name='worker_delete'),
]