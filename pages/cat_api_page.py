import requests

class CatApiPage:

    base_url = 'https://api.thecatapi.com/v1/'

    @staticmethod
    def get_breeds():
        response = requests.get(f'{CatApiPage.base_url}breeds')
        return response.json()

    @staticmethod
    def get_random_cat():
        response = requests.get(f'{CatApiPage.base_url}images/search')
        return response.json()