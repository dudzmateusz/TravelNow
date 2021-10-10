import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin



class Schedule(models.Model):
    originplace = models.CharField(max_length=200)
    outboundpartialdate = models.DateField(auto_now=False, auto_now_add=False)
    destinationplace = models.CharField(max_length=200)
    inboundpartialdate = models.DateField(auto_now=False, auto_now_add=False,blank=True)
    telephone = models.CharField(max_length=12,blank=True)
    adults = models.IntegerField(blank=True)

    def __str__(self):
        return self.originplace

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text