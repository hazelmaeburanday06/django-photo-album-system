from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Photo
from .forms import PhotoForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Album, Photo
from .forms import AlbumForm, PhotoForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.urls import reverse


class PhotoCreateView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'albums/photo_upload.html'

    def form_valid(self, form):

        album = Album.objects.get(
            id=self.kwargs['pk']
        )

        form.instance.album = album

        return super().form_valid(form)

    def get_success_url(self):

        return reverse(
            'album-detail',
            kwargs={'pk': self.kwargs['pk']}
        )


class HomeView(TemplateView):
    template_name = "albums/home.html"

class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'albums/album_list.html'

    def get_queryset(self):
        return Album.objects.filter(
            owner=self.request.user
        )


class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'albums/album_detail.html'

    def get_queryset(self):
        return Album.objects.filter(
            owner=self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['photos'] = Photo.objects.filter(
            album=self.object
        )

        return context
class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/form.html'
    success_url = reverse_lazy('album-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/form.html'
    success_url = reverse_lazy('album-list')

    def get_queryset(self):
        return Album.objects.filter(
            owner=self.request.user
        )


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'albums/delete.html'
    success_url = reverse_lazy('album-list')

    def get_queryset(self):
        return Album.objects.filter(
            owner=self.request.user
        )


class PhotoCreateView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'albums/photo_upload.html'

    def form_valid(self, form):

        album = Album.objects.get(
            id=self.kwargs['pk']
        )

        form.instance.album = album

        return super().form_valid(form)

    def get_success_url(self):

        return reverse(
            'album-detail',
            kwargs={'pk': self.kwargs['pk']}
        )
def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(request,'registration/signup.html',{
        'form':form
    })