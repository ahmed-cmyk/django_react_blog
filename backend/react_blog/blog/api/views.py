from rest_framework import viewsets
from rest_framework.response import Response

from blog.models import Blog
from blog.api.serializers import BlogSerializer

class BlogView(viewsets.ViewSet):

      def list(self, request):
        queryset = Blog.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)
        