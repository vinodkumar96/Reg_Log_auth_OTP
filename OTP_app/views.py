from django.shortcuts import render
from django.http import HttpResponse
from . models import Reg
from . forms import Reg_form
from . forms import Log_form
from django.core.mail import send_mail
from django.conf import settings
import random
import http.client
import json

# Create your views here.
def home (request):
    return render(request,'home.html')
def reg (request):
    if request.method == 'POST':
        regform = Reg_form(request.POST)
        if regform.is_valid():
            x = otp_send (request)
            if x:
                return render(request,'otp.html')
            else:
                return render(request,'reg.html',{'regform':regform})
        else:
            return render(request, 'reg.html', {'regform': regform})
    else:
        regform = Reg_form
        return render(request,'reg.html',{'regform':regform})
def OTP (request):
    n_otp = request.POST["otp"]
    o_otp = request.session["otp"]
    if n_otp == o_otp:
        form=Reg_form(request.session["details"])
        form.save()
        return HttpResponse("Registration success")
    else:
        return render(request,'otp.html')

def log (request):
    if request.method == "POST":
        logform = Log_form(request.POST)
        if logform.is_valid():
            un = logform.cleaned_data['username']
            pw = logform.cleaned_data['password']
            dbuser = Reg.objects.filter(u_name=un,p_word=pw)
            if not dbuser:
                return HttpResponse("Login Failed")
            else:
                return HttpResponse("Login Success")
    else:
        logform=Log_form
        return render(request,'log.html',{'logform':logform})

def otp_send (request):
    ot = str(random.randint(100000,999999))
    mobno = request.POST['mob_no']
    emailid = request.POST['email']
    subject = "registration OTP"
    From_mail = settings.EMAIL_HOST_USER
    to_list =[emailid]
    send_mail(subject,ot,From_mail,to_list, fail_silently=False)
    print("OTP sent Succesfully")
    request.session["details"] =request.POST
    request.session["otp"] = ot
    conn = http.client.HTTPConnection("api.msg91.com")
    payload = "{ \"sender\":\"VINOD\", \"route\": \"4\", \"country\": \"91\", \"sms\": [ { \"message\":\"" + ot + "\",\"to\": [ \"" + mobno + "\" ] } ] }"
    headers = {
        'authkey': "**********",  # PLEASE ENTER THE AUTHKEY BEFORE EXECUTING THE PROGRAM
        'content-type': "application/json"
    }

    conn.request("POST",
                 "/api/v2/sendsms?country=91&sender=&route=&mobiles=&authkey=&encrypt=&message=&flash=&unicode=&schtime=&afterminutes=&response=&campaign=",
                 payload, headers)

    data = conn.getresponse()
    res = json.loads(data.read().decode("utf-8"))
    print(res)
    if res["type"] == "success":
        return True
    else:
        return False