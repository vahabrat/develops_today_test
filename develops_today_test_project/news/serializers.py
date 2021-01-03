from rest_framework import serializers
from .models import Post, Comment


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title',
                  'author_name',
                  )


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'link',
                  'creation_date',
                  'amount_of_upvotes',
                  'author_name',
                  )


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',
                  'creation_date',
                  'id')


###############################

class Figure:
    def draw(self):
        #raise NotImplementedError
        print('Я не знаю как рисовать себя потому что я абстрактная фигура')

class Square:
    def draw(self):
        print('Рисуем квадрат')

class Circle:
    def draw(self):
        print('Рисуем круг')

obj =Figure()