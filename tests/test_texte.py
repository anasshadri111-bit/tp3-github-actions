import pytest
from app.texte import nettoyer_texte


@pytest.mark.parametrize("entree, attendu", [
    ("  BONJOUR    monde  ", "bonjour monde"),
    ("  déjà propre  ", "déjà propre"),
    ("", ""),
    ("     ", ""),
    ("MAJUSCULES", "majuscules"),
])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu


@pytest.mark.parametrize("entree_invalide", [123, None])
def test_entree_non_textuelle_leve_type_error(entree_invalide):
    with pytest.raises(TypeError):
        nettoyer_texte(entree_invalide)


def test_nettoyer_un_texte_deja_nettoye_ne_le_change_plus():
    une_fois = nettoyer_texte("  BONJOUR    monde  ")
    assert nettoyer_texte(une_fois) == une_fois