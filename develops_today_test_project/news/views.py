
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Post
from .serializers import PostListSerializer, CommentListSerializer, PostCreateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


########################Post##########################

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = (AllowAny,)



class PostRetrieveView(generics.RetrieveAPIView):
    #serializer_class = PostListSerializer
    permission_classes = (AllowAny,)

    def get(self, request, id):
        post=Post.objects.get(id=id)
        serializer = PostListSerializer(post)
        return Response(serializer.data)






class PostUpdateView(generics.UpdateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = (AllowAny,)

class PostDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = PostListSerializer
    permission_classes = (AllowAny,)

########################Comment##########################
class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentListSerializer
    permission_classes = (AllowAny,)

class CommentRetrieveView(generics.RetrieveAPIView):
    serializer_class = CommentListSerializer
    permission_classes = (AllowAny,)

class CommentUpdateView(generics.UpdateAPIView):
    serializer_class = CommentListSerializer
    permission_classes = (AllowAny,)

class CommentDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = CommentListSerializer
    permission_classes = (AllowAny,)

# Create your views here.
