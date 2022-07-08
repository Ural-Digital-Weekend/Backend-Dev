from rest_framework.viewsets import ModelViewSet

from avia.models import Airport
from avia.serializers.airport import AirportSerializer
from avia.serializers.airport_list import AirportListElementSerializer


class AirportsViewSet(ModelViewSet):
    authentication_classes = []

    queryset = Airport.objects
    serializer_class = AirportSerializer
    ordering = ('id',)

    def list(self, request, *args, **kwargs):
        self.serializer_class = AirportListElementSerializer
        return super(AirportsViewSet, self).list(request, *args, **kwargs)
