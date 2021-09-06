from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect
from django.urls import reverse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import HttpResponse
from .models import Post
from .serializers import PostSerializer


def index(request):
    return render(request, 'mysite/index.html')

@api_view(['GET'])
def get_api(request):
    posts = Post.objects.all()
    serialized_posts = PostSerializer(posts, many = True)
    return Response(serialized_posts.data)

@api_view(['POST'])
def post_api(request):
    if request.method == 'GET':
        return HttpResponse(status = 200)
    if request.method == 'POST':
        serializer = PostSerializer(data = request.data, many = True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)