from django.shortcuts import render
from django.http import HttpResponse
from .models import UserData

def index(request, user_url):
	user_check = UserData.objects.filter(url=user_url)

	if user_check:
	    data = {
	        "title":"title",
	        "user_data":user_check[0]
	    }
	    return render(request, "main/index.html", data)