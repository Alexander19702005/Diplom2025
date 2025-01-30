from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.base import kwarg_re
from yaml import serialize

from .models import  Like
from .models import Comment
from .models import Post
from .serializers import CommentSerializer
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



class AddLike(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):
        post = Like.objects.get(pk=pk)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break


        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        return HttpResponseRedirect(reverse('like', args=[str(pk)]))



class AddDislike(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):
        post = Like.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)



        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        return HttpResponseRedirect(reverse('like', args=[str(pk)]))

# Create your views here.
