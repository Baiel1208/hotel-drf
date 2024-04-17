from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SettingsViewSet, FormSubmissionViewSet, FAQViewSet, CarouselItemViewSet, MapViewSet

router = DefaultRouter()
router.register('settings', SettingsViewSet)
router.register('form', FormSubmissionViewSet)
router.register('faq', FAQViewSet)
router.register('carousel', CarouselItemViewSet)
router.register('map', MapViewSet)

urlpatterns = [
    path('', include(router.urls)),
]