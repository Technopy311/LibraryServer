from django.urls import path
from . import views
from .views import SearchView

urlpatterns = [
    path('', views.index),
    path('buscar', SearchView.as_view(), name="search_page"),
    path('perfil', views.profile),
    path('registrar', views.register),
    path('libro/<int:bookid>', views.book)
]