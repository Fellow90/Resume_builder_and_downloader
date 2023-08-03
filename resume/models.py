from django.db import models
from .enums import GENDER_CHOICES, EDUCATION_DEGREE

# Create your models here.

class CustomUser(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES, default='M')
    phone = models.IntegerField(unique = True)
    date_of_birth = models.DateField("Enter date of birth: ",null= True, blank=True )
    email = models.EmailField("Please enter unique email: ")
    profile_picture = models.ImageField(null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.username}"
   
    
class PersonalInformation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='informations')
    # url to profile
    linkedin = models.URLField()
    github = models.URLField()
    #resume objective
    summary = models.TextField()

class Education(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='educations')
    title = models.CharField(choices=EDUCATION_DEGREE, max_length=8)
    faculty = models.CharField(max_length=50)
    institution_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    score =models.FloatField()

class Job(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='jobs')
    title = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    startdate = models.DateField()
    enddate = models.DateField()

class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name="projects")
    title = models.CharField(max_length=50)
    description = models.TextField()

class Skill(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="skills")
    skill = models.CharField(max_length=25)

class Language(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="languages")
    language = models.CharField(max_length=20)

class Reference(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="references")
    reference = models.CharField(max_length=100)






