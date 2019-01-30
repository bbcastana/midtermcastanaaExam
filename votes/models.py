from django.db import models
from datetime import datetime

# Create your models here.
class Candidate(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    bday = models.DateTimeField(default=datetime.now)
    position = models.CharField(max_length=100)
    platform = models.TextField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'Title: {}'.format(self.title)

class Votes(models.Model):
    Vote_date = models.DateTimeField(default=datetime.now)
    cois_acntent = models.TextField(max_length=200)
    candidate = models.ForeignKey(Candidate,
                on_delete=models.CASCADE,
                related_name='comments',
                null=True, blank=True)
