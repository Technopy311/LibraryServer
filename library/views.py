from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q

from .models import Book

from random import randrange


def index(request):
    template = loader.get_template('library/index.html')

    i = 0
    book_count = Book.objects.all().count()

    # Check that the results ar not the same until they hit different
    while i == 0:
        first_id = randrange(1, book_count)
        second_id = randrange(1, book_count)

        if first_id != second_id:
            i = 1
    
    # Retrive the values of each selected book and pass it as response (context).
    first = Book.objects.get(pk=first_id)
    second = Book.objects.get(pk=second_id)

    context = {
        "primero": first.title,
        "primero_description": first.description,
        "primer_id": first_id,
        "segundo": second.title,
        "segundo_description": second.description,
        "segundo_id": second_id,
    }

    return HttpResponse(template.render(context, request))


# Class of the searching view
class SearchView(ListView):
    model = Book
    template_name = 'library/search.html'
    
    def get_queryset(self):
        query = self.request.GET.get("q")        

        if query == None:
            query = ''
            return []
        
        else:
            object_list = Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(description__icontains=query)
            )
            return object_list


# Function to show the person's profile
def profile(request):
    template = loader.get_template('library/profile.html')
    return HttpResponse(template.render())


# Function to register a new normal user
def register(request):
    template = loader.get_template('library/register.html')
    return HttpResponse(template.render())


# The function that shows a detail of each book
def book(request, bookid):
    template = loader.get_template('library/book.html')
    book = Book.objects.get(pk=bookid)
    context = {
        "id": book.pk,
        "title": book.title,
        "author": book.author,
        "description": book.description,
        "pages": book.last_page,
    }
    return HttpResponse(template.render(context, request))

