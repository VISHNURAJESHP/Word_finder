from rest_framework import status
from rest_framework.response import Response
from .models import Paragraph
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from user.utils import authenticate_user
from utlis import tokenize_and_index_paragraphs

class ParagraphOperations(APIView):
    def post(request):
        token = request.COOKIES.get('jwt')

        try:
            user = authenticate_user(token)
            user_id = user.id
        except AuthenticationFailed:
            return Response({'error':'The User is not Authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            paragraphs=request.data.get('paragraphs', [])
        except:
            return Response({'error':'No data is provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        for paragraph_text in paragraphs:

            paragraph = Paragraph.objects.create(content=paragraph_text, creator=user)

            tokenize_and_index_paragraphs(paragraph)

        return Response({'message': 'Paragraphs processed successfully'}, status=status.HTTP_201_CREATED)   
