# j1hg over-count final drain — all 12 are regex false-positives (`over_count_count → 0`)

**Date:** 2026-06-30
**Bean:** `j1hg` (canonical-watcher over-count 3-input rollup) — closed.
**Disposition:** B (owner ruling 2026-06-30 — see
[`docs/workplans/2026-06-30-j1hg-z5vu-overcount-q0repin-sequencing.md`](../workplans/2026-06-30-j1hg-z5vu-overcount-q0repin-sequencing.md)).
**Audit:** `computations/audits/canonical_script_input_audit.py` →
`canonical-script-input-audit.witness.json`.

## Result

The `4-input-mp-and-mn` over-count signal is now **0 / 1588**. The
2026-06-22 triage had left 23 "genuine input" candidates; sibling refactors
since then dropped that to 12, and rigorous per-script inspection on
2026-06-30 finds **all 12 remaining are regex false-positives** — none feeds
CODATA `m_n` into a mass/binding *prediction*. They are allowlisted in
`OVER_COUNT_MN_NOT_INPUT` with per-script rationale.

## Why the 12 are not over-counts

The over-count audit is pure-regex: it fires whenever a script references both
`M_P_MEV` and `M_N_MEV` tokens. Two patterns make that a false positive here:

### (a) Vestigial `M_N_MEV` import — computation uses *derived* m_n (11 scripts)

`atomic_mass_via_rho_k`, `channel_product_mass`, `hecke_core_legacy`,
`iterative_lp_dual_h6_deuteron`, `rho_k_h3a_{co_casimir,crystal,lp_dual,refinement,wenzl_bridge}`,
`unified-mass-molecular`, `vol_density_per_block_wiring`.

Each **imports** `M_N_MEV` but has **zero non-import uses** of it (verified:
`grep M_N_MEV | grep -v '^…:(from|import)'` → 0 lines). The actual constituent
sums use `m_n_derived_3input` (= m_p + Q_β + m_e), the canonical chain — e.g.
`channel_product_mass.py:105` `M_free = Z*M_P_MEV + N*m_n_derived_3input + Z*me`.
So the genuine three-calibration refactor is **already done**; only the
now-unused import lingers. (Removing those vestigial imports is a cosmetic
canonical-env follow-up — for the Hecke producers it would scriptHash-drift a
witness that can only be cleanly regenerated with `pyhecke_native`.)

### (b) `M_N_MEV` as a CODATA comparison reference (1 script)

`per_knot_density_per_block_wiring.py` — `mnc = mp.mpf(repr(M_N_MEV))` (L100) is
used only as the experimental comparison value (`codata = mpc if proton else mnc`,
L126; `codata_avg = (mpc+mnc)/2`, L144), never as a prediction input. This is
the same "comparison-only" class the 2026-06-22 triage whitelisted 27 scripts under.

## Scope honesty

This drain corrects a **false signal**, it does not perform value-changing
refactors. The audit number reflects reality: on `main`, **no** script
over-counts the three-calibration discipline by feeding CODATA `m_n` into a
prediction. Per disposition B, this was decoupled from the `z5vu` q₀ migration
(closed will-not-migrate-by-design) — `m_n = m_p + Q_β + m_e` is the same value
regardless of the muon/proton anchor.
