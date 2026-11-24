/-
# QOU.Hecke.WedderburnWeightDegeneracy

The Wedderburn weights of the Markov trace on `H_3(q)` with the loop parameter
`z` left **free**, and where they vanish.

Bean `qou-vvv4`.  Companion probe:
`computations/hecke/h3_gram_degeneracy_is_wedderburn_weight_vanishing.py` (19/19).

## Why this file exists

`QOU.Interactions.GramMatrixH3Symbolic` records the convention-C Gram
determinant's factorisation as *computed output*:

    det G(u) = -(u-1)(u+1)(u^3+u-1)^5 (u^3+u^2+1)^5 S1(u) S2(u) / (u^10 (u^2+1)^12)

and `QOU.Archimedean.spectrahedral_phase_collapse` reads the `(u^3+u-1)^5` zero
as a hadronic phase transition.  The probe measures that

    det G / (y_(3) * y_(2,1)^4 * y_(1^3))|_{z = z_C}
      = -(u^4+1)^2 (u^2-u+1)^6 (u^2+u+1)^6 (u^4-u^2+1)^6 / u^28,

which has no positive real zero and no positive real pole — so on `u > 0` every
Gram degeneracy IS a Wedderburn weight vanishing, and the two multiplicity-5
factors are exactly the two roots of `y_(2,1)`, each also killing one
one-dimensional block.

What is proved here is the algebraic half of that: the closed forms, the root
structure of `y_(2,1)`, and the consequence that **convention D reaches neither
root at any real `q`**.  The determinant identity itself is not restated in Lean
(it needs the 36 Gram entries, which live in the file above).

## Base ring (§7c)

This file is entirely generic: every statement here is a rational-function
identity or a root count over an arbitrary `Field K`, needing no ordering.  The
statements that ARE about signs and reachability — where `ℝ` is genuine — live
in the sibling `WedderburnWeightDegeneracyReal`.

Note `zD_ne_self` is here rather than there: "`z_D = q` forces `q = 0`" holds
over any field.  Its companion `z_D = -1/q` does not — that forces
`q⁴+q²+1 = 0`, which has no REAL root but is satisfied by a primitive 12th root
of unity, so it is genuinely archimedean and sits in the sibling.

## Provenance of the closed forms

The three weights below are transcribed from the probe's derivation (it solves
the three-by-three linear system from the character table); this file states and
uses them, it does not re-derive them.  What is proved here is everything
downstream: the normalisation, the root structure, and the convention-D values.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

namespace QOU.Hecke.WedderburnWeightDegeneracy

section GenericField

variable {K : Type*} [Field K]

/-- Wedderburn weight of the trivial block `(3)`, with the Markov loop `z` free. -/
noncomputable def y3 (q z : K) : K :=
  (q * z + 1) * (q ^ 3 * z + q * z + 1) / ((q ^ 2 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1))

/-- Wedderburn weight of the two-dimensional block `(2,1)`, with `z` free. -/
noncomputable def y21 (q z : K) : K :=
  -q * (z - q) * (q * z + 1) / ((q ^ 2 - q + 1) * (q ^ 2 + q + 1))

/-- Wedderburn weight of the sign block `(1^3)`, with `z` free. -/
noncomputable def y111 (q z : K) : K :=
  q ^ 2 * (z - q) * (q ^ 2 * z + z - q ^ 3) / ((q ^ 2 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1))

/-- The canonical (convention-D) Markov parameter. -/
noncomputable def zD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- The convention-C Markov parameter in the square-root variable `u`, `q = u^2`. -/
noncomputable def zC (u : K) : K := u / (u ^ 2 + 1)

/-- **Markov normalisation.**  `y_(3) + 2 y_(2,1) + y_(1^3) = 1` for EVERY `z` —
the weights are a partition of the trace, not three independent quantities. -/
theorem weights_sum_to_one (q z : K) (h1 : (q ^ 2 + 1) ≠ 0)
    (h2 : (q ^ 2 - q + 1) ≠ 0) (h3 : (q ^ 2 + q + 1) ≠ 0) :
    y3 q z + 2 * y21 q z + y111 q z = 1 := by
  have hD : ((q ^ 2 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1) : K) ≠ 0 :=
    mul_ne_zero (mul_ne_zero h1 h2) h3
  have hD2 : ((q ^ 2 - q + 1) * (q ^ 2 + q + 1) : K) ≠ 0 := mul_ne_zero h2 h3
  unfold y3 y21 y111
  rw [← mul_div_assoc, div_add_div _ _ hD hD2, div_add_div _ _ (mul_ne_zero hD hD2) hD,
      div_eq_one_iff_eq (mul_ne_zero (mul_ne_zero hD hD2) hD)]
  ring

/-- **The `(2,1)` block degenerates at exactly two loop values.**
`y_(2,1)(z) = 0` iff `z = q` or `z = -1/q`.  Both roots are needed below: under
convention C they are the corpus `detFactor3` and `detFactor4`. -/
theorem y21_eq_zero_iff (q z : K) (hq : q ≠ 0)
    (h2 : (q ^ 2 - q + 1) ≠ 0) (h3 : (q ^ 2 + q + 1) ≠ 0) :
    y21 q z = 0 ↔ z = q ∨ z = -1 / q := by
  have hden : ((q ^ 2 - q + 1) * (q ^ 2 + q + 1)) ≠ 0 := mul_ne_zero h2 h3
  unfold y21
  rw [div_eq_zero_iff]
  simp only [hden, or_false]
  rw [mul_eq_zero, mul_eq_zero, neg_eq_zero]
  constructor
  · rintro ((h | h) | h)
    · exact absurd h hq
    · exact Or.inl (sub_eq_zero.mp h)
    · refine Or.inr ?_
      field_simp
      linear_combination h
  · rintro (rfl | rfl)
    · exact Or.inl (Or.inr (sub_self _))
    · refine Or.inr ?_
      field_simp
      norm_num

