# Made by sarthak :)
from ast import NotIn
import imp
from string import punctuation
from django.shortcuts import render , HttpResponse , redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User , auth
from django.contrib import messages

'''def index(request):
    return HttpResponse('Hello </br> <a href="https://www.youtube.com/watch?v=Bp6YwNmJshc">AOT Clip</a>')'''

def about(request):
    return render(request,'about.html')
    
    
def index(request):
    return render(request,"index.html")

def logoutUser(request):
    auth.logout(request)
    return redirect("/")

def loginUser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Successfully logged in !!!")
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("login")
    else:
        return render(request,"login.html")

def analyze(request):
    djtext=request.POST.get('text','default text')
    removepunc=request.POST.get('removepunc','off')
    firstcapss=request.POST.get('firstletter','off')
    fullcapss=request.POST.get('fullcaps','off')
    newline=request.POST.get('newline','off')
    extraspaceremover=request.POST.get('extraspace','off')
    charcount=request.POST.get('charcount','off')
    
    if removepunc=='on':
        punctuations='''?!,—––:;“‘[]()@#-`~$%^&*'''
        analyzed=""
        for i in djtext:
            if i not in punctuations :
                analyzed += i
        djtext=analyzed
        params={'purpose':' after Removing puncuations','analyzed_text':analyzed}
    
    if extraspaceremover=='on':
        analyzed=''
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]==" ":
                pass
            else:
                analyzed += char
        params={'purpose':' after removing extra spaces','analyzed_text':analyzed}
        djtext=analyzed
    
    if fullcapss=='on':
        analyzed=""
        for i in djtext:
            analyzed += i.upper()
        djtext=analyzed
        params={'purpose':' after Changing into UPPERCASE','analyzed_text':analyzed}
        
    if firstcapss=='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if index==0:
                analyzed += char.upper()
            else:
                if (djtext[index-1]==".") or (djtext[index-1]==" " and djtext[index-2]=="."):
                    analyzed += char.upper()
                else:
                    analyzed+=char
        djtext=analyzed
        params={'purpose':' after Changing into UPPERCASE','analyzed_text':analyzed}
    
    if newline=='on':
        analyzed=''
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params={'purpose':' after removing new line','analyzed_text':analyzed}
        djtext=analyzed
    
    if charcount=='on':
        analyzed=""
        for i in djtext:
            if not (i==" "  or i=="\n" or i=='\r'):
                analyzed+=i
                count=len(analyzed)
        params={'purpose':' Number of characters','analyzed_text':str(count)}
    
    
    if removepunc != "on" and newline != "on" and fullcapss != "on" and extraspaceremover != "on" and charcount != "on" and firstcapss != "on":
        return HttpResponse("<h1>ERROR! Choose any one of the checkbox...!</h1>")
    
    return render(request,"analyze.html",params)

def registerr(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is already taken...")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is already taken...")
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
                user.save()
                messages.success(request,"User created")
                return redirect('login')
        
        else:
            messages.info(request,"Password did not match")
        return redirect('register')
        
    else:
        return render(request,'register.html')