from django.urls import path

from . import views

app_name = "react"


urlpatterns = [
    #Leave as empty string for base url

    #------------ (STORE - URLS) ------------

	path('', views.home, name="home"),

    ]
