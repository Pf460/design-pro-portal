from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicationForm
from .models import Application
from .service import ApplicationViewFunction
from django.contrib.auth.decorators import login_required

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

@login_required
def create_application(request):
    service = ApplicationViewFunction()

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            service.create_application(form.cleaned_data, request.user)
            messages.success(request, 'Заявка успешно создана')
            return redirect('profile')
    else:
        form = ApplicationForm()
    return render(request, 'create_application.html', {'form': form})

@login_required
def delete_application_for_user(request, application_id):
    service = ApplicationViewFunction()
    application = get_object_or_404(Application, pk=application_id)

    if not service.delete_application_rule(application, request.user):
        messages.error(request, 'Вы не можете удалить эту заявку')
        return redirect('profile')
    if request.method == 'POST':
        application.delete()
        messages.success(request, 'Заявка успешно удалена')
        return redirect('profile')
    else:
        return render(request, 'delete_application.html')

@login_required
def view_applications(request):
    service = ApplicationViewFunction()

    applications = service.view_applications_for_user(request.user)
    status_filter = request.GET.get('status')
    if status_filter in ['n', 'a', 'c']:
        applications = applications.filter(status=status_filter)

    return render(
        request,
        'profile.html',
        context={
            'applications': applications,
        }
    )

@login_required
def application_detail(request, application_id):
    service = ApplicationViewFunction()

    app = service.find_application_for_user(application_id, request.user)

    return render(
        request,
        'application_detail.html',
        context={
            'application': app,
        }
    )
