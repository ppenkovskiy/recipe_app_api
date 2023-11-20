"""
Tests for the Django admin modifications.
"""

# TestCase is the base class for all Django test cases
from django.test import TestCase
# get_user_model is a helper function to get the user model
from django.contrib.auth import get_user_model
# reverse is used for generating URLs for Django admin pages
from django.urls import reverse
# Client is a Django test client for making requests
from django.test import Client


class AdminSiteTests(TestCase):
    """Tests for Django admin."""

    def setUp(self):
        """Create user and client."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test User'
        )

    def test_users_list(self):
        """Test that users are listed in page."""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test that edit user page works."""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        # OK success
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test the create use page works."""
        url = reverse('admin:core_user_add',)
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)