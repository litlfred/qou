import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import Mathlib.FieldTheory.RatFunc.AsPolynomial
import Mathlib.RingTheory.Polynomial.RationalRoot

/-!
# QOU.Mass.ColorCubicIrreducible — the colour cubic has no polynomial root in `z`

The colour spectral cubic of the Lever-1 binding kernel
(`QOU.Mass.ColorSpectralCubicGeometry`) is

  `C_z(X) := X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)`.

This file proves, for every field `K` of characteristic zero, that **no
polynomial `r ∈ K[z]` is a root**: `C_z(r) ≠ 0` in `K[z]`. Since `C_z` is monic
over `K[z]` and `K[z]` is integrally closed, a root in `K(z)` would already lie in
`K[z]` (Gauss); a cubic with no root over a field is irreducible. So `C_z(X)` is
**irreducible over `K(z)`**, i.e. the three colour sheets `X_i(z)` are genuinely
algebraic of degree 3 and none of them is a rational function of `z`.

## Why this matters for the prolongation-symbol keystone (bean `qou-1z28`)

The W1 wall (`qou-d8de`) asks for a q-difference prolongation `D_q` on the curve,
and its first named route is a q-shift on the base, `z ↦ q²z`, with a q-connection
lift. A rational rank-3 q-difference system in `z ↦ λz` whose solutions are the
three sheets would give each sheet a scalar linear q-difference equation with
rational coefficients (four shifts of one sheet in a 3-dimensional `K(z)`-span).
Each sheet is algebraic, hence D-finite (the *classical* prolongation, proved
exact in `prop:sw-classical-jet-exactness`). A power series that is both
D-finite and q-holonomic with `λ` not a root of unity is **rational**
(Bézivin 1994; Ramis 1992; unified in Schäfke–Singer, *Consistent systems of
linear differential and difference equations*, JEMS 21 (2019)). Irreducibility —
this file — is exactly what makes that conclusion contradictory. The analytic
theorem is cited, not formalised; what is formalised here is the algebraic
half the citation needs.

## Proof shape

`r ∈ K[z]` of degree `d ≥ 2`: the leading term `r³` has degree `3d`, strictly
above the other three terms (`1+2d`, `2+d`, `3`), so `C_z(r)` has degree `3d ≠ 0`.
Degree `≤ 1`, `r = a z + b`: the four `z`-coefficients of `C_z(az+b)` are

  `z³ : (a+1)(a²+1)`,  `z² : 3a²b + a² + 2ab + a + b + 1`,
  `z¹ : 3ab² + 2ab + a + b² + b + 1`,  `z⁰ : (b+1)(b²+1)`,

and each of the two branches `a = −1`, `a² = −1` of the leading coefficient
reduces the `z²` / `z⁰` pair to an inconsistent system, with an explicit integer
Bézout certificate (`5 = 0`, resp. `65 = 0`). Characteristic zero is used exactly
there. The certificates were computed by exact `sympy` in
`computations/probes/w1_base_qshift_rationality_prune_probe.py` and are checked
here by `linear_combination`.

Ground ring: a generic `[Field K]`, `[CharZero K]` only where a nonzero integer
must be nonzero (§7c). Nothing archimedean.
-/

namespace QOU.Mass.ColorCubicIrreducible

open Polynomial

variable {K : Type*} [Field K]

/-- The colour cubic `C_z(X)` evaluated at `X := r ∈ K[z]`; the polynomial
variable `X` of `K[X]` plays the role of the base coordinate `z`. -/
noncomputable def colorCubicAt (r : K[X]) : K[X] :=
  r ^ 3 + (X + 1) * r ^ 2 + (X ^ 2 + X + 1) * r + (X ^ 3 + X ^ 2 + X + 1)

/-- The four `z`-coefficients of `C_z(az + b)`. -/
theorem colorCubicAt_linear (a b : K) :
    colorCubicAt (C a * X + C b) =
      C (a ^ 3 + a ^ 2 + a + 1) * X ^ 3
        + C (3 * a ^ 2 * b + a ^ 2 + 2 * a * b + a + b + 1) * X ^ 2
        + C (3 * a * b ^ 2 + 2 * a * b + a + b ^ 2 + b + 1) * X
        + C (b ^ 3 + b ^ 2 + b + 1) := by
  unfold colorCubicAt
  simp only [map_add, map_mul, map_pow, map_one, map_ofNat]
  ring

