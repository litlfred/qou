---
# qou-dsif
title: 'GAP: (P), the Pieri step of the Macdonald telescope — the induction over addable corners'
status: todo
type: task
priority: high
created_at: 2026-08-27T05:35:38Z
updated_at: 2026-08-27T05:36:22Z
---

Successor to `qou-6a7w`, which is completed (PR #5857 merged `6f4d0d2a3a`).
Live on PR #5871.

## The goal

`QOU.MathlibExt.MacdonaldTelescope.PieriStep Q X lam`, i.e.

    Σ_{μ ∈ addableCorners λ}  s_μ(Q,X)  =  ((1 − X)/(1 − Q)) · s_λ(Q,X)

for general `λ`. Everything it needs to be *stated* exists; the induction is
what is missing.

## What is already in Lean (all on main or #5871, all sorry-free)

- `hookLength_addBoxRow_of_ne_corner` — the per-cell update rule, every cell
  but the new box. The corner is excluded because its hook is `1` only under
  weak decrease, which the bare `List ℕ` carrier does not carry.
- `schurElement_eq_prod` — `schurElement` as a product over rows, not a fold.
  Nothing cell-by-cell can be said about a fold.
- All three row-factor cases: `_row_below` (equal), `_same_row`
  (`List.range_succ` split), `_row_above` (+ `_short`) via product surgery at
  one interior index (`Finset.mul_prod_erase`), stated division-free.
- `nLambda_addBoxRow` (`n(λ)+r`) and `nLambda_addBoxNewRow` (`n(λ)+ℓ(λ)`).
- `addBoxNewRow` and its kit, plus `addBoxRow_at_length` recording that
  `addBoxRow` is a no-op out of range.
- `addableCorners` with four `decide` checks, including the negative `(2,2)`.
- `pieriStep_one` and `pieriStep_two_one` — (P) proved at two shapes and shown
  to be instances of the general proposition.

## What is measured, and where

`computations/y_lambda_pieri_step_probe.py` (exact sympy, no floats, no
witness) establishes three things, each of which I had previously asserted
wrongly from memory:

1. (P) holds with `X` FREE at eight shapes, up to `(3,2,1)`.
2. The per-shape ratio has a closed form and needs no collapse:
   `s_{λ+□(r)}/s_λ = Q^r · (1 − X·Q^{λ_r−r})/(1 − Q^{h_μ(r,λ_r)}) ·
   ∏_{h ∈ arm ∪ leg} (1−Q^h)/(1−Q^{h+1})`.
3. **The shift product does NOT collapse** — `(Q²+Q+1)/((Q+1)³(Q²+1))` at
   `(3,2,1), r=1`. Genuine rational function. What telescopes is the SUM over
   corners, never the summand. Do not go looking for a hook-walk collapse in
   the summand; there isn't one, and I wasted a turn claiming there was.

## What the induction actually has to do

Sum the per-shape ratio over the corners and get `(1−X)/(1−Q)`. Every summand
is a different rational function; the cancellation is across them. Note the
denominators `1 − Q^h` may vanish, so the division-free discipline used
throughout should carry into the sum rather than being dropped for
convenience.

Open question worth settling first, cheaply, in the probe: is there a partial-
fraction identity over the corners that makes the sum term-by-term, or does it
genuinely need all corners at once? Measure before formalising — that is what
the three corrections above cost.
