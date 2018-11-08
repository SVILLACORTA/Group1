'''
from Bigfit.models import User

class TestUserModel:

    def test_save(self):
        user1 = User(
            name= 'Tom',
            password = 123456,
            email = 'Tom123@gmail.com'

        )
        assert user1.name == 'Tom'
        assert user1.password == 123456
        assert user1.email == 'Tom123@gmail.com'
'''