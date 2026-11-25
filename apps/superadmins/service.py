from django.db.models import QuerySet
from ..applications.models import Application, Category


class SuperAdmin:
    def view_all_application(self)->QuerySet[Application]:
        return Application.objects.all().order_by('-created_at')

    def update_status_on_a(self, application, comment)->bool:
        if application.status == 'n':
            application.status = 'a'
            application.admin_comment = comment
            application.save()
            return True
        return False

    def update_status_on_c(self, application, design_image)->bool:
        if application.status == 'n':
            application.status = 'c'
            application.design_image = design_image
            application.save()
            return True
        return False

    def get_all_categories(self)->QuerySet[Category]:
        return Category.objects.all().order_by('id')

    def add_category(self, name)->Category:
        return Category.objects.create(name=name)

    def delete_category(self, category):
        Category.objects.filter(id=category.id).delete()

