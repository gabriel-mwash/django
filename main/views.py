from django.shortcuts import render
from .models import Resident

# Create your views here.


def resident_data(request):
    data = Resident.objects.all()
    return render(request, "index.html", {"residentData": data})
