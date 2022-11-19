from django.urls import path
from . import views

app_name = 'server'
urlpatterns = [
    path("landingpage/", views.landing_page, name='landing_page'),
]
