from django.urls import path
from . import views
from .views import ObcanView, ObecView, SamospravaView


urlpatterns = [

    path('', views.homePageView, name='home'),
    path('obec/', ObecView.as_view(), name='obec'),
    path('samosprava/', SamospravaView.as_view(), name='samosprava'),
    path('obcan/', ObcanView.as_view(), name='obcan'),

]