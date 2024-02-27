from django import forms
from django.core.exceptions import ValidationError


class PropertyForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        property = cleaned_data.get("property")
        value = cleaned_data.get("value")
        print(property)
        print(value)
        if property.name == 'Сезонность' and value not in ['Зимние', 'зимние', 'летние', 'Летние']:
            raise ValidationError("Сезонность должна быть либо 'Зимние', либо 'Летние'")
        return cleaned_data
