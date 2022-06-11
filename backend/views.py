from rest_framework import viewsets
from backend.models import VitalData
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from backend.serializers import VitalDataSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 5


class VitalDataViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination

    queryset = VitalData.objects.all()
    serializer_class = VitalDataSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filter_fields = ["user_id"]

    # def get_queryset(self):
    #     queryset = VitalData.objects.all()
    #     return queryset
