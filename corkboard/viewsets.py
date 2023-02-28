from rest_framework import viewsets
from corkboard.models import User
from corkboard.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
