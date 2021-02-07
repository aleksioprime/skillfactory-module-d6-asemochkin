from django.shortcuts import render,redirect
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from home_library.models import Book, Author, Publisher, Friend
from django.urls import reverse_lazy

class BookList(ListView):
    model = Book
    context_object_name = "books"
    template_name = "book_list.html"

class BookDetail(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'book_add.html'
    def get_form(self, form_class=None):
        form = super(BookCreate, self).get_form(form_class)
        form.fields['copy_count'].required = False
        form.fields['price'].required = False
        form.fields['ISBN'].required = False
        form.fields['friends'].required = False
        return form

class BookEdit(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'book_edit.html'
    def get_form(self, form_class=None):
        form = super(BookEdit, self).get_form(form_class)
        form.fields['copy_count'].required = False
        form.fields['price'].required = False
        form.fields['ISBN'].required = False
        form.fields['friends'].required = False
        return form
    @staticmethod
    def return_book(request):
        if request.method == 'POST':
            book_id = request.POST['id']
            if not book_id:
                return redirect(reverse_lazy('home_library:index'))
            else:
                book = Book.objects.filter(id=book_id).first()
                if not book:
                    return redirect(reverse_lazy('home_library:index'))
                book.friends = None
                book.save()
        return redirect(reverse_lazy('home_library:index'))

class BookDelete(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('home_library:index')

class AuthorList(ListView):
    model = Author
    context_object_name = "authors"
    template_name = "author_list.html"

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    template_name = 'author_add.html'

class AuthorEdit(UpdateView):
    model = Author
    fields = '__all__'
    template_name = 'author_edit.html'

class AuthorDelete(DeleteView):
    model = Author
    template_name = 'author_delete.html'
    success_url = reverse_lazy('home_library:authors')

class PublisherList(ListView):
    model = Publisher
    context_object_name = "publishers"
    template_name = "publisher_list.html"

class PublisherCreate(CreateView):
    model = Publisher
    fields = '__all__'
    template_name = 'publisher_add.html'

class PublisherEdit(UpdateView):
    model = Publisher
    fields = '__all__'
    template_name = 'publisher_edit.html'

class PublisherDelete(DeleteView):
    model = Publisher
    template_name = 'publisher_delete.html'
    success_url = reverse_lazy('home_library:publishers')

class FriendList(ListView):
    model = Friend
    context_object_name = "friends"
    template_name = "friend_list.html"

class FriendCreate(CreateView):
    model = Friend
    fields = '__all__'
    template_name = 'friend_add.html'

class FriendEdit(UpdateView):
    model = Friend
    fields = '__all__'
    template_name = 'friend_edit.html'

class FriendDelete(DeleteView):
    model = Friend
    template_name = 'friend_delete.html'
    success_url = reverse_lazy('home_library:friends')