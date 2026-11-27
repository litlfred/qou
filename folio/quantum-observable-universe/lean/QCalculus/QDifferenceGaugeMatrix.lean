/-
Copyright (c) 2026 litlfred. All rights reserved.

# Closing a third prose-only step: the gauge law and the moving spectral curve, at matrix level

`QOU.Mass.QGaugeSpectralRigidity` (#7208) proves that the colour spectral cubic is not
stable under the scalar gauge action, and closes with:

> *"Not formalised, prose only: the covering/gauge dictionary — that 'a gauge
> transformation of the q-difference system' and 'a change of the `X` coordinate over the
> base' are the same move — is DVRSZ's, cited above, and is not re-proved in Lean."*

That file's `charCubic_smul` carries the mechanism at the level of *coefficients*, by
factoring a cubic over its roots. What was missing is the step before it: that the gauge
really does scale the system matrix, and that scaling the system matrix really does move
the characteristic polynomial by a substitution. Both are short over `Matrix`, and both
are here.

## What is proved

* `scalar_gauge_eq` — DVRSZ eq. (2.4.1) `B = (σ_q F)⁻¹ A F` for a **scalar** gauge
  `F = c·1`, stated cleared of the inverse as `(σc · 1) * B = A * (c · 1) → B = (c/σc)·A`.
  With `σ_q : z ↦ q·z` and `c = z^k` this is `B = q^{-k}·A` — the fact #7208 uses to say
  that the gauge scalars reachable by a monomial gauge are exactly `q^ℤ`.

* `det_charMatrix_smul` — scaling the system matrix substitutes in the characteristic
  polynomial: `det(X·1 − t·A) = t^n · det((X/t)·1 − A)` for `t ≠ 0`, any finite index
  type. So the spectral curve of `t·A` is the curve of `A` with `X ↦ X/t`; it **moves**,
  and `QGaugeSpectralRigidity.weight_relations` then says what surviving that motion
  would cost.

* `det_charMatrix_conj` — the **contrast**, and the reason the differential case behaves
  differently: conjugation `A ↦ F A F⁻¹` leaves the characteristic polynomial alone. This
  is what makes the Seiberg–Witten spectral curve of a Higgs field well defined, and its
  failure for `(σ_q F)⁻¹ A F` is the whole of #7208. The probe verified it numerically
  over `ℚ` (T3); this is the general statement.

## Why "cleared of the inverse"

Stating (2.4.1) as `B = (σ_q F)⁻¹ A F` needs `σ_q F` invertible and drags
`Matrix.inv` — which in Mathlib is a junk-valued total function — into every downstream
step. The hypothesis form `(σc · 1) * B = A * (c · 1)` says exactly the same thing about
exactly the same systems, with no invertibility side-condition and no junk value. Same
discipline as `QOU.Mass.MoebiusThreePointRigidity`, where clearing the denominator
removed the need for a chart at `∞`.

## Scope

Nothing here constructs `D_q`, and nothing identifies `Σ` with a q-difference module's
spectral data — #7208 shows it is *not* that. These are the two mechanism steps that
file cited to DVRSZ rather than proving. The remaining prose in the W1 arc is the
geometric covering step (`Σ`-automorphism ⇒ permutes the branch locus) and the group
packaging of `Stab(B) ↪ S₆`, both flagged where they occur.

§7c: generic `[Field K]` and a generic finite index type; no archimedean construct.
Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-09-12-w1-route3-spectral-curve-not-a-q-gauge-invariant.md
-/
import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse

namespace QOU.Mass.QDifferenceGaugeMatrix

open Matrix

variable {K : Type*} [Field K]
variable {n : Type*} [Fintype n] [DecidableEq n]

/-- **The q-difference gauge law for a scalar gauge** — DVRSZ eq. (2.4.1),
`B = (σ_q F)⁻¹ A F`, with `F = c·1` and cleared of the inverse.

Read `s = σ_q(c)` and `t = c`: the hypothesis is `(σ_q F) · B = A · F`, and the
conclusion is `B = (c / σ_q c) · A`. Taking `c = z^k` and `σ_q : z ↦ q·z` gives
`c / σ_q c = q^{-k}`, so a monomial gauge multiplies the system matrix by a power of `q`
— which is the step #7208 needs and cites rather than proves.

The action is **not** conjugation: the two sides carry *different* scalars, `σ_q c` on
the left and `c` on the right, and they fail to cancel exactly when `σ_q c ≠ c`. -/
theorem scalar_gauge_eq (s t : K) (hs : s ≠ 0) (A B : Matrix n n K)
    (h : (s • (1 : Matrix n n K)) * B = A * (t • (1 : Matrix n n K))) :
    B = (t / s) • A := by
  rw [smul_mul_assoc, one_mul, mul_smul_comm, mul_one] at h
  have : B = s⁻¹ • (t • A) := by
    rw [← h, smul_smul, inv_mul_cancel₀ hs, one_smul]
  rw [this, smul_smul, div_eq_inv_mul]

/-- **Scaling the system matrix moves the characteristic polynomial by a substitution.**

`det(X·1 − t·A) = t^n · det((X/t)·1 − A)` for `t ≠ 0`, where `n` is the size. So the
spectral locus of `t·A` is that of `A` pulled back along `X ↦ X/t` — it moves, unless the
locus happens to be invariant under that substitution.

Combined with `scalar_gauge_eq`, this is the dictionary #7208 assumed: *a gauge
transformation of the q-difference system* and *a change of the `X` coordinate over the
base* are the same move. `QGaugeSpectralRigidity.weight_relations` then measures what
surviving it would cost a monic cubic — every non-leading coefficient. -/
theorem det_charMatrix_smul (t X : K) (ht : t ≠ 0) (A : Matrix n n K) :
    (X • (1 : Matrix n n K) - t • A).det
      = t ^ Fintype.card n * ((X / t) • (1 : Matrix n n K) - A).det := by
  have hfac : X • (1 : Matrix n n K) - t • A
      = t • ((X / t) • (1 : Matrix n n K) - A) := by
    rw [smul_sub, smul_smul, mul_div_cancel₀ X ht]
  rw [hfac, Matrix.det_smul]

/-- **The contrast: conjugation leaves the characteristic polynomial alone.**

`det(X·1 − F A F⁻¹) = det(X·1 − A)` for invertible `F`. This is why the Seiberg–Witten
spectral curve of a *Higgs field* is well defined — gauge acts there by conjugation — and
its failure for the twisted q-difference action `(σ_q F)⁻¹ A F` is precisely the finding
of #7208. The probe checks this numerically over `ℚ` (T3); this is the statement it is a
sample of. -/
theorem det_charMatrix_conj (X : K) (A F : Matrix n n K) (hF : IsUnit F.det) :
    (X • (1 : Matrix n n K) - F * A * F⁻¹).det = (X • (1 : Matrix n n K) - A).det := by
  have hconj : X • (1 : Matrix n n K) - F * A * F⁻¹
      = F * (X • (1 : Matrix n n K) - A) * F⁻¹ := by
    rw [Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_smul, Matrix.mul_one,
      Matrix.smul_mul, Matrix.mul_nonsing_inv F hF]
  rw [hconj, Matrix.det_mul, Matrix.det_mul, Matrix.det_nonsing_inv,
    mul_right_comm, Ring.mul_inverse_cancel _ hF, one_mul]


/-- **Equal-scalar specialization of `scalar_gauge_eq` (`qou-59i6`).**
When `s = t` with `s ≠ 0`, `(s • 1) * B = A * (s • 1)` implies `B = A`. -/
theorem scalar_gauge_self (s : K) (hs : s ≠ 0) (A B : Matrix n n K)
    (h : (s • (1 : Matrix n n K)) * B = A * (s • (1 : Matrix n n K))) :
    B = A := by
  rw [scalar_gauge_eq s s hs A B h, div_self hs, one_smul]

end QOU.Mass.QDifferenceGaugeMatrix
