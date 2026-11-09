import pytest
from app.livraison import frais_livraison


def test_livraison_panier_ordinaire():
    # Arrange
    montant = 120
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 25


def test_livraison_payante_juste_sous_le_seuil_299():
    assert frais_livraison(299) == 25


def test_livraison_gratuite_au_seuil_exact_300():
    assert frais_livraison(300) == 0


def test_livraison_gratuite_au_dessus_du_seuil_301():
    assert frais_livraison(301) == 0


def test_livraison_panier_vide_0_dh_est_payante():
    assert frais_livraison(0) == 25


def test_montant_negatif_leve_value_error():
    with pytest.raises(ValueError):
        frais_livraison(-1)