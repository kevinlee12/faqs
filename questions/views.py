# Copyright 2016 FAQ Authors
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

from django.contrib.postgres.search import TrigramSimilarity
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from django.forms.models import model_to_dict

from .models import Thread, FailureThread

class HomeView(TemplateView):

    template_name = 'questions/home.html'

    def get(self, request):
        """Returns the home page"""
        return render(request, self.template_name)

class SearchHandler(View):
    def get(self, request, query=None):
        """Returns a json of the search results"""
        assert type(query) == str or query is None, \
            'Query must be a string type or None!'

        ret = {'answers': []}
        answers = []

        if query:
            answers = [
                model_to_dict(thread, fields=('title', 'response')) for thread
                in Thread.objects.annotate(similarity=\
                    TrigramSimilarity('response', query) +
                    TrigramSimilarity('title', query),
                ).filter(similarity__gt=0.09).order_by('-similarity')]

            if len(ret['answers']) == 0:
                if FailureThread.objects.count():
                    answers = [
                        model_to_dict(FailureThread.objects.get(pk=1),
                                      fields=('title', 'response'))
                    ]
                else:
                    answers = [{
                        'title': 'Tell the site admin that...',
                        'response': 'the failure threads aren\'t loaded!'
                    }]
        else:
            if Thread.objects.count():
                answers = [
                    model_to_dict(thread, fields=('title', 'response')) for
                    thread in Thread.objects.all()
                ]
            else:
                answers = [{
                    'title': 'Whoops!',
                    'response': 'Looks there isn\'t anything yet!'
                }]

        ret['answers'] = answers
        return JsonResponse(ret)
