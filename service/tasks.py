from datetime import datetime, time, timedelta

from django.core.exceptions import ValidationError


def validate_past_or_today(value):
    if value > datetime.now().date():
        raise ValidationError("Дата не може бути у майбутньому.")

def validate_past_or_current_time(value):
    current_time = datetime.now().time()
    value_str = value.strftime('%H:%M:%S')
    value_time = (datetime.strptime(value_str, '%H:%M:%S') + timedelta(hours=3)).time()
    print(value_str)
    print(value_time)

    if value_time > current_time:
        raise ValidationError("Час не може бути у майбутньому.")

