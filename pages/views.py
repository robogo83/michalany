from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from .models import (
    Novinky, 
    Oznamy, 
    UradnaTabula, 
    Odpad, 
    Aktuality, 
    Vzn, 
    FakturyRok, 
    ZmluvyRok,
    ZapisniceObdobie,
    )

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

######################################## Samosprava #######################################

class SamospravaView(TemplateView):
    template_name = 'samosprava.html'

def uradnaTabulaView(request):
    posts = UradnaTabula.objects.all().order_by('-date')[5:]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj' : page_obj,}

    return render(request, 'samosprava/uradna_tabula.html', context)

class SearchResultsUradnaView(ListView):
    model = UradnaTabula
    context_object_name = 'zaznamy'
    template_name = 'samosprava/uradna_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return UradnaTabula.objects.filter(
            Q(title__icontains=query) | 
            Q(title1__icontains=query) |
            Q(title2__icontains=query) |
            Q(title3__icontains=query) |
            Q(title4__icontains=query) |
            Q(title5__icontains=query) 
        )

def vznView(request):
    nariadenia = Vzn.objects.all() 
    context = {'nariadenia' : nariadenia}
    return render(request, 'samosprava/vzn.html', context)

class StarostaView(TemplateView):
    template_name = 'samosprava/starosta.html'

class ZastupitelstvoView(TemplateView):
    template_name = 'samosprava/obecne_zastupitelstvo.html'

class ClenoviaOzView(TemplateView):
    template_name = 'samosprava/clenovia_oz.html'

class PozvankaOzView(TemplateView):
    template_name = 'samosprava/pozvanka_oz.html'

class ZapisniceOzView(ListView):
    model = ZapisniceObdobie
    context_object_name = 'zapisnice'
    template_name = 'samosprava/zapisnice.html'
    ordering = '-obdobie'

class FakturyView(ListView):
    model = FakturyRok
    context_object_name = 'faktury'
    template_name = 'samosprava/faktury.html'
    ordering = '-rok'

class ZmluvyView(ListView):
    model = ZmluvyRok
    context_object_name = 'zmluvy'
    template_name = 'samosprava/zmluvy.html'
    ordering = '-rok'