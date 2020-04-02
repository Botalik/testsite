from django.shortcuts import render
from django.http import HttpResponse

def index_mainpage(request):
    return render(request, 'mainpage/homePage.html', )

def contacts(request):
    return render(request, 'mainpage/contacts.html', {'values': ['Если у вас есть вопросы, то задавайте их по телефону',
                                                          'мне поебать какие у тебя вопросы']})
