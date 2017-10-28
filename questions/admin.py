# Copyright 2017 FAQ Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Thread
from .models import FailureThread
# Register your models here.


class ThreadAdmin(MarkdownxModelAdmin):
    list_display = (('title', 'response', 'last_edited'))
    list_display_links = (('title', ))
    exclude = (('last_edited', ))

    fieldsets = (
        (None, {
            'fields': ('title', 'response')
        }),
        ('Advanced options', {
            'classes': ('collapse', ),
            'description': (
                'Optional extra information for the thread in JSON format'),
            'fields': ('extra', ),
        })
    )

class FailureThreadAdmin(MarkdownxModelAdmin):
    list_display = (('title', 'response', 'last_edited'))
    list_display_links = (('title', ))
    exclude = (('last_edited', ))

admin.site.register(Thread, ThreadAdmin)
admin.site.register(FailureThread, FailureThreadAdmin)
