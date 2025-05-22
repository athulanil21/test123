from django.urls import path
from . import views

urlpatterns = [
    # path('redirect-test/', views.test, name="test_redirect"),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('registration/', views.registration, name="registration"),
]

app_name = "web"

