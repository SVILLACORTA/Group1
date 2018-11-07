from django.test import TestCase
<<<<<<< HEAD
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
=======

from ..forms import SignUpForm


class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2', ]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)
        # this will test the form of the signup when our client try to signup for the account .
>>>>>>> 1e04d072b0e49b7d117fb9913cf761ea40655a04
