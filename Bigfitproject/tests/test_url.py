from django.urls import reverse, resolve

class TestUrls:

    def test_login_url(self):
        path = reverse('login page')
        assert resolve(path).view_name == 'login page'

    def test_register_url(self):
        path = reverse('register page')
        assert resolve(path).view_name == 'register page'

    def test_index_url(self):
        path = reverse('index page')
        assert resolve(path).view_name == 'index page'
