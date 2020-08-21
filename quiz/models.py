from django.db import models

# Create your models here.
class Quiz_Category(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cat_name


class Sets(models.Model):
    set_id = models.IntegerField(primary_key=True)
    set_topic = models.CharField(max_length=100)
    set_date = models.DateField()
    set_category = models.ForeignKey(Quiz_Category, on_delete=models.CASCADE)

    q1 = models.CharField(max_length=200)
    op_1a = models.CharField(max_length=100)
    op_1b = models.CharField(max_length=100)
    op_1c = models.CharField(max_length=100)
    q1_ans = models.CharField(max_length=100)

    q2 = models.CharField(max_length=200)
    op_2a = models.CharField(max_length=100)
    op_2b = models.CharField(max_length=100)
    op_2c = models.CharField(max_length=100)
    q2_ans = models.CharField(max_length=100)

    q3 = models.CharField(max_length=200)
    op_3a = models.CharField(max_length=100)
    op_3b = models.CharField(max_length=100)
    op_3c = models.CharField(max_length=100)
    q3_ans = models.CharField(max_length=100)

    q4 = models.CharField(max_length=200)
    op_4a = models.CharField(max_length=100)
    op_4b = models.CharField(max_length=100)
    op_4c = models.CharField(max_length=100)
    q4_ans = models.CharField(max_length=100)

    q5 = models.CharField(max_length=200)
    op_5a = models.CharField(max_length=100)
    op_5b = models.CharField(max_length=100)
    op_5c = models.CharField(max_length=100)
    q5_ans = models.CharField(max_length=100)

    def __str__(self):
        return self.set_topic
    
class Blog_Category(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cat_name

class Blog_article(models.Model):
    article_id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Blog_Category, on_delete=models.CASCADE)
    article_head = models.CharField(max_length=500, null=True)
    article_summary = models.CharField(max_length=500, null=True)
    article_text = models.CharField(max_length=5000, null=True)
    article_img_url = models.TextField(null=True)
    article_author = models.CharField(max_length=100)
    article_author_profile = models.TextField(null=True)
    article_date = models.DateField()

    def __str__(self):
        return self.article_head