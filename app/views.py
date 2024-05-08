import json

from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from inertia import render, share
from marshmallow import ValidationError

from .models import Note
from .schemas import NoteSchema


def index(request):
    return render(request, "Index", props={"name": "World"})


def notes(request):
    notes = Note.objects.all()
    favorite_notes = Note.objects.filter(is_favorite=True)
    notes_serialized = NoteSchema(many=True).dump(notes)
    favorite_notes_serialized = NoteSchema(many=True).dump(favorite_notes)
    return render(
        request,
        "Notes",
        props={
            "notes": notes_serialized,
            "favorite_notes": favorite_notes_serialized,
        }
    )


def create_note(request):
    return render(
        request,
        "CreateNote",
        props={
            "errors": []
        }
    )


def store_note(request: HttpRequest):
    try:
        note_deserialized = NoteSchema().loads(request.body)
        note = Note(**note_deserialized)
        note.save()
        return redirect('/notes')
    except ValidationError as e:
        return render(
            request,
            "CreateNote",
            props={
                "errors": e.messages_dict
            }
        )


def destroy_note(request: HttpRequest, id_note: int):
    if request.method == "DELETE":
        note = Note.objects.get(id=id_note)
        note.delete()
        return redirect('/notes')


def toggle_is_favorite_note(request: HttpRequest, id_note: int):
    if request.method == "PATCH":
        note = Note.objects.get(id=id_note)
        note.is_favorite = not note.is_favorite
        note.save()
        return redirect('/notes')


def inertia_share(get_response):
    def middleware(request):
        share(request,
              errors=[],
              )

        return get_response(request)

    return middleware
