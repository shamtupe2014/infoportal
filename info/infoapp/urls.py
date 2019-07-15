from django.contrib import admin
from django.urls import path,include
from.import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
]
