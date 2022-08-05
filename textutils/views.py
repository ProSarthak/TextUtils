# Made by sarthak :)
from ast import NotIn
import imp
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

'''def index(request):
    return HttpResponse('Hello </br> <a href="https://www.youtube.com/watch?v=Bp6YwNmJshc">AOT Clip</a>')'''

def about(request):
    return render(request,'about.html')
    
    
def index(request):
    return render(request,"index.html")

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
