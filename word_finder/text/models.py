from django.db import models
from user.models import User

class Paragraph(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Word(models.Model):
    word = models.CharField(max_length=100)
    Paragraph = models.ForeignKey(Paragraph, related_name='words', on_delete=models.CASCADE)
