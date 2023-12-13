from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
#from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.http import HttpResponseRedirect
from .forms import NumeroClient
from .models import Client, ForfaitClient

# Connexion via logic number
def connexion(request):
   if request.method == "POST":

      numero_fourni = request.POST.get("numero")
      try:
       numero_client = Client.objects.get(numero=numero_fourni)
       return redirect('client', client_id=numero_client.id);
      except Client.DoesNotExist:
         return render(request, 'client/connexion.html', {'form': NumeroClient(), 'error': 'Numero client inconnu'})
   else:
      return render(request, 'client/connexion.html', {'form': NumeroClient()})

# Home Page of Client
def client(request, client_id):
   numero_client = get_object_or_404(Client, id=client_id)
   forfait_client = ForfaitClient.objects.filter(numero_client=numero_client)
   return render(request,
'client/client.html', { 'numero_client': numero_client, 'forfait_client': forfait_client })

def deconnexion(request):
   logout(request)
   return redirect('connexion');