from django.urls import path

from . import views

app_name = "beer_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('beer/', views.beer_form, name='beer_form'),
]