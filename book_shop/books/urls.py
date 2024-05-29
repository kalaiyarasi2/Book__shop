"""from django.urls import path
from .views import BookListCreate, BookRetrieveUpdateDestroy, AuthorListCreate, AuthorRetrieveUpdateDestroy, GenreListCreate, GenreRetrieveUpdateDestroy

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroy.as_view(), name='author-retrieve-update-destroy'),
    path('genres/', GenreListCreate.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroy.as_view(), name='genre-retrieve-update-destroy'),
]
from django.urls import path, include

urlpatterns = [
    path('api/', include('book_shop.urls')),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('library.urls')),  # Include the library app URLs
]"""
from django.urls import path
from .views import BookListCreate, BookRetrieveUpdateDestroy, AuthorListCreate, AuthorRetrieveUpdateDestroy, GenreListCreate, GenreRetrieveUpdateDestroy

urlpatterns = [
    # Book URLs
    path('books/', BookListCreate.as_view(), name='book_list_create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book_retrieve_update_destroy'),

    # Author URLs
    path('authors/', AuthorListCreate.as_view(), name='author_list_create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroy.as_view(), name='author_retrieve_update_destroy'),

    # Genre URLs
    path('genres/', GenreListCreate.as_view(), name='genre_list_create'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroy.as_view(), name='genre_retrieve_update_destroy'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),  # Include the library app URLs
]
