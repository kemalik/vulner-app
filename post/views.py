from django.shortcuts import render
from post.models import News
from django.contrib.auth.models import User

def news_details(request):
    news_id = request.GET['news_id']
    news = User.objects.raw("select * from post_news where id=%s order by id" % news_id)

    return render(request, 'index.html', {'news': news[0]})


def search(request):
    query = request.GET['q']
    return render(request, 'search.html', {'query': query})
