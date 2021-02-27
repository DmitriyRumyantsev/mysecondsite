from django.db import models

#Модель для отработки вопроса

class Question(models.Model):
    text = models.CharField(max_length=500)
    pubDate = models.DateTimeField('date published')

    def __str__(self):
        return self.text

#модель для отработки ответа

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


    text = models.CharField(max_length=500)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text