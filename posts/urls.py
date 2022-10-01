from django.urls import path
from .views import (
    PostListView,
    DraftPostListView,
    PublishedPostListView,
    ArchivedPostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)


urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('drafts/', DraftPostListView.as_view(), name='draft_list'),
    path('published/', PublishedPostListView.as_view(), name='published_list'),
    path('archived/', ArchivedPostListView.as_view(), name='archived_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]
