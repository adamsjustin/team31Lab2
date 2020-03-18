import pytest
import mock
import builtins
from invoice import Invoice

@pytest.fixture
def qnt():
    pytest.qnt = "y"


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


def test_can_input_answer_yes(invoice):
    with mock.patch.object(builtins, 'input', lambda x: 'y'):
        assert invoice.inputAnswer('Test') == 'y'


def test_can_input_answer_no(invoice):
    with mock.patch.object(builtins, 'input', lambda x: 'n'):
        assert invoice.inputAnswer('Test') == 'n'
