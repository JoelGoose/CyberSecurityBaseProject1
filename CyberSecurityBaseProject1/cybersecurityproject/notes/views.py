from django.contrib.auth.decorators import login_required
from .models import Note
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import sqlite3
## FLAW 5: Insufficient Logging & Monitoring: 
	# import logging
	# logger = logging.getLogger("logger")


@login_required
@csrf_exempt ## FLAW 1 remove csrf_exempt
def addView(request):
	## FLAW 2: Injection with fixed implementation commented out below
	# if request.method == 'POST':	
		# note = request.POST.get('note')
		# owner = request.user
		# newNote = Note.objects.create(owner=owner,note=note)
		# newNote.save()
	## FLAW 2: End of fixed implementation
	conn = sqlite3.connect("db.sqlite3")
	cursor = conn.cursor()
	text = request.POST.get('note') 
	owner_id = request.user.id
	cursor.execute("INSERT INTO notes_note (note, owner_id) VALUES ('%s',%d)" % (text,owner_id))
	conn.commit()
	# logger.info("New note created: " + text) ## FLAW 5: Insufficient Logging & Monitoring
	return redirect('/')

@login_required
def homePageView(request):
	note = Note.objects.filter(owner=request.user) 
	return render(request, 'pages/index.html', {'note': note})

#@login_required ## FLAW 3: implement @login_required
def changePasswordView(request):
	user = User.objects.get(username=request.GET.get("user")) ## FLAW 3: should retrieve user with user = request.user
	password = request.GET.get('password') ## FLAW 1 & 3: should use 'POST' instead of 'GET'
	if (password):
		user.set_password(password)
		user.save()
		# logger.info("Password got changed by the user: " + user.username) ## FLAW 5: Insufficient Logging & Monitoring
		return redirect('/')
	else:
		return redirect('/')

