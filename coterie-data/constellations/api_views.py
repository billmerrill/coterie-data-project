from constellations.models import Constellation
from constellations.serializers import ConstellationSerializer
from rest_framework import generics

class ConstellationList(generics.ListAPIView):
    queryset = Constellation.objects.all()
    serializer_class = ConstellationSerializer


class ConstellationDetail(generics.RetrieveAPIView):
    queryset = Constellation.objects.all()
    serializer_class = ConstellationSerializer
