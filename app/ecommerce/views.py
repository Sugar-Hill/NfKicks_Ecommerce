from django.shortcuts import render


def home_page(request):
    context = {
        'title': 'Hello The World!'
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        'title': 'About page'
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    context = {
        'title': 'Contact page'
    }
    return render(request, "home_page.html", context)
