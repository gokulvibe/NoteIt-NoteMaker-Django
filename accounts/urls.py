from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='home'),
    path('register/',views.register, name='register'),
    path('notes',views.notes, name='notes'),
    path('logout',views.logout,name='logout'),
    path('login', views.login, name='login'),
    #path('notes2', views.index, name='home'),
    
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    
    #For password reset:
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html", html_email_template_name='accounts/password_reset_email.html'),name="reset_password"),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),name="password_reset_done"),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"),name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"),name="password_reset_complete"),
]