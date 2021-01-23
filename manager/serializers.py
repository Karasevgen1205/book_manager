from rest_framework.serializers import ModelSerializer
from manager.models import Comment, LikeComment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class LikeCommentUserSerialize(ModelSerializer):
    class Meta:
        model = LikeComment
        fields = "__all__"