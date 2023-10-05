from pages.dog_api_page import DogApiPage

def test_get_breeds():
    breeds_data = DogApiPage.get_breeds()
    assert len(breeds_data) > 0

def test_get_random_dog():
    random_dog_data = DogApiPage.get_random_dog()
    assert 'id' in random_dog_data[0]
    assert 'url' in random_dog_data[0]
