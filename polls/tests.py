from datetime import datetime, timedelta
from django.test import TestCase
from django.utils import timezone
from .models import Question


# Create your tests here.

class QuestionModelTests(TestCase):
    def test_was_published(self):
        time = timezone.now() + timedelta(days=30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(),False)
