from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField
from markdownx.models import MarkdownxField

class Thread(models.Model):

    class Meta:
        get_latest_by = 'last_edited'
        ordering = ['last_edited', 'title']

    title = models.CharField(max_length=50)

    response = MarkdownxField()

    last_edited = models.DateField(auto_now=True)

    # This field stores extra information regarding the thread. If the contents
    # inside the extra field become stable, then it is time to promote the
    # item(s) to separate fields.
    extra = JSONField(blank=True,null=True)

    def __str__(self):
        return self.title
