# checklists/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('checklists/', views.pagina_checklists, name='pagina_checklists'),
    path('workbooks/', views.pagina_workbooks, name='pagina_workbooks'),
    path('planners/', views.pagina_planners, name='pagina_planners'),
]
