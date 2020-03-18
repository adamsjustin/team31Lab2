import pytest
from invoice import Invoice

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
