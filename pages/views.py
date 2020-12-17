from django.shortcuts import render
from .models import Novinky, Oznamy, UradnaTabula, Odpad, Aktuality

# Create your views here.

def homePageView(request):
    novinky = Novinky.objects.all().order_by('id')
    oznamy = Oznamy.objects.all()
    posts = UradnaTabula.objects.all().order_by('-date')[:5]
    odpady = Odpad.objects.all().order_by('day')
    aktuality = Aktuality.objects.all()

    context = {
        'novinky' : novinky,
        'oznamy' : oznamy,
        'posts' : posts,
        'odpady' : odpady,
        'aktuality' : aktuality,
    }
    
    return render(request, 'home.html', context)