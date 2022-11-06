from django.urls import path
from . import views

urlpatterns = [
    path("landingpage/", views.landing_page, name='landing_page'),
]