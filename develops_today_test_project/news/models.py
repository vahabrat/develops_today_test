
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db import models

from django.conf import settings


class Post(models.Model):

    title = models.TextField('Текст (название) поста')
    link = models.CharField('Ссылка на пост', max_length=250, blank=True)
    creation_date = models.DateTimeField('Дата публикации поста', auto_now_add=True)
    amount_of_upvotes = models.IntegerField(default=0)
    author_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name='posts',)

    #def get_absolute_link(self):
        #print('urigurisdusi')
        #return settings.BASE_URL + reverse('news:detail_post', args=[self.id])
        #Post.objects.filter(id=self.id)
        #print(link)
        #link='http://127.0.0.1:8000/news/create/'+self.id
        #post=Post.objects.filter(id=self.id)

    def save(self,**kwargs):
        #self.link = self.get_absolute_link()
        #print('ujyrguyrsulys')
        super().save(**kwargs)  # сохранение обьекта в базу данных
        self.link = settings.BASE_URL + reverse('news:detail_post', args=[self.id])
        super().save()  # сохранить объект в базу данных




class Comment(models.Model):
    author_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name='comments')
    post = models.ForeignKey('Post', on_delete=models.CASCADE,)
    content = models.TextField('Текст комментария')
    creation_date = models.DateTimeField('Дата публикации комментария', auto_now_add=True)

# Create your models here.
