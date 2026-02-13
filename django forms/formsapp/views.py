from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Note
from .forms import NoteForm


def contact_view(request):
    notes = Note.objects.all().order_by("-created_at")

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Note added successfully!")
            return redirect("contact")
    else:
        form = NoteForm()

    return render(request, "formsapp/contact_form.html", {"form": form, "notes": notes})


def edit_view(request, id):
    note = get_object_or_404(Note, id=id)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Note updated successfully!")
            return redirect("contact")
    else:
        form = NoteForm(instance=note)

    return render(request, "formsapp/contact_form.html", {"form": form})


def delete_view(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    messages.success(request, "Note deleted successfully!")
    return redirect("contact")


def toggle_publish(request, id):
    note = get_object_or_404(Note, id=id)
    note.isPublish = not note.isPublish
    note.save()
    return redirect("contact")
