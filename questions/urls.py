# pylint: disable=invalid-name
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^search/(?P<query>\w+)', views.SearchHandler.as_view(),
        name='search_handler'),
    url(r'^search/', views.SearchHandler.as_view(),
        name='search_handler'),
]
