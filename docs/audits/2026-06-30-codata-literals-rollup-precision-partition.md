# CODATA hidden-literal rollup (bean 46ke) — precision partition + data-integrity findings

**Date:** 2026-06-30
**Branch:** `claude/46ke-codata-literals-rollup-2026-06-30`
**Bean:** `46ke` — "Integration: canonical watcher — hidden codata literals rollup (53 scripts)"
**Related beans:** `me3r` (reconcile three m_e CODATA registries — truncation),
`ce18` (data integrity: stale CODATA-2018 m_e), `fvxq` (route remaining inline mass literals).

## TL;DR

Bean 46ke is **not** a blanket-mechanical rollup. Routing a hardcoded CODATA
literal onto `computations/substrate/codata_constants.py` is **value-preserving
only for a narrow subset**. This audit partitions the remaining literals into
*safe-to-route*, *witness-identical-but-not-raw-identical*, *precision-losing*,
and *value-mismatch (data integrity)*, so future agents (and the `me3r`/`ce18`
siblings) do not silently change numbers by "rolling up" a literal that does not
actually equal the registry value at the consumer's working precision.

## The registry-precision footgun (root cause)

`codata_constants.py` exposes `mp.mpf` **objects**, frozen at the precision they
were created with:

| Symbol | How created | Effective dps of the stored `mpf` |
|--------|-------------|-----------------------------------|
| `M_E_MEV`, `M_E_MEV_ERR` | `from codata_2022_source import …` | full source precision |
| `Q_BETA_MEV`, `M_{P,N}_…_VALIDATION`, AME bindings | `_load_mpf(...)` with `mp.workdps(max(50, …))` | **50 dps** |
| `M_MU_MEV_VALIDATION`, `M_PI_*`, `M_K_*`, `M_H1_*_VALIDATION` | bare `mp.mpf("…")` at import-time `mp.dps` | **default ~15 dps** |
| `U_MEV` | `mp.mpf(regex match)` at import-time `mp.dps` | **default ~15 dps** |

A consumer that parses a string literal `mp.mpf("0.51099895069")` at its own
working precision therefore compares to the registry object as follows
(verified empirically this session):

| Literal → symbol | dps = 50 | dps = 100 |
|------------------|----------|-----------|
| `0.51099895069` → `M_E_MEV` | **identical** | differ (5.6e-52) |
| `938.27208816` → `M_P_MEV_VALIDATION` | **identical** | differ |
| `105.6583755` → `M_MU_MEV_VALIDATION` | **differ** (registry ~15 dps) | differ |
| `931.49410242` → `U_MEV` | **differ** (registry ~15 dps) | differ |
| `497.611` → `M_K_0_MEV_VALIDATION` | **differ** (registry ~15 dps) | differ |

Consequences:

1. **Raw-bit-identical routing holds only for `M_E_MEV`/`M_P_MEV_VALIDATION` at
   working precision ≤ 50 dps.** The `_precision.set_compute_dps()` **default is
   65 dps compute** (50 dps serialization), so several `*_50dps`-named scripts
   that call `set_compute_dps()` bare actually run at 65 dps. For those the raw
   `mpf` bits change at ~1e-52 — **below the 50-dps witness serialization floor**
   (so committed `*.witness.json` are unchanged) but **not** raw-identical.
2. **Routing onto `M_MU`/`U_MEV`/`M_K0` *loses* precision** today (registry holds
   only ~15 dps), so it would change numbers even at 50 dps. These constants
   should first be lifted to ≥50-dps parsing in the registry (that is `me3r`
   territory — do **not** do it under 46ke without owner sign-off).

## Literal partition (non-`_deprecated`, non-witness)

### A. Safe-to-route (raw-bit-identical, ≤50 dps, exact-value match)

Only `M_E_MEV` / `M_P_MEV_VALIDATION` exact-match literals in scripts pinned to
exactly 50 dps. Routed in this PR:

