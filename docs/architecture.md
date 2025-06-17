# LMNP‑Tax‑Engine – Architecture & Roadmap (Draft v0.3 – 2025‑06‑17)

## 1 Purpose

Turn raw 2025 LMNP rental data into a complete, legally traceable tax result (micro‑BIC vs réel) that a landlord or accountant can rely on.

## 2 Guiding principles

| #                               | Principle                                                                                 | Practical effect |
| ------------------------------- | ----------------------------------------------------------------------------------------- | ---------------- |
| **P‑1 Single source of truth**  | Thresholds & rates live in `config/{year}.yaml`; no hard‑coded numbers.                   |                  |
| **P‑2 Typed core**              | All inputs / outputs move through Pydantic models in `core/models.py`.                    |                  |
| **P‑3 Legal‑reference hygiene** | Implementations cite the PDF page / article; if missing, add `# TODO‑reference`.          |                  |
| **P‑4 Vertical slices**         | Build thin, end‑to‑end features; each slice delivers a user‑runnable command or function. |                  |
| **P‑5 Progressive hardening**   | Looseness first; tighten CI, mypy, docs after APIs stabilise.                             |                  |
| *Note on numeric types*         | We currently use `Decimal` for money; it’s recommended, **not mandated**.                 |                  |

## 3 Current repository layout

```
lmnp_tax_engine/
├─ core/
│  ├─ engine.py    # calculate(), decide_regime()
│  ├─ helpers.py   # small utilities
│  └─ models.py    # Pydantic types
├─ config/2025.yaml
├─ cli/            # placeholder
├─ io/             # placeholder
├─ api/            # placeholder
├─ optim/          # placeholder
├─ tracking/       # placeholder
└─ tests/
```

## 4 Behavioural spec for v0.1 (today)

1. **Regime choice** – `decide_regime()` inside `core/engine.py`

   * Default: pick micro‑BIC when eligible.
   * Allow `force_regime="reel"` to override.
   * Cite relevant PDF pages.
2. **Refactor `calculate()`** – remove `regime` arg; add optional `force_regime`.
3. **Update tests** – adapt existing two cases + add one forced‑réel case.
4. **Tag `v0.0.1`** – green CI, create git tag.

## 5 Road‑map

| Version  | End‑user story                                                  |
| -------- | --------------------------------------------------------------- |
| **v0.1** | Know cheaper régime or force réel with citations.               |
| **v0.2** | CERFA 2031 export + CLI command.                                |
| **v0.3** | Multi‑property, LMP switch, amortisation cap.                   |
| **v1.0** | Full 2025 compliance inc. CFE, social contributions, audit log. |

## 6 Administrative

* Create GitHub label **`tech‑debt`** for deferred clean‑ups.
* Ensure PDF copy remains available for citations; re‑upload if needed.
