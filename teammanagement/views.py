from rest_framework import viewsets
from .models import Team, Person
from .serializers import TeamSerializer, PersonSerializer


class TeamViewSet(viewsets.ModelViewSet):
    # Prefetch team members to avoid N+1 problem in serializer
    queryset = Team.objects.all().prefetch_related("members")
    serializer_class = TeamSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
