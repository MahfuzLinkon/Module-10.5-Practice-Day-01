from django.shortcuts import render


# Create your views here.
def contact(request):
    return render(request, "navigation_app/contact.html")


def about(request):
    return render(request, "navigation_app/about.html")
