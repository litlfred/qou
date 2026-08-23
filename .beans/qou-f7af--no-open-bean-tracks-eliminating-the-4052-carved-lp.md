---
# qou-f7af
title: No open bean tracks eliminating the 4,052 carved LP-dual float64s — qou-ftuv closed with route 2's solver half undone
status: todo
type: task
priority: normal
created_at: 2026-08-23T07:36:54Z
updated_at: 2026-08-23T07:37:20Z
---


Asked directly while working `qou/augu`: *what are the carved floats, and is
anything beaned to fix them?* Answer to the second half: **no.**

## What they are

Seven field names — `x_star`, `y_star`, `y0_star`, `u_lambda_star`,
`primal_obj`, `dual_obj`, `duality_gap` — raw LP/SDP solver output.
Measured 2026-08-22:

```
carved-name floats, live tree      4,246 in 45 witnesses
  of which SHADOWED (a *_str
  full-precision companion exists)   194 in  2 witnesses
  → genuinely excused               4,052 in 45 witnesses
```

(The two shadowed files are `binding-k-solver` and
`rho-prefactor-structural-verifier`; route 2's shadow rule skips those before
the carve-out counts them, which is exactly the arithmetic
`4,246 − 194 = 4,052` the audit reports.)

Concentration, top of the list:

```
1,066  pn-alpha-lp-dual              278  frobenius-repose
  812  a-K-via-lp-dual-full          227  ak-lp-dual-quotient-probe
  158  he4-binding-k-stage2          154  binding-k-solver
```

## Why they are excused, and by whom

`qou/ftuv` (closed 2026-08-11) laid out four routes and the **owner chose two
of them**: route 2 (the `*_str` shadow rule) and then route 3 (this carve-out).
The bean records both — *"route 2 taken (owner decision)"*, *"Owner took route
3 after route 2's audit half landed"* — so the `# owner decision 2026-08-11`
comment in `witness_raw_float64_audit.py` is accurate, not self-asserted.

The reason is structural: `scipy.linprog` and Clarabel are float64 solvers, so
the standing fix ("carry `mpmath.mpf` from the source, serialize with
`_precision.fmt`") has **no source to carry from**. And stringifying is
explicitly ruled out by `lp_dual_solver.to_dict()`'s own docstring — 56
producers do arithmetic on those values (`sum(r["y_star"] …)`,
`r["duality_gap"] < 1e-6`), so it would break readers *silently*.

## The gap

The only route that would actually remove them is **route 2's solver half** —
build `clarabel-operator-selection-lp` and move onto an MPFR backend. `ftuv`
records it as *"Not taken, and no longer needed for the gate … Left undone
deliberately"*, then closed. So:

- the carve-out is permanent unless someone reopens the question;
- **nothing tracks reopening it**; and
- the ratchet reports the excused count every run, so the number grows quietly
  as new LP witnesses land. It went 3,661 → 4,052 in one afternoon of `augu`
  work — legitimately (duals that should always have been emitted), but with
  no ceiling and no owner looking at the total.

`ftuv` itself anticipated the shape: *"A carve-out that cannot be seen is
indistinguishable from a hole."* It is seen. What is missing is anyone
deciding whether it should ever close.

## Not claimed

That the carve-out is wrong. The reasoning behind it is sound and the
alternative was measured and rejected on evidence. This bean exists so the
*absence of a plan to retire it* is tracked rather than implied by a closed
bean's parenthesis.

## Next

- [ ] Owner: is the carve-out permanent, or is an MPFR/Clarabel exact backend
      wanted eventually? If permanent, say so in
      `witness_raw_float64_audit.py` so a future reader does not re-derive the
      four routes — which `ftuv` explicitly tried to prevent.
- [ ] If not permanent: scope route 2's solver half. `ftuv` notes the shadow
      rule is already in place to recognise the `*_str` companions it would
      produce, so the audit side is done.
- [ ] Either way, consider a ceiling or a per-witness cap on the excused
      count, so growth is a decision rather than a side effect.
