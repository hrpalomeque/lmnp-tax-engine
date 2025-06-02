from __future__ import annotations
from decimal import Decimal
from datetime import date
from pydantic import BaseModel

class Property(BaseModel):
    """Basic info about one rental property."""
    id: str
    address: str
    acquisition_price: Decimal
    acquisition_date: date
    classification: str        # e.g. "tourisme_non_classe"

class RegimeResult(BaseModel):
    """Single-year tax result for one régime (Micro-BIC, Réel, …)."""
    year: int
    regime: str
    taxable_income: Decimal
    income_tax: Decimal
    social_contributions: Decimal
    explanation: str | None = None
