from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("buy/", views.buy, name="buy"),
    path("predict-buy/", views.predict_buy, name="predict-buy"),
    path("rent/", views.rent, name="rent"),
    path("predict-rent/", views.predict_rent, name="predict-rent"),
]