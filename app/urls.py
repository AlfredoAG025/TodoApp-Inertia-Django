from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notes", views.notes, name="notes"),
    path("create_note", views.create_note, name="create_note"),
    path("store_note", views.store_note, name="store_note"),
    path("destroy_note/<int:id_note>", views.destroy_note, name="destroy_note"),
]
