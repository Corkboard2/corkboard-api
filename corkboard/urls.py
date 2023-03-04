from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import viewsets

router = DefaultRouter()
router.register('users', viewsets.UserViewSet)
urlpatterns = [
    path('restaurants/latitude/<latitude>/longitude/<longitude>/username/<username>', views.index, name='index'),
    path('', include(router.urls)),
]
