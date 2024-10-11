from datacenter.models import Visit
from django.shortcuts import render
from .models import get_duration, format_duration, is_visit_long

def storage_information_view(request):
    peopls_in_bank = Visit.objects.filter(leaved_at__isnull=True)

    new_non_closed_visits = []

    for visit in peopls_in_bank:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)
        is_strange = is_visit_long(visit)
        new_non_closed_visits.append(
            {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at.strftime('%d-%m-%Y %H:%M:%S'),
            'duration': formatted_duration,
            'is_strange': is_strange
        }
        )


    context = {
        'non_closed_visits': new_non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)


