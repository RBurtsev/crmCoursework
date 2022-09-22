from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^parts/$', views.PartListView.as_view(), name='parts'),
    re_path(r'^board/$', views.BoardListView.as_view(), name='board'),
    re_path(r'^clients/$', views.ClientsListView.as_view(), name='clients')
]