from django.shortcuts import render


# Create your views here.
def landing(request):
    title = "Mai-Carpool"
    context = {"title": title}

    return render(request, 'landing.html', context)
