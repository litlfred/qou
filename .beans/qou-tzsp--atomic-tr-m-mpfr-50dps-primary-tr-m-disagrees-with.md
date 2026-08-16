---
# qou-tzsp
title: 'atomic-tr-m-mpfr-50dps: primary tr_M disagrees with its own peel_cross_check by 1.85e-9'
status: todo
type: task
priority: normal
created_at: 2026-08-16T21:23:42Z
updated_at: 2026-08-16T21:24:24Z
---

## Evidence (PR #5260, rho_k_h3a_residual_decomposition.py)

`atomic-tr-m-mpfr-50dps.witness.json` carries two deuteron tr_M values that
disagree with each other:

    results.tr_M_at_q0_50dps                  = 0.57517232916588433221594741758...
    results.peel_cross_check.tr_M_at_q0_50dps = 0.57517233101788385191979179668...
    difference                                = 1.8519995e-9

An INDEPENDENT route — the Schur-Weyl sum Sum_lambda y_lambda chi^lambda, built
from the Wenzl-bridge y_lambda and a fresh Hoefsmit chi, evaluated at the
witness's own muon q_0 — lands on:

    0.5751723310178838519197917966871536588755

i.e. it matches the **peel_cross_check** branch to 3.1e-49 (the 50-dps engine
floor) and misses the **primary** branch by exactly 1.852e-9.

Two independent computations agreeing to the floor is strong evidence the
PRIMARY value is the wrong one. That matters beyond bookkeeping: `primary` is
the field consumers read (`rho_k_h3a_refinement.py:303` takes
`r["tr_M_at_q0_50dps"]`), so every downstream self-check has been differencing
against the less reliable of the witness's own two numbers.

Same magnitude appears on the other atoms in that witness (helium-3, helium-4,
tritium rows each show a primary/peel gap in the 1e-9 range), so this is likely
systematic in the peel-vs-direct routes rather than specific to the deuteron.

**Not fixed here** — the fix belongs to that witness's producer, and deciding
WHICH branch is canonical needs the producer's author. Scope-(a): this is a
localisation, not a proof that `peel` is right; it is evidence, and the third
independent route is what would settle it.
