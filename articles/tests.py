from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Article


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
