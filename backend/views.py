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
		email=request.POST['email'],
		password=request.POST['password'],
		first_name=request.POST['first_name'],
		last_name=request.POST['last_name'],
		expertise=request.POST['expertise'],
		experience=request.POST['experience'],
		location=request.POST['location'],
		bio=request.POST['bio'])

	return JsonResponse({
		'response': 1
	})
