"""
URL configuration for hwproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from hwproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hw_1/', include('app_hw_1.urls')),
    path('hw_2/', include('app_hw_2.urls')),
    path('hw_3/', include('app_hw_3.urls')),
    path('hw_4/', include('app_hw_4.urls')),
    # path('hw_5/', include('app_hw_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
