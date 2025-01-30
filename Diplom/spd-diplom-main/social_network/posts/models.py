from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime
User = get_user_model()


class Post(models.Model):
      text=models.TextField(max_length=256,default='прекрасное фото')
      image = models.ImageField(upload_to='images',verbose_name='Изображение')
      created_at=models.DateTimeField(null=True,default=datetime.now)

      def __str__(self):
            return self.text

      class Meta:
          verbose_name = 'Название фото'
          verbose_name_plural = 'Названия'


# для доп. задания
# class PostImage(models.Model):
#     ...


class Like(models.Model):
      likes = models.ManyToManyField(User, blank=True, related_name='likes')
      dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
      def __str__(self):
            return self.like

      class Meta:
          verbose_name = 'Лайк'
          verbose_name_plural = 'Лайки'
class Comment(models.Model):
      comment=models.TextField(max_length=500,default='класс')
      def __str__(self):
            return self.comment

      class Meta:
          verbose_name = 'Комментарий'
          verbose_name_plural = 'Комментарии'