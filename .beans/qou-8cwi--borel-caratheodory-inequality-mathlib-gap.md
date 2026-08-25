---
# qou-8cwi
title: 'PROVE(lean): Borel-Carathéodory inequality — Mathlib v4.24.0 gap, PI-5 prerequisite'
status: completed
type: task
priority: normal
tags:
    - lean
    - mathlib-gap
    - hadamard
    - paper-qou
created_at: 2026-08-08T03:30:00Z
updated_at: 2026-08-08T03:30:00Z
parent: qou-v4if
---

## Why

PI-5 of `QOU.Mathlib.HadamardFactorization` needs to bound the modulus of a
branch of `log f` from a bound on its real part: the growth hypothesis
`‖f z‖ ≤ A exp(C‖z‖^rho)` controls `Re log f = log‖f‖` and says nothing about
`|log f|`, which is what the polynomial-degree bound on `g` needs. That trade —
real part in, modulus out — is Borel-Carathéodory.

## Done

`content/quantum-observable-universe/lean/QOU/Mathlib/BorelCaratheodory.lean`.
Sorry-free; `#print axioms` = [propext, Classical.choice, Quot.sound] on all
three declarations. Wired into QOU.lean.

    norm_le_norm_two_mul_sub   Re w <= M, 0 < M  =>  ‖w‖ <= ‖2M - w‖
    two_mul_sub_ne_zero        2M - w /= 0 under the same hypotheses
    norm_le_of_re_le           ‖f z‖ <= 2 M r / (R - r) for ‖z‖ <= r < R

Two deviations from the textbook, both recorded in the file:

  * the Möbius INVERSION is avoided. From `g(2M - f) = f` alone,
    ‖f‖ = ‖g‖‖2M - f‖ <= ‖g‖(2M + ‖f‖), and rearranging with ‖g‖ < 1 gives the
    bound. No `f = 2Mg/(1+g)`, no division by `1 + g`.
  * Mathlib's Schwarz lemma wants an OPEN target ball, i.e. a STRICT bound, but
    `Re f <= M` only gives `‖g‖ <= 1`. Rather than strengthen the hypothesis,
    apply Schwarz at radius `1 + eps` for every eps > 0 and pass to the limit.

## ROAST

**"It's vacuous."** No. A non-vacuity witness is in the file: `f = id`, `R = 1`,
`M = 1`, `r = 1/2`, all hypotheses discharged, conclusion non-trivial.

**"`hr : 0 <= r` was unused — that smells like a vacuous regime."** Correct
instinct, and it was checked rather than waved off. The hypothesis is unused
because for `r < 0` the hypothesis `‖z‖ <= r` is unsatisfiable, so the statement
is vacuous exactly there and nowhere else. `hr` was removed; the theorem is
marginally stronger without it. SURVIVES.

**"Does it actually serve PI-5?"** PARTIALLY — and this is the real hit. The
classical statement hypothesises `Re f <= M` on the CIRCLE `‖z‖ = R` and
upgrades to the ball by the maximum principle FOR HARMONIC FUNCTIONS. This
version hypothesises the bound on the whole BALL. For the Hadamard application
that is fine, because the growth bound `‖F z‖ <= A exp(C‖z‖^rho)` is a ball
bound to begin with — `log‖F‖ <= log A + C‖z‖^rho` holds everywhere, not just on
a circle. But a caller holding only a circle bound CANNOT use this lemma, and
would need the harmonic maximum principle, which was not checked for in Mathlib.
Recorded in the file's SCOPE paragraph. SURVIVES for its intended use; does not
generalise.

**"The `f 0 = 0` hypothesis is a real restriction."** True. The general form
carries an extra `(R+r)/(R-r)·|f 0|` term. Not proved here. Callers who need
`f 0 /= 0` must subtract `f 0` first, which is exactly what the Hadamard
argument does anyway. Flagged, not hidden.

**"2M is a magic constant."** It is not magic: `Re w <= M` says precisely that
`w` is at least as close to `0` as to `2M`, which is why `w/(2M-w)` lands in the
closed unit disc. That geometric content is the docstring of
`norm_le_norm_two_mul_sub`.
