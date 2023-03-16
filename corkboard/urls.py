from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import viewsets

router = DefaultRouter()
router.register('users', viewsets.UserViewSet)
urlpatterns = [
    path('restaurants/latitude/<latitude>/longitude/<longitude>/username/<username>', views.index, name='index'),
    path('users/<user_id>/restaurants', views.get_past_restaurants, name='past_restaurants'),
    path('users/<user_id>/restaurants/<restaurant_name>/rating/<rating>/update', views.update_restaurant_rating, name='update_rating'),
    path('', include(router.urls)),
]
