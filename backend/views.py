from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import User

# TODO error validations should return JSON response with errors

def test(request):
	print("test response")
	return JsonResponse({
		"test": 1
	})

def all_users(request):
	dataset = list(User.objects.values())
	return JsonResponse({"results":dataset}, safe=False)

def show_single_user(request, user_id):
	# this is kinda rusty but sorta still works. see if I can include connections and skills
	srlData = serializers.serialize('json', [User.objects.get(id=user_id)])
	srlData = eval(srlData)
	return JsonResponse(srlData, safe=False)

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

def edit_user(request, user_id):
	# TODO make this PUT request only, though this might be hard because
	# postman was having trouble sending it as a PUT request. works as POST though
	this_user = User.objects.get(id=user_id)
	# TODO check if user is logged in
	this_user.email = request.POST['email']
	this_user.password = request.POST['password']
	this_user.first_name = request.POST['first_name']
	this_user.last_name = request.POST['last_name']
	this_user.expertise = request.POST['expertise']
	this_user.experience = request.POST['experience']
	this_user.location = request.POST['location']
	this_user.bio = request.POST['bio']

	this_user.save()

	return JsonResponse({
		'response': 1
	})