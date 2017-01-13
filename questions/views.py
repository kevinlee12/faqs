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

import json
import requests

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.html import escape, format_html
from django.views import View
from django.views.generic import TemplateView

from fyi.settings import SOLR_SEARCH_URL

class HomeView(TemplateView):

    template_name = 'questions/home.html'

    def get(self, request):
        """Returns the home page"""
        return render(request, self.template_name)

class SearchHandler(View):
    """Handles all search requests."""

    def get(self, request):
        """
        Handles GET requests for search. If no query is provided, all search
        queries will be returned.
        """
        query = escape(request.GET.get('query', None)).strip()
        start = escape(request.GET.get('start', 0))

        url = format_html('{0}/select', SOLR_SEARCH_URL)
        if query:
            params = {
                'q': query,
                'defType': 'edismax',
                'ps': '10',
                'start': start,
                'tie': '0.1',
                'wt':'json'
            }
        else:
            # Return all threads if no query is given
            params = {
                'q': '*',
                'start': start,
                'wt': 'json'
            }

        response = requests.get(url, params)

        json_reponse = {}
        if response.status_code == requests.codes.ok:
            json_reponse = json.loads(response.text)['response']
        else:
            raise requests.RequestException('Solr errored!')

        # Empty query case.
        if json_reponse['numFound'] < 1:
            json_reponse['docs'].append({
                'title': 'Oops couldn\'t find anything',
                'response': 'Keep on typing, we may find something interesting'
            })
        return JsonResponse(json_reponse)
