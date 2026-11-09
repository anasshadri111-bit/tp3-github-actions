from unittest.mock import Mock
import pytest
from app.moderation import decider


def test_classe_spam_donne_decision_bloquer():
    modele = Mock()
    modele.predict.return_value = "spam"
    decision = decider(modele, "Offre miracle")
    assert decision == "bloquer"
    modele.predict.assert_called_once_with("Offre miracle")


def test_classe_normal_donne_decision_autoriser():
    modele = Mock()
    modele.predict.return_value = "normal"
    decision = decider(modele, "Bonjour")
    assert decision == "autoriser"
    modele.predict.assert_called_once_with("Bonjour")


def test_erreur_du_modele_est_propagee():
    modele = Mock()
    modele.predict.side_effect = RuntimeError("Modele indisponible")
    with pytest.raises(RuntimeError):
        decider(modele, "Offre miracle")
