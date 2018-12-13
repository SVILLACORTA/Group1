

class TestViewRespond:
    def test_weightinput_view(self,client):
        response = client.get('/weightinput')
        assert response.status_code == 301

    def test_calorieinput_view(self,client):
        response = client.get('/calorieinput')
        assert response.status_code == 301

    def test_index_view(self,client):
        response = client.get('/index')
        assert response.status_code == 301

    def test_weighthistory_view(self,client):
        response = client.get('/weighthistory')
        assert response.status_code == 301

    def test_caloriehistory_view(self,client):
        response = client.get('/caloriehistory')
        assert response.status_code == 301

    def test_viewprofile_view(self,client):
        response = client.get('/index')
        assert response.status_code == 301
