from rest_framework import serializers
from models import Comment
from models import Post
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        field=('id','comment')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        field=('id','text','image','created_at')