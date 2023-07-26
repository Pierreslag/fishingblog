from django import forms
from .models import FishingJournalEntry


class FishingJournalEntryForm(forms.ModelForm):
    class Meta:
        model = FishingJournalEntry
        fields = ['title', 'location', 'date', 'catch_details', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
