---
# qou-qyy0
title: 'SW-5a: offDiag nonvanishing at admissible distances (|d| >= 2)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-19T19:43:43Z
updated_at: 2026-08-19T19:44:36Z
parent: qou-59vq
blocking:
    - qou-jfr8
---

## Statement

`offDiag q d != 0` for real `q != 0`, `q^2 != 1`, and `|d| >= 2`. Blocks SW-5
(`qou-jfr8`): without it, an admissible swap gives only ONE oriented matrix unit,
and one orientation per edge does not reach every ordered pair `single U V 1`.

    offDiag q d = if d < 0 then 1 + a(d).a(-d) else 1     (SeminormalRep.lean:92)

so `d >= 0` is the plain 1 and the whole content is `d <= -2`.

## Derivation — DO NOT RE-DERIVE, and do not assume it is generic-only

Set `x = q^(2d)`, `y = q^2 > 0` (real q), so `x = y^d`.

    a(d) = (q - 1/q)/(1 - x^-1),   a(-d) = (q - 1/q)/(1 - x)
    (1 - x^-1)(1 - x) = -(1-x)^2/x
    => 1 + a(d)a(-d) = 1 - (q - 1/q)^2 . x/(1-x)^2

vanishes iff `(q - 1/q)^2 x = (1-x)^2`; and `(q-1/q)^2 = (y-1)^2/y`, so iff

    (y-1)^2 . y^(d-1) = (1 - y^d)^2                       (*)

**(*) is invariant under d -> -d** (multiply through by y^(2d)), so both signs
reduce to the natural-number case `e = |d| >= 2`.

**The natural-number inequality, and why e = 1 is the exception.** Factor
`y^e - 1 = (y-1).S` with `S = sum_{i<e} y^i`. Then (*) becomes `y^(e-1) = S^2`.
The sum contains the i=0 term `1` and the i=e-1 term `y^(e-1)`, DISTINCT exactly
when `e >= 2`, all terms positive, so `S >= 1 + y^(e-1)` and

    S^2 >= (1 + y^(e-1))^2 = 1 + 2y^(e-1) + y^(2e-2) > y^(e-1).

At `e = 1`: `S = 1`, `S^2 = 1 = y^0` — EQUALITY. That is precisely
`offDiag q (-1) = 0`, the size-1 orbit. So the vanishing is not an accident of
special q; it is the e=1 case and nothing else.

**No AM-GM, no half-powers.** An earlier sketch of mine reached for AM-GM on the
two middle terms; the `1 + y^(e-1)` bound is strictly simpler and avoids
`y^((e-1)/2)` entirely. Use it.

## Verified in EXACT RATIONALS before formalising

121 rationals q x 12 distances: 0 mismatches between the direct form and the
reduction (*), 0 vanishings at |d| >= 2, driving inequality strictly positive
throughout. No float64 anywhere.

## Implementation order

1. `sq_geom_lt` — pure real inequality, N powers: for `0 < y`, `y != 1`,
   `1 <= m`: `(y-1)^2 * y^m < (y^(m+1) - 1)^2`. Route: geom_sum factorisation +
   the `S >= 1 + y^m` bound via `Finset.sum_le_sum_of_subset_of_nonneg` on
   `{0, m} subset range (m+1)`.
2. The zpow reduction (*) for `d >= 2` and, by the `d -> -d` symmetry, `d <= -2`.
3. `offDiag_ne_zero_of_two_le_abs` — case on the sign; `d >= 0` is `offDiag_of_not_neg`.

## Why this is load-bearing, not plumbing

If offDiag DID vanish at an admissible distance, the tableaux reachable in one
direction would span an invariant subspace and the seminormal representation
would NOT be irreducible. The inequality is the mathematics, not the bookkeeping.
