from rest_framework import viewsets
from .models import Settings, FormSubmission, FAQ, CarouselItem, Map
from .serializers import SettingsSerializer, FormSubmissionSerializer, FAQSerializer, CarouselItemSerializer, MapSerializer


class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer


class FormSubmissionViewSet(viewsets.ModelViewSet):
    queryset = FormSubmission.objects.all()
    serializer_class = FormSubmissionSerializer


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class CarouselItemViewSet(viewsets.ModelViewSet):
    queryset = CarouselItem.objects.all()
    serializer_class = CarouselItemSerializer


class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer