from django.shortcuts import render
from django.http import HttpResponse
from .models import StockMarket
from datetime import datetime
# Create your views here.
def dashboard(request):
    context = {
        'currentTime':datetime.now(),
        "market" : StockMarket.objects.all(),
        "CEtotOI" : StockMarket.objects.last().CEtotOI,
        "CEtotVoi" : StockMarket.objects.last().CEtotVoi,
        "PEtotOI" : StockMarket.objects.last().PEtotOI,
        "PEtotVoi" : StockMarket.objects.last().PEtotVoi,
    }
    return render(request, 'dashboard/dashboard.html',context)
    