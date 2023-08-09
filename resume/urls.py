from django.urls import path
from . import views
app_name = 'resume'

urlpatterns = [
    path('home/', views.home,name="home"),
    path('register/', views.register_user, name = 'register_user'),
    path('login/', views.login_user, name = 'login_user'),
    path('logout/',views.logout_user, name = 'logout_user'),
    path('userdetails/',views.userdetails, name = 'userdetails'),
    path('personalinformation/',views.personalinformation, name = 'personalinformation'),
    path('education/',views.education, name = 'education'),
    path('job/',views.job, name = 'job'),
    path('project/',views.project, name = 'project'),
    path('skill/',views.skill, name = 'skill'),
    path('language/',views.language, name = 'language'),
    path('reference/',views.reference, name = 'reference'),
    path('displayinformation/',views.displayinformation,name='displayinformation'),
    path('downloadinpdf/',views.downloadinpdf,name='downloadinpdf'),
    path('under_20/',views.under_20,name='under_20'),
    path('language_address_filter/',views.language_address_filter,name='language_address_filter'),





    


]