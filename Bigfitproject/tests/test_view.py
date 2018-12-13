from Bigfit.models import User,WeightTracker,CalorieTracker
from django.test import TestCase
import pytest

class UserTest(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.email = "testuser@testbase.com"
        self.first_name = "Test"
        self.last_name = "User"
        self.password = "z"

        self.test_user = User.objects.create_user(
            username=self.username,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name
        )

    def test_create_user(self):
        assert isinstance(self.test_user,User)

    def test_default_user_is_active(self):
        assert self.test_user.is_active

    def test_default_user_is_staff(self):
        assert not self.test_user.is_staff

    def test_default_user_is_superuser(self):
        assert not self.test_user.is_superuser

    def test_get_full_name(self):
        assert self.test_user.get_full_name() == 'Test User'

    def test_get_email(self):
        assert self.test_user.get_email_field_name() == 'email'


@pytest.mark.django_db
def test_user_count():
    assert User.objects.count() == 0

@pytest.mark.django_db
def test_weighttracker_count():
    assert WeightTracker.objects.count() == 0

@pytest.mark.django_db
def test_calorietracker_count():
    assert CalorieTracker.objects.count() == 0
