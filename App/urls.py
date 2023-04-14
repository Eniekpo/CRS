from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('civilservants/', views.civilservants, name='civilservants'),
    path('criteria/', views.criteria, name='criteria'),
    path('reports/', views.reports, name='reports'),
    path('output/', views.output, name='output'),
]
