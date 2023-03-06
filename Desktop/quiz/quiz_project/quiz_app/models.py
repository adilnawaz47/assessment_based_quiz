# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    question = models.CharField(max_length=255)

class Answer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    score = models.IntegerField(default=0)

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)


# class Quiz(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     topic = models.CharField(max_length=255)

# class Question(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     text = models.TextField()

# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     text = models.TextField()
#     is_correct = models.BooleanField(default=False)
