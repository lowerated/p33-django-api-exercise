from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from datetime import datetime

class ScheduleOptimizationTests(TestCase):
    def test_schedule_within_limits(self):
        """Schedule should be within HOS limits, clearly within a single workday."""
        response = self.client.get(reverse('schedule_view'), {
            'pickup_time': '2023-07-01T09:00:00',
            'dropoff_time': '2023-07-01T18:00:00',  # 9 hours later
            'last_rest_time': '2023-07-01T01:00:00'  # 8 hours before pickup
        })
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'valid': True, 'message': 'Schedule within HOS regulations.'}
        )



class HOSViolationTests(TestCase):
    def test_hos_violations(self):
        """Test if HOS violations are detected for the 14-hour rule."""
        response = self.client.get(reverse('hos_violation_view'), {
            'driving_time': '10',  # Within the 11-hour driving limit
            'hours_since_last_rest': '5'  # Total time will not exceed 14 hours
        })
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'valid': True, 'messages': []}
        )

