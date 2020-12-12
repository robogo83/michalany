from django.shortcuts import render
from .models import Novinky, Oznamy, UradnaTabula, Odpad

# Create your views here.

def homePageView(request):
    novinky = Novinky.objects.all()
    oznamy = Oznamy.objects.all()
    posts = UradnaTabula.objects.all().order_by('-date')[:5]
    odpady = Odpad.objects.all().order_by('day')

    context = {
        'novinky' : novinky,
        'oznamy' : oznamy,
        'posts' : posts,
        'odpady' : odpady,
    }
    
    return render(request, 'home.html', context)