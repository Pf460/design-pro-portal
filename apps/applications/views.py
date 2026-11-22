from django.shortcuts import render
from .service import ApplicationViewFunction

def index(request):
    service = ApplicationViewFunction()

    return render(
        request,
        'index.html',
        context={
            'completed': service.completed_applications(),
            'num_in_progress_applications': service.num_in_progress_applications()
        }
    )
