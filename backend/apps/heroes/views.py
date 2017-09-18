from rest_framework import viewsets
from .serializers import HeroSerializer, AbilitySerializer
from .models import Hero, Ability
# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    lookup_field = 'hero_id'

class AbilityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer
    lookup_field = 'ability_name'
