from django.urls import path
from . import views
from .views import (
    ObcanView, 
    ObecView, 
    SamospravaView, 
    SearchResultsUradnaView, 
    StarostaView,
    ZastupitelstvoView,
    ClenoviaOzView,
    PozvankaOzView,
    ZapisniceOzView,
    FakturyView,
    ZmluvyView,
)



urlpatterns = [

    path('', views.homePageView, name='home'),
    # Obec
    path('obec/', ObecView.as_view(), name='obec'),
    # Samosprava
    path('samosprava/', SamospravaView.as_view(), name='samosprava'),
    path('samosprava/uradna_tabula', views.uradnaTabulaView, name='uradna_tabula'),
    path('samosprava/uradna_tabula/search', SearchResultsUradnaView.as_view(), name='uradna_results'),
    path('samosprava/vzn', views.vznView, name='vzn' ),
    path('samosprava/starosta_obce', StarostaView.as_view(), name='starosta'),
    path('samosprava/obecne_zastupitelstvo', ZastupitelstvoView.as_view(), name='zastupitelstvo'),
    path('samosprava/obecne_zastupitelstvo/clenovia', ClenoviaOzView.as_view(), name='clenovia'),
    path('samosprava/obecne_zastupitelstvo/pozvanka', PozvankaOzView.as_view(), name='pozvanka'),
    path('samosprava/obecne_zastupitelstvo/zapisnice', ZapisniceOzView.as_view(), name='zapisnice'),
    path('samosprava/faktury', FakturyView.as_view(), name='faktury'),
    path('samosprava/zmluvy', ZmluvyView.as_view(), name='zmluvy'),
    # Obcan
    path('obcan/', ObcanView.as_view(), name='obcan'),
    

]