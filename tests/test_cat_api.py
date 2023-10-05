from pages.cat_api_page import CatApiPage

def test_get_breeds():
    breeds_data = CatApiPage.get_breeds()
    assert len(breeds_data) > 0

def test_get_random_cat():
    random_cat_data = CatApiPage.get_random_cat()
    assert 'id' in random_cat_data[0]
    assert 'url' in random_cat_data[0]
