"""
Deterministic engine for LMNP 2025 rules.
Public API: calculate(...)
"""

from decimal import Decimal
from pathlib import Path
import yaml
from .models import Property, RegimeResult

CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"

def load_config(year: int) -> dict:
    """Read YAML thresholds for the requested year."""
    with open(CONFIG_DIR / f"{year}.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)

def calculate(
    property: Property,
    gross_rent: Decimal,
    charges: Decimal,
    regime: str,
    year: int = 2025,
) -> RegimeResult:
    """Return tax outcome for one property / one régime / one year."""
    cfg = load_config(year)

    if regime == "micro_bic":
        abat_pct = cfg["micro_bic"]["taux_abattement"][property.classification]
        abat_min = cfg["micro_bic"].get("abattement_minimum", 0)
        from decimal import Decimal
        abat_pct_dec = Decimal(str(abat_pct))
        abat_min_dec = Decimal(str(abat_min))
        abattement = gross_rent * abat_pct_dec
        if abattement < abat_min_dec:
            abattement = abat_min_dec
        taxable_base = gross_rent - abattement
        return RegimeResult(
            year=year,
            regime=regime,
            taxable_income=taxable_base,
            income_tax=Decimal(0),           # placeholder for now
            social_contributions=Decimal(0),
            explanation=f"Abattement {abat_pct_dec:.0%} appliqué",
        )

    raise NotImplementedError(regime)
