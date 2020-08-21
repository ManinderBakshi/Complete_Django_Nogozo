from django.contrib import admin
from quiz.models import Quiz_Category, Sets, Blog_Category, Blog_article

# Register your models here.

admin.site.register(Quiz_Category)
admin.site.register(Sets)
admin.site.register(Blog_Category)
admin.site.register(Blog_article)