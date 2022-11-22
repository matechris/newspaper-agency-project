from django.contrib.auth import get_user_model
from django.test import TestCase

from bureau.models import Topic, Newspaper


class ModelsTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(name="Test")
        self.assertEqual(str(topic), topic.name)

    def test_redactor_str(self):
        redactor = get_user_model().objects.create_user(
            username="Test",
            password="test1234",
            first_name="Test first",
            last_name="Test second",
        )
        self.assertEqual(str(redactor), f"{redactor.first_name} {redactor.last_name}")

    def test_newspaper_str(self):
        topic = Topic.objects.create(name="Test")
        newspaper = Newspaper.objects.create(
            title="Test", topic=topic, content="Test content"
        )

        self.assertEqual(
            str(newspaper),
            f"{newspaper.title} (publishing date: {newspaper.published_date})",
        )
