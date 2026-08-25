---
# qou-fu8c
title: aK LP dual degenerates under convention D — re-pose on the two-row quotient
status: completed
type: task
priority: normal
created_at: 2026-08-14T16:21:57Z
updated_at: 2026-08-14T18:45:19Z
---

## The finding

`computations/aK_via_lp_dual_full.py` recovers `a_K` as

    a_K = 1 + (chirality dual sum) / |y0*|

so it exists only while the net constraint's shadow price `y0*` is nonzero.
Under **convention D** it is not. Every `ℓ(λ) ≥ 3` weight vanishes identically
(`qou-u2jg`, Lean), the Wedderburn blocks this LP is posed over collapse, and
the solve returns the trivial point.

Measured on the merged branch (PR #4928), all six atoms:

| atom | A | y0* | primal_obj | dual_obj | a_K^dual |
|---|---|---|---|---|---|
| proton | 1 | −0.0000 | 0.0 | 0.0 | degenerate |
| neutron | 1 | −0.0000 | 0.0 | 0.0 | degenerate |
| deuteron | 2 | −0.0000 | 0.0 | 0.0 | degenerate |
| tritium | 3 | −0.0000 | 0.0 | 0.0 | degenerate |
| helium-3 | 3 | −0.0000 | 0.0 | 0.0 | degenerate |
| helium-4 | 4 | −0.0000 | 0.0 | 0.0 | degenerate |

Under convention C the guard fired on **none** of them (`a_K^dual ≈ 58.73` at
row 0). So this is a convention-induced collapse, not a solver flake.

## Scope — stated per the (a)/(b) rule

**Scope (a), NOT (b).** The claim is: *this LP, as posed over the full
partition set, has no dual solution under convention D.* It is **not** a claim
that no LP recovers `a_K`. Re-posing on the two-row quotient is untested and is
exactly what this bean asks for. Do not cite this as "the LP-dual route to a_K
is ruled out."

## Why it is the same shape as two known items

This is the **third** convention-D degeneracy with one structure — the
`ℓ(λ) ≥ 3` blocks are the radical under D, so any object built over the full
block set inherits a null direction:

1. **The Gram form goes singular** — `tools/pyhecke/python/pyhecke/gram.py`,
   `G_INV = np.linalg.inv(G)` at import; `QOU/QBeta/GramSignature.lean`.
   Blocked deliberately; bean `qou-w8zz` (D1(b)).
2. **`y-lambda-sdp`'s positivity question changes its answer** — under C no
   non-negative solution (`n = 4,5,6` carry negatives to −8.4e-4); under D it
   holds exactly, and the C-era violators are precisely the partitions D sends
   to zero.
3. **This LP** — same collapse, same fix shape.

In all three the live content is the two-row block and the right object is on
the quotient, not the full 6-dim / full-partition ambient.

## What was done, and what deliberately was not

**Done** (PR #4928, commit `291914b5f5`):
- `a_K_via_lp_dual` emits `null`, never `float("nan")`. Bare NaN is not valid
  JSON (RFC 8259) — `json.dump` writes the token `NaN`, which Python reads back
  and strict parsers reject. It also poisoned the impact report, which scored
  this witness at 2.1e21 ppm purely from differencing against NaN.
- New `a_K_dual_status` field carries the reason beside the value.
- Fixed a pre-existing crash: the summary table hit `unsupported format string
  passed to mpf.__format__` **after** `w.save()`, so the producer exited 1
  having actually succeeded — which the harness records as a failure and
  re-runs forever.

**Deliberately NOT done.** No nonzero normaliser was invented. Manufacturing a
`y0*` to make `a_K` come out would be a fit, not a derivation
(§"Axiomatization is NOT a Proof").

## Next step

Re-pose the LP on `H_n / rad` — the span of the `ℓ(λ) ≤ 2` blocks — and check
whether `y0*` is nonzero there and whether the recovered `a_K` agrees with
`a_K_closed(A)`. If it does, that is the convention-D form of the probe and it
should replace the ambient one. If `y0*` is still zero on the quotient, that is
a genuinely stronger negative and worth recording as such.

Cross-refs: `qou-w8zz` (the Gram quotient — same repair, do them together or at
least share the quotient construction), `qou-ng7j` (the detector is blind to
non-`y_λ` convention-C quantities, which is why this file was never on the
work list under its own name).
