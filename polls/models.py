from django.db import models


class Question(models.Model):
    question_category = models.CharField(max_length=45)
    question_text = models.CharField(max_length=200)
    point = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
