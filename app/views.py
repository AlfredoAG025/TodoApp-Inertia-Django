import json

from django.http import HttpRequest
from django.shortcuts import redirect
from inertia import render
from marshmallow import ValidationError

from .models import Note
from .schemas import NoteSchema


def index(request):
    return render(request, "Index", props={"name": "World"})


def notes(request):
    notes = Note.objects.all()
    notes_serialized = NoteSchema(many=True).dump(notes)
    return render(
        request,
        "Notes",
        props={
            "notes": notes_serialized,
        }
    )


def create_note(request):
    return render(
        request,
        "CreateNote",
        props={

        }
    )


def store_note(request: HttpRequest):
    try:
        note_deserialized = NoteSchema().loads(request.body)
        note = Note(**note_deserialized)
        note.save()
        return redirect('/notes')
    except ValidationError as e:
        return redirect('/create_note', kwargs={'errors': e.messages_dict})


def destroy_note(request: HttpRequest, id_note: int):
    if request.method == "DELETE":
        note = Note.objects.get(id=id_note)
        note.delete()
        return redirect('/notes')