/-- **No affine root.** For `r = a z + b` the coefficient system is inconsistent:
the `z³` coefficient forces `a = −1` or `a² = −1`, and in each branch the `z²` and
`z⁰` coefficients contradict each other (`5 = 0`, resp. `65 = 0`). -/
theorem colorCubicAt_linear_ne_zero [CharZero K] (a b : K) :
    colorCubicAt (C a * X + C b) ≠ 0 := by
  intro h
  rw [colorCubicAt_linear] at h
  have e3 := congrArg (fun p : K[X] => p.coeff 3) h
  have e2 := congrArg (fun p : K[X] => p.coeff 2) h
  have e0 := congrArg (fun p : K[X] => p.coeff 0) h
  simp only [coeff_add, coeff_C_mul_X_pow, coeff_C_mul_X, coeff_C, coeff_zero] at e3 e2 e0
  norm_num at e3 e2 e0
  have hfac : (a + 1) * (a ^ 2 + 1) = 0 := by linear_combination e3
  rcases mul_eq_zero.mp hfac with ha | ha
  · -- branch `a = −1`: the `z²` coefficient is `2b + 1`, the `z⁰` one is then `5/8`.
    have h2' : 2 * b + 1 = 0 := by
      linear_combination e2 - ((3 * b + 1) * a - b) * ha
    have h5 : (5 : K) = 0 := by
      linear_combination 8 * e0 - (4 * b ^ 2 + 2 * b + 3) * h2'
    norm_num at h5
  · -- branch `a² = −1`: the `z²` coefficient is `a(2b+1) − 2b`; squaring it
    -- against `a² = −1` gives `8b² + 4b + 1 = 0`, coprime to the `z⁰` cubic.
    have h2' : 2 * a * b + a - 2 * b = 0 := by
      linear_combination e2 - (3 * b + 1) * ha
    have hb : 8 * b ^ 2 + 4 * b + 1 = 0 := by
      linear_combination (2 * b + 1) ^ 2 * ha - (a * (2 * b + 1) + 2 * b) * h2'
    have h65 : (65 : K) = 0 := by
      linear_combination (8 * b ^ 2 - 4 * b + 1) * hb + (64 - 64 * b) * e0
    norm_num at h65

/-- **No root of degree `≥ 2`.** The leading term `r³` has degree `3d`, strictly
above `1 + 2d`, `2 + d` and `3`, so `C_z(r)` has degree `3d > 0`. -/
theorem colorCubicAt_ne_zero_of_two_le_natDegree (r : K[X]) (hd : 2 ≤ r.natDegree) :
    colorCubicAt r ≠ 0 := by
  have h3 : (r ^ 3).natDegree = 3 * r.natDegree := natDegree_pow r 3
  have hX1 : (X + 1 : K[X]).natDegree ≤ 1 := by compute_degree
  have hX2 : (X ^ 2 + X + 1 : K[X]).natDegree ≤ 2 := by compute_degree
  have hX3 : (X ^ 3 + X ^ 2 + X + 1 : K[X]).natDegree ≤ 3 := by compute_degree
  have hA : ((X + 1) * r ^ 2).natDegree ≤ 1 + 2 * r.natDegree := by
    calc ((X + 1) * r ^ 2).natDegree
        ≤ (X + 1 : K[X]).natDegree + (r ^ 2).natDegree := natDegree_mul_le
      _ ≤ 1 + 2 * r.natDegree := by rw [natDegree_pow]; omega
  have hB : ((X ^ 2 + X + 1) * r).natDegree ≤ 2 + r.natDegree := by
    calc ((X ^ 2 + X + 1) * r).natDegree
        ≤ (X ^ 2 + X + 1 : K[X]).natDegree + r.natDegree := natDegree_mul_le
      _ ≤ 2 + r.natDegree := by omega
  have hT : ((X + 1) * r ^ 2 + ((X ^ 2 + X + 1) * r + (X ^ 3 + X ^ 2 + X + 1))).natDegree
      < (r ^ 3).natDegree := by
    rw [h3]
    calc ((X + 1) * r ^ 2 + ((X ^ 2 + X + 1) * r + (X ^ 3 + X ^ 2 + X + 1))).natDegree
        ≤ max ((X + 1) * r ^ 2).natDegree
            ((X ^ 2 + X + 1) * r + (X ^ 3 + X ^ 2 + X + 1)).natDegree := natDegree_add_le _ _
      _ ≤ max (1 + 2 * r.natDegree) (max (2 + r.natDegree) 3) := by
          apply max_le_max hA
          calc ((X ^ 2 + X + 1) * r + (X ^ 3 + X ^ 2 + X + 1)).natDegree
              ≤ max ((X ^ 2 + X + 1) * r).natDegree
                  (X ^ 3 + X ^ 2 + X + 1 : K[X]).natDegree := natDegree_add_le _ _
            _ ≤ max (2 + r.natDegree) 3 := max_le_max hB hX3
      _ < 3 * r.natDegree := by omega
  have hsplit : colorCubicAt r
      = r ^ 3 + ((X + 1) * r ^ 2 + ((X ^ 2 + X + 1) * r + (X ^ 3 + X ^ 2 + X + 1))) := by
    unfold colorCubicAt; ring
  have hdeg : (colorCubicAt r).natDegree = 3 * r.natDegree := by
    rw [hsplit, natDegree_add_eq_left_of_natDegree_lt hT, h3]
  intro h0
  rw [h0, natDegree_zero] at hdeg
  omega

