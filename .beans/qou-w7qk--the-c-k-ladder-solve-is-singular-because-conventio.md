---
# qou-w7qk
title: The c_k ladder solve is singular because convention D zeroes y_(1,1,1) — an import, not the file
status: todo
type: task
created_at: 2026-08-24T02:26:06Z
updated_at: 2026-08-24T02:26:06Z
---

`qbeta_ck_local_taylor_around_u0_probe.py` exits rc=0 in ~14 s and writes a
witness whose entire payload is

    "solver_failure": "matrix is numerically singular"

All ten real data keys (`c_extracted`, `R_taylor_around_u_0`, `c_2_gate`,
`ladder_consistency_passed`, …) are gone. The failure is inside
`mp.findroot(residuals, c0, solver="mnewton", tol=1e-30)` — the singular matrix
is mnewton's Jacobian.

**The producer is honest about it**, and that is worth saying: the assertion
`operator_markov_route_is_not_canonical_ladder_target` goes
`computed 1 -> 0, passed True -> False` rather than vanishing. It records the
failure and fails its gate — precisely what the `probe_4_li6` conditional did
NOT do (fixed in e1a6295df). That is why this surfaced as a visible
collapse-with-flip instead of a silent thinning.

---

## Both commits touching the file are EXONERATED — bisected, not reasoned

The file has changed exactly twice since its witness was computed (2026-07-07),
and neither is the cause. Each was reverted individually, at HEAD, and re-run:

  **`70d1ade38` (2026-08-09, the C->D excision)** changed one line:

      -    z_qq = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))     # C
      +    z_qq = q**3 / (q**2 + 1)                      # D

  Restoring the C form: **`matrix is numerically singular`, identically.**

  **`34b2a75d4` (2026-08-23, the dps sweep)** changed `mp.mp.dps = 50` to
  `set_compute_dps()`. Restoring the literal `50`: **identical failure**,
  confirmed by the run's own banner (`Step 2: Converting to mpmath (dps=50)`).

Precision is independently exonerated at `QOU_COMPUTE_DPS` 50, 60, 70 **and
90** — four points, because a singular Jacobian is exactly where precision
could plausibly be the culprit. Raising precision does not approach a solution.

## The cause is an IMPORT, and the mechanism is exact

The probe's only domain import is
`y_lambda_wenzl_bridge.y_lambda_wenzl_bridge_symbolic`, and that module changed
TWICE after the witness was computed:

    b88aabc73  2026-08-09  "the Wenzl bridge was C under a D interface, and a
                            WITNESS CACHE was a second hybrid"
    993e15015  2026-08-10  "both y_lambda roots to D — muon cache and the
                            28k-entry wenzl table"

Evaluated today, the bridge returns:

    y_(3,)       (q**4 + 1)/(q**4 + 2*q**2 + 1)    ->  0.5054042276904083…
    y_(2, 1)     q**2/(q**2 + 1)**2                ->  0.2472978861547958…
    y_(1, 1, 1)  0                                 ->  0     <- free_symbols: {}

`y_(1,1,1)` is now the **integer 0**, not a small number. That is the convention-D
row cap stated verbatim in `y_lambda_at`'s docstring: *"under C, y_λ(3,q₀) =
(0.4153958, 0.2809296, 0.0227449); under D it is (0.5054042, 0.2472979, 0) —
the defining difference being the row cap y_λ = 0 for ℓ(λ) > 2."*

The probe builds

    tr_M = y_3*chi_3 + y_21*chi_21 + y_111*chi_111

so under D **the third term is structurally gone**, and it then fits 7 unknowns
(c_2..c_8) against Taylor orders of that tr_M. The Jacobian is singular because
a degree of freedom the fit needs no longer exists — which is exactly why the
failure is identical at every precision.

## This is NOT "the corpus ceasing to lie"

Every other flip on this branch has been a number moving to a correct new
value. Here the producer **cannot compute its answer at all** under the current
formulation. Recording the assertion as "refuted" would be wrong in the
opposite direction from a stale pass: the mathematical claim was not tested and
failed, it was never evaluated.

## The decision

The probe's premise — fit the c_k ladder against a three-character tr_M — does
not survive the row cap. Either:

  (a) **Re-formulate for the two-character D tr_M.** With `y_(1,1,1) ≡ 0` the
      system has fewer independent orders; the number of fittable c_k must come
      down accordingly, or the fit must be re-posed. This is a re-derivation,
      not a patch.
  (b) **Record the probe as superseded by the D ruling** and retire it, if the
      c_k ladder question it was built to answer is now answered elsewhere.

Do NOT relax the solver or seed it differently to get a number out — a singular
Jacobian is telling the truth about the system it was handed.

Note the docstring already flags a *nearby* singularity as expected by
construction ("indicating a nearby singularity… PR #1786 PROVED c_2 = -1"),
which makes (a) plausible: the ruling may have moved the evaluation point onto
a singularity it was designed to sit near.

## The structural lesson, and it is the second instance

**The C->D pre-check missed this, and correctly so as written.** Scanning the
file for `y_lambda_at`, `gram`, `TR_M` or `habiro-coefficients-atomic` returns
nothing — the migration reached it through a DIFFERENT entry point to the same
family, one import away.

That is the same gap as bean qou-w701, where the drift axis could not see a
producer whose own hash barely moved while its imports changed underneath it.
Twice now the answer has been one level up the import graph, and twice nothing
mechanical could point there. **Any C->D pre-check needs to follow first-party
imports, not just grep the file.**
