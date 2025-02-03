from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.base import kwarg_re
from yaml import serialize

from .models import  Like
from .models import Comment
from .models import Post
from .serializers import CommentSerializer
from .serializers import LikeSerializer
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response

class CommentView(APIView):
    def get (self,request, *arqs , **kwargs):
        queryset=Comment.objects.all()
        serializer=CommentSerializer(queryset,many=True)
        return Response.serializer.data

class PostView(APIView):
    def get (self,request, *arqs , **kwargs):
        queryset=Post.objects.all()
        serializer=CommentSerializer(queryset,many=True)
        return Response.serializer.data



class LikeView(APIView):
    def get (self,request, *arqs , **kwargs):
        queryset=Like.objects.all()
        serializer=LikeSerializer(queryset,many=True)
        return Response.serializer.data





# Create your views here.
