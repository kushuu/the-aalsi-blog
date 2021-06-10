from django.shortcuts import render
from home.models import Contact, Articles
from datetime import datetime

# Create your views here.
def index(request):
    articles = Articles.objects.all()
    print(len(articles))
    ctx = {
        'articles' : articles,
        'title' : "All Posts"
    }
    return render(request, 'articles.html', context=ctx)

def contact(request):
    if request.method == 'POST':
        print("before save\n")
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
    print(cp_articles)
    ctx = {
        'articles' : cp_articles,
        'title' : "Trivia :)"
    }
    return render(request, 'articles.html', context=ctx)

def all_articles(request):
    articles = Articles.objects.all()
    print(len(articles))
    ctx = {
        'articles' : articles,
        'title' : "All Posts"
    }
    return render(request, 'articles.html', context=ctx)
