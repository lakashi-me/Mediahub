from django.urls import path
from . import views

app_name = 'media_assets'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]