from django.urls import reverse, resolve 

class TestUrls:

    def test_login_url(self):
        path = reverse('login')
        assert resolve(path).view_name == 'login'

    def test_register_url(self):
        path = reverse('register')
        assert resolve(path).view_name == 'register'

    def test_index_url(self):
        path = reverse('index page')
        assert resolve(path).view_name == 'index page'
