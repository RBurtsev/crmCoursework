from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^parts/$', views.PartListView.as_view(), name='parts'),
    re_path(r'^board/$', views.BoardListView.as_view(), name='board'),
    re_path(r'^clients/$', views.ClientsListView.as_view(), name='clients')
]


urlpatterns += [
    re_path(r'^part/create/$', views.PartCreate.as_view(), name='part_create'),
    re_path(r'^part/(?P<pk>\d+)/update/$', views.PartUpdate.as_view(), name='part_update'),
    re_path(r'^part/(?P<pk>\d+)/delete/$', views.PartDelete.as_view(), name='part_delete'),
]

urlpatterns += [
    re_path(r'^client/create/$', views.ClientCreate.as_view(), name='client_create'),
    re_path(r'^client/(?P<pk>\d+)/update/$', views.ClientUpdate.as_view(), name='client_update'),
    re_path(r'^client/(?P<pk>\d+)/delete/$', views.ClientDelete.as_view(), name='client_delete'),
]