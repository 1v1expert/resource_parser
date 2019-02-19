from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from core.models import Cars


def render_page(request):
    template = loader.get_template('base.html')
    context = {'Cars': Cars.objects.all()}
    return HttpResponse(template.render(context, request))