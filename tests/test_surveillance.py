from unittest.mock import patch
import pytest
from app.surveillance import surveiller


def test_taux_0_15_declenche_alerte_et_notification():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.15)
    assert resultat == "alerte"
    notifier.assert_called_once_with("Taux eleve")


def test_taux_0_05_ok_sans_notification():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.05)
    assert resultat == "ok"
    notifier.assert_not_called()


def test_taux_exact_0_10_ok_sans_notification():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.10)
    assert resultat == "ok"
    notifier.assert_not_called()


def test_panne_du_service_est_propagee():
    with patch("app.surveillance.envoyer_notification") as notifier:
        notifier.side_effect = RuntimeError("Service non configure")
        with pytest.raises(RuntimeError):
            surveiller(0.15)
