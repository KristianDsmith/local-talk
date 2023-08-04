"""localtalk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import home, ArtistListView, ArtistDetailView, ArtistCreateView, ArtistUpdateView, ArtistDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('artists/', ArtistListView.as_view(), name='artist_list'),
    path('artist/<int:pk>/', ArtistDetailView.as_view(), name='artist_detail'),
    path('artist/new/', ArtistCreateView.as_view(), name='artist_new'),
    path('artist/<int:pk>/edit/', ArtistUpdateView.as_view(), name='artist_edit'),
    path('artist/<int:pk>/delete/',
         ArtistDeleteView.as_view(), name='artist_delete'),
]
