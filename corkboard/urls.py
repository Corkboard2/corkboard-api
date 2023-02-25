from django.urls import path

from . import views

urlpatterns = [
    path('latitude/<latitude>/longitude/<longitude>', views.index, name='index')
]
