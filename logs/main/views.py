from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date
def main(request):

    return render(request, "main.html")

def date(request):
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
