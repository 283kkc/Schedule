from django.urls import path

from . import views

app_name='schedule'

urlpatterns = [
    path('', views.edit, name='edit'),
    path('<int:pk>/end/', views.end, name='end'),
    path('index/', views.index, name='index'),
]


