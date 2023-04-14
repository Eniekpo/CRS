from django.shortcuts import render

from App.models import Civilservants, Reports, Retirement

# Create your views here. 
def index(request):
    return render(request, 'App/index.html')

def civilservants(request):
    return render(request, 'App/civilservants.html')

def criteria(request):
    return render(request, 'App/criteria.html')

def output(request):
    rs = Retirement.objects.all()
    context = {'rs': rs}
    return render(request, 'App/output.html', context)

def reports(request):
    retiree = Reports.objects.all()
    context = {'retiree': retiree}
    return render(request, 'App/reports.html', context)
