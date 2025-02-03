from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime

from psycopg2.errorcodes import NULL_VALUE_NOT_ALLOWED

User = get_user_model()


class Post(models.Model):
      text=models.TextField(max_length=256,default='прекрасное фото')
      image = models.ImageField(upload_to='static',verbose_name='Изображение',default=1)
      created_at=models.DateTimeField(null=True,default=datetime.now)


      def __str__(self):
            return self.text

      class Meta:
          verbose_name = 'Фотография'
          verbose_name_plural = 'Фотографии'


# для доп. задания
# class PostImage(models.Model):
#     ...


class Like(models.Model):
      likes = models.ManyToManyField(User, blank=True, related_name='likes')
      likes_user = models.ManyToManyField(User, blank=True, related_name='нравится')

      def __str__(self):
            return self.likes



      class Meta:
          verbose_name = 'Лайк'
          verbose_name_plural = 'Лайки'

class Comment(models.Model):
      comment=models.TextField(max_length=500,default='класс')
      comment_user = models.ManyToManyField(User, blank=True, related_name='коммент')
      def __str__(self):
            return self.comment

      class Meta:
          verbose_name = 'Комментарий'
          verbose_name_plural = 'Комментарии'