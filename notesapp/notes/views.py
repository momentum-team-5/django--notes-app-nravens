from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm
from .forms import SearchForm

# Create your views here.
def notes_list(request):
    notes =  Note.objects.all()
    return render(request, "notes/notes_list.html",
                  {"notes": notes})

def notes_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/notes_detail.html", {"note": note})



def add_note(request):
    """
    Create a new note.
    """
    if request.method == "GET":
        form = NoteForm()

    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="notes_list")

    return render(request, "notes/add_note.html", {"form": form})


# Update a note
def update_note(request, pk):
    """
    Update an existing note.
    """
    note = get_object_or_404(Note, pk=pk)

    if request.method == "GET":
        form = NoteForm(instance=note) #Intialize form with specific instance of Note

    else:
        form = NoteForm(data=request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect(to="notes_list") # If form is valid --> redirect to notes_list view

    #If it is the first time viewing the page (a GET request will be sent), or if the form was not found valid, render an empty form
    return render(request, "notes/update_note.html", {"form": form}) 

def delete_note(request, pk):
    """
    Delete an existing note.
    """
    note = get_object_or_404(Note, pk = pk)
    note.delete()
    return redirect(to="notes_list")

def search(request):
    if request.method == "GET":
        form = SearchForm()

    else:
        form = SearchForm(data=request.POST)

        if form.is_valid():
            notes = Note.objects.all()
            title = form.cleaned_data['title']
            order_by = form.cleaned_data['order_by']

            notes = notes.filter(title__exact=title)
            notes = notes.order_by(order_by)

            return render(request, "notes/search_results.html", {"notes": notes})

    return render(request, "notes/search.html", {"form": form})
    
