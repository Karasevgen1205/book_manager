from django.contrib import admin
from articles.models import Article, Comment


class CommentAdmin(admin.StackedInline):
    model = Comment
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentAdmin]
    #readonly_fields = ['rate']
    #exclude = ['count_all_stars', 'count_rated_users']
    # prepopulated_fields = {'slug' : 'title'}
    admin.site.register(Article, ArticleAdmin)

# Register your models here.
