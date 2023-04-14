from django.shortcuts import render, redirect

from App.models import Civilservants, Reports, Retirement
from . forms import CivilservantsForm, RetirementForm

# Create your views here. 
def index(request):
    return render(request, 'App/index.html')

def civilservants(request):
    return render(request, 'App/civilservants.html')

def criteria(request):
    if request.method == 'POST':
        form = RetirementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('output')
    else:
        form = RetirementForm()
    context = {
        'form': form
    }
    return render(request, 'App/criteria.html', context)

def output(request):
    rs = Retirement.objects.all()
    context = {'rs': rs}
    return render(request, 'App/output.html', context)

def reports(request):
    retiree = Reports.objects.all()
    context = {'retiree': retiree}
    return render(request, 'App/reports.html', context)
