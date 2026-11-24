from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('', index, name='home'),
    path('create/', views.create_application, name='create_application'),
    path('delete/<int:application_id>/', views.delete_application_for_user, name='delete_application'),
    path('profile/', views.view_applications, name='profile'),
    path('application/<int:application_id>/', views.application_detail, name='application_detail'),
]
