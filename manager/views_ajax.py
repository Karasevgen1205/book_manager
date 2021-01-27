from requests import auth
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from manager.models import LikeComment, Comment, Book
from rest_framework.generics import DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView, ListCreateAPIView
from manager.permissions import IsAuthor
from manager.serializers import CommentSerializer, LikeCommentUserSerializer, BookSerializer



class AddLikeComment(RetrieveUpdateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LikeCommentUserSerializer
    queryset = LikeComment.objects.all()

    def get_object(self):
        return None


class DeleteComment(DestroyAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAuthor]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CreateBook(CreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.object.all()


class CreateToken(CreateAPIView):
    def post(self, request):
        login = request.data.get('login')
        pwd = request.data.get('pwd')
        user = auth.authenticate(request, username=login, password=pwd)
        if user is not None:
            token = Token.objects.get_or_create(user=user)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)