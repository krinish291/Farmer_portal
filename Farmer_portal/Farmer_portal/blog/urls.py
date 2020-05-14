from django.urls import path
from django.conf.urls import url

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    QueryCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    typecon,
    price,
    querygenerate,
    addquery,
    myQueryans,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('Query/new/', QueryCreateView.as_view(), name='Query-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    url(r'^like/$',views.like,name='like'),
    url(r'^disLike/$',views.disLike,name='disLike'),
    url(r'^filter/$', typecon),
    url(r'^myQueryans/$', myQueryans),
    url(r'^price/$', price),
    url(r'^addquery/$', addquery),
    url(r'^querygenerate/$', querygenerate),

]
