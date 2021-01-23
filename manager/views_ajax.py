from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from manager.models import LikeComment, Comment, Book
from rest_framework.generics import DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
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
