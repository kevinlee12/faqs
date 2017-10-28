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

from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import JSONField
from markdownx.models import MarkdownxField

class Content(models.Model):

    class Meta:
        abstract = True
        get_latest_by = 'last_edited'
        ordering = ['last_edited', 'title']

    title = models.CharField(max_length=50)

    response = MarkdownxField()

    last_edited = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Thread(Content):

    # This field stores extra information regarding the thread. If the contents
    # inside the extra field become stable, then it is time to promote the
    # item(s) to separate fields.
    extra = JSONField(blank=True, null=True)


# Ensures that only one instance of a model can be created. Code from:
# http://stackoverflow.com/a/6436008
def validate_only_one_instance(obj):
    model = obj.__class__
    if model.objects.count() > 0 and obj.id != model.objects.get().id:
        raise ValidationError(
            'Can only create 1 {0} instance'.format(str(model)))

class FailureThread(Content):

    def title_default():
        """Returns the default failture thread title."""
        return 'Looks like we couldn\'t find a solution :('

    def response_default():
        """Returns the default failure thread response."""
        return 'Try again with another search term or keep typing'

    def clean(self):
        return validate_only_one_instance(self)

    title = models.CharField(max_length=50, default=title_default)

    response = MarkdownxField(default=response_default)

    def __str__(self):
        return 'Failure Message'
