from django.urls import path
from commons.views import registro
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.notesPage, name='notesPage'),
    path('', views.notesPage, name='notesPagePag'),
    path('createNote', views.newNotePage, name='createNotePage'),
    path('editNote/<id>', views.editNotePage, name='editNotePage'),
    path('deleteNote/<id>', views.deleteNotePage, name='deleteNotePage'),
    path('viewNote/<id>/<page>', views.viewNotePage, name='viewNotePage'),
    path('registro', registro, name='registro'),
    path('admin/', admin.site.urls, name='adminPg'),
]