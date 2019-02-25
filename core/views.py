from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from core.models import Cars, OzonPoints


def render_page(request):
    template = loader.get_template('base.html')
    context = {'Cars': Cars.objects.all()}
    return HttpResponse(template.render(context, request))

def render_page_points(request):
    print('He')
    template = loader.get_template('points.html')
    part1 = OzonPoints.objects.all()[0:999]
    part2 = OzonPoints.objects.all()[999:1998]
    tagnews = []
    payt_list = list()
    payt_list += list(part1)
    payt_list += list(part2)
    tagnews.append(list(part1))
    tagnews.append(list(part2))
    print(tagnews)
    context = {'Points': payt_list}
    return HttpResponse(template.render(context, request))