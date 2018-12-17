from django.urls import path
from rest_framework import routers
from . import views
from .views import PostViewSet

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
