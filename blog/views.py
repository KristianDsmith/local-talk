from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Artist, Record, BlogPost

from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    latest_blog_posts = BlogPost.objects.order_by('-pub_date')[:2]
    latest_releases = Record.objects.filter(
        category='LATEST').order_by('-release_date')[:4]
    albums = Record.objects.filter(
        category='ALBUM').order_by('-release_date')[:4]
    singles = Record.objects.filter(
        category='SINGLE').order_by('-release_date')[:4]
    
    context = {
        'latest_blog_posts': latest_blog_posts, # Corrected variable name here
        'latest_releases': latest_releases,
        'albums': albums,
        'singles': singles,
    }

    return render(request, 'home.html', context)





class ArtistListView(ListView):
    model = Artist
    template_name = 'artist_list.html'
    context_object_name = 'artists'

    def get_queryset(self):
        return Artist.objects.order_by('name')


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


class RecordListView(ListView):
    model = Record
    template_name = 'record_list.html'
    context_object_name = 'records'


class RecordDetailView(DetailView):
    model = Record
    template_name = 'record_detail.html'
    context_object_name = 'record'


def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'blog_posts': blog_posts})

def blog_detail(request, pk):
    blog_post = BlogPost.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'blog_post': blog_post})

def contact(request):
    return render(request, 'contact.html')