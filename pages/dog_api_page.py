import requests

class DogApiPage:

    base_url = 'https://api.thedogapi.com/v1/'

    @staticmethod
    def get_breeds():
        response = requests.get(f'{DogApiPage.base_url}breeds')
        return response.json()

    @staticmethod
    def get_random_dog():
        response = requests.get(f'{DogApiPage.base_url}images/search')
        return response.json()