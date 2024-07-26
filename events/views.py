from django.shortcuts import render, redirect
from .models import Student, Payment
from django.conf import settings
from django_daraja.mpesa.core import MpesaClient
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from members.forms import UserUpdateForm 
from .models import userlogincount
from .forms import StudentForm
from .models import Student, Payment
from django.contrib.auth.models import User
from django.db.models import Count
from members.models import Login
import requests
import json
import datetime
import base64
import hashlib
from .generateaccesstoken import get_access_token
import logging
from django.conf import settings
from .forms import PaymentForm
from requests.auth import HTTPBasicAuth
from django.conf import settings
import requests
from datetime import datetime
from .forms import ProfileUpdateForm
from .forms import PaymentForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


   
def dashboard(request):
 
    return render(request, 'home.html', ) 

def home(request):
    context = {
        'uni_name': 'Taita Taveta University Muslim Students Association'
    }

    user = request.user
    first_name = user.first_name
    last_name = user.last_name
    context = {
        'first_name': first_name,
        'last_name': last_name
    }

    return render(request, 'home.html', context) 

@login_required
def profile(request):
    student = request.user.student  
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'profile.html', {'student': student, 'form': form})

@login_required
def update_profile(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        return redirect('profile')  # Redirect to create a student profile if none exists

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        form = StudentForm(instance=student)

    return render(request, 'profile.html', {'form': form})

@login_required
def finances(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            amount = form.cleaned_data['amount']
            response = lipa_na_mpesa_online(phone_number, amount)
            if response.get('ResponseCode') == '0':
                messages.success(request, 'STK Push sent successfully. Please complete the payment on your phone.')
            else:
                messages.error(request, 'Failed to send STK Push. Please try again.')
        else:
            messages.error(request, 'Invalid form data. Please try again.')
    else:
        form = PaymentForm()
    return render(request, 'finances.html', {'form': form})


def payment_success(request):
    return render(request, 'payment_success.html')  

def payment_failure(request):
    return render(request, 'payment_failure.html')  
def tasks(request):
    return render(request, 'tasks.html')  

def help(request):
    return render(request, 'help.html')  

def csrf_failure(request, reason=""):
    return render(request, "403_csrf.html", {"reason": reason}, status=403)  

def index(request):
    cl = MpesaClient()
    phone_number = '0114521175'  
    amount = 10
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = getattr(settings, 'MPESA_CALLBACK_URL', 'http://127.0.0.1:8000/events/mpesa_callback/')
    
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return render(request, 'events/index.html')  

@csrf_exempt
def mpesa_callback(request):
    if request.method == 'POST':
        mpesa_body = request.body.decode('utf-8')
        mpesa_payment_data = json.loads(mpesa_body).get('Body', {}).get('stkCallback', {})

        result_code = mpesa_payment_data.get('ResultCode')
        result_desc = mpesa_payment_data.get('ResultDesc')
        merchant_request_id = mpesa_payment_data.get('MerchantRequestID')
        checkout_request_id = mpesa_payment_data.get('CheckoutRequestID')
        amount = mpesa_payment_data.get('CallbackMetadata', {}).get('Item', [])[0].get('Value')
        mpesa_receipt_number = mpesa_payment_data.get('CallbackMetadata', {}).get('Item', [])[1].get('Value')
        transaction_date = mpesa_payment_data.get('CallbackMetadata', {}).get('Item', [])[3].get('Value')
        phone_number = mpesa_payment_data.get('CallbackMetadata', {}).get('Item', [])[4].get('Value')

        if result_code == 0:
            Payment.objects.create(
                phone_number=phone_number,
                amount=amount,
                mpesa_receipt_number=mpesa_receipt_number,
                transaction_date=transaction_date,
                merchant_request_id=merchant_request_id,
                checkout_request_id=checkout_request_id,
                status='Completed',
            )
            return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})
        else:
            return JsonResponse({"ResultCode": 1, "ResultDesc": "Rejected"})
    
    return JsonResponse({"ResultCode": 1, "ResultDesc": "Rejected"})

@login_required
def settings(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password has been updated successfully.')
            return redirect('settings')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'settings.html', {
        'form': form
    })

def get_access_token():
    consumer_key = 'usWLVf1u5FqjSAi4OJDlHo8WOkidBwGHMThVAWhabhbknzPz'
    consumer_secret = 'ubpZeWegHAqWL2yNbGPfL4qaEbeywGMVgkWLuuqJWm75AlsGi5mmcHACOwUxAGuv'
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(api_url, auth=(consumer_key, consumer_secret))
    json_response = response.json()
    access_token = json_response['access_token']
    return access_token

def lipa_na_mpesa_online(phone_number, amount):
    access_token = get_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {
        "Authorization": "Bearer %s" % access_token
    }
    timestamp = get_timestamp()
    password = generate_password(timestamp)
    payload = {
        "BusinessShortCode": '931206',
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerBuyGoodsOnline",  
        "Amount": '10',
        "PartyA": '0114521175',
        "PartyB": '931206',
        "PhoneNumber": '0114521175',
        "CallBackURL": settings.MPESA_CALLBACK_URL,
        "AccountReference": "ttumsa",  
        "TransactionDesc": "Payment"  
    }
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

@csrf_exempt
def initiate_stk_push(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        phone_number = data.get('254114521175')
        amount = data.get('10')
        
        if phone_number and amount:
            response = lipa_na_mpesa_online(254114521175, 10)
            if response.get('ResponseCode') == '0':
                return JsonResponse({'success': True, 'message': 'STK Push sent successfully.'})
            else:
                return JsonResponse({'success': False, 'message': response.get('errorMessage', 'Failed to initiate STK Push.')})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid phone number or amount.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})      

def generate_password(timestamp):
    data_to_encode = '931206' + settings.MPESA_PASSKEY + '%Y%m%d%H%M%S'
    encoded_string = base64.b64encode(data_to_encode.encode())
    return encoded_string.decode('utf-8')

def get_timestamp():
    return datetime.now().strftime('%Y%m%d%H%M%S')
