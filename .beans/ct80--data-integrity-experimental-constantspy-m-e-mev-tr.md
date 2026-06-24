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

## Blast-radius scope (2026-06-24, session bold-mendel)

Concrete counts (non-deprecated): **173 importers** of `experimental_constants`;
**155 are witness-emitting**; **143 import `M_E_MEV`**. Canonical full-value
source confirmed: `codata_constants.py:111` does `from codata_2022_source import
M_E_MEV` (full 0.51099895069).

**Fix is one line** — route `experimental_constants.py` M_E_MEV/ERR to
`codata_2022_source` (dedup, single source of truth, matches the sibling).
**But** it drifts ~143 witness-emitting producers' m_e-dependent values by
1.35e-9 → a substantive (non-metadata) witness-field change across ~143
witnesses → **large coordinated regen, owner-gated** (option 3 in the triage
above, NOT the small option-2 case). Same scope/producer set as the `768d9ddf`
"143-producer canonical regen".

**Recommendation:** fold the m_e import-unification into the **next coordinated
canonical regen** (don't spin a standalone 143-witness churn PR). Physically
negligible (1.35e-9, ~580× below the CAL-2 floor); single-source-of-truth
hygiene, not an accuracy fix. Gated on owner scheduling the regen.

## Regen attempt 2026-06-24 — SANDBOX DEGRADES PRECISION (must be full-env)

Owner-authorized "rerun witnesses on separate branch". Ran the
M_E_MEV-importing producers (349 scanned) in the sandbox → **the regenerated
witnesses REGRESS precision**: e.g. `atomic-mass-via-rho-k.witness.json`
`tr_M_at_q0` went 50-dps mpf `1.06530623807587821568…` → f64
`1.06530622861316705936…000000` (trailing zeros). `tr_M` does **not** depend on
m_e — the change is the **f64 fallback** (no `pyhecke_native` / 50-dps in this
env), NOT the m_e fix. Committing sandbox regens would be a precision
regression (L1 violation). All regenerated witnesses reverted.

**Conclusion:** the value fix (`M_E_MEV 0.51099895000 → 0.51099895069`) is on
the branch, but the **witness regen MUST be run in a full env** (pyhecke_native
+ 50-dps) so the ~143 m_e-dependent witnesses re-emit at full precision. Fix +
regen must land **together** (don't merge the fix alone — it leaves the
importers' witnesses stale). Same native-dep gate as the `768d9ddf` follow-up.
