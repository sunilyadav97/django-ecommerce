from django.urls import path,include
from .views import *


urlpatterns = [
    path('',store,name='store'),
    path('cart',cart,name='cart'),
    path('checkout',checkOut,name='checkout'),
    path('login',signin,name='login'),
    path('logout',signout,name='logout'),
    path('register',register,name='register'),
    path('update-cart',addToCart,name='updatecart'),
]
