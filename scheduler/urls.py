# scheduler/urls.py
from django.urls import path
from . import views
from .views import schedule_form

urlpatterns = [
    path('optimize/', views.schedule_view, name='schedule_view'),
    path('hos_violation/', views.hos_violation_view, name='hos_violation_view'),
    path('form/', schedule_form, name='schedule_form'),
]

