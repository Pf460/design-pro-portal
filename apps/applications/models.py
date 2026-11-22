from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Application(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='applications_images/')
    APPLICATION_STATUS = (
        ('n', 'Новая'),
        ('a', 'Принято в работу'),
        ('c', 'Выполнено'),
    )
    status = models.CharField(max_length=1, choices=APPLICATION_STATUS, default='n')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    admin_comment = models.TextField(max_length=500, blank=True, null=True)
    design_image = models.ImageField(upload_to='applications_design/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('application_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

