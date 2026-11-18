# Uncomment the required imports before adding the code

# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
# from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth import logout
# from django.contrib import messages
# from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
# from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# User authentication endpoints
@csrf_exempt
def login_user(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    try:
        data = json.loads(request.body or '{}')
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    username = data.get('userName', data.get('username', ''))
    user = authenticate(request, username=username, password=data.get('password', ''))
    if user is None:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)
    login(request, user)
    return JsonResponse({'userName': user.username, 'status': 'Authenticated'})

@csrf_exempt
def logout_request(request):
    logout(request)
    return JsonResponse({'userName': ''})

@csrf_exempt
def registration(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    try:
        data = json.loads(request.body or '{}')
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    username = data.get('userName', data.get('username', '')).strip()
    password = data.get('password', '')
    email = data.get('email', '')
    if not username or not password:
        return JsonResponse({'error': 'Username and password are required'}, status=400)
    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'Username already exists'}, status=409)
    user = User.objects.create_user(username=username, password=password, email=email, first_name=data.get('firstName', ''), last_name=data.get('lastName', ''))
    login(request, user)
    return JsonResponse({'userName': user.username, 'status': 'Registered'}, status=201)

# Update the `get_dealerships` view to render the index page with
# a list of dealerships
# def get_dealerships(request):
# ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request,dealer_id):
# ...

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request):
# ...
