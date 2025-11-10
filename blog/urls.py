from django.urls import path
from .views import renderRegisterForm,loginPage



urlpatterns = [
    path('register/', renderRegisterForm),
    path('login/', loginPage)
]