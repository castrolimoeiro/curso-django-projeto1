from django.http import HttpResponse
# from django.shortcuts import render


# HTTP request
def home(request):
    return HttpResponse('HOME 1')
    # HTTP RESPONSE


def contato(request):
    return HttpResponse('CONTATO 1')


def sobre(request):
    return HttpResponse('SOBRE 1')
    # HTTP RESPONSE