- `yekutieli_volume_join.py:456` — `m_e = mp.mpf("0.51099895069")` (`mp.mp.dps = 50`).

Candidates needing a per-file dps confirmation before routing (named `_50dps`
but using `set_compute_dps()` whose default is 65): `h4_residual_vs_fine_structure_50dps`,
`implied_h2_coefficient_audit_50dps`, `reading_a_residual_at_50dps`,
`q_dirac_linking_weight_extended_50dps`. For these the routing is
**witness-identical** (50-dps serialized output unchanged) but not raw-identical;
left for a follow-up that runs each before/after.

### B. Value-mismatch — data integrity, NOT a mechanical rollup (→ `me3r`/`ce18`)

These literals do **not** equal the registry value; "rolling them up" would
*change* the number. They are stale or variant CODATA editions and must be
reconciled deliberately (which edition is canonical?), not silently routed:

| File / line | Literal | Registry | Note |
|-------------|---------|----------|------|
| `mass_binding_dashboard.py:178` | `U_MEV = 931.49410372` | `931.49410242` | wrong u→MeV (…372 vs …242) |
| `m_sym_error_budget.py:50` | `U_TO_MEV = 931.49410372` | `931.49410242` | same wrong u→MeV |
| `probes/hecke_channel_binding_probe.py:130-131` | `938.27208943` / `939.56542194` | `…816` / `…052` | proton/neutron variant edition |
| `probes/deuteron_fpn_wlambda_wiring.py:129-130` | `938.27208943` / `939.56542194` | `…816` / `…052` | same variant |
| many (`0.51099895`, `0.510998950`, `0.51099895000`) | 8–11 fig m_e | `0.51099895069` | truncated/stale m_e (the `me3r` truncation class) |

The `931.49410372` u-conversion in two **production** scripts
(`mass_binding_dashboard`, `m_sym_error_budget`) is the highest-value item here —
it is a genuinely wrong constant, not just a truncation. Flagged to `ce18`.

### C. Exploratory tail — deferred per bean (low value)

`probes/`, `qbeta/`, `phase5/`, `ocneanu_*`, `mmu_*`, `q_beta_*`, and
`_deprecated/` (≈100+ literal sites) — the bean's prior drains
(PR #2606, 2026-06-22) explicitly stopped here for diminishing returns. Not
touched.

### D. False positives (docstrings / prints / labels) — leave alone

`atlas_render_per_z.py:181`, `audits/hardcoded_literal_audit.py:292`,
`binding_alpha_shift_witness.py:18`, `gap_a3_cross_atom_overshoot_probe.py:18`,
`hydrogen_step_by_step.py:146`, `per_observable_100x_status.py:162`,
`m_pi_hecke_prediction_probe.py:12/36/365`, `vendor_ame2020.py:215`,
`m_p_substrate_identity_50dps.py:55/59` — the literal is in prose/comparison
text, not a live assignment.

## Recommendation

1. **46ke is effectively at diminishing returns for *consumer* routing.** The
   safe set is small; most remaining sites are exploratory (C) or data-integrity
   (B). Routing the witness-identical (A-candidate) files is low-value churn.
2. **The real unblock is a registry fix** (`me3r`): store CODATA values as the
   canonical **strings** (or re-parse at the consumer's `mp.dps`) so a routed
   import is bit-identical at *any* precision, and lift `M_MU`/`U_MEV`/`M_K`/
   `M_PI` off default-dps parsing. Until then, routing onto those symbols is a
   precision regression.
3. **The `931.49410372` u-conversion in two production scripts is a concrete
   bug** (`ce18`): it disagrees with CODATA-2022 `931.49410242` at the 7th
   figure. Owner should confirm before a fix lands (it will change those scripts'
   numbers).

This audit is the durable deliverable; the single safe routing below is a
down-payment that demonstrates the value-preserving pattern.
