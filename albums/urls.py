from django.urls import path
from .views import (
    AlbumListView,
    AlbumDetailView,
    AlbumCreateView,
    AlbumUpdateView,
    AlbumDeleteView,
    PhotoCreateView
)

urlpatterns = [
    path('', AlbumListView.as_view(), name='album-list'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),
    path('album/create/', AlbumCreateView.as_view(), name='album-create'),
    path('album/<int:pk>/update/', AlbumUpdateView.as_view(), name='album-update'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album-delete'),
    path('photo/create/', PhotoCreateView.as_view(), name='photo-create'),
]