from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from django.shortcuts import render

from .forms import BookForm
from .models import Book



def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)  # 🔥 MUHIM
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)  # 🔥 MUHIM

    return render(request, 'edit_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
