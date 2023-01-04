from django.db import models

class Book(models.Model):
	title = models.CharField("Título" ,max_length=60)
	author = models.CharField("Autor", max_length=40)
	description = models.CharField("Descripción breve", max_length=300)
	start_page = models.IntegerField("Nro de primera página")
	last_page = models.IntegerField("Nro de la última página")
	taken = models.BooleanField("Libro tomado", default=False)
	
	def __str__(self):
		return self.title 


class User(models.Model):
	name = models.CharField("Nombre", max_length=40)
	lastname = models.CharField("Apellido", max_length=40)
	reading_state = models.BooleanField("Estado de lectura", default=False)
	reading_book = models.OneToOneField(
		Book, 
		on_delete=models.CASCADE,
		primary_key=True
	)
	read_books_amount = models.IntegerField("Cantidad de libros leídos", default=0)

	def __str__(self):
		return "%s the user" % self.name