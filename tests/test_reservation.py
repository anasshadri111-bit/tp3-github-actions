import pytest
from app.reservation import Stock, Reservation


@pytest.fixture
def stock():
    return Stock(5)


def test_reserver_2_unites_confirmee_et_stock_a_3(stock):
    statut = Reservation(stock).reserver(2)
    assert statut == "confirmee"
    assert stock.quantite == 3


def test_reserver_6_unites_refusee_et_stock_inchange(stock):
    statut = Reservation(stock).reserver(6)
    assert statut == "refusee"
    assert stock.quantite == 5


def test_reserver_5_unites_confirmee_et_stock_vide(stock):
    statut = Reservation(stock).reserver(5)
    assert statut == "confirmee"
    assert stock.quantite == 0


def test_reserver_0_unite_leve_value_error_et_stock_intact(stock):
    with pytest.raises(ValueError):
        Reservation(stock).reserver(0)
    assert stock.quantite == 5