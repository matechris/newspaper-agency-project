from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from bureau.models import Topic, Newspaper

LOGIN_PAGE = reverse("login")
HOME_PAGE = reverse("bureau:index")
REDACTOR_LIST = reverse("bureau:redactor-list")
NEWSPAPER_LIST = reverse("bureau:newspaper-list")
TOPIC_LIST = reverse("bureau:topic-list")


class PublicViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_login_required(self):
        response = self.client.get(HOME_PAGE)

        self.assertNotEqual(response.status_code, 200)

    def test_redactor_list_login_required(self):
        response = self.client.get(REDACTOR_LIST)

        self.assertNotEqual(response.status_code, 200)

    def test_newspaper_list_login_required(self):
        response = self.client.get(NEWSPAPER_LIST)

        self.assertNotEqual(response.status_code, 200)

    def test_topic_list_login_required(self):
        response = self.client.get(TOPIC_LIST)

        self.assertNotEqual(response.status_code, 200)

    def test_login_page_login_not_required(self):
        response = self.client.get(LOGIN_PAGE)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")


class PrivateViewsTest(TestCase):
    def setUp(self) -> None:
        topic = Topic.objects.create(
            name="Test",
        )
        Newspaper.objects.create(
            title="Test title", content="Test content", topic=topic
        )
        self.user = get_user_model().objects.create_user("new_user", "user1234")
        self.client.force_login(self.user)

    def test_user_access_to_home_page(self):
        response = self.client.get(HOME_PAGE)

        self.assertEqual(response.status_code, 200)

    def test_user_access_to_newspaper_list(self):
        newspapers = Newspaper.objects.all()
        response = self.client.get(NEWSPAPER_LIST)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["newspaper_list"]), list(newspapers))

    def test_user_access_to_redactor_list(self):
        redactors = get_user_model().objects.all()
        response = self.client.get(REDACTOR_LIST)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["redactor_list"]), list(redactors))

    def test_user_access_to_topic_list(self):
        topics = Topic.objects.all()
        response = self.client.get(TOPIC_LIST)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["topic_list"]), list(topics))

    def test_user_access_to_login_page(self):
        response = self.client.get(LOGIN_PAGE)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")


class CreateViewsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user("new_user", "user1234")
        self.client.force_login(self.user)

    def test_redactor_create_view(self):
        form_data = {
            "username": "test_user",
            "password1": "user1234",
            "password2": "user1234",
            "first_name": "Test first",
            "last_name": "Test last",
            "years_of_experience": 5,
        }
        self.client.post(reverse("bureau:redactor-create"), data=form_data)
        user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(user.first_name, form_data["first_name"])
        self.assertEqual(user.last_name, form_data["last_name"])
        self.assertEqual(user.years_of_experience, form_data["years_of_experience"])


class TestSearchField(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "user", "testuser123"
        )
        self.client.force_login(self.user)

    def test_search_topic(self):
        response = self.client.get("/topics/?name=a/")

        self.assertQuerysetEqual(
            response.context["topic_list"],
            Topic.objects.filter(name__icontains="a")
        )
        self.assertEqual(response.status_code, 200)

    def test_search_redactor(self):
        response = self.client.get("/redactors/?username=a/")

        self.assertQuerysetEqual(
            response.context["redactor_list"],
            get_user_model().objects.filter(username__icontains="a")
        )
        self.assertEqual(response.status_code, 200)

    def test_search_newspaper(self):
        response = self.client.get("/newspapers/?title=t/")

        self.assertQuerysetEqual(
            response.context["newspaper_list"],
            Newspaper.objects.filter(title__icontains="t")
        )
        self.assertEqual(response.status_code, 200)
