from django.contrib import admin
from .models import Station, Line, Train
# Register your models here.


from django.contrib import admin
from .models import Train, Line, Station

admin.site.register(Train)
admin.site.register(Line)
admin.site.register(Station)
