from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
import requests
from xhtml2pdf import pisa

### library for template loading
from django.template.loader import get_template 
from django.template import Context 

from django.http import HttpResponse
from .models import CustomUser,PersonalInformation, Education, Project, Job, Reference, Language, Skill

##working with django forms
from .forms import CustomUserForm,LoginForm, RegisterForm, EducationForm, JobForm, SkillForm, ReferenceForm, LanguageForm,ProjectForm, PersonalInformationForm

## register
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Process the form data and save the user
            form.save()
            return redirect('resume:login_user')
            # Redirect to a success page or login page
            # For example: return redirect('resume:login_user')
    else:
        form = RegisterForm()

    return render(request, 'register.html',{'form':form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = CustomUser.objects.filter(username=username, password=password)
            user_id = user.values('id')
            if user.exists():
                user = user.first()
                request.session['user_id'] = user.id
                return redirect(reverse('resume:home'))
            else:
                return HttpResponse("Invalid Username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def logout_user(request):
    request.session.pop('user_id',None)
    return redirect(reverse('resume:login_user'))

### home function in general
# def home(request):
#     user_id = request.session.get('user_id')

#     if user_id:    
#         user = CustomUser.objects.filter(id = user_id).first()
#         context = {
#             'user':user,
#         }
#         return render(request,'index.html',context)
#     else:
#         return redirect(reverse('resume:login_user'))
    













### added upto here

# # Create your views here.
# def register_user(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         phone = request.POST['phone']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
        
#         if not(username and phone and password and confirm_password):
#             print("Please fill up the required details!!")
#         elif password != confirm_password:
#             print("Passwords didnt match!! Please try again.")
#         else:
#             CustomUser.objects.create(username = username, phone = phone, password = password)
#             # user = CustomUser(username = username, phone = phone, password = password)
#             # user.save()
#             return redirect(reverse('resume:login_user'))
#     return render(request,'register.html')

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         ## user filter with exists instead of get with DoesNotExists
#         user= CustomUser.objects.filter(username=username, password=password)
#         user_id = user.values('id')

#         if user.exists():
#             user = user.first()
#             request.session['user_id'] = user.id
#             return redirect(reverse('resume:indexpage'))       
#         else:
#             return HttpResponse("Invalid Username or password.")       
#     return render(request,'login.html')



# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             user = User.objects.get(username=username, password=password)
#         except User.DoesNotExist:
#             user = None

#         if user is not None:
#             return redirect(reverse('resume:indexpage'))
#         else:
#             return HttpResponse("Invalid Username or password.")

#     return render(request, 'login.html')


# def logout_user(request):
#     request.session.pop('user_id',None)
#     return redirect(reverse('resume:login_user'))

# def indexpage(request):
#     user_id = request.session.get('user_id')

#     if user_id:    
#         user = CustomUser.objects.filter(id = user_id).first()
#         context = {
#             'user':user,
#         }
#         return render(request,'index.html',context)
#     else:
#         return redirect(reverse('resume:login_user'))
    

# # View function for CustomUser (User Details)
# def user_details(request):
#     if request.method == 'POST':
#         form = CustomUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('user_details'))
#     else:
#         form = CustomUserForm()
#     users = CustomUser.objects.all()
#     context = {
#         'form': form,
#         'users': users,
#     }
#     return render(request, 'user_details.html', context)

#view function for general details

'''
## needs some logic for customization
def userdetails(request):
    print(77777777777777777,request.FILES.get('profile_picture'))
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.filter(id=user_id).first()
        if user:
            # user_details = user

            user_details,created= CustomUser.objects.get_or_create(id = user_id)
            form = CustomUserForm(instance=user_details)
            if request.method == 'POST':
                if 'Save' in request.POST:
                    form = CustomUserForm(request.POST, instance=user_details)
                    if form.is_valid():
                        form.save()
                        return redirect(reverse('resume:userdetails'))
 
                
            else:
                form = CustomUserForm(instance=user_details)
            context = {
                'form': form,
                'user_details':user_details,
            }
            return render(request, 'userdetails.html', context)
    else:
        return redirect(reverse('resume:login_user'))'''



def userdetails(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.filter(id=user_id).first()
        if user:
            user_details, created = CustomUser.objects.get_or_create(id=user_id)
            if request.method == 'POST':
                form = CustomUserForm(request.POST, request.FILES, instance=user_details)
                if form.is_valid():
                    form.save()
                    return redirect(reverse('resume:userdetails'))
                else:
                    print(form.errors)
            else:
                form = CustomUserForm(instance=user_details)
            context = {
                'form': form,
                'user_details': user_details,
            }
            return render(request, 'userdetails.html', context)
    else:
        return redirect(reverse('resume:login_user'))











        
# View function for Personal Information
def personalinformation(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.filter(id=user_id).first()
        if user:
            personal_info, created = PersonalInformation.objects.get_or_create(user=user)
            form = PersonalInformationForm(instance=personal_info)
            if request.method == 'POST':
                if 'Save' in request.POST:
                # Create or Update operation
                    form = PersonalInformationForm(request.POST, instance=personal_info)
                    if form.is_valid():
                        form.save()
                        return redirect(reverse('resume:personalinformation'))
                elif 'Delete' in request.POST:
                    personal_info.delete()
                    return redirect(reverse('resume:personalinformation'))
            else:
                form = PersonalInformationForm(instance=personal_info)
            context = {
                'form': form,
                'personal_info': personal_info,
            }
            return render(request, 'generalinformation.html', context)
        else:
            return HttpResponse("User not found.")
    else:
        return redirect(reverse('resume:login_user'))



### works well with adding and deleting information regarding education
def education(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.filter(id=user_id).first()
        if user:
            education_info = Education.objects.filter(user=user)
            if request.method == 'POST':
                if 'delete' in request.POST:
                    education_id = int(request.POST.get('delete'))
                    education = get_object_or_404(Education, id=education_id, user=user)
                    print(education_id,7777777)
                    education.delete()
                    return redirect(reverse('resume:education'))

                # For other form submissions (Add and Save), we'll handle form validation
                form = EducationForm(request.POST)
                if form.is_valid():
                    new_education = form.save(commit=False)
                    new_education.user = user
                    new_education.save()
                    return redirect(reverse('resume:education'))
            else:
                form = EducationForm(initial={'user': user})
                
            context = {
                'education_info': education_info,
                'form': form,
            }

            return render(request, 'education.html', context)
        else:
            return HttpResponse("User not found.")
    else:
        return redirect(reverse('resume:login_user'))
    


## adding and removing job 
def job(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.filter(id=user_id).first()
        if user:
            job_info = Job.objects.filter(user=user)
            if request.method == 'POST':
                if 'delete' in request.POST:
                    job_id = int(request.POST.get('delete'))
                    job = get_object_or_404(Job, id=job_id, user=user)
                    job.delete()
                    return redirect(reverse('resume:job'))

                # For other form submissions (Add and Save), we'll handle form validation
                form = JobForm(request.POST)
                if form.is_valid():
                    new_job = form.save(commit=False)
                    new_job.user = user
                    new_job.save()
                    return redirect(reverse('resume:job'))
            else:
                form = JobForm(initial={'user': user})
                
            context = {
                'job_info': job_info,
                'form': form,
            }

            return render(request, 'job.html', context)
        else:
            return HttpResponse("User not found.")
    else:
        return redirect(reverse('resume:login_user'))


## adding and removing project 
def project(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.filter(id=user_id).first()
        if user:
            project_info = Project.objects.filter(user=user)
            if request.method == 'POST':
                if 'delete' in request.POST:
                    project_id = int(request.POST.get('delete'))
                    project = get_object_or_404(Project, id=project_id, user=user)
                    project.delete()
                    return redirect(reverse('resume:project'))

                # For other form submissions (Add and Save), we'll handle form validation
                form = ProjectForm(request.POST)
                if form.is_valid():
                    new_project = form.save(commit=False)
                    new_project.user = user
                    new_project.save()
                    return redirect(reverse('resume:project'))
            else:
                form = ProjectForm(initial={'user': user})
                
            context = {
                'project_info': project_info,
                'form': form,
            }

            return render(request, 'project.html', context)
        else:
            return HttpResponse("User not found.")
    else:
        return redirect(reverse('resume:login_user'))
    

## adding and removing skill 
def skill(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.filter(id=user_id).first()
        if user:
            skill_info = Skill.objects.filter(user=user)
            if request.method == 'POST':
                if 'delete' in request.POST:
                    skill_id = int(request.POST.get('delete'))
                    skill = get_object_or_404(Skill, id=skill_id, user=user)
                    skill.delete()
                    return redirect(reverse('resume:skill'))

                # For other form submissions (Add and Save), we'll handle form validation
                form = SkillForm(request.POST)
                if form.is_valid():
                    new_skill = form.save(commit=False)
                    new_skill.user = user
                    new_skill.save()
                    return redirect(reverse('resume:skill'))
            else:
                form = SkillForm(initial={'user': user})
                
            context = {
                'skill_info': skill_info,
                'form': form,
            }

            return render(request, 'skill.html', context)
        else:
            return HttpResponse("User not found.")
    else:
        return redirect(reverse('resume:login_user'))



# adding and deleting languages
def language(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.filter(id=user_id).first()
        if user:
            language_info = Language.objects.filter(user=user)
            if request.method == 'POST':
                if 'delete' in request.POST:
                    language_id = int(request.POST.get('delete'))
                    language = get_object_or_404(Language, id=language_id, user=user)
                    language.delete()
                    return redirect(reverse('resume:language'))

                # For other form submissions (Add and Save), we'll handle form validation
                form = LanguageForm(request.POST)
                if form.is_valid():
                    new_language = form.save(commit=False)
                    new_language.user = user
                    new_language.save()
                    return redirect(reverse('resume:language'))
            else:
                form = LanguageForm(initial={'user': user})
                
            context = {
                'language_info': language_info,
                'form': form,
            }

            return render(request, 'language.html', context)
        else:
            return HttpResponse("User not found.")
    else:
        return redirect(reverse('resume:login_user'))
    
# adding and deleting references
def reference(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.filter(id=user_id).first()
        if user:
            reference_info = Reference.objects.filter(user=user)
            if request.method == 'POST':
                if 'delete' in request.POST:
                    reference_id = int(request.POST.get('delete'))
                    reference = Reference.objects.filter(id=reference_id, user = user)

                    
                    # reference = get_object_or_404(Reference, id=reference_id, user=user)
                    reference.delete()
                    return redirect(reverse('resume:reference'))

                # For other form submissions (Add and Save), we'll handle form validation
                form = ReferenceForm(request.POST)
                if form.is_valid():
                    new_reference = form.save(commit=False)
                    new_reference.user = user
                    new_reference.save()
                    return redirect(reverse('resume:reference'))
            else:
                form = ReferenceForm(initial={'user': user})
                
            context = {
                'reference_info': reference_info,
                'form': form,
            }

            return render(request, 'reference.html', context)
        else:
            return HttpResponse("User not found.")
    else:
        return redirect(reverse('resume:login_user'))


def displayinformation(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.filter(id=user_id).first()

        if user:
            user_details = user
            
            personal_info = user.informations.first()
            educations = user.educations.all()
            jobs = user.jobs.all()
            projects = user.projects.all()
            skills = user.skills.all()
            languages = user.languages.all()
            references = user.references.all()

            context = {
                'user': user,
                'user_details':user_details,
                'personal_info': personal_info,
                'educations': educations,
                'jobs': jobs,
                'projects': projects,
                'skills': skills,
                'languages': languages,
                'references': references,
            }

            return render(request, 'displayinformation.html', context)
        else:
            return HttpResponse("User not found.")
    else:
        return redirect(reverse('resume:login_user'))

  
def downloadinpdf(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.filter(id=user_id).first()
        user_details = user
        if user:
            
            user_details = user
            
            personal_info = user.informations.first()
            educations = user.educations.all()
            jobs = user.jobs.all()
            projects = user.projects.all()
            skills = user.skills.all()
            languages = user.languages.all()
            references = user.references.all()

            context = {
                'user': user,
                'user_details':user_details,
                'personal_info': personal_info,
                'educations': educations,
                'jobs': jobs,
                'projects': projects,
                'skills': skills,
                'languages': languages,
                'references': references,
            }
            template = get_template('displayinformation.html')
            html = template.render(context)


            pdf_file = '/home/aayulogic/Nabaraj/ResumeBuilder/resume/generatedpdf/file.pdf'
            with open(pdf_file,'wb') as f:
                pisa_status = pisa.CreatePDF(html, dest = f)


            if pisa_status.err:
                return HttpResponse('Failed to generate PDF.',status = 500)
            else:
                with open(pdf_file,'rb') as f:
                    response = HttpResponse(f.read(), content_type='application/pdf')
                    response['Content-Disposition'] = 'attachment; filename="CV.pdf"'

                    return response
        else:
            return HttpResponse("User profile not found.")
    else:
        return(redirect(reverse('resume:login_user')))
  

    
def home(request):
    user_id = request.session.get('user_id')
    if user_id:    
        user = CustomUser.objects.filter(id = user_id).first()
        if user:
            user_details = user           
            personal_info = user.informations.first()
            educations = user.educations.all()
            jobs = user.jobs.all()
            projects = user.projects.all()
            skills = user.skills.all()
            languages = user.languages.all()
            references = user.references.all()
            context = {
                'user': user,
                'user_details':user_details,
                'personal_info': personal_info,
                'educations': educations,
                'jobs': jobs,
                'projects': projects,
                'skills': skills,
                'languages': languages,
                'references': references,
            }
            sample = request.POST.get('sample')
            if sample == 'First Sample':
                template = get_template('firstsample.html')
                              
            elif sample == 'Second Sample':               
                template = get_template('secondsample.html')
                       
            elif sample == 'Third Sample':                
                template = get_template('thirdsample.html')
            
            else:
                return render(request,'index.html',context)

            html = template.render(context)
            pdf_file = '/home/aayulogic/Nabaraj/ResumeBuilder/resume/generatedpdf/file.pdf'
            with open(pdf_file,'wb') as f:
                pisa_status = pisa.CreatePDF(html, dest = f)
            if pisa_status.err:
                return HttpResponse('Failed to generate PDF.',status = 500)
            else:
                with open(pdf_file,'rb') as f:
                    response = HttpResponse(f.read(), content_type='application/pdf')
                    response['Content-Disposition'] = 'attachment; filename="Resume.pdf"'
                    return response           
        else:
            return HttpResponse("User not found.")      
    else:
        return redirect(reverse('resume:login_user'))



# #### passing with the dictionary of sample : template
# def home(request):
#     user_id = request.session.get('user_id')
#     if user_id:    
#         user = CustomUser.objects.filter(id=user_id).first()
#         if user:
#             user_details = user           
#             personal_info = user.informations.first()
#             educations = user.educations.all()
#             jobs = user.jobs.all()
#             projects = user.projects.all()
#             skills = user.skills.all()
#             languages = user.languages.all()
#             references = user.references.all()
#             context = {
#                 'user': user,
#                 'user_details': user_details,
#                 'personal_info': personal_info,
#                 'educations': educations,
#                 'jobs': jobs,
#                 'projects': projects,
#                 'skills': skills,
#                 'languages': languages,
#                 'references': references,
#             }

#             sample_templates = {
#                 'First Sample': 'firstsample.html',
#                 'Second Sample': 'secondsample.html',
#                 'Third Sample': 'thirdsample.html',
#             }

#             sample = request.POST.get('sample')
#             if sample in sample_templates:
#                 template_name = sample_templates[sample]
#                 template = get_template(template_name)
#                 html = template.render(context)
#                 pdf_file = '/home/aayulogic/Nabaraj/ResumeBuilder/resume/generatedpdf/file.pdf'
#                 with open(pdf_file, 'wb') as f:
#                     pisa_status = pisa.CreatePDF(html, dest=f)
#                 if pisa_status.err:
#                     return HttpResponse('Failed to generate PDF.', status=500)
#                 else:
#                     with open(pdf_file, 'rb') as f:
#                         response = HttpResponse(f.read(), content_type='application/pdf')
#                         response['Content-Disposition'] = 'attachment; filename="CV.pdf"'
#                         return response

#             return render(request, 'index.html', context)

#         else:
#             return HttpResponse("User not found.")      
#     else:
#         return redirect(reverse('resume:login_user'))

def under_20(request):
    from django.utils import timezone
    from datetime import timedelta
    
    from dateutil.relativedelta import relativedelta
    today = timezone.now().date()
    # user = CustomUser.objects.filter(age<=20)
    # age=relativedelta(today,self.date_of_birth).years
    # return age

    ## will return more accurate data working with age
    point_twenty_ago = today - timedelta(days=365*20)
    # point_twenty_ago = today - relativedelta(years=20)

    age_with_user = CustomUser.objects.filter(date_of_birth__gt=point_twenty_ago)
    context = {
        'age_with_user':age_with_user,
        'point_twenty_ago':point_twenty_ago,
        
    }
    return render(request,'under20.html',context)

    
    
'''def language_address_filter(request):
    x = Reference.objects.filter(user__address="Balaju").values()
    name = []
    for i in x:
        each = i['user__username']
        name.append(each)
    return HttpResponse(name)
    # y = x.filter(user__languages__language='English').values()
    # data = f"{x}\n\n\n111\n\n{y}"
    # context = {
    #     'data':data,
    # }'''

def language_address_filter(request):
    x = Reference.objects.filter(user__address="Balaju", reference = "Tek").values()
        

    return HttpResponse(x)

