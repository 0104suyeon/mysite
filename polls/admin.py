from django.contrib import admin
from .models import Laptop, Question, Choice
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)