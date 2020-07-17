import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Question
import logging
from django.test import Client
from django.test.runner import DiscoverRunner

# Get an instance of a logger
logger = logging.getLogger('django')


class QuestionModelTest(TestCase):
    def test_was_published_recently_with_feature_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questio
        ns whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)


class TestingResponseAndRunner(TestCase):
    def setUp(self):
        logger.debug(f"Before setup {Question.objects.all().first()}")
        Question.objects.create(question_text="What is this?", pub_date=timezone.now())
        Question.objects.bulk_create(
            Question(question_text="What is this?", pub_date=timezone.now()),
            Question(question_text="What is this?", pub_date=timezone.now()),
            Question(question_text="What is this?", pub_date=timezone.now()),
            Question(question_text="What is this?", pub_date=timezone.now()),
            Question(question_text="What is this?", pub_date=timezone.now()),
            Question(question_text="What is this?", pub_date=timezone.now()),
            Question(question_text="What is this?", pub_date=timezone.now()),
            Question(question_text="What is this?", pub_date=timezone.now()),
        )

    def test_detail(self):
        response = self.client.get(reverse('polls:detail', args=[1]))
        print(response)
        logger.error('test logger')
        self.assertEqual(response.status_code, 404)

    def test_Login(self):
        c = Client()
        response = c.post(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)

    def test_db_create(self):
        logger.debug(f'After setup : {Question.objects.all()}')

