import requests
from urllib.parse import urljoin
from config.config import Config
from endpoints.endpoints import Endpoints

class UsersApiClient():

    @staticmethod
    def _prepare_url(url, base_url=Config.BASE_URL):
        return urljoin(base_url, url)
        

    @staticmethod 
    def list_users():
        return requests.get(
            url=UsersApiClient._prepare_url(Endpoints.USERS)
            ).json()

    @staticmethod 
    def single_user():
        return requests.get(
            url=UsersApiClient._prepare_url(Endpoints.P_USER)
            ).json()

    @staticmethod
    def create_user(user_details):
        return requests.post(
            url=UsersApiClient._prepare_url(Endpoints.USERS), json=user_details
            ).json()

    @staticmethod
    def update_user(user_details):
        return requests.put(
            url=UsersApiClient._prepare_url(Endpoints.USERS), json=user_details
            ).json()
    
    @staticmethod
    def delete_user(id):
        return requests.delete(
            url=UsersApiClient._prepare_url(Endpoints.USERS), json=id
            )

    
