from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from register.forms import UpdateForm
from django.contrib.auth import logout as lt
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from main.models import Author
from django.utils.text import slugify



#usernames = [user.username for user in User.objects.all()]

def signup(request):
    context = {}
    form = CustomUserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active = False  # Email verification
            new_user.save()
            # Generate a unique slug
            slug = generate_unique_slug(new_user.username)
            # Only create ONE Author object!
            Author.objects.create(
                user=new_user,
                fullname=new_user.username,
                slug=slug,
                profile_pic='authors/default_pfp.png'
            )
            # SEND ACTIVATION EMAIL
            from django.utils.http import urlsafe_base64_encode
            from django.utils.encoding import force_bytes
            from django.contrib.auth.tokens import default_token_generator
            from django.contrib.sites.shortcuts import get_current_site

            current_site = get_current_site(request)
            subject = "Activate Your Account"
            uid = urlsafe_base64_encode(force_bytes(new_user.pk))
            token = default_token_generator.make_token(new_user)
            activation_link = f"http://{current_site.domain}/account/activate/{uid}/{token}/"

            message = f"Hi {new_user.username},\nPlease click the link below to activate your account:\n{activation_link}"

            send_mail(
                subject,
                message,
                'noreply@yourforum.com',
                [new_user.email],
                fail_silently=False,
            )

            messages.info(request, "Please check your email to activate your account.")
            return redirect("signin")
    context.update({
        "form": form,
        "title": "Signup",
    })
    return render(request, "register/signup.html", context)


def generate_unique_slug(username):
    base_slug = slugify(username)
    slug = base_slug
    counter = 1
    while Author.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    return slug

def signin(request):
    context = {}
    form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=user, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    context.update({
        "form": form,
        "title": "Signin",
    })
    return render(request, "register/signin.html", context)

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        if not Author.objects.filter(user=user).exists():
            Author.objects.create(user=user, fullname=user.username)
        messages.success(request, "Your account has been activated! Please sign in.")
        return redirect("signin")
    else:
        messages.error(request, "Activation link is invalid!")
        return redirect("signup")

@login_required
def update_profile(request):
    context = {}
    user = request.user 
    form = UpdateForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            update_profile = form.save(commit=False)
            update_profile.user = user
            update_profile.save()
            return redirect("home")

    context.update({
        "form": form,
        "title": "Update Profile",
    })
    return render(request, "register/update.html", context)

@login_required
def logout(request):
    lt(request)
    return redirect("home")