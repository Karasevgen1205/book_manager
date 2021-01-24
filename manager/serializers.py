from rest_framework.serializers import ModelSerializer
from manager.models import Comment, LikeComment, Book


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class LikeCommentUserSerializer(ModelSerializer):
    class Meta:
        model = LikeComment
        fields = "__all__"


class BookSerializer(ModelSerializer):
#    date = serializer
    class Meta:
        model = Book
        fields = ["title", "text"]
