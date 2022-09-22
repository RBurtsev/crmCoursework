from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^parts/$', views.PartListView.as_view(), name='parts')
]