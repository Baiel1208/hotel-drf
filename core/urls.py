"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .drf_yasg import urlpatterns as urls_swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blog/', include('apps.blog.urls')),
    path('api/users/', include('apps.users.urls')),
    path('api/hotel/', include('apps.hotel.urls')),
    path('api/job/', include('apps.job.urls')),
    path('api/news/', include('apps.news.urls')),
    path('api/review/', include('apps.review.urls')),
    path('api/team-members/', include('apps.teammember.urls')),

]   + urls_swagger

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)