from django.http import HttpResponse
from django.shortcuts import render
from .models import Details
# Create your views here.


def home(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        location = request.POST.get("location")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")

        Details.objects.create(full_name=full_name,
                               location=location, phone_number=phone_number,
                               email=email)
        return render(request, "fill/thanks.html")
    return render(request, "fill/form.html")