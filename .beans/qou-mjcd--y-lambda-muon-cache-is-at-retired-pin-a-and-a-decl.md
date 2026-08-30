---
# qou-mjcd
title: y_lambda muon cache is at RETIRED pin A, and a declared-proton producer straddles on it
status: in-progress
type: bug
priority: high
created_at: 2026-08-30T12:32:00Z
updated_at: 2026-08-30T12:32:00Z
---

Found while closing `qou-0hnz`; measured before filing.

## The cache

`computations/y-lambda-mpfr-witness.json` is stamped `q0Anchor: muon` and holds
`q_0_50dps = 1.1099785955573347198997632204832250266562084087802` — **pin A**,
the vintage `fca08de7d2` RETIRED on 2026-08-22 (owner ruling "A -> CODATA 2022").
The current muon pin is C, `1.109978595642739…`. So this table is stale *as a
muon table*, independently of anything else.

**13 files read it on a non-comment line** (resolved, not `grep -rl`):
`atomic_tr_m_mpfr_50dps`, `audits/y_lambda_two_row_cap_gate`, `binding_K_direct`,
`chi_dual_path_xref_audit`, `iterative_lp_dual_h6_deuteron`,
`regenerate_y_lambda_mpfr`, `tr_m_wenzl_bridge_mpfr`, `witness_regen_wave`,
`y_lambda_macdonald_telescope`, + 4 more.

## The live straddle, quantified

`computations/iterative_lp_dual_h6_deuteron.py` is **manifest-declared
`physical_proton`** and `q_parameter.Q` resolves to `1.1099785827513808` for it.
But:

- `:155` `y_at_q0` <- `y-lambda-mpfr-witness.json`  (muon / pin A)
- `:174` `chi_at_q0` <- `chi_lambda_numerical(..., q_val)` where `q_val =
  float(Q0_FLOAT)` (**proton**)
- `:185` `tr_M_check = sum(y_at_q0[p] * chi_at_q0[p] ...)` — **the product mixes
  the two layers**

Consequence, measured in the committed witness: it declares `q0Anchor: proton`
and records `parameters.q_0 = 1.1099785827513808`, yet
`tr_M_check_at_q0 = 0.5751722457697738` sits **3.22 ppb** from the corpus
canonical proton `tr_M(beta_D) = 0.5751722439177718708265`. That gap IS the
straddle. A declared-proton witness is asserting proton over a mixed number.

## Todo

- [x] Decide the fix at the consumer: a declared-proton producer should read the
      PROTON table (`y-lambda-mpfr-proton-witness.json`), which
      `tr_m_wenzl_bridge_mpfr._Y_LAMBDA_BY_ANCHOR` already maps.
- [x] Confirm the proton table covers partitions of 6 before swapping.
- [x] Audit the other 12 readers for the same mixed-product shape.
- [ ] Separately: the muon table is at a RETIRED vintage. Regenerating it at pin C
      is an owner-visible change (`regenerate_y_lambda_mpfr.py --anchor ideal`)
      and must not be done silently.
- [ ] Regenerate affected witnesses (qou-jjge).


## Progress 2026-08-30

**Consumer fixed and verified.** `iterative_lp_dual_h6_deuteron` now takes its
weights from `tr_m_wenzl_bridge_mpfr.load_y_lambda_for_q0(6, Q0_FLOAT)`, which
selects the table from the q0 it is handed and refuses to serve the other
layer's. Measured on the regenerated witness:

| | tr_M_check_at_q0 | gap from canonical proton |
|---|---|---|
| before | 0.5751722457697738 | **3.22e-9** (the straddle) |
| after  | 0.5751722439177743 | **4.22e-15** (float64 round-off) |

All 3 assertions still pass.

**Audit of the other 12 readers — one more live instance found, and it was
already failing.** `y_lambda_symbolic_validate.load_mpfr_witness()` hardcoded
the muon table, while `Q0_STR = q_parameter.Q_50_DIGIT_STR` (PROTON) is in
`PROBES`, so `test_1_cross_q` used muon weights as the reference for the proton
probe at `TOL_CROSS_Q = 1e-30`. Run before fixing:

```
q=1.05                     4.41e-51  PASS
q=1.08                     4.57e-52  PASS
q=1.10997858275138080759…  5.93e-10  FAIL   <- the only probe reading this table
q=1.15                     2.16e-51  PASS
q=1.20                     9.36e-52  PASS
```

Fixed by selecting the table from `anchor_of_q0(Q0_STR)`, raising rather than
guessing. After: the proton probe passes at **1.93e-51**, same order as the rest.

The remaining readers are clean: anchor-aware via the accessor
(`atomic_tr_m_mpfr_50dps`, `chi_dual_path_xref_audit`, `binding_K_direct`,
`y_lambda_two_row_cap_gate`), the writer/accessor themselves
(`regenerate_y_lambda_mpfr`, `tr_m_wenzl_bridge_mpfr`), muon-only consumers, or
already fixed for this exact defect (`y_lambda_tower_infra`, whose comment
documents it).
