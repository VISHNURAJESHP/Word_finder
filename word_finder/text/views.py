from rest_framework import status
from rest_framework.response import Response
from .models import Paragraph
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from user.utils import authenticate_user
from .utlis import tokenize_and_index_paragraphs
from django.db.models import Count
from django.http import JsonResponse
import json

class ParagraphOperations(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')

        try:
            user = authenticate_user(token)
            user_id = user.id
        except AuthenticationFailed:
            return Response({'error':'The User is not Authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
        content = request.data.get('content', '')
        if not content:
            return Response({'error': 'No data is provided'}, status=status.HTTP_400_BAD_REQUEST)

        paragraphs = content.split('\n\n')
        
        for paragraph_text in paragraphs:

            paragraph = Paragraph.objects.create(content=paragraph_text, creator=user)

            tokenize_and_index_paragraphs(paragraph)

        return Response({'message': 'Paragraphs processed successfully'}, status=status.HTTP_201_CREATED) 


class WordSearching(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        try:
            user = authenticate_user(token)
        except AuthenticationFailed:
            return Response({'error':'The User is not Authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            data = json.loads(request.body)
            search_word = data.get('word', '').strip().lower()
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        if not search_word:
            return JsonResponse({'error': 'No word provided'}, status=400)

        # Retrieve top 10 paragraphs where the word is present and associated with the logged-in user
        paragraphs = (
            Paragraph.objects
            .filter(creator=user)  # Filter by the logged-in user
            .filter(words__word=search_word)  # Filter by the specified word
            .annotate(word_count=Count('words'))  # Count occurrences of the word in each paragraph
            .order_by('-word_count')[:10]  # Order by word count in descending order, limit to top 10
        )

        # Prepare the response data
        result = [{'id': p.id, 'content': p.content} for p in paragraphs]
        return Response({'paragraphs': result})