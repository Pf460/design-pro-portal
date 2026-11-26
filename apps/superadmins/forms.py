from django import forms
from ..applications.models import Category


class AcceptStatusForm(forms.Form):
    comment = forms.CharField(
        label="Комментарий к заявке",
        max_length=500,
        required=True,
        error_messages={'required': 'Комментарий обязателен для этого статуса!'}
    )

class CompleteStatusForm(forms.Form):
    design_image = forms.ImageField(
        label="Фото готового дизайна",
        required=True,
        error_messages={'required': 'Необходимо загрузить картинку дизайна!'}
    )

    def clean_design_image(self):
        design_image = self.cleaned_data.get('design_image')
        if design_image:
            if design_image.size > 2 * 1024 * 1024:
                raise forms.ValidationError("Файл не должен превышать 2 МБ.")

            ext = design_image.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png', 'bmp']:
                raise forms.ValidationError("Допустимые форматы: jpg, jpeg, png, bmp.")
        return design_image

class CategoryForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Название новой категории",
        required=True
    )
