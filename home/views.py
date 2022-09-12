from utils import get_db_handle
import os
import bs4
import json
from datetime import datetime
import TAB.settings as settings
from home.models import *
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from mongoengine import Document, fields
from dotenv import load_dotenv
load_dotenv()

MONGO_PASS = os.getenv('mongo_pass')
WPM = 200
WORD_LENGTH = 5
DB_HANDLE, CLIENT = get_db_handle(
    'tab-mongo', 
    f'mongodb+srv://aalsisendsmail:{MONGO_PASS}@cluster0.9docwgy.mongodb.net/?retryWrites=true&w=majority',
    27017, 
    'aalsisendsmail', 
    MONGO_PASS
)


def index(request):
    if request.method == 'POST':
        email = request.POST['email_aalsi']
        all_subscribers = Subscriber.objects.all()
        if (all_subscribers.filter(email=email)):
            messages.error(request, "User already subscribed!")
            return redirect('home')

        # mailing stuff.
        subject = "Welcomeeee 🎉🎉"
        email_from = settings.EMAIL_HOST_USER
        template = render_to_string('email.html', {'email': email})

        user_email = EmailMessage(
            subject,
            template,
            email_from,
            [email],
        )
        user_email.fail_silently = False
        user_email.send()
        subscriber, _ = Subscriber.objects.get_or_create(
            email=email, date_subed=django.utils.timezone.now())
        subscriber.save()

        return redirect('home')
    else:
        articles_collection = DB_HANDLE['articles']
        articles = list(articles_collection.find({}))
        articles = articles[:5]
        ctx = {
            'articles': articles,
            'title': "Home"
        }
        return render(request, 'index.html', context=ctx)


def contact(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        date = datetime.now()

        contact_object = Contact(
            phone=phone, email=email, message=message, date=date)

        # email stuff
        subject = f"Feedback from user-email {email}"
        email_from = settings.EMAIL_HOST_USER
        template = message  # render_to_string('email.html', {'email': email})

        send_mail(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
        )

        contact_object.save()
    return render(request, 'contact.html')


def cp(request):
    articles_collection = DB_HANDLE['articles']
    articles = list(articles_collection.find({}))
    cp_articles = []
    for art in articles:
        if "CP" in art['tags'].split(','):
            cp_articles.append(art)

    ctx = {
        'articles': cp_articles,
        'title': "Competitive Programming"
    }
    return render(request, 'articles.html', context=ctx)


def cyber(request):
    articles_collection = DB_HANDLE['articles']
    articles = list(articles_collection.find({}))
    cyebr_articles = []
    for art in articles:
        if "CYBER" in art['tags'].split(','):
            cyebr_articles.append(art)

    ctx = {
        'articles': cyebr_articles,
        'title': "Cyber Security"
    }
    return render(request, 'articles.html', context=ctx)


def ml(request):
    articles_collection = DB_HANDLE['articles']
    articles = list(articles_collection.find({}))
    ml_articles = []
    for art in articles:
        if "ML" in art['tags'].split(','):
            ml_articles.append(art)

    ctx = {
        'articles': ml_articles,
        'title': "Machine Learning"
    }
    return render(request, 'articles.html', context=ctx)


def trivia(request):
    articles_collection = DB_HANDLE['articles']
    articles = list(articles_collection.find({}))
    trivia_articles = []
    for art in articles:
        if "TRIVIA" in art['tags'].split(','):
            trivia_articles.append(art)
    ctx = {
        'articles': trivia_articles,
        'title': "Trivia :)"
    }
    return render(request, 'articles.html', context=ctx)


def all_articles(request):
    # articles = Articles.objects.all().order_by('-date_added')
    
    articles_collection = DB_HANDLE['articles']
    articles = list(articles_collection.find({}))
    ctx = {
        'articles': articles,
        'title': "All Posts"
    }
    return render(request, 'articles.html', context=ctx)


def extract_text(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    texts = soup.findAll(text=True)
    # print(texts)
    return texts


def is_visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif isinstance(element, bs4.element.Comment):
        return False
    elif element.string == "\n":
        return False
    return True


def filter_visible_text(page_texts):
    return filter(is_visible, page_texts)


def count_words_in_text(text_list, word_length):
    total_words = 0
    for current_text in text_list:
        total_words += len(current_text)/word_length
    return total_words


def estimate_reading_time(html):
    texts = extract_text(html)
    filtered_text = filter_visible_text(texts)
    total_words = count_words_in_text(filtered_text, WORD_LENGTH)
    return total_words/WPM


def article(request, title):
    # article = Articles.objects.get(title=title)
    articles_collection = DB_HANDLE['articles']
    article = articles_collection.find_one({"title" : title})
    
    context = {
        'title': title,
        'article': article
    }
    
    read_time = round(estimate_reading_time(article['article_body']))
    if read_time == 0:
        articles_collection.update_one(
            {"title" : title},
            {"$set": { 'reading_time': read_time } }
        )
    else:
        articles_collection.update_one(
            {"title" : title},
            {"$set": { 'reading_time': 1 } }
        )
    # article.save()
    return render(request, 'article.html', context)


def update_like(request):
    data = json.loads(request.body)
    # print(data)
    articleId = data['articleId']
    action = data['action']
    article, created = Articles.objects.get_or_create(id=articleId)
    if action == "like":
        article.likes += 1
    else:
        article.likes -= 1
        article.likes = max(0, article.likes)
    article.save()
    return JsonResponse("Item added :)", safe=False)