/-- **The colour cubic has no polynomial root in `z`** (characteristic zero):
`C_z(r) ≠ 0` for every `r ∈ K[z]`. With Gauss's lemma (monic over the integrally
closed `K[z]`) this is irreducibility of `C_z(X)` over `K(z)`: no colour sheet
is a rational function of `z`. -/
theorem colorCubicAt_ne_zero [CharZero K] (r : K[X]) : colorCubicAt r ≠ 0 := by
  rcases le_or_gt 2 r.natDegree with hd | hd
  · exact colorCubicAt_ne_zero_of_two_le_natDegree r hd
  · have h1 : r.natDegree ≤ 1 := by omega
    rw [eq_X_add_C_of_natDegree_le_one h1]
    exact colorCubicAt_linear_ne_zero _ _

/-! ### From `K[z]` to `K(z)`: no rational-function root either -/

/-- The colour cubic as a **monic** polynomial over `K[z]`: the outer variable is
the colour coordinate, the inner `X` is `z`. -/
noncomputable def colorCubicPoly : (K[X])[X] :=
  X ^ 3 + C (X + 1) * X ^ 2 + C (X ^ 2 + X + 1) * X + C (X ^ 3 + X ^ 2 + X + 1)

theorem colorCubicPoly_monic : (colorCubicPoly : (K[X])[X]).Monic := by
  unfold colorCubicPoly
  monicity!

theorem colorCubicPoly_eval₂ (f : RatFunc K) :
    (colorCubicPoly : (K[X])[X]).eval₂ (algebraMap K[X] (RatFunc K)) f
      = f ^ 3 + algebraMap K[X] (RatFunc K) (X + 1) * f ^ 2
          + algebraMap K[X] (RatFunc K) (X ^ 2 + X + 1) * f
          + algebraMap K[X] (RatFunc K) (X ^ 3 + X ^ 2 + X + 1) := by
  simp [colorCubicPoly, eval₂_add, eval₂_mul, eval₂_pow, eval₂_X, eval₂_C]

theorem colorCubicPoly_eval₂_poly (r : K[X]) :
    (colorCubicPoly : (K[X])[X]).eval₂ (algebraMap K[X] (RatFunc K))
        (algebraMap K[X] (RatFunc K) r)
      = algebraMap K[X] (RatFunc K) (colorCubicAt r) := by
  rw [colorCubicPoly_eval₂, colorCubicAt]
  simp only [map_add, map_mul, map_pow]

/-- **No rational-function root** (Gauss). A root `f ∈ K(z)` of the monic
`C_z(X)` is integral over `K[z]`; `K[z]` is integrally closed, so `f` is a
polynomial, and `colorCubicAt_ne_zero` bites. Hence `C_z(X)`, a cubic with no root
over the field `K(z)`, is irreducible there: **no colour sheet is a rational
function of `z`**. -/
theorem colorCubic_no_ratFunc_root [CharZero K] (f : RatFunc K) :
    f ^ 3 + algebraMap K[X] (RatFunc K) (X + 1) * f ^ 2
      + algebraMap K[X] (RatFunc K) (X ^ 2 + X + 1) * f
      + algebraMap K[X] (RatFunc K) (X ^ 3 + X ^ 2 + X + 1) ≠ 0 := by
  intro h
  have hint : IsIntegral K[X] f := ⟨colorCubicPoly, colorCubicPoly_monic, by
    rw [colorCubicPoly_eval₂]; exact h⟩
  obtain ⟨r, hr⟩ := IsIntegrallyClosed.isIntegral_iff.mp hint
  rw [← hr, ← colorCubicPoly_eval₂, colorCubicPoly_eval₂_poly] at h
  exact colorCubicAt_ne_zero r
    ((map_eq_zero_iff _ (IsFractionRing.injective K[X] (RatFunc K))).mp h)

end QOU.Mass.ColorCubicIrreducible
