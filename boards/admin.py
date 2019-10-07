from django.contrib import admin
from .models import Board, Topic, Post
# Register your models here.

admin.site.register([Board, Topic, Post])
