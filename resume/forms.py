from django import forms
from .models import CustomUser, PersonalInformation, Education, Job, Project, Skill, Language, Reference


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        # password = forms.CharField(widget=forms.PasswordInput)
        # confirm_password = forms.CharField(widget=forms.PasswordInput)
        # widgets = {
        #    'password': forms.PasswordInput(),
        #    'confirm_password': forms.PasswordInput(),
        # }

        fields = ['full_name','address','gender','phone','date_of_birth','email','profile_picture']

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        password = forms.CharField(widget=forms.PasswordInput)
        confirm_password = forms.CharField(widget=forms.PasswordInput)

        fields =['username','phone','password','confirm_password']



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = ['linkedin','github','summary']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = '__all__'

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = '__all__'
