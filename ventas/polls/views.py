from django.http import HttpResponse
from .models import Pedido
from django.template import loader


def index(request):
    template = loader.get_template('polls/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
