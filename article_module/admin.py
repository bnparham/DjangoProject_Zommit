from django.contrib import admin
from django.http import HttpRequest

from .models import *

class articleCategory_admin(admin.ModelAdmin):
    list_display = ["title", "parent", "is_active"]
    list_editable = ["parent", "is_active"]
    list_filter = [
        ("parent", admin.RelatedOnlyFieldListFilter),
        ("parent", admin.EmptyFieldListFilter),
        ("is_active")
    ]

class article_admin(admin.ModelAdmin):
    list_display = ["title", "slug", "get_category", "is_active", "author", "view_count","is_suggest"]
    list_editable = ["is_active","is_suggest"]
    list_filter = [
        ("selected_categories", admin.RelatedOnlyFieldListFilter)
        , "is_active", "is_suggest"]
    def get_category(self, obj):
        return [course.title for course in obj.selected_categories.all()]
    def save_model(self, request:HttpRequest, obj:Article, form, change):
        if not change:
            obj.author = request.user
        return super(article_admin, self).save_model(request,obj,form,change)


admin.site.register(ArticleCategory, articleCategory_admin)
admin.site.register(Article, article_admin)