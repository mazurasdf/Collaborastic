from django.db import models

class Tag(models.Model):
	tag_text = models.CharField(max_length=50)
	# event_jobs
	# events

class Skill(models.Model):
	skill_text = models.CharField(max_length=50)
	# users

class User(models.Model):
	email = models.CharField(max_length=320)
	password = models.CharField(max_length=60)
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	expertise = models.IntegerField()
	experience = models.CharField(max_length=50)
	location = models.CharField(max_length=50, blank=True)
	bio = models.TextField(blank=True)
	connections = models.ManyToManyField("self", blank=True,  symmetrical=True)
	skills = models.ManyToManyField(Skill, related_name="users")
	# events
	# collaborations
	# attending
	# event_jobs
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# objects = User_Manager()

class Event(models.Model):
	creator = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
	start = models.DateTimeField()
	end = models.DateTimeField()
	description = models.TextField()
	collaborators = models.ManyToManyField(User, related_name='collaborations')
	attendees = models.ManyToManyField(User, related_name='attending')
	tags = models.ManyToManyField(Tag, related_name="events")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Event_Job(models.Model):
	creator = models.ForeignKey(User, related_name='event_jobs', on_delete=models.CASCADE)
	description = models.TextField()
	struggle = models.CharField(max_length=50)
	date_decided = models.IntegerField() #is date undecided(0), final(1), or flexible(2)
	scope_date = models.DateTimeField()
	pay_hour = models.DecimalField(max_digits=6, decimal_places=2)
	pay_total = models.DecimalField(max_digits=6, decimal_places=2)
	event_place = models.IntegerField()
	# event place is no preference(0),in person(1), online(2), both(3)
	tags = models.ManyToManyField(Tag, related_name="event_jobs")
	partner_description = models.TextField()

