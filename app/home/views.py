from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.db.models import Q

def postAd(request):
	if request.method == 'GET':
		return render(request, 'post.html')
	elif request.method == 'POST':
		post = request.POST
		file = request.FILES
		ad = Advertisment()

		ad.user = request.user
		ad.title = post.get('title')
		ad.category = post.get('category')
		ad.description = post.get('description')
		ad.name = post.get('name')
		ad.price = post.get('price')
		ad.mobileNumber = post.get('number')
		ad.address = post.get('address')
		ad.image = request.FILES.get('image')

		ad.save()

		return HttpResponse("<h1>Ad posted Successfully!</h1>")



def search(request):
	query = request.GET.get('search', '')
	if query:
		qset = (
				Q(title__icontains=query) |
				Q(category__icontains=query) 

			)
		result = Advertisment.objects.filter(qset).distinct()
	else:
		result = []

	return render(request, 'search.html', {'search' : result})	