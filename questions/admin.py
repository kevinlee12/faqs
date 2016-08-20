from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Thread
# Register your models here.


class ThreadAdmin(MarkdownxModelAdmin):
    list_display = (('title', 'response', 'last_edited'))
    list_display_links = (('title', ))
    exclude = (('last_edited', ))


admin.site.register(Thread, ThreadAdmin)
