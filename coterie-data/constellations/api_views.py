from constellations.models import Constellation
from constellations.serializers import ConstellationSerializer
from rest_framework import generics


class ConstellationList(generics.ListAPIView):
    queryset = Constellation.objects.all()
    serializer_class = ConstellationSerializer


class ConstellationDetailByName(generics.RetrieveAPIView):
    queryset = Constellation.objects.all()
    serializer_class = ConstellationSerializer
    lookup_field = 'abbreviation'


class ConstellationDetail(generics.RetrieveAPIView):
    queryset = Constellation.objects.all()
    serializer_class = ConstellationSerializer
