from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('civilservants/', views.civilservants, name='civilservants'),
    path('criteria/', views.criteria, name='criteria'),
    path('csdetails/', views.csdetails, name='csdetails'),
    path('reports/', views.reports, name='reports'),
]
