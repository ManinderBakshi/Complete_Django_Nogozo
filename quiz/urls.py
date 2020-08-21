
from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.index, name='index'),
    path('nogozo/quiz/categories/', views.quiz_cat, name='categories'),
    path('nogozo/quiz/categories/<int:cat_id>/', views.get_sets, name='sets'),
    path('nogozo/quiz/categories/sets/<int:set_id>/', views.quiz, name='quiz'),
    path('nogozo/blog/articles', views.blog_articles, name='blog_articles'),
    path('nogozo/blog/artciles/<int:article_id>', views.article, name='article'),
]
