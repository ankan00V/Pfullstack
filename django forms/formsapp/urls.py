from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact_view, name="contact"),
    path("edit/<int:id>/", views.edit_view, name="edit"),
    path("delete/<int:id>/", views.delete_view, name="delete"),
    path("toggle/<int:id>/", views.toggle_publish, name="toggle"),
]
