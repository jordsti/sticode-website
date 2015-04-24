from django.shortcuts import render
from models import News
# Create your views here.


def index(request):
    news = list(News.objects.order_by('-postedOn')[0:10])
    context = {'news': news}
    return render(request, "news/index.html", context)