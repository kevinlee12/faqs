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

from django.test import TestCase

from .models import Thread

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

    def test_thread_title(self):
        """String of the thread should be title of the thread object."""
        thread_title = 'Explain the origins of knowledge'
        knowledge_thread = Thread.objects.get(title=thread_title)

        self.assertEqual(str(knowledge_thread), thread_title)
