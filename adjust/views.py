from django.db.models import F
from django_filters import rest_framework as filters
from rest_framework.viewsets import ReadOnlyModelViewSet

from adjust.filters import AdjustFilter
from adjust.models import Adjust
from adjust.serializers import AdjustSerializer


class AdjustViewSet(ReadOnlyModelViewSet):
    """Home task for adjust viewset."""

    queryset = Adjust.objects.annotate(cpi=F("spend") / F("installs")).all()
    serializer_class = AdjustSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AdjustFilter
