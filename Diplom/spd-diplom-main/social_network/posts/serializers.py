from rest_framework import serializers
from models import Comment
from models import Post
from models import Like
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        field=('id','comment')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        field=('id','text','image','created_at')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        field = ('likes', 'dislikes')