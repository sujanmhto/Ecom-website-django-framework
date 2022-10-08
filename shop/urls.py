from django.urls import path
from . import views

urlpatterns = [
    path("", views.index , name="ShopHome"),
    path("contact/", views.contact , name="ContactUs"),
    path("about/", views.about , name="AboutUs"),
    path("tracker/", views.tracker , name="TrackingStatus"),
    path("search/", views.search , name="Search"),
    path("product-view/", views.productView , name="ProductView"),
    path("checkout/", views.checkout , name="CheckOut"),
]