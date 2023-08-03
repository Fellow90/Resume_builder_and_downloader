from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
import requests


from xhtml2pdf import pisa

### library for template loading
from django.template.loader import get_template 
from django.template import Context 

from django.http import HttpResponse
from .models import CustomUser,PersonalInformation, Education, Project, Job, Reference, Language, Skill

## added from here
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
            print(1111111111111111)
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = CustomUser.objects.filter(username=username, password=password)
            user_id = user.values('id')
            if user.exists():
                user = user.first()
                request.session['user_id'] = user.id
                return redirect(reverse('resume:indexpage'))
            else:
                return HttpResponse("Invalid Username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def logout_user(request):
    request.session.pop('user_id',None)
    return redirect(reverse('resume:login_user'))

def indexpage(request):
    user_id = request.session.get('user_id')

    if user_id:    
        user = CustomUser.objects.filter(id = user_id).first()
        context = {
            'user':user,
        }
        return render(request,'index.html',context)
    else:
        return redirect(reverse('resume:login_user'))
    











# def personalinformation(request):
#     user_id = request.session.get('user_id')
#     if user_id:
#         user = CustomUser.objects.filter(id=user_id).first()

#         if user:
#             personal_info, created = PersonalInformation.objects.get_or_create(user = user)
#             if request.method == 'POST':         
#                 form = PersonalInformationForm(request.POST, instance=personal_info)
#                 if form.is_valid():
#                     form.save()
#                     return redirect(reverse('resume:personalinformation'))
#             else:
#                 form = PersonalInformationForm(instance=personal_info)
#             context = {
#                 'user': user,
#                 'form': form,
#             }
#             return render(request, 'personalinformation.html', context)
#         else:
#             return HttpResponse("User not found.")
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
    



### this will work for accessing information but we cant edit and update
# def personalinformation(request):
#     user_id = request.session.get('user_id')
#     if user_id:
#         user = CustomUser.objects.filter(id=user_id).first()

#         if user:
            
#             personal_info = user.informations.first()
#             educations = user.educations.all()
#             jobs = user.jobs.all()
#             projects = user.projects.all()
#             skills = user.skills.all()
#             languages = user.languages.all()
#             references = user.references.all()

#             context = {
#                 'user': user,
#                 'personal_info': personal_info,
#                 'educations': educations,
#                 'jobs': jobs,
#                 'projects': projects,
#                 'skills': skills,
#                 'languages': languages,
#                 'references': references,
#             }

#             return render(request, 'generalinformation.html', context)
#         else:
#             return HttpResponse("User not found.")
#     else:
#         return redirect(reverse('resume:login_user'))

# def personalinformation(request):
#     user_id = request.session.get('user_id')
#     if user_id:
#         user = CustomUser.objects.filter(id=user_id).first()

#         if user:
#             personal_info, created =  PersonalInformation.objects.get_or_create(user=user)
#             if request.method == 'POST':
#                 form = PersonalInformationForm(request.POST, instance=personal_info)
#                 if form.is_valid():
#                     form.save()
#                     return redirect(reverse('resume:personalinformation'))
#             else:
#                 form = PersonalInformationForm(instance=personal_info)
#             personal_info = user.informations.first()
#             context = {
#                 'user': user,
#                 'form': form,
#                 'personal_info':personal_info,
#             }
#             return render(request, 'generalinformation.html', context)
#         else:
#             return HttpResponse("User not found.")
#     else:
#         return redirect(reverse('resume:login_user'))








'''
            # personal_info = user.informations.first()
            educations = user.educations.all()
            jobs = user.jobs.all()
            projects = user.projects.all()
            skills = user.skills.all()
            languages = user.languages.all()
            references = user.references.all()

            context = {
                'user': user,
                'personal_info': personal_info,
                'educations': educations,
                'jobs': jobs,
                'projects': projects,
                'skills': skills,
                'languages': languages,
                'references': references,
            }

            return render(request, 'generalinformation.html', context)
        else:
            return HttpResponse("User not found.")
    else:
        return redirect(reverse('resume:login_user'))
'''






# def personalinformation(request):
#     user_id = request.session.get('user_id')
#     if user_id:
#         user = CustomUser.objects.filter(id=user_id).first()

#         if user:
#             personal_info, created = PersonalInformation.objects.get_or_create(user=user)

#             if request.method == 'POST':
#                 # Create or Update operation
#                 form = PersonalInformationForm(request.POST, instance=personal_info)
#                 if form.is_valid():
#                     form.save()
#                     return redirect(reverse('resume:personalinformation'))
#             else:
#                 # Read operation (displaying the form)
#                 form = PersonalInformationForm(instance=personal_info)

#             if 'delete' in request.POST:
#                 # Delete operation
#                 personal_info.delete()
#                 return redirect(reverse('resume:personalinformation'))

#             context = {
#                 'user': user,
#                 'form': form,
#                 'personal_info': personal_info,
#             }
#             return render(request, 'generalinformation.html', context)
#         else:
#             return HttpResponse("User not found.")
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
def userdetails(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.filter(id=user_id).first()
        if user:
            # user_details = user
            user_details,created= CustomUser.objects.get_or_create(id = user_id)
            form = CustomUserForm(instance=user_details)
            if request.method == 'POST':
                # Create or Update operation
                form = CustomUserForm(request.POST, instance=user_details)
                if form.is_valid():
                    form.save()
                    return redirect(reverse('resume:userdetails'))
                else:
                # Read operation (displaying the form)
                    form = CustomUserForm(instance=user_details)

            if 'Delete' in request.POST:
                # Delete operation
                user_details.delete()
                return redirect(reverse('resume:userdetails'))
            context = {
                'form': form,
                'user_details':user_details,
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
            if request.method == 'POST':
                # Create or Update operation
                form = PersonalInformationForm(request.POST, instance=personal_info)
                if form.is_valid():
                    form.save()
                    return redirect(reverse('resume:personalinformation'))
            else:
                # Read operation (displaying the form)
                form = PersonalInformationForm(instance=personal_info)
            if 'Delete' in request.POST:
                # Delete operation
                personal_info.delete()
                return redirect(reverse('resume:personalinformation'))
            context = {
                'form': form,
                'personal_info': personal_info,
            }
            return render(request, 'generalinformation.html', context)
        else:
            return HttpResponse("User not found.")
    else:
        return redirect(reverse('resume:login_user'))
        


# View function for Education
def education(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.filter(id=user_id).first()

        if user:
            education_info = Education.objects.filter(user = user).first()
            form = EducationForm(instance=education_info)
            if request.method == 'POST':
                # education_info , _ = Education.objects.get_or_create(user = user, title = request.POST.title )
                education_info , _ = Education.objects.get_or_create(user = user)

                form = EducationForm(request.POST, instance=education_info)
                if form.is_valid():
                    form.save()
                    return redirect(reverse('resume:education'))
                else:
                    form = EducationForm(instance=education_info)
                form = EducationForm(request.POST, instance=education_info)
                context = {
                    'user': user,
                    'education_info': education_info,
                    'form':form,
                }
                return render(request, 'education.html', context)
    else:
        return redirect(reverse('resume:login_user'))
# View function for Job
def job(request):
    user_id = request.session.get('user_id')
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = user
            job.save()
            return redirect(reverse('job', args=[user_id]))
    else:
        form = JobForm()
    jobs = user.jobs.all()
    context = {
        'user': user,
        'form': form,
        'jobs': jobs,
    }
    return render(request, 'job.html', context)

# View function for Project
def project(request):
    user_id = request.session.get('user_id')
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = user
            project.save()
            return redirect(reverse('project', args=[user_id]))
    else:
        form = ProjectForm()
    projects = user.projects.all()
    context = {
        'user': user,
        'form': form,
        'projects': projects,
    }
    return render(request, 'project.html', context)

# View function for Skill
def skill(request):
    user_id = request.session.get('user_id')
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = user
            skill.save()
            return redirect(reverse('skill', args=[user_id]))
    else:
        form = SkillForm()
    skills = user.skills.all()
    context = {
        'user': user,
        'form': form,
        'skills': skills,
    }
    return render(request, 'skill.html', context)

# View function for Language
def language(request):
    user_id = request.session.get('user_id')
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            language = form.save(commit=False)
            language.user = user
            language.save()
            return redirect(reverse('language', args=[user_id]))
    else:
        form = LanguageForm()
    languages = user.languages.all()
    context = {
        'user': user,
        'form': form,
        'languages': languages,
    }
    return render(request, 'language.html', context)

# View function for Reference
def reference(request):
    user_id = request.session.get('user_id')
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = ReferenceForm(request.POST)
        if form.is_valid():
            reference = form.save(commit=False)
            reference.user = user
            reference.save()
            return redirect(reverse('reference', args=[user_id]))
    else:
        form = ReferenceForm()
    references = user.references.all()
    context = {
        'user': user,
        'form': form,
        'references': references,
    }
    return render(request, 'reference.html', context)


def displayinformation(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.filter(id=user_id).first()

        if user:
            user_details = user
            # import ipdb;ipdb.set_trace()
            
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
            context = {
                'user':user,
                'user_details':user_details,
                
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
                    response['Content-Disposition'] = 'attachment; filename="user_details.pdf"'

                    # response = HttpResponse(f.read() )
                    return response
        else:
            return HttpResponse("User profile not found.")
    else:
        return(redirect(reverse('resume:login_user')))

    