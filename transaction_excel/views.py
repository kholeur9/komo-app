from django.shortcuts import render
from .forms import ExcelInputForm

# Create your views here.

def excel_data(request):
  if request.method == "POST":
    form = ExcelInputForm(request.Post, request.Files)
    
  else:
    form = ExcelInputForm()
    
  return render(request, 'transaction/extract_data.html', {'form': form});