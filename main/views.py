from django.contrib import messages
from django.shortcuts import render, redirect
from .utils import Convert
from django.http import FileResponse, JsonResponse, HttpResponse
from django.contrib.auth.models import auth
from .models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if request.method == "POST":
        img_type  = request.POST["image_type"]
        image  = request.FILES["image"]
        if len(request.FILES.getlist('image')) == 1:
            mutate = Convert(request.FILES.getlist('image'), img_type)
            file = mutate.convert()
            filename = image.name.split(".")[0] + "." + img_type
        else:
            mutate = Convert(request.FILES.getlist('image'), img_type)
            file = mutate.convert()
            filename = file.split("/")[-1]

        data = {
            "file": file.split("/")[-1],
            "filename": filename
        }
        return JsonResponse(data, safe=False)
    context = {}
    return render(request, "main/index.html", context)


def download_file(request, file, filename):
    """This function finds the file and sends it to the user"""

    img = open(f"./download/{file}", 'rb')
    response = FileResponse(img, as_attachment=True, filename=filename)
    return response

def register(request):
    """This function registers the user in the database"""

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email is already taken')
                data = {"message": "Email is already taken"}
                return JsonResponse(data, safe=False)
            else:
                user = User.objects.create_user( email=email, password=password)
                user.save()
                data = {"message": "created"}
                return JsonResponse(data, safe=False)

        else:
            messages.info(request, 'Not a valid password')
            data = {"message": "Not a valid password"}
            return JsonResponse(data, safe=False)
            
    else:
        return HttpResponse("Request method is not a GET")

def login_user(request):
    """This function signs in the user to application"""

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            data = {"message": 'login successful'}
            return JsonResponse(data, safe=False)
        else:
            messages.info(request, 'Invalid email or Password')
            data = {"message": 'Invalid email or Password'}
            return JsonResponse(data, safe=False)

    else:
        return HttpResponse("Request method is not a GET")


@login_required
def logout_user(request):
    """This function logs out the user"""
    auth.logout(request)
    return redirect('index')


def privacy_policy(request):
    context = {}
    return render(request, "main/privacy_policy.html", context)


def terms_cond(request):
    context = {}
    return render(request, "main/terms_cond.html", context)


def cookie_policy(request):
    context = {}
    return render(request, "main/cookie_policy.html", context)