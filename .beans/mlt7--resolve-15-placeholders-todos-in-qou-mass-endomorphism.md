
## Result (2026-06-23, session nifty-cerf, PR #2649)

Honest actionable 2 → **0**.
- `explicit-central-idempotent` item: already resolved on main (commit
  16deaa76 cited the (2,2) central-idempotent witness sorry). Counter
  confirms 0 there.
- `qbeta-per-block-chi-closed-forms.lean`: `delta_tau_M_surrogate_taylor_coeff_2`
  was a **`theorem : True := trivial` vacuity dodge** (forbidden by AGENTS.md
  §1a, caught by vacuity audit 508cbd70). Converted to the **honest §1a
  disposition 2**: stated the real proposition
  `deriv (deriv delta_tau_M_surrogate) 1 / 2 = 5/6` (the order-2 Taylor
  coefficient f''(1)/2! = 5/6, matching the docstring's `+(5/6)w²` and the
  SymPy witness) with `sorry` + the existing `-- Ref:`. Reworded the trailing
  "Stated as TODO" comment. Full 2nd-derivative proof deferred (build-gated;
  orders 3..7 remain future work vs the same witness).

NOT done (build-gated): proving the cited order-2 sorry. Pending human close.