/-- **`y_(1^3)` vanishes identically at the canonical loop value.**  This is the
same fact as `gramMatrixD_det_eq_zero`: convention D annihilates the sign block,
which is why the D determinant is identically singular and cannot be used to
locate a transition — the question has to be put to the block weight instead. -/
theorem y111_at_zD (q : K) (h1 : (q ^ 2 + 1) ≠ 0) : y111 q (zD q) = 0 := by
  unfold y111 zD
  have hz : q ^ 2 * (q ^ 3 / (q ^ 2 + 1)) + q ^ 3 / (q ^ 2 + 1) - q ^ 3 = 0 := by
    field_simp
    ring
  rw [hz]
  ring

/-- **The `(2,1)` weight at the canonical loop value is `q²/(q²+1)²`.**
The `(q²−q+1)(q²+q+1) = q⁴+q²+1` of the denominator cancels against the
numerator; nothing of the block structure survives except a square. -/
theorem y21_at_zD (q : K) (h1 : (q ^ 2 + 1) ≠ 0)
    (h2 : (q ^ 2 - q + 1) ≠ 0) (h3 : (q ^ 2 + q + 1) ≠ 0) :
    y21 q (zD q) = q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  have hD2 : ((q ^ 2 - q + 1) * (q ^ 2 + q + 1) : K) ≠ 0 := mul_ne_zero h2 h3
  unfold y21 zD
  rw [div_eq_div_iff hD2 (pow_ne_zero 2 h1)]
  field_simp
  ring

/-- **The trivial block at the canonical loop value.** -/
theorem y3_at_zD (q : K) (h1 : (q ^ 2 + 1) ≠ 0)
    (h2 : (q ^ 2 - q + 1) ≠ 0) (h3 : (q ^ 2 + q + 1) ≠ 0) :
    y3 q (zD q) = (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  have hD : ((q ^ 2 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1) : K) ≠ 0 :=
    mul_ne_zero (mul_ne_zero h1 h2) h3
  unfold y3 zD
  rw [div_eq_div_iff hD (pow_ne_zero 2 h1)]
  field_simp
  ring

/-- **`z_D = 1` iff `q³ = q²+1`** — the supergolden equation.  This is a
DIFFERENT point from the convention-C Gram degeneracy `u³+u−1 = 0` (there
`u = √q`, so `q = 1/ψ²`); here it is `q = ψ` itself.  It is where the Markov
trace collapses onto the Frobenius counit. -/
theorem zD_eq_one_iff (q : K) (h1 : (q ^ 2 + 1) ≠ 0) :
    zD q = 1 ↔ q ^ 3 = q ^ 2 + 1 := by
  unfold zD
  rw [div_eq_one_iff_eq h1]

/-- **The convention-C degeneracy `z_C = q` is the corpus `detFactor3`.**
With `q = u²` and `z_C(u) = u/(u²+1)`, the condition `z_C = q` is `u(u³+u−1) = 0`,
whose only nonzero root is the corpus threshold. -/
theorem zC_eq_qsq_iff (u : K) (hu : u ≠ 0) (h1 : (u ^ 2 + 1) ≠ 0) :
    zC u = u ^ 2 ↔ u ^ 3 + u - 1 = 0 := by
  unfold zC
  rw [div_eq_iff h1]
  constructor <;> intro h
  · have hfac : u * (u ^ 3 + u - 1) = 0 := by linear_combination -h
    rcases mul_eq_zero.mp hfac with h' | h'
    · exact absurd h' hu
    · exact h'
  · linear_combination -u * h

/-- **The other convention-C degeneracy `z_C = −1/q` is the corpus `detFactor4`.**
Its only real root is `u = −ψ`, outside the `u > 0` regime — which is why the
corpus sees just one positive-`u` threshold despite two roots of `y_(2,1)`. -/
theorem zC_eq_neg_inv_qsq_iff (u : K) (hu : u ≠ 0) (h1 : (u ^ 2 + 1) ≠ 0) :
    zC u = -1 / u ^ 2 ↔ u ^ 3 + u ^ 2 + 1 = 0 := by
  unfold zC
  rw [div_eq_div_iff h1 (pow_ne_zero 2 hu)]
  constructor <;> intro h <;> linear_combination h

/-- **`z_D = q` forces `q = 0`.**  Convention D never reaches the first root of
`y_(2,1)`, over ANY field — this one needs no ordering. -/
theorem zD_ne_self (q : K) (hq : q ≠ 0) (h1 : (q ^ 2 + 1) ≠ 0) : zD q ≠ q := by
  unfold zD
  intro h
  rw [div_eq_iff h1] at h
  exact hq (by linear_combination -h)

end GenericField

end QOU.Hecke.WedderburnWeightDegeneracy
