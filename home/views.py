from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from home.models import Contact, Articles
from datetime import datetime
import json

# Create your views here.
def index(request):
    articles = Articles.objects.all()[:5]
    ctx = {
        'articles' : articles,
        'title' : "Home"
    }
    return render(request, 'index.html', context=ctx)

def contact(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        date = datetime.now()

        contact_object = Contact(phone=phone, email=email, message=message, date=date)
        contact_object.save()
    return render(request, 'contact.html')

def cp(request):
    articles = Articles.objects.all()
    cp_articles = []
    for art in articles:
        if "CP" in art.tags.split(','):
            cp_articles.append(art)
    
    ctx = {
        'articles' : cp_articles,
        'title' : "Competitive Programming"
    }
    return render(request, 'articles.html', context=ctx)

def cyber(request):
    articles = Articles.objects.all()
    cp_articles = []
    for art in articles:
        if "CYBER" in art.tags.split(','):
            cp_articles.append(art)
    
    ctx = {
        'articles' : cp_articles,
        'title' : "Cyber Security"
    }
    return render(request, 'articles.html', context=ctx)

def ml(request):
    articles = Articles.objects.all()
    cp_articles = []
    for art in articles:
        if "ML" in art.tags.split(','):
            cp_articles.append(art)
    
    ctx = {
        'articles' : cp_articles,
        'title' : "Machine Learning"
    }
    return render(request, 'articles.html', context=ctx)

def trivia(request):
    articles = Articles.objects.all()
    cp_articles = []
    for art in articles:
        if "TRIVIA" in art.tags.split(','):
            cp_articles.append(art)
    ctx = {
        'articles' : cp_articles,
        'title' : "Trivia :)"
    }
    return render(request, 'articles.html', context=ctx)

def all_articles(request):
    articles = Articles.objects.all()
    ctx = {
        'articles' : articles,
        'title' : "All Posts"
    }
    return render(request, 'articles.html', context=ctx)

def article(request, title):
    article = Articles.objects.get(title = title)
    context = {
        'title' : title,
        'article' : article
    }
    return render(request, 'article.html', context)

def update_like(request):
    data = json.loads(request.body)
    # print(data)
    articleId = data['articleId']
    action = data['action']
    article, created = Articles.objects.get_or_create(id = articleId)
    if action == "like":
        article.likes += 1
    else:
        article.likes -= 1
        article.likes = max(0, article.likes)
    article.save()
    return JsonResponse("Item added :)", safe=False)