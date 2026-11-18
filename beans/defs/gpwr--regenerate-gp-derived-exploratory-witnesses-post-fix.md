---
# gpwr
title: Regenerate GP-derived exploratory witnesses after the qou-b2ie GP fix (needs pyhecke_native wheel; canonical chain confirmed clean)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-18T01:30:00Z
updated_at: 2026-10-04T15:23:20Z
parent: qou-5vkl
---

## Context

The Geck–Pfeiffer cyclic-shift completion (bean `qou-b2ie`, merged) fixed
`chi_lambdas_via_gp` / `chi_q_via_gp`, which previously returned WRONG χ on
some long braid words (stalled reduction). Witnesses produced by the pre-fix
GP path should be regenerated to confirm/replace their values.

## Blast-radius audit (2026-07-18, in-sandbox checkcorpus)

**Certified chain — CLEAN (no action).** `canonical_tr_m_via_chi_cache.py`
and `chi_at_q0_via_hoefsmit_mpfr.py` do NOT call the GP path (seminormal
throughout) — confirmed by grep. All canonical binding / L1 / L2 witnesses
are unaffected.

**At-risk = exploratory only (regenerate to confirm).** Committed
GP-derived witnesses, none wired to a dashboard:
- `computations/deltalambda/he4-binding-k-averaged-interface.witness.json`
- `computations/deltalambda/he4-binding-k-fingerprint-stage1.witness.json`
- `computations/deltalambda/he4-binding-k-presentation-correction.witness.json`
- `computations/deltalambda/he4-binding-k-stage2.witness.json`  (this probe
  already CAUGHT the bug and rebuilt on seminormal; low risk)
- `derived-chi-catalogue*.witness.json` set (exploratory χ catalogue)

## Why not done here

Regeneration requires the `pyhecke_native` wheel (maturin build), unavailable
in this sandbox. Run in a dev/CI env: rebuild the wheel, re-run each producer
`2>&1 | tee /tmp/<script>.log` per the long-compute logging discipline, and
diff the witness. Each GP result can be pre-screened for free with the new
`pyhecke_native.chi_gp_trivial_rep_consistent(n, word)` (χ_[n]=q^writhe).
