---
# qou-cds4
title: 'S4 (SCIENCE): p/n convention — 6 live non-comparison files + 28 witnesses off bring_color_weighted'
status: todo
type: task
priority: normal
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-15T00:00:00Z
---

Parent: `qou-cdx1`. Ruling R3: `pn_convention="bring_color_weighted"` is
canonical.

## Measured 2026-08-15 (live Python assignments, excluding `_deprecated/`)

| value | assignment sites |
|---|---|
| **`bring_color_weighted`** (canonical) | **16** |
| `chi_lambda_braid` | **9** |
| `strict_averaged` | **6** |

83 files mention `pn_convention` overall (`.py`+`.json`+`.md`).
**28 committed witnesses** record a non-colour-weighted `pn_convention`.

## R3 is largely already true

`bring_color_weighted` is already the default in the production path:
`closed_form_tau_M.py` (×4) and `mass_at_3A_proper.py`. R3 makes it canonical
and puts the alternatives on notice.

## The 8 live Python files off-canon

```
computations/_habiro_coefficient_extract.py
computations/atomic_tr_m_helium4_canonical.py
computations/binding_bring_enhancement_compare.py      <- name says comparison
computations/binding_canonical.py                      <- READ THIS FIRST
computations/binding_combiner_markov_peel_fallback.py  <- PN_CONVENTION = "strict_averaged"
computations/chi_monotone_transfer.py
computations/closed_form_tau_M_verification_phase5q.py
computations/iterative_knot_builder.py
```

**`binding_canonical.py` first.** A file with `canonical` in its name assigning a
non-canonical p/n convention is either a naming defect or a real one, and the
two need different fixes.

`*_compare` and `*_fallback` are plausibly legitimate under R3 — a **labelled**
comparison against a non-canonical convention is fine. Confirm the label exists;
do not assume it from the filename.

## Why SCIENCE and not hygiene

`chi_lambda_braid` vs `strict_averaged` vs `bring_color_weighted` is the p/n
interface factor — the Bring colour-weighted asymmetry. Switching it moves
binding numbers. This is not a rename.
