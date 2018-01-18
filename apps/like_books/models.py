# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    uploader = models.ForeignKey(User, related_name="uploaded_books")
    liked_by = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# ///////////////////////////////////////////////////////////////////////////////////
# Create 3 different user accounts

>>> User.objects.create(first_name ="Franklin", last_name ="Kirimi", email= "Frank@yahoo.com")
>>> User.objects.create(first_name ="Asher", last_name ="Kiogora", email= "asher@yahoo.com")
>>> User.objects.create(first_name ="Marian", last_name ="kinya", email= "marian@yahoo.com")
>>> User.objects.all()

# Have the first user create 2 books.
user_one = User.objects.get(id=1)
Book.objects.create(name ="Book1", uploader =user_one)
Book.objects.create(name ="Book2", uploader =user_one)

# Have the second user create 2 other books.
user_two = User.objects.get(id=2)
Book.objects.create(name ="Book3", uploader =user_two)
Book.objects.create(name ="Book4", uploader =user_two)

# Have the third user create 2 other books.
user_three = User.objects.get(id=3)
Book.objects.create(name ="Book5", uploader =user_three)
Book.objects.create(name ="Book6", uploader =user_three)

# Have the first user like the last book and the first book
user_one = User.objects.get(id=1)

book_one = Book.objects.get(id=1);
book_one.name
u'Book1'
user_one.objects.add(book_one)

book_six = Book.objects.get(id=6);
book_six.name
u'Book6'

book_one.liked_by.add(user_one)
book_six.liked_by.add(user_one)


# Have the second user like the first book and the third book
user_two = User.objects.get(id=2)
book_one = Book.objects.get(id=1);
book_three= Book.objects.get(id=3)
book_one.liked_by.add(user_two)
book_three.liked_by.add(user_two)
book_two =Book.objects.get(id=2)

# Have the third user like all books
user_three=User.objects.get(id=3)
all_books=Book.objects.all()
all_books.liked_by.add(user_three)

#Display all users who like the first book
first book liked by users
display_users
book_one.liked_by.all()

# Display the user who uploaded the first book
for uploader in book_one.uploader.all()
  print uploader.first_name

# Display all users who like the second book
for uploader in book_two.uploader.all()
    print uploader.first_name
# Display the user who uploaded the second book







