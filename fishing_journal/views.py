from django.shortcuts import render, redirect, get_object_or_404
from .models import FishingJournalEntry
from .forms import FishingJournalEntryForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView


@login_required
def entry_base(request):
    return ListView.as_view(
        model=FishingJournalEntry,
        paginate_by=1,
        template_name='fishing_journal/entry_base.html',
        context_object_name='entries',
        queryset=FishingJournalEntry.objects.filter(user=request.user),
    )(request)


@login_required
def create_entry(request):
    if request.method == 'POST':
        form = FishingJournalEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, 'Entry Saved')
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
            messages.success(request, 'Entry Updated')
            return redirect('fishing_journal:entry_base')

    form = FishingJournalEntryForm(instance=entry)
    return render(request, 'fishing_journal/update_entry.html', {'form': form})


@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(FishingJournalEntry, id=entry_id, user=request.user)

    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Entry Deleted')
        return redirect('fishing_journal:entry_base')

    return render(request, 'fishing_journal/delete_entry.html', {'entry': entry})
