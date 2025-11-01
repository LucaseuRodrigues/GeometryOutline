from django.http import HttpResponse


def home_view(request):
    return HttpResponse('Pagina Home do projeto')
