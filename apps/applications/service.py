from django.db.models import QuerySet
from django.http import request
from django.shortcuts import get_object_or_404

from .forms import ApplicationForm
from .models import Application


class ApplicationViewFunction:
    def num_in_progress_applications(self)->int:
        return Application.objects.filter(status__exact='a').count()

    def completed_applications(self)->QuerySet[Application]:
        return Application.objects.filter(status__exact='c').order_by('-updated_at')[:4]

    @staticmethod
    def create_application(validated_data, author)->Application:
        return Application.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            category=validated_data['category'],
            photo=validated_data['photo'],
            author=author
        )

    @staticmethod
    def delete_application_rule(application, user)->bool:
        if application.author != user:
            return False
        if application.status != 'n':
            return False
        else:
            return True

    def view_applications_for_user(self, user)->QuerySet[Application]:
        return Application.objects.filter(author=user).order_by('-created_at')

    def find_application_for_user(self ,application_id, user)->Application:
        return get_object_or_404(Application ,id=application_id, author=user)
