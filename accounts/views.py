from django.shortcuts import redirect, render

def index(request):
    return render(request, 'accounts.html')