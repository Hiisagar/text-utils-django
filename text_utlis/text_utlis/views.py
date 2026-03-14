from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render('request','index.html')

def analyzer(request):
    #get text from the textarea
    getText = request.GET.get('text','default')
    
    #if checkbox value is true they assign the value into the getPunc vars
    getPunc = request.GET.get('removepunc','off')

    #if checkbox value is true they assign the value into the fullcaps vars
    fullcaps = request.GET.get('fullcaps','off')

    #if checkbox value is true they assign the value into the newlinerm vars
    newlinerm = request.GET.get('newlineremover','off')

    #if checkbox value is true they assign the value into the spacrm vars
    spacrm = request.GET.get('spaceremover','off')

    #if checkbox value is true they assign the value into characer count
    wcount = request.GET.get('wordcount','off')

    # assign empty vars
    analyzed = ''
    
    #rule of punctutations
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    #remove punctuations 
    if getPunc == 'on':
        for char in getText:
            if char not in punctuations:
                analyzed += char
        params = {
            'purpose' : 'Remove Punctuations',
            'Analyzed_text' : analyzed
        }
        return render(request,'removepunc.html',params)
    
    #change word to uppercase
    elif(fullcaps == 'on'):
        analyzed = ''
        for char in getText:
            analyzed += char.upper()
        params = {
            'purpose' : 'Change to Uppercase',
            'Analyzed_text' : analyzed
        }
        return render(request,'removepunc.html',params)
    
    #new line remover
    elif(newlinerm == 'on'):
        analyzed = ''
        for char in getText:
            if char != '\n':
                analyzed += char.upper()
        params = {
            'purpose' : 'New Line Remover',
            'Analyzed_text' : analyzed
        }
        return render(request,'removepunc.html',params)
    
    #space remover
    elif(spacrm == 'on'):
        analyzed = ' '.join(getText.split())
        params = {
            'purpose' : 'Extra Space Remover',
            'Analyzed_text' : analyzed
        }
        return render(request,'removepunc.html',params)

    #character count
    elif(wcount == 'on'):
        analyzed = len(getText)
        params = {
            'purpose' : 'Character Count',
            'Analyzed_text' : analyzed
        }
        return render(request,'removepunc.html',params)
    
    #else part executed if default value off is true
    else:
        return HttpResponse('Error !!!')


def capitalfirst(request):
    return HttpResponse('Capital First')

def newlineremove(request):
    return HttpResponse("New Line Remove")

def spaceremove(request):
    return HttpResponse('Space Remover')

def charactercount(request):
    return HttpResponse("Character Count")