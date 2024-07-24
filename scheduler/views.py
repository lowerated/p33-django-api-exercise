from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from django.http import JsonResponse
from datetime import datetime
from .utils import plan_optimal_schedule

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Django HOS Scheduler API Project! Visit /scheduler/ to access the API endpoints.")

def schedule_optimization(request):
    pickup_time = datetime.strptime(request.GET.get('pickup_time'), '%Y-%m-%dT%H:%M:%S')
    dropoff_time = datetime.strptime(request.GET.get('dropoff_time'), '%Y-%m-%dT%H:%M:%S')
    valid, message = plan_optimal_schedule(pickup_time, dropoff_time)
    return JsonResponse({'valid': valid, 'message': message})


from django.http import JsonResponse
from .utils import plan_optimal_schedule, get_access_token, detect_hos_violations

from django.http import JsonResponse, HttpResponseBadRequest
from datetime import datetime
from .utils import plan_optimal_schedule

def schedule_view(request):
    try:
        pickup_time = request.GET.get('pickup_time')
        dropoff_time = request.GET.get('dropoff_time')
        last_rest_time = request.GET.get('last_rest_time')

        if not all([pickup_time, dropoff_time, last_rest_time]):
            return HttpResponseBadRequest("Missing required datetime parameters.")

        pickup_time = datetime.strptime(pickup_time, '%Y-%m-%dT%H:%M:%S')
        dropoff_time = datetime.strptime(dropoff_time, '%Y-%m-%dT%H:%M:%S')
        last_rest_time = datetime.strptime(last_rest_time, '%Y-%m-%dT%H:%M:%S')
        
        valid, message = plan_optimal_schedule(pickup_time, dropoff_time, last_rest_time)
        return JsonResponse({'valid': valid, 'message': message})
    except ValueError as e:
        return HttpResponseBadRequest(f"Invalid datetime format: {str(e)}")


def hos_violation_view(request):
    driving_time = float(request.GET.get('driving_time'))
    hours_since_last_rest = float(request.GET.get('hours_since_last_rest'))
    
    valid, messages = detect_hos_violations(driving_time, hours_since_last_rest)
    return JsonResponse({'valid': valid, 'messages': messages})


def validate_datetime(date_text):
    try:
        return datetime.strptime(date_text, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        return None


# views.py

from django.shortcuts import render
from .forms import ScheduleForm

def schedule_form(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            pickup_time = form.cleaned_data['pickup_time']
            dropoff_time = form.cleaned_data['dropoff_time']
            last_rest_time = form.cleaned_data['last_rest_time']
            valid, message = plan_optimal_schedule(pickup_time, dropoff_time, last_rest_time)
            return JsonResponse({'valid': valid, 'message': message})
    else:
        form = ScheduleForm()
    return render(request, 'scheduler/schedule_form.html', {'form': form})
