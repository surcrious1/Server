from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('sign_in/', views.sign_in , name = 'sign_in'),
    path('sign_up/', views.sign_up, name = 'sign_up'),
    path('sign_out/', views.sign_out, name = 'sign_out'),
]