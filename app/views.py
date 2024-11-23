from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def meghana(request):
    return HttpResponse('My Name is Meghanaaaaa Sir')

def jaipal(request):
    return HttpResponse('<h1 align="center"> JaiPal is a play boy and have 3 girl friends</h1>')

def abdhullah(request):
    return HttpResponse('<h1 align="center"><marquee direction="left">Kya bache(Abdhullah) kya kartha hu practice karo bhai</marquee></h1>')

def harshad(request):
    return HttpResponse('''
    <h1 aligh="center">Name of the trainer is:Harshad</h1>
    <h1 aligh="center">course is:Python and Django</h1>
    
    ''')