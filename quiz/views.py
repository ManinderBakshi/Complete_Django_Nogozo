from django.shortcuts import render
from django.http import HttpResponse
from quiz.models import Quiz_Category, Sets, Blog_article

# Create your views here.
def index(request):
    return render(request, 'quiz/index.html')


def quiz_cat(request):
    categories = Quiz_Category.objects.all()

    context = {
        'categories': categories
    }
    return render(request, 'quiz/quiz_home.html', context)

def get_sets(request, cat_id):
    sets = Sets.objects.filter(set_category=cat_id)
    
    context={
        'sets':sets
    }

    return render(request, 'quiz/sets.html', context)

def quiz(request, set_id):
    set_info = Sets.objects.get(set_id=set_id)

    context = {
        'set_info':set_info
    }

    return render(request, 'quiz/quiz.html', context)

def blog_articles(request):
    articles = Blog_article.objects.all()

    context = {
        'articles':articles
    }

    return render(request, 'quiz/blog_articles.html', context)


def article(request, article_id):
    article = Blog_article.objects.get(article_id=article_id)

    context = {
        'article':article
    }

    return render(request, 'quiz/article.html', context)