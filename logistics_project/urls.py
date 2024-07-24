# logistics_project/urls.py
from django.urls import include, path
from . import views  # Adjust this import as needed

urlpatterns = [
    path('', views.home, name='home'),
    path('scheduler/', include('scheduler.urls')),  # Note the trailing slash
]
