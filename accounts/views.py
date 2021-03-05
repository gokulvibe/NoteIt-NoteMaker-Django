from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    else:
        if request.method=="POST":
            email=request.POST["email"]
            password=request.POST["password"]
            user=auth.authenticate(username=email,password=password)
            try:
                userObject = User.objects.get(email=email)
            except User.DoesNotExist:
                userObject = None
            
            if user is not None:
                auth.login(request,user)
                return redirect("notes")
            
            else:
                if userObject is not None and userObject.is_active == False:
                    messages.info(request,"Your account hasn't been activated yet. Please check your Email for the activation link.")
                else:
                    messages.info(request,"Invalid Credentials")
                return redirect('login')
        else:
            return render(request,'accounts/login.html')
        
        
def index(request):
    # if request.user.is_authenticated:
    #     return render(request,"accounts/notes.html")
        
    # else:
    #     return redirect('/login')
    
    return render(request,"accounts/notes.html")
        

def register(request):
    if request.method=='POST':
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password=request.POST["password"]
        password2=request.POST["password2"]
        
        if password==password2:
            if User.objects.filter(username=email).exists():
                messages.info(request,'Account with the given email already exists, please try to login instead.')
                return redirect('register')
            else:
                user=User.objects.create_user(email=email,username=email,password=password,first_name=first_name,last_name=last_name)
                user.save()
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your blog account.'
                message = render_to_string('accounts/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
                })
                email = EmailMessage(
                        mail_subject, message, to=[email]
                        )
                email.content_subtype = 'html'
                email.send()
                messages.info(request,'Verification Link has been sent to you given E-mail id, click the link to activate your account.')
                return redirect('login')
        else:
            messages.info(request,'Passwords do not match')
            return redirect('register')
        
    else:
        return render(request, 'accounts/register.html')
        
    
    
def notes(request):
    return render(request, 'accounts/notes.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        #login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
    
    

