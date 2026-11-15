---
# qou-3bq6
title: 'GAP: d_from_scratch emits 3 raw float64 fields — latent, newly visible now the producer can run'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T14:43:39Z
updated_at: 2026-11-15T09:00:00Z
parent: qou-9nnz
---

`computations/d_from_scratch.py` **could not run at all** on a clean tree — it
looked for `habiro-coefficients-atomic.witness.json` beside itself in
`computations/`, and the file lives in `computations/habiro/` (written there by
`habiro/habiro_coefficients_atomic.py`). Fixed: try the real location first,
keep the old as fallback, and raise a message naming the producer instead of a
bare `FileNotFoundError`.

**Making it runnable exposed a latent defect.** With the path fixed it reaches
exit 0 and the precision guard reports:

    raw-float64: d-from-scratch.witness.json: 3 raw float64 field(s) would enter
      .parameters.E_0_MeV_per_cat, .data.terms_50dps.err_pct, .data.terms_50dps.err_ppb

**The regenerated witness was NOT committed.** Committing it would grow the
raw-float64 population, which AGENTS.md forbids ("baselines drain, never grow;
fix at the producer"). It would also downgrade the environment record —
this container is python 3.11.15 against the witness's 3.12.3.

**Fix at the producer:** carry those three as `mpmath.mpf` and serialize with
`_precision.fmt`. Then re-run and diff — noting the committed witness predates
the path breakage, so its numbers come from a run nobody in this clone could
reproduce until now.

Found while cost-checking the 11 `qou-tekx` "reads a declared pin, merely
stale" producers.

## 2026-11-15 — closed

The three named fields were moved to `_precision.fmt` in #7826 (merged `99781d7aa8`). The remaining
float64 inputs, `tr_M_f64` (free traces from `light_isotope_sweep.tr_M_at_q0`), are removed
entirely by the one-functional fix (tracker #7735, owner "1 2 fix"): every trace in Term 1 is now
read at 50 dps from `atomic-tr-m-mpfr-50dps-proton` / `binding-canonical`. The producer no longer
emits any float64-derived value.
