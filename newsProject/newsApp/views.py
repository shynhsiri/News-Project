from django.shortcuts import render
from newsapi import NewsApiClient


def index(request):
    newsApi = NewsApiClient(api_key = 'fef9b1d5e1d545188ab1f30415b94e42')
    headLines = newsApi.get_top_headlines(sources='bbc-news')
    articles =headLines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news, desc, img)


    return render(request, "main/index.html", context = {"mylist" : mylist})