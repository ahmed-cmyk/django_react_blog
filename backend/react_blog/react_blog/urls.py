from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

from blog.api.views import BlogView

router = routers.DefaultRouter()
router.register(r'blogs', BlogView, 'blog')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
