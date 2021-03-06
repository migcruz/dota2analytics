from rest_framework import viewsets
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .serializers import UserSerializer, GroupSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    search_fields = ('first_name', 'last_name', 'email')
    filter_fields = ('id', 'first_name', 'last_name', 'email')


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer