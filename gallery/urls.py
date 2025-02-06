from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('upload/', views.upload_painting, name='upload_painting'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit/<int:pk>/', views.edit_painting, name='edit_painting'),
    path('delete/<int:pk>/', views.delete_painting, name='delete_painting'),
]
