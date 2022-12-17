from django.contrib import admin

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
    list_display = ["title", "slug", "get_category", "is_active"]
    list_editable = ["is_active"]
    list_filter = [
        ("selected_categories", admin.RelatedOnlyFieldListFilter)
        , "is_active"]
    def get_category(self, obj):
        return [course.title for course in obj.selected_categories.all()]


admin.site.register(ArticleCategory, articleCategory_admin)
admin.site.register(Article, article_admin)