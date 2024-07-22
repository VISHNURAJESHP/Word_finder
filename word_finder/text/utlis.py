from .models import  Word

def tokenize_and_index_paragraphs(paragraph):
  
    paragraph_text = paragraph.content
    words = paragraph_text.split()

    # Convert words to lowercase
    words_lower = [word.lower() for word in words]

    # Index words against the paragraph
    for word_lower in words_lower:
        Word.objects.create(word=word_lower, paragraph=paragraph)