/-
  **The directional generalized Wronskian** `det ((Dᶜ)ⁱ fⱼ)`, and its equivalence with
  independence of line restrictions.

  Bean `qou-sq3h`.  ⚠ Staged for Mathlib; depends only on other staged files
  (`QOU.Mathlib.GenWronskian`, `QOU.Mathlib.LineRestriction`), never on QOU content.

  ═══ WHERE THIS SITS ═══

  `QOU.Mathlib.MvGenWronskian` proves that an independent family has a non-zero generalized
  Wronskian, but with **unbounded operator order**, and witnesses there
  (`mvGenWronskian_pow_five_six`) show that proof cannot be sharpened — it argues from the
  origin, and bounded-order Wronskians can vanish at the origin.

  Roth's lemma needs bounded order.  The route to it runs through `Dᶜ = ∑ᵢ cᵢ ∂ᵢ`, an
  operator of order **one**, so `(Dᶜ)ⁱ` has order exactly `i`.  This file builds the
  determinant of those operators and connects it to the univariate criterion.

  ═══ WHAT IS PROVED, AND WHAT IS NOT ═══

  `dirGenWronskian_ne_zero_iff_exists_linearIndependent_lineRestrict`:

      dirGenWronskian c f ≠ 0  ↔  ∃ a, the restrictions along `t ↦ a + tc` are
                                       linearly independent over `K`

  Both directions.  This **reduces the remaining problem to a single question about the
  direction `c` alone** — the base point `a` is no longer part of it.  What is still open is
  the existence of a good `c`:

      f linearly independent over K  ⟹  ∃ c, dirGenWronskian c f ≠ 0

  ⚠ That is genuinely open here, not an oversight.  It is a genericity statement over a
  vector space of directions, and the naive argument fails: for each *fixed* non-zero
  `p ∈ span f` the bad set of `c` is small, but `span f` is infinite, so no finite union
  argument closes it.

  And even granting it, one step would remain before the result lands in the shape
  `mvGenWronskian` takes: `(Dᶜ)ⁱ` is a *linear combination* of monomial operators, so a
  multilinear expansion of the determinant is needed to exhibit a single bounded-order
  generalized Wronskian.
-/
import QOU.Mathlib.GenWronskian
import QOU.Mathlib.LineRestriction
import Mathlib.Algebra.CharZero.Infinite

namespace MvPolynomial

open Matrix

variable {σ K : Type*} [CommRing K]

/-- The Wronskian matrix built from the directional derivative `Dᶜ`. -/
noncomputable def dirWronskianMatrix [Fintype σ] {m : ℕ} (c : σ → K)
    (f : Fin m → MvPolynomial σ K) : Matrix (Fin m) (Fin m) (MvPolynomial σ K) :=
  Matrix.of fun i j => (dirDeriv c)^[(i : ℕ)] (f j)

/-- The **directional generalized Wronskian**: `det ((Dᶜ)ⁱ fⱼ)`.

Its rows have order `0, 1, …, m-1` by construction, which is exactly the bound Roth's lemma
asks for — the bound is inherited from `Dᶜ` rather than engineered. -/
noncomputable def dirGenWronskian [Fintype σ] {m : ℕ} (c : σ → K)
    (f : Fin m → MvPolynomial σ K) : MvPolynomial σ K :=
  (dirWronskianMatrix c f).det

/-- **The pullback:** restricting the directional Wronskian to a line gives the ordinary
univariate Wronskian of the restrictions.

`lineRestrict` is an `AlgHom`, so it commutes with `det`; the entries then match by the
iterated chain rule. -/
theorem lineRestrict_dirGenWronskian [Fintype σ] [DecidableEq σ] {m : ℕ} (a c : σ → K)
    (f : Fin m → MvPolynomial σ K) :
    lineRestrict a c (dirGenWronskian c f)
      = Polynomial.genWronskian (fun j => lineRestrict a c (f j)) := by
  have hmap : (dirWronskianMatrix c f).map ((lineRestrict a c).toRingHom)
      = Polynomial.wronskianMatrix (fun j => lineRestrict a c (f j)) := by
    refine Matrix.ext fun i j => ?_
    simp only [Matrix.map_apply, dirWronskianMatrix, Matrix.of_apply,
      Polynomial.wronskianMatrix_apply, AlgHom.toRingHom_eq_coe, RingHom.coe_coe]
    exact (iterate_derivative_lineRestrict a c i (f j)).symm
  rw [dirGenWronskian, Polynomial.genWronskian, ← hmap, ← RingHom.mapMatrix_apply,
    ← RingHom.map_det]
  rfl

