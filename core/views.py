from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse


def render_page(request):
    template = loader.get_template('base.html')
    context = {}
    return HttpResponse(template.render(context, request))