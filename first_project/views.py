from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request,"home.html")

def result(request):
    words = request.GET['words']   #SQUARE BRACKETS ONLY !!!!!!!!!!!!!!
    word_count = words.split()

    return render(request, 'result.html',{'count':len(word_count)})

