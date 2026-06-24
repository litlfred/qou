---
# ct80
title: 'Data-integrity: experimental_constants.py M_E_MEV truncated vs codata_constants sibling (me3r follow-up)'
status: todo
type: task
created_at: 2026-06-24T17:51:20Z
updated_at: 2026-06-24T17:51:20Z
---

**Finding (me3r follow-up).** `computations/substrate/experimental_constants.py:41`
has `M_E_MEV = 0.51099895000` (truncated), while its sibling
`computations/substrate/codata_constants.py` imports the full
`0.51099895069` from `codata_2022_source`. Both live in
`computations/substrate/`, so the in-repo compute layer carries a
**split** m_e (000 vs 069). ~266 non-deprecated scripts do
`from experimental_constants import M_E_MEV` (e.g. `atom_mass_derived.py:80`).

PR #2725 reconciled the two **external-package** registries
(`qou_substrate/constants.py`, `qou-mass/.../codata_constants.py`) but its
3-registry enumeration did **not** include this in-repo file.

**Impact is likely low**, not high: #2725's controlled A/B proved the L2
dashboards (`per_observable_100x_status`) use `codata_constants` (069), so
L2 is unaffected. The open question is how many of the 266
`experimental_constants` importers emit **committed production witnesses**
that would drift if the value were corrected.

**Triage / fix path:**
1. Of the 266 importers, identify those that write committed
   `*.witness.json` whose values depend on m_e at > 8 sig figs.
2. If that subset is empty/tiny → make `experimental_constants.py` import
   `M_E_MEV`/`M_E_MEV_ERR` from `codata_2022_source` (dedup to one source of
   truth) and regen the few witnesses.
3. If the subset is large → coordinated re-run (owner-gated; `… 2>&1 | tee`
   per long-compute discipline), or relabel the comment 8-fig-honest if the
   truncation is deliberate (no rationale is currently documented).

Physically negligible (1.35e-9 rel, ~580× below CAL-2 floor); this is
single-source-of-truth hygiene, not a precision-accuracy fix.