section Field

variable {K : Type*} [Field K] [CharZero K]

/-- Independent restrictions force a non-zero directional Wronskian: the univariate
criterion, which already carries the order bound, transfers upstairs. -/
theorem dirGenWronskian_ne_zero_of_lineRestrict_linearIndependent
    [Fintype σ] [DecidableEq σ] {m : ℕ} (hm : 0 < m) (a c : σ → K)
    (f : Fin m → MvPolynomial σ K)
    (h : LinearIndependent K (fun j => lineRestrict a c (f j))) :
    dirGenWronskian c f ≠ 0 := by
  intro hzero
  have hg : Polynomial.genWronskian (fun j => lineRestrict a c (f j)) = 0 := by
    rw [← lineRestrict_dirGenWronskian, hzero, map_zero]
  obtain ⟨lam, hlam, hsum⟩ := (Polynomial.genWronskian_eq_zero_iff _ hm).mp hg
  refine hlam (_root_.funext fun j => ?_)
  refine Fintype.linearIndependent_iff.mp h lam ?_ j
  rw [← hsum]
  exact Finset.sum_congr rfl fun j _ => Polynomial.smul_eq_C_mul _

/-- Conversely, a non-zero directional Wronskian produces a line whose restrictions are
independent. -/
theorem exists_linearIndependent_lineRestrict_of_dirGenWronskian_ne_zero
    [Fintype σ] [DecidableEq σ] {m : ℕ} (hm : 0 < m) (c : σ → K)
    (f : Fin m → MvPolynomial σ K) (h : dirGenWronskian c f ≠ 0) :
    ∃ a : σ → K, LinearIndependent K (fun j => lineRestrict a c (f j)) := by
  obtain ⟨a, ha⟩ := exists_lineRestrict_ne_zero h c
  rw [lineRestrict_dirGenWronskian] at ha
  refine ⟨a, ?_⟩
  rw [Fintype.linearIndependent_iff]
  intro lam hsum i
  by_contra hi
  refine ha ((Polynomial.genWronskian_eq_zero_iff _ hm).mpr ⟨lam, ?_, ?_⟩)
  · intro h0
    exact hi (by simpa using congrFun h0 i)
  · rw [← hsum]
    exact Finset.sum_congr rfl fun j _ => (Polynomial.smul_eq_C_mul _).symm

/-- **The directional Wronskian is non-zero exactly when some line in that direction has
independent restrictions.**

The base point drops out of the problem: what is left to decide is a question about the
**direction alone**. -/
theorem dirGenWronskian_ne_zero_iff_exists_linearIndependent_lineRestrict
    [Fintype σ] [DecidableEq σ] {m : ℕ} (hm : 0 < m) (c : σ → K)
    (f : Fin m → MvPolynomial σ K) :
    dirGenWronskian c f ≠ 0
      ↔ ∃ a : σ → K, LinearIndependent K (fun j => lineRestrict a c (f j)) :=
  ⟨exists_linearIndependent_lineRestrict_of_dirGenWronskian_ne_zero hm c f,
   fun ⟨a, ha⟩ => dirGenWronskian_ne_zero_of_lineRestrict_linearIndependent hm a c f ha⟩

end Field

/-! ### Next

What remains for `qou-sq3h`, in order:

1. **A good direction exists.** `f` independent over `K` ⟹ `∃ c, dirGenWronskian c f ≠ 0`.
   By the iff above this is equivalent to finding *one* line whose restrictions stay
   independent. ⚠ Genuinely open: a genericity statement over the space of directions, and
   the naive per-element argument does not close it because `span f` is infinite.
2. **Multilinear expansion.** `(Dᶜ)ⁱ` is a linear combination of monomial operators of order
   `i`; expanding `det` over those exhibits a single bounded-order `mvGenWronskian`. The
   useful direction is the contrapositive — if every bounded-order generalized Wronskian
   vanishes then `dirGenWronskian c f = 0` for every `c` — which needs only multilinearity
   of `det` in its rows, not a multinomial theorem.

Then Roth's lemma itself. -/

end MvPolynomial
