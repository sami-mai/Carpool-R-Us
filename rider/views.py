from django.shortcuts import render


# Create your views here.
def home(request):
    title = "Rider"
    context = {"title": title}

    return render(request, 'index_rider.html', context)
