from django.shortcuts import render, redirect, get_object_or_404
from .models import FishingJournalEntry
from .forms import FishingJournalEntryForm
from django.contrib.auth.decorators import login_required


@login_required
def entry_base(request):
    entries = FishingJournalEntry.objects.filter(user=request.user)
    return render(request, 'fishing_journal/entry_base.html', {'entries': entries})


@login_required
def create_entry(request):
    if request.method == 'POST':
        form = FishingJournalEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('fishing_journal:entry_base')
    else:
        form = FishingJournalEntryForm()
    return render(request, 'fishing_journal/create_entry.html', {'form': form})


@login_required
def update_entry(request, entry_id):
    entry = get_object_or_404(FishingJournalEntry, id=entry_id, user=request.user)

    if request.method == 'POST':
        form = FishingJournalEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('fishing_journal:entry_base')

    form = FishingJournalEntryForm(instance=entry)
    return render(request, 'fishing_journal/update_entry.html', {'form': form})


@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(FishingJournalEntry, id=entry_id, user=request.user)

    if request.method == 'POST':
        entry.delete()
        return redirect('fishing_journal:entry_base')

    return render(request, 'fishing_journal/delete_entry.html', {'entry': entry})