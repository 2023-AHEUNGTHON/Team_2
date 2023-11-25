from django.urls import path
from main import views

app_name = 'articles'
urlpatterns = [
    path('', views.home, name='home'),
]