/-!
# `QOU.IwahoriHecke.AvgCrossing` — Foundational identity for inter-nucleon Avg crossings

**Sprint 6 follow-up to the Sprint 2 IwahoriHecke infrastructure.**

This file contributes the **algebraic core** of PR-D Step 4 (the
load-bearing categorical claim for the atom-braid exterior-algebra
conjecture, `conj:atom-braid-exterior-algebra`):

  > For the canonical atom-braid `T_w(Z, N) ∈ H_{3A}(q)`, every
  > inter-nucleon Avg crossing `σ_{3k+2} − h/2` acts by left/right-
  > multiplication on the Coxeter-length filtration preserving the
  > Boolean grading.

The full claim requires Sprint 5+ infrastructure (Coxeter-length
filtration accessor + Hoefsmit basis to make Boolean grading
concrete) per
[`docs/audits/2026-05-30-atom-braid-categorical-proof-feasibility.md`](../../../../docs/audits/2026-05-30-atom-braid-categorical-proof-feasibility.md).
But the **algebraic essence** — that each averaged Hecke generator
satisfies a Clifford-like scalar-squaring identity — is provable
*directly* from the Hecke quadratic relation alone, with no
filtration or basis machinery.

## The foundational identity

In the Hecke quotient `IwahoriHeckeQuot R q S`, every generator
`T_s` satisfies `(T_s - q)(T_s + 1) = 0` (Quotient.lean's
`T_hecke_quadratic_relation`). From this we derive:

  `(2 · T_s - (q - 1))² = (q + 1)²`

This is the *scaled* form of "`σ_i − h/2` squares to a scalar", where
`h = q − 1` in the standard form (vs `h = q − q⁻¹` in the symmetric
form). The identity holds in any `CommRing R` and is structurally
the reason inter-nucleon Avg crossings generate a **Clifford-type
Z/2Z-graded sub-algebra** — which is the algebraic source of the
Boolean grading in PR-D Step 4.

## Status

- `T_avg_squares_to_scalar` — fully proved, `sorry`-free, depends
  only on Quotient.lean's `T_hecke_quadratic_relation`.
- The opaque `AvgCrossingPreservesGradeHolds` in
  [`conj-atom-braid-exterior-algebra.lean`](../../mass-theory/conj-atom-braid-exterior-algebra.lean)
  is **not** discharged by this lemma — that would require the
  filtration accessor + combinatorial argument linking the algebraic
  identity to grading preservation. This file contributes the
  algebraic prerequisite that any future discharge must cite.

Refs:
- [bourbaki1968] Bourbaki, "Groupes et Algèbres de Lie" Ch IV-VI
- [humphreys1990] Humphreys, "Reflection Groups and Coxeter Groups"
- [manuscript] docs/audits/2026-05-30-atom-braid-categorical-proof-feasibility.md
-/

import QOU.IwahoriHecke.Quotient
import Mathlib.Tactic.LinearCombination

namespace QOU.IwahoriHecke.AvgCrossing

universe u v

variable {W : Type u} (R : Type v) [CommRing R] (q : R)
  (S : Set W) [DecidableEq W]

/-- **Foundational identity: scaled averaged crossing squares to a scalar.**

    For every generator `T_s` of `IwahoriHeckeQuot R q S` (the
    Hecke-quadratic-only quotient), the algebraic identity

      `(2 · T_s − (q − 1))² = (q + 1)²`

    holds.  This is the scaled form of the "`σ − h/2` squares to
    a scalar" Clifford-like identity for inter-nucleon Avg
    crossings in the canonical atom-braid sub-algebra of
    `H_{3A}(q)`; in the standard form `(T − q)(T + 1) = 0` the
    scalar `h = q − 1` (not `q − q⁻¹`, which would require the
    symmetric form `(T − q)(T + q⁻¹) = 0`).

    Proof: `linear_combination 4 * (Hecke quadratic)`.  Both
    sides expand to `4·T² + (linear in T) + const`; using
    `T² = (q − 1)·T + q` from the Hecke relation eliminates
    the `T²` term, the linear-in-`T` coefficients cancel, and
    the constant-term identity `4q + (q − 1)² = (q + 1)²` is
    `ring`-true. -/
theorem T_avg_squares_to_scalar (s : S) :
    (2 * Quotient.T R q S s -
      (algebraMap R _ q - 1))^2 = (algebraMap R _ q + 1)^2 := by
  -- The Hecke quadratic relation:
  --   (T_s - algebraMap R _ q) * (T_s + 1) = 0
  have h := Quotient.T_hecke_quadratic_relation R q S s
  -- Reduce LHS − RHS to 4 · (Hecke quadratic), which is `4 · 0 = 0`.
  linear_combination 4 * h

/-- **Corollary** — the centered Avg-crossing element
    `T_s − (q − 1)/2` is "scalar up to factor 2".  Stated here in
    a form that avoids division so it works over any `CommRing R`:

      `(2 · T_s − (q − 1))² − (q + 1)² = 0`. -/
theorem T_avg_centered_squared_eq_zero (s : S) :
    (2 * Quotient.T R q S s -
      (algebraMap R _ q - 1))^2 - (algebraMap R _ q + 1)^2 = 0 := by
  rw [T_avg_squares_to_scalar R q S s, sub_self]

end QOU.IwahoriHecke.AvgCrossing
