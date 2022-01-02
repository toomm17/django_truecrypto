from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django import forms 
from django.contrib.auth.admin import UserAdmin

from ckeditor.widgets import CKEditorWidget

from .models import Tag, Category, Article, Event


class EventAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Event
        fields = '__all__'


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ['title', 'created_at', 'is_news', 'category']


@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display = ['title', 'date']
    form = EventAdminForm

