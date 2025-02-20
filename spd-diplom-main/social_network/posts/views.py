from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.base import kwarg_re
from rest_framework.decorators import api_view
from yaml import serialize

from .models import Like
#from .models import Message
from .models import Post
from .models import Post_1
from .serializers import MessageSerializer
from .serializers import LikeSerializer
from .serializers import PostSerializer
from .serializers import Post_1Serializer

from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
<<<<<<< HEAD
from django.db.models import Count,Max,Min,Avg
=======
>>>>>>> ea163d5ff6bbce2a44a8e5f39315c7e6db34870b


@api_view(["GET","POST"],)
class MessageView(APIView):
    def get(self, request, *arqs, **kwargs):
         queryset = Message.objects.all()
         serializer = MessageSerializer(queryset, many=True)
         return Response(serializer.data)


class PostView(APIView):
    def get (self,request, *arqs , **kwargs):
        #post = Post.objects.create(post='Сочи 2015',created_at ='default')
        queryset=Post.objects.all()
        serializer=PostSerializer(queryset,many=True)
        return Response(serializer.data)



class LikeView(APIView):
    def get (self,request, *arqs , **kwargs):
        queryset=Like.objects.all()
        serializer=LikeSerializer(queryset,many=True)
        return Response(serializer.data)


class Post_1View(APIView):
    def get (self,request, *arqs , **kwargs):
        #post = Post.objects.create(post='Сочи 2015',created_at ='default')
        queryset=Post_1.objects.all()
        serializer=Post_1Serializer(queryset,many=True)
        return Response(serializer.data)
<<<<<<< HEAD
    def Likes(request):
        likes=Like.object.aggregate(Count('like'))
        return Response

=======
>>>>>>> ea163d5ff6bbce2a44a8e5f39315c7e6db34870b


# Create your views here.
