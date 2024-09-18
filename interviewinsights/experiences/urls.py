from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('share/', views.submit_experience, name='share_experience'),
    path('search/', views.search_experiences, name='search_experiences'),
]
