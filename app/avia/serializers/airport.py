from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from avia.models import Airport


class AirportSerializer(ModelSerializer):
    type = StringRelatedField()

    class Meta:
        model = Airport
        fields = (
            "ident",
            "local_code",
            "name",
            "coordinates",
            "elevation_ft",
            "gps_code",
            "iata_code",
            "type",
        )
