from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Artist
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'home.html')


class ArtistListView(ListView):
    model = Artist
    template_name = 'artist_list.html'
    context_object_name = 'artists'


class ArtistDetailView(UpdateView):
    model = Artist
    fields = ['name', 'bio', 'image']
    template_name = 'artist_detail.html'
    success_url = '/artists/'


class ArtistCreateView(CreateView):
    model = Artist
    fields = ['name', 'bio', 'image']
    template_name = 'artist_form.html'
    success_url = '/artists/'


class ArtistUpdateView(UpdateView):
    model = Artist
    fields = ['name', 'bio', 'image']
    template_name = 'artist_form.html'
    success_url = '/artists/'


class ArtistDeleteView(DeleteView):
    model = Artist
    template_name = 'artist_confirm_delete.html'
    success_url = '/artists/'
