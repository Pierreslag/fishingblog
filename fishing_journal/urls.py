from django.urls import path
from . import views

app_name = 'fishing_journal'

urlpatterns = [
    path('create/', views.create_entry, name='create_entry'),
    path('update/<int:entry_id>/', views.update_entry, name='update_entry'),
    path('delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    path('entry_base/', views.entry_base, name='entry_base'),
]
