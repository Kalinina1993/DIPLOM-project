import requests


class TestAPI1:
    """Check to correct work of app"""

    def test_app_is_available(self):
        response = requests.get("https://petstore.swagger.io/")
        assert response.ok

    def test_registration(self, new_user):
        """Test of user registration"""
        response = new_user
        assert response.status_code == 200

    def test_user_login(self, user_datas):
        """Test login user"""
        response = user_datas
        assert response.status_code == 200

    def test_get_user_datas(self, user_username):
        """Test output user datas"""
        response = user_username
        assert response.status_code == 200

    def test_delete_user(self, delete_user):
        """Test delete user"""
        response = delete_user
        assert response.status_code == 200
