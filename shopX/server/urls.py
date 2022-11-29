from django.urls import path
from . import views

app_name = 'server'
urlpatterns = [
    path("landingpage/", views.landing_page, name='landing_page'),
    path("confirmationpage/", views.confirmation_page, name='confirmation_page'),
    path("create/", views.create, name="create"),
]
