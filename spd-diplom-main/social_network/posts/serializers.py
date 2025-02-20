from rest_framework import serializers
#from .models import Message
from .models import Post
from .models import Post_1
from .models import Like
from .models import Message
from django.db.models import Count,Max,Min,Avg
#Сериализатор для лайков
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
#

#Сериализатор для комментариев старый
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields='__all__'
#Сериализатор для постов с фото
class PostSerializer(serializers.ModelSerializer):
    #comments=Post_1Serializer(many=False,read_only=True,source='image')
    #likes=LikeSerializer(many=True,read_only=True,source='post')
    #comments_1 = Post_1Serializer(many=True, read_only=True)
    class Meta:
        model=Post
        fields='__all__'
 #  Сериализатор    для    комментариев

class Post_1Serializer(serializers.ModelSerializer):
    comments = PostSerializer(many=False, read_only=True, source='image')
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return Like.objects.aggregate(likes_count=Count('like'))
        #return Like.objects.filter(post=obj.post).count()

    #likes = Like.object.aggregate(Count('like'))
    class Meta:
        model = Post_1
        fields =['id','text_1','user','created_at','image','comments','likes_count']
    #def likes_count(self,likes):
        #return likes.like.aggregate(Count('like'))


    #def create(self, validated_data):
        #comments_data = validated_data.pop('comments')
        #post = Post.objects.create(**validated_data)
        #for comments_data in comments_data:
            #Post.objects.create(post=post, **comments_data)
        #return post


