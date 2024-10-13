from django.db import models
from django.utils import timezone


SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


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
    hours = int(total_second // SECONDS_IN_HOUR)
    minutes = int(
        (total_second % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
    )
    seconds = int(total_second % SECONDS_IN_MINUTE)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration.total_seconds() > minutes * SECONDS_IN_MINUTE
