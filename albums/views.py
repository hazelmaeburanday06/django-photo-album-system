from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Album, Photo

class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'albums/album_list.html'


class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'albums/album_detail.html'


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['title', 'description']
    template_name = 'albums/form.html'
    success_url = reverse_lazy('album-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AlbumUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Album
    fields = ['title', 'description']
    template_name = 'albums/form.html'
    success_url = reverse_lazy('album-list')

    def test_func(self):
        album = self.get_object()
        return self.request.user == album.owner or self.request.user.is_superuser


class AlbumDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Album
    template_name = 'albums/delete.html'
    success_url = reverse_lazy('album-list')

    def test_func(self):
        album = self.get_object()
        return self.request.user == album.owner or self.request.user.is_superuser


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['album', 'image', 'caption']
    template_name = 'albums/form.html'
    success_url = reverse_lazy('album-list')