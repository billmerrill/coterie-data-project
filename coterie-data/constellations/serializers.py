from rest_framework import serializers
from constellations.models import Constellation, Star


class ConstellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constellation
        fields = ('id', 'abbreviation')
        lookup_field = 'abbreviation'
