---
# qou-qexu
title: 'q-RH: QExplicitFormula is uninhabitable — proved for empty spectrum, general case open'
status: in-progress
type: task
priority: high
created_at: 2026-08-30T06:30:00Z
updated_at: 2026-08-30T06:30:00Z
---

`QExplicitFormula` (`q-geometric-langlands/explicit-formula.lean`) formalises
the q-explicit formula with the spectral side as a **finite** `List
ReebEigenvalue`. In that form it holds for **no** datum with an empty spectrum,
whatever its ideals, `Ω_q` and `q > 1`. Proved:
`not_qExplicitFormula_of_nil_spectrum`, `#print axioms` clean.

## Why the question got asked at all

`not_qExplicitFormula_empty` (already in the file) refutes exactly **one**
datum. That is weaker than it looks: a class refuted on one instance can still
be satisfiable on another, and a conditional theorem over it is only worthless
if **no** instance exists. Satisfiability is a separate question from
refutability-on-an-instance and has to be asked separately.

This is the same lesson as the `HasReebSpectralCoords` case on this branch, in
the negative direction — *"exhibit a witness of the thing the conditional
theorems actually depend on"*, and when you cannot, find out whether one can
exist. The sibling's `HasQPlancherelCLT` finding is the third instance in a
week.

## The mechanism

- `ψ_q(X)` sums over a **finite** `List MaxIdeal`, terms switched on and off by
  `N(𝔪) ≤ X`, never grown ⇒ bounded uniformly in `X` (`qChebyshev_abs_le`).
- `−½·ln_q(1 − X^{−2})` **→ +∞ as X → 1⁺** (`tail_term_unbounded`).

A bounded function cannot equal an unbounded one.

`tail_term_unbounded` is constructive, not a limit: `X := 1/√(1−ε)` makes
`1 − X^{−2} = ε` exactly, so `ε ≤ q^{−2B}` forces the term above `B`; capping
`ε ≤ 1/2` keeps `X ≤ √2`, which is what bounds the other side's `X` term.

## This is a formalisation defect, NOT a refutation of the mathematics

The classical explicit formula carries the *same* `−½log(1−x^{−2})` term and is
true. There the spectral sum runs over **infinitely many** zeros and converges
only conditionally: that term is the closed form of the trivial-zero series, and
its blow-up near `x = 1` is cancelled by the divergence of the non-trivial-zero
sum. A finite `List` cannot reproduce that cancellation.

**So a faithful carrier needs the spectral side to be an infinite sum with a
specified summation order.** That is the repair, and it is not cosmetic — the
summation order is part of the classical statement.

## What is still open (the reason this bean is in-progress, not completed)

The **general finite-spectrum** case: for a datum with a *nonempty* finite
spectrum, the same argument should apply, because on `X ∈ (1, √2]` the spectral
sum is a finite sum of terms `‖(X:ℂ)^ρ‖ = X^{Re ρ}` divided by fixed brackets,
hence bounded by a constant of the datum. Not proved here.

What it needs, concretely:

1. `‖(X:ℂ)^ρ‖ = X^{Re ρ}` for real `X > 0`. **This branch already has that
   lemma** — `abs_cpow_ofReal_eq_rpow_re` in `spectral-half-line.lean` — but it
   is a **content-block sibling**, outside the package globs, so
   `explicit-formula.lean` cannot import it (§0a). Same structural obstruction
   as `qou-sibdup`. Either move it to a library module (as `WeilZeta.lean` and
   `ReebSpectrum.lean` were) or re-prove it locally.
2. A per-element bound `X^{Re ρ} ≤ max 1 (√2 ^ Re ρ)` on `X ∈ (1, √2]`.
3. The list-sum bound, in the shape of `qChebyshev_abs_le`'s induction.

Estimated ~40 lines. Nothing in it looks hard; it was left because the
empty-spectrum result already establishes the defect and names the repair.

**Note the `qInteger` zero case** when doing it: `[ρ]_q = 0` at `ρ = 0`, and
Lean's `x/0 = 0`, so such a term contributes `0`. That helps rather than
hurts — but a proof that assumes `[ρ]_q ≠ 0` will not go through.

## Blast radius: none in Lean, two remarks in content

Zero Lean consumers of `explicit_formula` or `QExplicitFormula` outside the file.
Two content blocks cite `conj:explicit-formula` in `uses[]` —
`rem:yekutieli-quantum-li` and `rem:unitary-stability` — and both are `remark`s,
which make no logical claim, so nothing downstream is built on the refuted form.
