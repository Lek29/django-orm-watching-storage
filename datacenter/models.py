from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(visit):
    start_time = timezone.localtime(visit.entered_at)
    if visit.leaved_at:
        finish_time = timezone.localtime(visit.leaved_at)
    else:
        finish_time = timezone.localtime(timezone.now())
    return finish_time - start_time


def format_duration(duration):
    total_second = duration.total_seconds()
    number_seconds_in_hour = 3600
    number_seconds_in_minute = 60
    hours = int(total_second // number_seconds_in_hour)
    minutes = int((total_second % number_seconds_in_hour) // number_seconds_in_minute)
    seconds = int(total_second % number_seconds_in_minute)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def is_visit_long(visit, minutes=60):
    number_second_in_minute = 60
    duration = get_duration(visit)
    return duration.total_seconds() > minutes * number_second_in_minute
