from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('searchtitle/', views.searchbytitle,name='searchtitle'),
    path('searchdate/', views.searchbydate,name='searchdate'),
 
]
