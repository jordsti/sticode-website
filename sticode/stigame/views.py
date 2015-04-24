from django.shortcuts import render
from django.db.models import ObjectDoesNotExist
from models import *
# Create your views here.

def index(request):
    news = StiGameNews.objects.order_by('-postedOn')[0:10]
    last_release = None
    context = {'news': news, 'last_release': last_release}

    try:
        releases = StiGameRelease.objects.order_by('-date')
        if len(releases) > 0:
            last_release = releases[0]
            context['last_release'] = last_release
    except ObjectDoesNotExist:
        pass

    return render(request, "stigame/index.html", context)