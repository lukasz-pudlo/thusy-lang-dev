"""
thusy_lang URL Configuration

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
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(
        '',
        TemplateView.as_view(
            template_name = 'bookings/index.html'
            )
        ),
    ] + static(
    settings.STATIC_URL, 
    document_root = settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT
)


#Alternative way of setting up static files according to Michael Dinder in "Becoming Enterprise Django Developer"
#urlpatterns = [...]
#if settings.DEBUG:
#    urlpatterns += static(
#        settings.STATIC_URL, 
#        document_root = settings.STATIC_ROOT
#    )
