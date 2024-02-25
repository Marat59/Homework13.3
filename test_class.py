import pytest

from category import Category
from product import Product

@pytest.fixture
def class_category():
    return Category('Телефон', 'Мощный', 'iPhone')

def test_category_init(class_category):
    assert class_category.name == 'Телефон'
    assert class_category.description == 'Мощный'
    assert class_category.goods == 'iPhone'


def test_count():
    assert Category.count_category == 1
    assert Category.count_unique_products == 1

@pytest.fixture
def class_product():
    return Product('Tele2', 'Оператор связи', 299.0, 100)

def test_product_init(class_product):
    assert class_product.name == 'Tele2'
    assert class_product.description == 'Оператор связи'
    assert class_product.price == 299.0
    assert class_product.quantity == 100