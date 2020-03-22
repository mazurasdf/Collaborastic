from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import User

def test(request):
	print("test response")
	return JsonResponse({
		"test": 1
	})

def all_users(request):
	print("trying to send all users")
	dataset = list(User.objects.values())
	return JsonResponse({"results":dataset}, safe=False)

def create_user(request):
	# TODO validate
	# TODO bcrypt

	print(request.POST)

	new_user = User.objects.create(
		email=request.POST.get('email',''),
		password=request.POST.get('password',''),
		first_name=request.POST.get('first_name',''),
		last_name=request.POST.get('last_name',''),
		expertise=request.POST.get('expertise',0),
		experience=request.POST.get('experience',0),
		location=request.POST.get('location',''),
		bio=request.POST.get('bio',''))

	return JsonResponse({
		'response': 1
	})
