from django.urls import path
from django.views.generic import (TemplateView, RedirectView)

urlpatterns = [
    path(
        '',
        TemplateView.as_view(
            template_name='bookings/index.html'
            )
        ),
    path(
        'my_path/my_unwanted_url/',
        RedirectView.as_view(
            url = 'http://localhost:8000/my_wanted_url/',
            permanent=True
            )
        ),
]