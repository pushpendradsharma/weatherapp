from django.urls import path
from .views import (Dashboard, SearchWeather, Signup, Login, Logout)

urlpatterns = [
    path('', Dashboard, name="index"),
    path('signup/', Signup, name="signup"), # signup form
    path('login/', Login, name="login"), # login form
    path('logout/', Logout, name="logout"), # logout form
]
