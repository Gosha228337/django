from django.db import models
class Question(models.Model):
    qustion_text = models.CharField(max_length=200)
    pud_date = models.DateTimeField('date published')

class Choise(models.Model):
    qustion = models.ForeignKey(Question,on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)