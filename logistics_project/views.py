# logistics_project/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Django HOS Scheduler API Project! Visit /scheduler/ to access the API endpoints.")
