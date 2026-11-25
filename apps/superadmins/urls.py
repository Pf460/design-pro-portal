from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_admin'),
    path('application/accept/<int:pk>/', views.update_status_on_accept_is_processed, name='update_status_a'),
    path('application/complete/<int:pk>/', views.update_status_on_completed, name='update_status_c'),
    path('categories/', views.list_categories, name='list_categories'),
    path('category/create/', views.create_category, name='create_category'),
    path('category/delete/<int:pk>/', views.destroy_category, name='destroy_category'),
]