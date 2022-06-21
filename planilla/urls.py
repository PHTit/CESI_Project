from django.urls import path

from planilla import views


app_name='planilla'
urlpatterns = [
    path('planilla', views.planilla, name='planilla')

]
