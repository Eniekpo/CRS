from django.shortcuts import render

# Create your views here. 
def index(request):
    return render(request, 'App/index.html')

def civilservants(request):
    return render(request, 'App/civilservants.html')

def csdetails(request):
    return render(request, 'App/csdetails.html')

def criteria(request):
    return render(request, 'App/criteria.html')

def reports(request):
    return render(request, 'App/reports.html')
