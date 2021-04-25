from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.login, name='login'),
    path('signup',views.signup, name='signup'),
    path('logout',views.logout, name='logout'),
    path('shopoverview',views.shopoverview, name='shopoverview'),
    path('shop',views.shop, name='shop'),
]