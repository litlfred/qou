---
# qou-dke6
title: 'LP/SDP witnesses: 107 of 241 dual records are f64-era or unattributable; re-running moves residuals ~36 orders'
status: todo
type: task
priority: normal
created_at: 2026-09-04T08:14:33Z
updated_at: 2026-09-04T08:15:08Z
---

Found while wiring `qou-fr4d` (certified LP duality residuals). NOT caused by
that change -- established by measurement, see the attribution test below.

## The measurement

Scanning all 3488 tracked `computations/*.witness.json` for records carrying
the full LP/SDP dual field set (`y0_star`, `y_star`, `primal_obj`, `dual_obj`,
`duality_gap`) -- 54 files, 241 records:

    clarabel-mpfr        134
    <no backend field>   105    <- predates the field; nothing says how solved
    scipy-highs            2

So **107 of 241 (44%) are explicitly float64 or unattributable.**

## Why that matters, measured on three producers

Re-running three LP producers in an environment where the clarabel-MPFR
binary IS present, against their committed witnesses:

| producer | changed existing values |
|---|---|
| `derive_e_0_lp_dual_h3` | 304 |
| `pn_alpha_lp_dual` | 2292 |
| `rho_k_h3a_lp_dual` | 86 |

and the movement is not noise, it is the backend transition:

    duality_gap   committed 1.3871930965660104e-15   re-run 5.3455294201843912e-51
    x_star[2]     committed 6.293838348221709e-15    re-run -8.888369995547171e-39
    y_star_str[4] committed 3.82694087248660635e-14  re-run 3.8269387334409869e-102

The committed values sit at the **float64 noise floor**; the re-run values are
genuine. This is precisely the hazard `lp_dual_solver.py` documents in its own
source: *"the same producer run in CI, in a fresh container, and on a developer
box could write witnesses differing by ~28 orders of magnitude in residual with
nothing in the file saying which had happened."* Here it is, live on `main`,
and the `<no backend field>` bucket is the population where it is undetectable
from the file.

## Attribution -- this is NOT the qou-fr4d solver change

Tested rather than reasoned, because a code read is not evidence. Reverted the
solver to HEAD and re-ran with the UNMODIFIED code:

- `rho_k_h3a_lp_dual`: `primal_obj` still moves 3.2843401771028216 ->
  3.283906568708643 (that producer does not even call the canonical entry
  point -- it uses `scipy.optimize.linprog` directly).
- `derive_e_0_lp_dual_h3`: **the identical 304** changed values.

So the drift is entirely pre-existing.

## What NOT to do

Do not mass-regenerate. Two reasons:

1. Regeneration is **environment-dependent by construction** -- the value you
   get depends on whether the clarabel-MPFR binary is on the box. A sweep run
   without it would rewrite 134 good MPFR records as f64, which is strictly
   worse than the current state. Any sweep must set `QOU_REQUIRE_CLARABEL=1`
   so a missing binary is an error rather than a silent downgrade.
2. These are real numbers that downstream analysis has read. A 36-order move
   in a residual may or may not change a conclusion; that is per-producer work.

## Cheapest first step

Not a sweep: an **audit** that reports, per LP/SDP witness, which backend its
dual records claim and whether the producer reproduces them under
`QOU_REQUIRE_CLARABEL=1`. That separates "stale because f64-era" from "stale
for some other reason" without rewriting anything, and gives the sweep a
denominator. The 105 unattributable records are the ones worth resolving first
-- they are the bucket where the file itself cannot tell you.

## Related

- `qou-fr4d` -- the certified-residuals wiring that surfaced this.
- `qou-ftuv` (completed) -- states the LP path is f64-only, which is stale.
