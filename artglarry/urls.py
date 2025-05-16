from django.urls import path
from .views import *
urlpatterns = [
    path('home/',home,name="home"),
    path('validate/',login,name="validate"),
    path('user_reg/',user_reg,name="user_reg"),
    path('profile/',profile,name="profile"),
    path('product/',product,name="product"),
    path('logout/',logout,name="logout"),
    path('upload_art/',upload_art,name="upload_art"),
    path('product_detail/',product_detail,name='product_detail'),
    path('user_bids/',user_bids,name="user_bids"),
    path('order/',order,name="order"),
    path('confirm_order/',confirm_order,name="confirm_order"),
    path('fillter_data/',fillter_data,name="fillter_data"),
]
