from rest_framework.viewsets import ModelViewSet

from .models import Office
from .serializers import OfficeSerializer


class OfficeViewSet(ModelViewSet):
    """Set of views for office objects."""
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
