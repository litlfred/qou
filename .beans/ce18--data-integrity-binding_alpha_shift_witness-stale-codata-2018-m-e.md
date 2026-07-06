---
# ce18
title: 'Data-integrity: binding_alpha_shift_witness.py uses stale CODATA-2018 m_e (0.5109989461)'
status: completed
type: task
priority: normal
created_at: 2026-06-28T05:50:00Z
updated_at: 2026-06-29T20:30:00Z
---

> **CLOSED 2026-06-29 (owner-directed)** — verified resolved on `main`: producer imports CODATA-2022 (`binding_alpha_shift_witness.py:50`) AND the witness is baked with `0.51099895069` (`binding-alpha-shift-witness.witness.json:8`). Remaining `0.5109989461` literals are `_deprecated/` only. Audit: `docs/audits/2026-06-29-bean-hygiene-data-integrity-verified-resolved.md`.

## Finding (surfaced 2026-06-28, Δ_λ ℓ¹-ceiling session, while triaging the data-integrity queue)

[`computations/binding_alpha_shift_witness.py:45`](../computations/binding_alpha_shift_witness.py)
hardcodes the **CODATA-2018** electron mass

```python
# CODATA 2018
M_E_MEV = 0.5109989461
```

The canonical anchor is **CODATA-2022** `0.51099895069` (per `codata_2022_source.py`,
and the ct80-fixed `substrate/experimental_constants.py`). This is **not a
truncation** (the me3r class) — it is the **wrong vintage**: 0.5109989461 (2018)
vs 0.51099895069 (2022), differing in the 8th significant figure.

## Why deferred (not fixed in the surfacing session)

The script is a **witness producer** (`binding_alpha_shift_witness.py` →
`binding-alpha-shift-*.witness.json`). Correcting the literal regenerates the
witness, and the surfacing session ran in an **ad-hoc pip env** (no canonical
`pyhecke_native`/pinned mpmath) where witness regen shows env-skew (tr_M 8th
sig fig, q_50dp 10th). Fixing the literal **without** a clean regen would leave
the witness inconsistent with its producer. Queue for a **canonical-env**
session.

## Fix (for a canonical-env session)

1. `binding_alpha_shift_witness.py:45` → import `M_E_MEV` from the canonical
   registry (`codata_constants` / `codata_2022_source`) instead of hardcoding,
   OR set the literal to `0.51099895069` (acceptance (a)).
2. Drop the `# CODATA 2018` comment.
3. Re-run the producer in the canonical env (`python3 -u … 2>&1 | tee /tmp/…log`),
   commit the refreshed `binding-alpha-shift-*.witness.json` alongside.
4. Verify no other `0.5109989461` (CODATA-2018) literals lurk:
   `grep -rn "0.5109989461" computations/ tools/ --include=*.py`.

## Scope note

Distinct from **me3r** (three CODATA *registries*, two *truncated* — owner-gated,
package sources) and **46ke** (hidden codata literals rollup, 53 scripts). This is
a single in-repo producer with a *stale-vintage* (not truncated) value. Close: §4a (owner).
