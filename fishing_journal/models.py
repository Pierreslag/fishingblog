from django.db import models
from django.contrib.auth.models import User


class FishingJournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    catch_details = models.TextField()
    notes = models.TextField(blank=True)

    class Meta:
        app_label = 'fishing_journal'
