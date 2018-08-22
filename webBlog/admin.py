from django.contrib import admin
from .models import Post
from markdownx.admin import MarkdownxModelAdmin
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(Post,MarkdownxModelAdmin )
