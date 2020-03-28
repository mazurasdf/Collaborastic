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
	dataset = list(User.objects.values())
	return JsonResponse({"results":dataset}, safe=False)

def create_user(request):
	# TODO validate
	# TODO bcrypt

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

def delete_user(request, user_id):
	# TODO make this delete request only
	this_user = User.objects.get(id=user_id)
	# TODO check if user is logged in
	User.objects.get(id=user_id).delete()
	# also would be nice to get this to display correctly
	return JsonResponse({
		'response': 1
	})