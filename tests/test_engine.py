from decimal import Decimal
from datetime import date
from lmnp_tax_engine.core.engine import calculate
from lmnp_tax_engine.core.models import Property

def test_micro_bic_abattement_classique_2025():
    """Gross rent 20 000 €, classique → 50 % abattement ⇒ taxable 10 000 €."""
    prop = Property(
        id="P1",
        address="42 rue de Python, Lyon",
        acquisition_price=Decimal("200000"),
        acquisition_date=date(2020, 5, 2),
        classification="classique",
    )
    result = calculate(
        property=prop,
        gross_rent=Decimal("20000"),
        charges=Decimal("0"),
        regime="micro_bic",
        year=2025,
    )
    assert result.taxable_income == Decimal("10000")


def test_micro_bic_abattement_tourisme_non_classe_2025():
    """Gross rent 12 000 €, tourisme_non_classe → 30 % abattement ⇒ taxable 8 400 €."""
    prop = Property(
        id="T1",
        address="1 chemin du Test, Paris",
        acquisition_price=Decimal("150000"),
        acquisition_date=date(2021, 1, 15),
        classification="tourisme_non_classe",
    )
    result = calculate(
        property=prop,
        gross_rent=Decimal("12000"),
        charges=Decimal("0"),
        regime="micro_bic",
        year=2025,
    )
    assert result.taxable_income == Decimal("8400")
    assert result.explanation == "Abattement 30% appliqué (tourisme_non_classe)"
