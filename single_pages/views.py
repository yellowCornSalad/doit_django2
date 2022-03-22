from django.shortcuts import render

# Create your views here.

# landing: 대문


def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

# about_me: 자기소개


def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )
