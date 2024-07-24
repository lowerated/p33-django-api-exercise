# forms.py in your scheduler app

from django import forms

class ScheduleForm(forms.Form):
    pickup_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M:%S'],
        widget=forms.DateTimeInput(attrs={
            'placeholder': '2023-07-10T09:00:00',
            'class': 'form-control'
        }),
        initial='2023-07-10T09:00:00'
    )
    dropoff_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M:%S'],
        widget=forms.DateTimeInput(attrs={
            'placeholder': '2023-07-10T19:00:00',
            'class': 'form-control'
        }),
        initial='2023-07-10T19:00:00'
    )
    last_rest_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M:%S'],
        widget=forms.DateTimeInput(attrs={
            'placeholder': '2023-07-10T01:00:00',
            'class': 'form-control'
        }),
        initial='2023-07-10T01:00:00'
    )
