

class TestView:
    def test_login_view(self,client):
        response = client.get('/login')
        assert response.status_code == 301

    def test_register_view(self,client):
        response = client.get('/register')
        assert response.status_code == 301

    def test_index_view(self,client):
        response = client.get('/index')
        assert response.status_code == 301

