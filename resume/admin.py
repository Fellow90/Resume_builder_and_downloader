from django.contrib import admin
from .models import CustomUser, PersonalInformation, Education, Project, Skill,Job, Language, Reference
# Register your models here.
admin.site.register([CustomUser, PersonalInformation, Education, Project,Skill,Job, Language, Reference])