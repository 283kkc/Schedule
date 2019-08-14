from django.urls import path

from . import views

app_name='schedule'

urlpatterns = [
    path('', views.edit, name='edit'),
    path('<int:pk>/end/', views.end, name='end'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('detail/<int:pk>/<int:month>/', views.detail),
]


