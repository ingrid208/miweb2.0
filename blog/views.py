from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def pagina1(request):
    return render(request, 'pagina1.html')

def pagina2(request):
    return render(request, 'pagina2.html')

