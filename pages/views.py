from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Novinky, Oznamy, UradnaTabula, Odpad, Aktuality

# Create your views here.

def homePageView(request):
    novinky = Novinky.objects.all().order_by('id')
    oznamy = Oznamy.objects.all().order_by('-date')
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

class ObcanView(TemplateView):
    template_name = 'obcan.html'

class ObecView(TemplateView):
    template_name = 'obec.html'

class SamospravaView(TemplateView):
    template_name = 'samosprava.html'