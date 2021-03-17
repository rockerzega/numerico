from django.shortcuts import render #, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import RequestContext
from programas.resta import resta
from .forms import CamposDinamicos

# Create your views here.

def index(request):
    return render(request, 'index.html')

def submitquery(request):
    q = request.GET['query']
    p = request.GET['numero']
    """
    responseJSon = {
        'q': q
    }
    return JsonResponse(responseJSon)
    """
    try:
        ans = resta(q,p)
        myDictionary = {
            "q" : q,
            "ans" : ans,
            "error" : False
        }
        return render(request, 'suma.html', context=myDictionary)
    except:
        pass

def suma(request):
    return render(request, 'suma.html', {})

def dinamico(request):
    if request.method=='POST':
        formulario = CamposDinamicos(request.POST)
        if formulario.is_valid():
            titulo = "Titulo de formulario"
            contenido = formulario.cleaned_data['prueba']+'\n'
            contenido += "seguido" + formulario.cleaned_data['datos']
            return HttpResponseRedirect('/')
    else:
        formulario=CamposDinamicos()
    return render(request, "dinamico.html",{'formulario': formulario})