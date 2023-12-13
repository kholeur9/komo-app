from django.contrib import admin
from .models import Client, ForfaitClient, CreditClient



class ForfaitInline(admin.TabularInline):
  model = ForfaitClient
  extra = 1 # le nombre initial de formulaires vides à afficher

class CreditInline(admin.TabularInline):
  model = CreditClient
  extra = 1 # le nombre initial de formulaires vides à afficher

class ClientAdmin(admin.ModelAdmin):
  inlines = [ForfaitInline, CreditInline]
  list_display = ('id', 'numero', 'total_credit')
  
  
# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(ForfaitClient)
admin.site.register(CreditClient)