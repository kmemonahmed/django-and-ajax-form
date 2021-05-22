from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.is_ajax and request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact_us(name=name,email=email,subject=subject,message=message).save()

        # return render(request,'main.html')
        return JsonResponse({"valid":True}, status = 200)
    return render(request,'index.html')

def main(request):
    return render(request,'main.html')