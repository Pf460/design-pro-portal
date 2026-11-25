from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AcceptStatusForm, CompleteStatusForm, CategoryForm
from .service import SuperAdmin
from ..applications.models import Application, Category


def is_admin(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(is_admin, login_url='login')
def index(request):
    service = SuperAdmin()
    applications = service.view_all_application()

    status_filter = request.GET.get('status')
    if status_filter in ['n', 'a', 'c']:
        applications = applications.filter(status=status_filter)

    return render(
        request,
        'index_admin.html',
        {'applications': applications}
    )

@user_passes_test(is_admin, login_url='login')
def update_status_on_accept_is_processed(request, pk):
    service = SuperAdmin()
    application = get_object_or_404(Application, pk=pk)

    if request.method == 'POST':
        form = AcceptStatusForm(data=request.POST)

        if form.is_valid():
            comment = form.cleaned_data['comment']
            service.update_status_on_a(application, comment)
            messages.success(request, 'Вы успешно обновили статус на принято в работу')
            return redirect('index_admin')
    else:
        form = AcceptStatusForm()
    return render(
        request,
        'form_for_update_status_a.html',
        {'application': application, 'form': form}
    )

@user_passes_test(is_admin, login_url='login')
def update_status_on_completed(request, pk):
    service = SuperAdmin()
    application = get_object_or_404(Application, pk=pk)

    if request.method == 'POST':
        form = CompleteStatusForm(request.POST, request.FILES)

        if form.is_valid():
            design_image = form.cleaned_data['design_image']
            service.update_status_on_c(application, design_image)
            messages.success(request, 'Вы успешно обновили ')
            return redirect('index_admin')
    else:
        form = CompleteStatusForm()
    return render(
        request,
        'form_for_update_status_c.html',
        {'application': application, 'form': form}
    )

@user_passes_test(is_admin, login_url='login')
def list_categories(request):
    service = SuperAdmin()
    categories = service.get_all_categories()
    return render(
        request,
        'list_categories.html',
        {'categories': categories}
    )

@user_passes_test(is_admin, login_url='login')
def create_category(request):
    service = SuperAdmin()

    if request.method == 'POST':
        form = CategoryForm(data=request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            service.add_category(name)
            messages.success(request, f'Категория: {name} успешно добавлена!')
            return redirect('list_categories')
    else:
        form = CategoryForm()
    return render(
        request,
        'create_category.html',
        {'form': form}
    )

@user_passes_test(is_admin, login_url='login')
def destroy_category(request, pk):
    service = SuperAdmin()
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        service.delete_category(category)
        messages.success(request, f'Категория: {category} успешно удалена')
        return redirect('list_categories')
    else:
        return render(
            request,
            'destroy_category.html',
            {'category': category}
        )
