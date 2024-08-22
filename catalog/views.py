from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render
from .models import Book, Author, BookInstance
from django.views.generic import ListView, DetailView
from .forms import FormAddAuthor, FormEditAuthor
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class AuthorDetailView(DetailView):
    model = Author


class AuthorListView(ListView):
    model = Author
    paginate_by = 5


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 5


class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('edit-books')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Create a New Book'
        return context


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('edit-books')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Edit the Book'
        return context


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('edit-books')


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')


def index(request):
    # Get the list of books with pagination
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 4)  # 4 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Calculate statistics
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    authors = Author.objects.all()
    num_authors = Author.objects.count()

    # Track visits to the site
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'page_obj': page_obj,
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'authors': authors,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    return render(request, 'catalog/index.html', context)


def about(request):
    text_head = "Data about Company"
    name = "Intellectual IT Systems"
    rab1 = "Software development based on AI"
    rab2 = "Recognizing road signs"
    rab3 = "Creation of art objects based on AI"
    rab4 = "Creation of digital interactive books, automated teaching systems"
    context = {
        'text_head': text_head,
        'name': name,
        'rab1': rab1,
        'rab2': rab2,
        'rab3': rab3,
        'rab4': rab4,
    }
    return render(request, 'catalog/about.html', context)


def contacts(request):
    text_head = "Contacts"
    name = "Intellectual IT Systems"
    address = "Gelvonu str. 35-20"
    telephone_number = "+37067178956"
    email = "dangluva@gmail.com"
    context = {
        'text_head': text_head,
        'name': name,
        'address': address,
        'telephone_number': telephone_number,
        'email': email,
    }
    return render(request, 'catalog/contacts.html', context)


def edit_author(request, id):
    author = Author.objects.get(id=id)
    # author = get_object_or_404(Author, pk=id)
    if request.method == 'POST':
        instance = Author.objects.get(pk=id)
        form = FormEditAuthor(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/edit_authors/')
    else:
        form = FormEditAuthor(instance=author)
        context = {
            'form': form,
        }
        return render(request, 'catalog/edit_author.html', context)


def edit_authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors,
    }
    return render(request, 'catalog/edit_authors.html', context)


# Creating new author in the database
def add_author(request):
    if request.method == "POST":
        form = FormAddAuthor(request.POST, request.FILES)
        if form.is_valid():
            # Get data from the form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            about = form.cleaned_data['about']
            photo = form.cleaned_data['photo']

            # Create and save the new author
            author = Author(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                about=about,
                photo=photo
            )
            author.save()
            # Redirect to the authors list view
            return HttpResponseRedirect(reverse('authors-list'))
    else:
        form = FormAddAuthor()

    context = {
        'form': form,
    }
    return render(request, 'catalog/authors_add.html', context)


# Deleting authors from the database
def delete_author(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect('/edit_authors/')
    except:
        return HttpResponseNotFound('<h2>Author is not found.</h2>')


def edit_books(request):
    book = Book.objects.all()
    context = {
        'book': book,
    }
    return render(request, 'catalog/edit_books.html', context)
