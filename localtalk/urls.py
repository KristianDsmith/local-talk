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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog.views import home, ArtistListView, ArtistDetailView, ArtistCreateView, ArtistUpdateView, ArtistDeleteView, RecordListView, RecordDetailView
from blog.views import blog_list, blog_detail, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('artists/', ArtistListView.as_view(), name='artist-list'),
    path('artist/<int:pk>/', ArtistDetailView.as_view(), name='artist-detail'),
    path('artists/create/', ArtistCreateView.as_view(), name='artist-create'),
    path('artist/<int:pk>/update/',
         ArtistUpdateView.as_view(), name='artist-update'),
    path('artist/<int:pk>/delete/',
         ArtistDeleteView.as_view(), name='artist-delete'),
    path('records/', RecordListView.as_view(), name='record-list'),
    path('record/<int:pk>/', RecordDetailView.as_view(), name='record-detail'),
    path('blog/', blog_list, name='blog-list'),
    path('blog/<int:pk>/', blog_detail, name='blog-detail'),
    path('contact/', contact, name='contact'),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
