from django.http import HttpResponse
from django.shortcuts import render, redirect
from scraper.models import *
from datetime import date
from django.core.validators import validate_email

def index(request):
    context = {}
    if 'error' in request.session:
        context['error'] = request.session['error']
        del request.session['error']
    if 'success' in request.session:
        context['success'] = request.session['success']
        del request.session['success']
    return render(request, 'scraper/index.html', context)

def mailing_assign(request):
    adress = request.POST.get('user-email')
    try:
        validate_email(adress)
        request.session['success'] = "Zapisano e-mail - dziękujemy"
    except:
        request.session['error'] = "Nieprawidłowy adres e-mail"
        return redirect('index')
    if request.POST.get('parp') == 'PARP':
        interest1 = "PARP"
    if request.POST.get('ncbr') == 'NCBR':
        interest2 = "NCBR"
    if request.POST.get('rposl') == 'RPOSL':
        interest3 = "RPOSL"
    try:
        agency1 = Institution.objects.get(name = interest1)
    except:
        agency1 = None
    try:
        agency2 = Institution.objects.get(name = interest2)
    except:
        agency2 = None
    try:
        agency3 = Institution.objects.get(name = interest3)
    except:
        agency3 = None
    if User.objects.filter(mail = adress).exists():
        mail = User.objects.get(mail = adress)
        mail.update(interest1 = agency1, interest2 = agency2,
            interest3 = agency3)
    else:
        new_user = User(mail=adress, date_since = date.today(),
            interest1 = agency1, interest2 = agency2, interest3 = agency3)
        new_user.save()
    return redirect('index')

def lookup_backwards_ncbr(request):
    lookup = (request.POST['lookup'])
    time_checked = int(request.POST['time'])
