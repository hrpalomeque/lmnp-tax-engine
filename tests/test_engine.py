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


def test_micro_bic_abattement_minimum_2025():
    """Abattement minimum 305 € when gross rent is low."""
    prop = Property(
        id="P2",
        address="1 rue de la Loi, Paris",
        acquisition_price=Decimal("150000"),
        acquisition_date=date(2021, 1, 15),
        classification="classique",
    )
    result = calculate(
        property=prop,
        gross_rent=Decimal("600"),
        charges=Decimal("0"),
        regime="micro_bic",
        year=2025,
    )
    assert result.taxable_income == Decimal("295")
