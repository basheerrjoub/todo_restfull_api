from django.test import TestCase
from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(
            title="Washing the car", body="All over the sides and windows"
        )

    def test_title_content(self):
        first = Todo.objects.get(id=1)
        excepted = str(first.title)
        self.assertEqual(excepted, "Washing the car")

    def test_body_content(self):
        first = Todo.objects.get(id=1)
        excepted = str(first.body)
        self.assertEqual(excepted, "All over the sides and windows")
