---
# qou-q7f1
title: Migrate wedderburn_lp_ew_wiring off float64 onto the MPFR LP path (62 baselined f64 fields)
status: todo
type: task
priority: normal
created_at: 2026-08-18T16:24:41Z
updated_at: 2026-08-18T16:27:52Z
---

## Scope (PR #5260, owner directive "no f64 path")

`wedderburn_lp_ew_wiring.py` runs float64 end-to-end and its witness carries
**62 raw float64 fields**, tolerated by an entry in
`raw-float64-baseline.json`. Baselines drain, never grow — this is the drain.

f64 sites in the producer:

    133, 204, 346   q0_value = float(sympy.Float(Q_50_DIGIT_STR, 50))
    45-82           _hoefsmit_f64_matrices -> np.array(..., dtype=np.float64)
    135, 202        t = np.zeros(..., dtype=float);  G = np.zeros(..., dtype=float)
    141, 224        float(np.trace(M_ij))
    250             np.array(..., dtype=np.complex128)
    273             q_0_float = float(q_0)

The 50-dps substrate constant is truncated to f64 on entry, so everything after
it is f64 regardless of what the LP solver can do.

**The pieces now exist, but it is not a drop-in.**

  * `pyhecke.lp_dual_solver.solve_..._mpfr` (line 292) solves at ≈50 dps and
    takes decimal strings, so the boundary adds no truncation.
  * `gram.gram_matrix_mp_strings()` / `tr_m_mp_strings()` feed exactly that
    boundary — and were returning **convention C** until PR #5260 fixed them
    (bean qou-h4ab). Any earlier attempt at this migration would have moved
    onto wrong numbers, 18.5 % off.

**Blockers, measured:**

  1. `solve_..._mpfr` needs the `clarabel-operator-selection-lp` CLI or a
     `pyhecke_native` wheel built `--features clarabel-lp`. Neither is present
     in this sandbox (no prebuilt binary; `cargo` is available, so it is
     buildable).
  2. Its own docstring: "EXPERIMENTAL ... NOT yet cross-checked against the
     scipy backend to 1e-25 — that needs a scipy+numpy environment. The scipy
     backend therefore remains the default." So the cross-check is itself a
     prerequisite deliverable, not an afterthought.
  3. `gram_matrix_mp` is the 6x6 H_3 NF Gram. This producer builds an
     n_pairs x n_pairs Gram over **pair amplitudes at H_{3A}** — a different
     object, so the mp Gram is not a substitute for `_full_wedderburn_gram`.
     An mpmath Hoefsmit builder is needed too (`hoefsmit_matrices_numeric`
     exists and is used at mp precision by `rho_k_h3a_refinement`).

**Expected outcome.** Not a value change of the kind that moves a conclusion —
f64 vs 50-dps on a well-conditioned Gram is ~1e-16 — unless the LP is
ill-conditioned, in which case the dual could move materially and that is worth
knowing. The witness's own `t_legacy` values differ from the KLR-positive `t`
by design, so do not read a `t` change as a precision result.

Do the cross-check (blocker 2) first: without it, a migrated result has nothing
to be validated against.
