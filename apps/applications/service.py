from django.db.models import QuerySet

from .models import Application


class ApplicationViewFunction:
    def num_in_progress_applications(self)->int:
        return Application.objects.filter(status__exact='a').count()

    def completed_applications(self)->QuerySet[Application]:
        return Application.objects.filter(status__exact='c').order_by('-updated_at')[:4]

