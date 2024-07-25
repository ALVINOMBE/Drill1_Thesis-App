from django.urls import path
from . import views

urlpatterns = [
    path('', views.thesis_list, name='thesis_list'),
    path('thesis/<int:pk>/', views.thesis_detail, name='thesis_detail'),
    path('thesis/new/', views.thesis_new, name='thesis_new'),
    path('thesis/<int:pk>/edit/', views.thesis_edit, name='thesis_edit'),
]
