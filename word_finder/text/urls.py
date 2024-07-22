from django.urls import path
from .views import ParagraphOperations, WordSearching

urlpatterns = [
    path('process-paragraphs', ParagraphOperations.as_view(), name='process_paragraphs'),
    path('search-word', WordSearching.as_view(), name='search_word')
]