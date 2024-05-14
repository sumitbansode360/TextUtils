# this file created by me - sumit
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html',context={'name':'sumit','age':18})
    

def about(request):
    return HttpResponse("about sumit")


def analyze(request):

    try:
        djtext = request.POST.get('text','default')
        removepunc = request.POST.get('removepunc','off')
        upper = request.POST.get('upper','off')
        newline = request.POST.get('newline','off')
        spaceremove = request.POST.get('spaceremove','off')
        counter = request.POST.get('counter','off')
        
        analyzed = djtext
        if removepunc == "on":
                
            analyzed = ' '
            punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


            for char in djtext:
                if char not in punc:
                    analyzed = analyzed+char
            parms = {'purpose':'remove punctuations','anayzed_text':analyzed}
            djtext = analyzed
            
        
        if upper=="on":
            analyzed = ' '
            for char in djtext:
                analyzed = analyzed+char.upper()
            parms = {'purpose':'Upper case operations','anayzed_text':analyzed}
            djtext = analyzed

        if newline =="on":
            analyzed = ' '
            for char in djtext:
                if char !="\n" and char!="\r":
                    analyzed = analyzed+char

            parms = {'purpose':'New line remover','anayzed_text':analyzed}
            djtext = analyzed

        if spaceremove =="on":
            analyzed = ' '
            for i in range(len(djtext)):
                if djtext[i] == " " and djtext[i+1] == " ":
                    pass
                else:
                    analyzed = analyzed + djtext[i]
            parms = {'purpose':'Space remover','anayzed_text':analyzed}

            djtext = analyzed
        
        if counter == "on":
            count = 0
            for i in range(len(djtext)):
                if djtext[i]==" ":
                    pass
                else:
                    count = count+1

            parms = {'purpose':'char counterr','anayzed_text':analyzed,'char_count':count}

        
        return render(request,'analyze.html',parms)
    
    except Exception as e:
        return HttpResponse('Error')
