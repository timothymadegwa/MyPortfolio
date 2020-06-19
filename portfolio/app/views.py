from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from smtplib import SMTP

import datetime

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def portfolio(request):
    return render(request, 'app/portfolio.html')

def project(request):
    return render(request, 'app/project.html')

def blog(request):
    return render(request, 'app/blog.html')

def cv(request):
    return render(request, 'app/cv.html')

def contact(request):
    if request.method == 'POST':
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact =Contact(first_name=f_name, last_name=l_name, email=email,phone=phone,message=message, contact_date=datetime.datetime.now())
        contact.save()
        message = 'You have recieved a message from '+f_name+' '+l_name+' | '+email+' | '+phone+' \n'+message
        server = SMTP('smtp.gmail.com' , 587)
        server.starttls()
        server.login('aiaqila20@gmail.com', 'aqila123?')
        server.sendmail('aiaqila20@gmail.com', 'timothy@aqila.co.ke', message)
        server.quit()
        reply_body = 'Thank you {},  Your message has been sent successfully'.format(f_name)

        reply = {'message': reply_body }

        return render(request, 'app/contact.html',  reply)

    return render(request, 'app/contact.html')