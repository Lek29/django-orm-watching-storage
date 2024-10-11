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
    finish_time = timezone.localtime(visit.leaved_at)
    return finish_time - start_time


def format_duration(duration):
    total_second = duration.total_seconds()
    hours = int(total_second // 3600)
    minutes = int((total_second % 3600) // 60)
    seconds = int(total_second % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def is_visit_long(visit, minutes=60):
    if visit.leaved_at is None:
        finish_time = timezone.now()
    else:
        finish_time = visit.leaved_at
    duration = finish_time - visit.entered_at
    return duration.total_seconds() > minutes * 60
