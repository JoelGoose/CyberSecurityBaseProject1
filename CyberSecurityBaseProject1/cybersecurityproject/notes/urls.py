from django.urls import path
from .views import  addView, homePageView, changePasswordView

urlpatterns = [
    path("", homePageView, name="home"),
    path('add/',addView,name='add'),
    path('changepassword/', changePasswordView, name="accept"),
]