from django import forms


# Below Class can also be used.
"""
class FullStackDeveloperForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'style': 'padding: 10px; border-radius: 5px; border: 1px solid #ccc;'}))
    address = forms.CharField(label='Address', max_length=100, widget=forms.TextInput(attrs={'style': 'padding: 10px; border-radius: 5px; border: 1px solid #ccc;'}))
    resume = forms.FileField(label='Resume', widget=forms.ClearableFileInput(attrs={'style': 'padding: 10px; border-radius: 10px; border: 1px solid;'}))
    area = forms.ChoiceField(label='Area', choices=[('Mirpur', 'Mirpur'), ('Mohammadpur', 'Mohammadpur')], widget=forms.Select(attrs={'style': 'padding: 10px; border-radius: 5px; border: 1px solid #ccc;'}))

class DigitalMarketingManagerForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'style': 'padding: 10px; border-radius: 5px; border: 1px solid #ccc;'}))
    address = forms.CharField(label='Address', max_length=100, widget=forms.TextInput(attrs={'style': 'padding: 10px; border-radius: 5px; border: 1px solid #ccc;'}))
    resume = forms.FileField(label='Resume', widget=forms.ClearableFileInput(attrs={'style': 'padding: 10px; border-radius: 10px; border: 1px solid;'}))
    area = forms.ChoiceField(label='Area', choices=[('Mirpur', 'Mirpur'), ('Mohammadpur', 'Mohammadpur')], widget=forms.Select(attrs={'style': 'padding: 10px; border-radius: 5px; border: 1px solid #ccc;'}))
"""

from django import forms
from .models import FullStackDeveloper, DigitalMarketingManager


class FullStackDeveloperForm(forms.ModelForm):
    """
    Full Stack Developer Form:
    A form to capture the data from the job application for Full Stack Developer position.
    """
    class Meta:
        model = FullStackDeveloper
        fields = ['name', 'address', 'resume', 'area']


class DigitalMarketingManagerForm(forms.ModelForm):
    """
    Digital Marketing Manager Form:
    A form to capture the data from the job application for Digital Marketing Manager position.
    """
    class Meta:
        model = DigitalMarketingManager
        fields = ['name', 'address', 'resume', 'area']
