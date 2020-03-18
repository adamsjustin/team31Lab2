import pytest
from invoice import Invoice


@pytest.fixture
def qnt():
    pytest.qnt = 50


@pytest.fixture
def price():
    pytest.price = 30


@pytest.fixture
def discount():
    pytest.discount = 15


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'price': 7.50, 'discount': 10}}
    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_can_calculate_total_impure_price(invoice, products):
    assert invoice.totalImpurePrice(products) == 75


def test_can_calculate_total_discount(invoice, products):
    assert invoice.totalDiscount(products) == 5.62


def test_can_calculate_total_pure_price(invoice, products):
    assert invoice.totalPurePrice(products) == 69.38


def test_can_add_product(invoice, qnt, price, discount):
    assert invoice.addProduct(pytest.qnt, pytest.price, pytest.discount) \
           == {'qnt': pytest.qnt, 'price': pytest.price, 'discount': pytest.discount}
