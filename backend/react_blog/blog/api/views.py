from rest_framework import viewsets

from blog.models import Blog
from blog.api.serializers import BlogSerializer

class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer(queryset, many=True)