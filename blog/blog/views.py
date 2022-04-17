from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request) -> HttpResponse:
    return render(
        request,
        "index.html"
    )


def about(request) -> HttpResponse:
    return render(request, "about.html" )

    
def contact(request) -> HttpResponse:
    return render(request, "contact.html" )