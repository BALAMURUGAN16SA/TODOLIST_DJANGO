from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('overview/', views.overview, name='overview'),
    path('create/', views.create, name='create'),
    path('add_and_edit/<int:listId>', views.add_and_edit, name='add_and_edit'),
    path('view/', views.view, name='view'),
]
