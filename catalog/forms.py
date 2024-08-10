from django import forms
from datetime import date
from .models import Author, Book


# Form to add new authors to the database
class FormAddAuthor(forms.Form):
    first_name = forms.CharField(label="Author Name")
    last_name = forms.CharField(label="Author Surname")
    date_of_birth = forms.DateField(
        label="Birthdate",
        initial=format(date.today()),
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    about = forms.CharField(label="Data About Author", widget=forms.Textarea)
    photo = forms.ImageField(label="Author Photo")


class FormEditAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
