from django.contrib.postgres.search import TrigramSimilarity
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from django.forms.models import model_to_dict

from .models import Thread

from whoosh.qparser import QueryParser

class HomeView(TemplateView):

    template_name = 'questions/home.html'

    def get(self, request):
        """Returns the home page"""
        return render(request, self.template_name)

class SearchHandler(View):
    def get(self, request, query=None):
        """Returns a json of the search results"""
        ret = {'answers': []}
        assert type(query) == str or query is None, \
            'Query must be a string type or None!'

        if query:
            ret['answers'] = [
                model_to_dict(thread, fields=('title', 'response')) for thread
                in Thread.objects.annotate(
                    similarity=TrigramSimilarity('title', query),
                    ).filter(similarity__gt=0.7).order_by('-similarity')
            ]
        else:
            ret['answers'] = [
                model_to_dict(thread, fields=('title', 'response')) for
                thread in Thread.objects.all()
            ]

        return JsonResponse(ret)
