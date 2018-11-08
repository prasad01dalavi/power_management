"""power_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from power_app import views

admin.site.site_header = 'Power Management'
admin.site.index_title = 'Power Management'
admin.site.site_title = 'Power Management'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add_service/', views.AddService.as_view()),
    path('get_values/', views.GetValues.as_view()),
    path('add_value/', views.AddValue.as_view())
    # path('add_service/', views.AddService.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
