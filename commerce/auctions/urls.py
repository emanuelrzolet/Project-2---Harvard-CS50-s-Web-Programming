from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("product", views.products_view, name="products"),
    #redenderização dos ids
    path("int:product_id",views.products_view, name="product"),
    path("addProduct",views.addProduct, name="addProduct")
]
