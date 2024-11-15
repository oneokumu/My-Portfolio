from django.urls import path
from .views import home_view, contact_view

urlpatterns = [
    path('', home_view, name='home'),  # Root path
    path('contact/', contact_view, name='contact'),
]
