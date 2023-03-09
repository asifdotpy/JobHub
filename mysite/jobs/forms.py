from django import forms
from .models import FullStackDeveloper, DigitalMarketingManager, SeniorBackendEngineer, AIMLEngineer, GameDeveloper, MobileAppDeveloper




# Added work_types
WORK_TYPES = [    ('on-site', 'On-Site'),    ('remote', 'Remote'),]


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


class FullStackDeveloperForm(forms.ModelForm):
    """
    Full Stack Developer Form:
    A form to capture the data from the job application for Full Stack Developer position.
    """
    email = forms.CharField(widget=forms.EmailInput)
    phone_number = forms.CharField(max_length=20)
    cover_letter = forms.CharField(widget=forms.Textarea)
    work_type = forms.ChoiceField(choices=WORK_TYPES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = FullStackDeveloper
        fields = ['name', 'email', 'address',
                  'resume', 'phone_number', 'cover_letter', 'work_type']


class DigitalMarketingManagerForm(forms.ModelForm):
    """
    Digital Marketing Manager Form:
    A form to capture the data from the job application for Digital Marketing Manager position.
    """
    email = forms.CharField(widget=forms.EmailInput)
    phone_number = forms.CharField(max_length=20)
    cover_letter = forms.CharField(widget=forms.Textarea)
    work_type = forms.ChoiceField(choices=WORK_TYPES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = DigitalMarketingManager
        fields = ['name', 'email', 'address',
                  'resume', 'phone_number', 'cover_letter', 'work_type']


class SeniorBackendEngineerForm(forms.ModelForm):
    """
    Senior Backend Engineer Form:
    A form to capture the data from the job application for Senior Backend Engineer position.
    """
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    cover_letter = forms.CharField(widget=forms.Textarea)
    work_type = forms.ChoiceField(choices=WORK_TYPES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = SeniorBackendEngineer
        fields = ['name', 'email', 'address',
                  'resume', 'phone_number', 'cover_letter', 'work_type']


class AIMLEngineerForm(forms.ModelForm):
    """
    AI/ML Engineer Form:
    A form to capture the data from the job application for AI/ML Engineer position.
    """
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    cover_letter = forms.CharField(widget=forms.Textarea)
    work_type = forms.ChoiceField(choices=WORK_TYPES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = AIMLEngineer
        fields = ['name', 'email', 'address',
                  'resume', 'phone_number', 'cover_letter', 'work_type']


class GameDeveloperForm(forms.ModelForm):
    """
    Game Developer Form:
    A form to capture the data from the job application for Game Developer position.
    """
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    cover_letter = forms.CharField(widget=forms.Textarea)
    work_type = forms.ChoiceField(choices=WORK_TYPES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = GameDeveloper
        fields = ['name', 'email', 'address',
                  'resume', 'phone_number', 'cover_letter', 'work_type']



class MobileAppDeveloperForm(forms.ModelForm):
    """
    Mobile App Developer Form:
    A form to capture the data from the job application for Mobile App Developer position.
    """
    email = forms.CharField(widget=forms.EmailInput)
    phone_number = forms.CharField(max_length=20)
    cover_letter = forms.CharField(widget=forms.Textarea)
    work_type = forms.ChoiceField(choices=WORK_TYPES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = MobileAppDeveloper
        fields = ['name', 'email', 'address', 'resume', 'phone_number', 'cover_letter', 'work_type']
