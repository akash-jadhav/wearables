from rest_framework import viewsets
from backend.models import VitalData

from backend.serializers import VitalDataSerializer


class VitalDataViewSet(viewsets.ModelViewSet):
    serializer_class = VitalDataSerializer

    def get_queryset(self):
        queryset = VitalData.objects.all()
        return queryset
