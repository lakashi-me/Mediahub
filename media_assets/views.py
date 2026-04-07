from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def dashboard(request):
    return render(request, 'media_assets/dashboard.html')
