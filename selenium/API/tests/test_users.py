import pytest
import requests
from config.config import Config
from api.users_api_client import UsersApiClient



@pytest.mark.smoke
def test_it_checks_user_list():
    users = UsersApiClient.list_users()
    assert users['per_page']==len(users['data'])
    print(users)


def test_it_checks_single_user():
    user = UsersApiClient.single_user()
    assert len(user['data']) == 5 



@pytest.mark.regression
def test_it_checks_user_created():
    user_details = {"name":"Katy",
                    "job":"leader"}
    user = UsersApiClient.create_user(user_details)
    print(user)
    assert "Katy" or "Olya" in user


def test_it_checks_user_updated():
    user_details = {"name":"Tanya",
                    "job":"QA"}
    user = UsersApiClient.update_user(user_details)
    print(user)
    assert user['name']== 'Tanya'
    

@pytest.mark.user
def test_it_checks_user_deleted():
    id = {"id":3}
    user = UsersApiClient.delete_user(id)
    assert user.status_code == 204



