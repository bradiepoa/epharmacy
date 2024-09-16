from django.urls import path
from . import views

app_name = "mainweb"
urlpatterns = [
    path("", views.homeView, name="home"),
    path("shop", views.shopView, name="shop"),
    path("single", views.singleView, name="single"),
    path("cart", views.CartView, name="cart"),
    path("checkout", views.checkOutView, name="checkout"),
    path("thanks", views.thanksView, name="thanks"),
    path("about-us", views.aboutView, name="aboutus"),
    path("contact-us", views.contactView, name="contact")
]
