from django.contrib import admin
from .models import Novinky, Oznamy, UradnaTabula, Odpad

# Register your models here.
admin.site.register(Novinky)
admin.site.register(Oznamy)
admin.site.register(UradnaTabula)
admin.site.register(Odpad)
