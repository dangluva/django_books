from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

@property
def is_overdue(self):
    if self.due_back and date.today() > self.due_back:
        return True
    return False

class Genre(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Enter the genre of the book",
                            verbose_name="Book Genre")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Enter the language of the book",
                            verbose_name="Book Language")

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Enter the publisher of the book",
                            verbose_name="Book Publisher")

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100,
                                  help_text="Enter the name of the author",
                                  verbose_name="Author Name")
    last_name = models.CharField(max_length=100,
                                 help_text="Enter the surname of the author",
                                 verbose_name="Author Surname")
    date_of_birth = models.DateField(help_text="Enter the date of birth",
                                     verbose_name="Birthday",
                                     null=True,
                                     blank=True)
    about = models.TextField(help_text="Enter the data about author",
                             verbose_name="About author")
    photo = models.ImageField(upload_to='images',
                              help_text="Upload author photo",
                              verbose_name="Author Photo",
                              null=True,
                              blank=True)

    def __str__(self):
        return self.last_name


class Book(models.Model):
    title = models.CharField(max_length=200,
                             help_text="Enter the title of the book",
                             verbose_name="Book Title")
    genre = models.ForeignKey('Genre',
                              on_delete=models.CASCADE,
                              help_text="Enter the genre of the book",
                              verbose_name="Book Genre",
                              null=True)
    language = models.ForeignKey('Language',
                                 on_delete=models.CASCADE,
                                 help_text="Enter the language of the book",
                                 verbose_name="Book Language",
                                 null=True)
    publisher = models.ForeignKey('Publisher',
                                  on_delete=models.CASCADE,
                                  help_text="Enter the publisher of the book",
                                  verbose_name="Publisher",
                                  null=True)
    year = models.CharField(max_length=4,
                            help_text="Enter the year of the book",
                            verbose_name="Book Year")
    author = models.ManyToManyField('Author',
                                    help_text="Enter the author(s) of the book",
                                    verbose_name="Book Author(s)")
    summary = models.TextField(max_length=1000,
                               help_text="Enter the short summary of the book",
                               verbose_name="Book Annotation")
    isbn = models.CharField(max_length=13,
                            help_text="It must contain 13 symbols",
                            verbose_name="ISBN of the Book")
    price = models.DecimalField(decimal_places=2,
                                max_digits=7,
                                help_text="Enter the price of the book",
                                verbose_name="Price in EUR")
    photo = models.ImageField(upload_to="images",
                              help_text="Enter the cover of the book",
                              verbose_name="Book Cover")

    def display_author(self):
        return ','.join([author.last_name for author in self.author.all()])

    display_author.short_description = 'Authors'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Status(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Enter the status of the book instance",
                            verbose_name="Book Status")

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    book = models.ForeignKey('Book',
                             on_delete=models.CASCADE,
                             null=True)
    inv_num = models.CharField(max_length=20,
                               null=True,
                               help_text="Enter the inventory number",
                               verbose_name="Inventory Number")
    status = models.ForeignKey('Status',
                               on_delete=models.CASCADE,
                               null=True,
                               help_text="Change the status of the book",
                               verbose_name='Status of the book')
    due_back = models.DateField(null=True,
                                blank=True,
                                help_text="Enter the due date",
                                verbose_name="Due date")
    borrower = models.ForeignKey(User,
                                 on_delete= models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 verbose_name='Customer',
                                 help_text='Choose Customer',
                                 )

    class Meta:
        ordering = ["due_back"]

        def __str__(self):
            return '%s %s %s' % (self.inv_num, self.book, self.status)
