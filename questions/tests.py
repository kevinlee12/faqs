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

from django.test import Client, TestCase

from .models import Thread
from .models import FailureThread

class ThreadTestCase(TestCase):
    def setUp(self):
        Thread.objects.create(
            title='What is the best animal to walk?',
            response='A cat')
        Thread.objects.create(
            title='What serves as the best patrol?',
            response='A cat')
        Thread.objects.create(
            title='Explain the origins of knowledge',
            response='Ask your parents or ask your mind.')
        FailureThread.objects.create()

    def test_thread_title(self):
        """String of the thread should be title of the thread object."""
        thread_title = 'Explain the origins of knowledge'
        knowledge_thread = Thread.objects.get(title=thread_title)

        self.assertEqual(str(knowledge_thread), thread_title)

    def test_no_valid_results(self):
        """JSON should contain a no results message when there are results
        to return.
        """
        c = Client()
        response = c.get('/search/dogs')

        self.assertEqual(response.json()['answers'],
            [{'title': 'Looks like we couldn\'t find a solution :(',
            'response': 'Try again with another search term or keep typing'}])

    def test_returns_valid_results(self):
        """JSON should contain results when there are results to return.
        """
        c = Client()
        response = c.get('/search/cat')

        self.assertEqual(response.json()['answers'],
            [{'title': 'What is the best animal to walk?', 'response': 'A cat'},
             {'title': 'What serves as the best patrol?', 'response': 'A cat'},
            ])

        response = c.get('/search/knowledge')
        self.assertEqual(response.json()['answers'],
            [{'title': 'Explain the origins of knowledge',
              'response': 'Ask your parents or ask your mind.'}])

    def test_returns_all_results_with_no_query(self):
        """JSON should include all results when query is None"""
        c = Client()
        response = c.get('/search/')

        self.assertEqual(response.json()['answers'],
            [{'title': 'Explain the origins of knowledge',
              'response': 'Ask your parents or ask your mind.'},
             {'title': 'What is the best animal to walk?', 'response': 'A cat'},
             {'title': 'What serves as the best patrol?', 'response': 'A cat'},
            ])

class EmptyDBThreadTestCase(TestCase):
    def test_returns_no_thread_message(self):
        """JSON should include all results when query is None"""
        c = Client()
        response = c.get('/search/')

        self.assertEqual(response.json()['answers'],
            [{'title': 'Whoops!',
              'response': 'Looks there isn\'t anything yet!'}])

    def test_returns_no_failure_thread_message(self):
        """JSON should include all results when query is None"""
        c = Client()
        response = c.get('/search/nofail')

        self.assertEqual(response.json()['answers'],
            [{'title': 'Tell the site admin that...',
              'response': 'the failure threads aren\'t loaded!'}])
