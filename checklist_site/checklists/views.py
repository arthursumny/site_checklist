# checklists/views.py

from django.shortcuts import render

def pagina_inicial(request):
    return render(request, 'checklists/pagina_inicial.html')

def pagina_checklists(request):
    return render(request, 'checklists/pagina_checklists.html')

def pagina_workbooks(request):
    return render(request, 'checklists/pagina_workbooks.html')

def pagina_planners(request):
    return render(request, 'checklists/pagina_planners.html') 
