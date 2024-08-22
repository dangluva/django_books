from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),

    # Book-related URLs
    path('books/', login_required(views.BookListView.as_view()), name='books'),
    path('books/<int:pk>/', login_required(views.BookDetailView.as_view()), name='book-detail'),
    path('book/create/', login_required(views.BookCreate.as_view()), name='book-create'),
    path('edit_books/', login_required(views.edit_books), name='edit-books'),
    path('book/update/<int:pk>/', login_required(views.BookUpdate.as_view()), name='book-update'),
    path('book/delete/<int:pk>/', login_required(views.BookDelete.as_view()), name='book-delete'),

    # Author-related URLs
    path('authors/', login_required(views.AuthorListView.as_view()), name='authors-list'),
    path('authors/<int:pk>/', login_required(views.AuthorDetailView.as_view()), name='authors-detail'),
    path('authors_add/', login_required(views.add_author), name='authors-add'),
    path('edit_authors/', login_required(views.edit_authors), name='edit-authors'),
    path('edit_author/<int:id>/', login_required(views.edit_author), name='edit-author'),
    path('delete_author/<int:id>/', login_required(views.delete_author), name='delete-author'),

    # User-specific URLs
    path('mybooks/', login_required(views.LoanedBooksByUserListView.as_view()), name='my-borrowed-books'),
]
