from django.contrib.import User
from django.contrib.sites. import Site
from django.core import mail
from django.test import TestCase
from registration.models import RegistrationProfile

class TestRegistration(TestCase):
    def test_activation_email(self):
        site = Site.objects.get()
        user = User(email='test@example.com')
        profile = RegistrationProfile(user=user, activation_key='activation-key')
        profile.send_activation_email(site)
        self.assertEqual(len(mail.outbox), 1)
        message = mail.outbox.pop()
        self.assertEqual(message.subject, 'Activate your Bigfitproject.com account')
