from django.test import TestCase
from .models import Post
import datetime
from django.utils import timezone
class TestPost(TestCase):
    def test_post(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Post(published_date=time)
        self.assertIs(future_question.was_published_recently(), False)