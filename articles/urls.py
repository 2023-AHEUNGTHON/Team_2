from django.urls import path
from articles import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/',views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('update/<int:pk>', views.update, name='update'),
]