from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name = "index"),#
    path("<int:month>", views.int_monthly_challenge),
    path("<str:month>", views.monthly_challenge, name = "monthly-challenge")
]
