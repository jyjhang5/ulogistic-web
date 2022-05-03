from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import News
from .apps import MENU_ITEMS

def index(request):
	news = News.objects.all().order_by("-pub_date")[:5]

	return render(request, 'public/index.html', {
		'menu_item': MENU_ITEMS,
		'newslist': news
	})

def news(request, id=None):
	news = News.objects.get(
		id__exact = id,
	)
	
	return render(request, 'public/news.html', {
		'news': news
	})


def newslist(request):
	limit = 10 # size per page
	topics = News.objects.all().order_by("-pub_date")
	paginator = Paginator(topics, limit)

	page = request.GET.get('page') # get page number
	try:
		topics = paginator.page(page)
	except PageNotAnInteger:
		topics = paginator.page(1)
	except EmptyPage:
		topics = paginator.page(paginator.num_pages)

	return render(request, 'public/newslist.html', {
		'topics': topics
	})

def hr(request):
	return render(request, 'public/hr.html')