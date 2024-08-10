from django.contrib import admin
from django.utils.html import format_html
# Importing the models from the current app's models module
from .models import Author, Book, Genre, Language, Publisher, Status, BookInstance


# Creating a custom admin class for the Author model.
# This class can be used to customize the admin interface for the Author model.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'photo', 'show_photo')
    fields = ['last_name', 'first_name', ('date_of_birth', 'photo')]
    readonly_fields = ['show_photo']

    def show_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-height: 100px;">', obj.photo.url)
        return "No Photo"

    show_photo.short_description = 'Photo'


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author', 'show_photo')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInline]
    readonly_fields = ['show_photo']

    def show_photo(self, obj):
        return format_html(f'<img src="{obj.photo.url}" style="max-height: 100px;">')

    show_photo.short_description = "Cover"


# Using the decorator to register the BookInstance model with the custom admin interface.
# This means the BookInstance model will be managed via the admin interface using BookInstanceAdmin settings.
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('book', 'status')
    fieldsets = (
        ('Book Instance', {'fields': ('book', 'inv_num')}
         ),
        ('Status and Due Date', {'fields': ('status', 'due_back', 'borrower')}),
    )


# Registering the Author model with the admin site using the AuthorAdmin class for customization.
admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)

admin.site.register(Language)

admin.site.register(Publisher)

admin.site.register(Status)
