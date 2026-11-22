import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic

/-!
# Spin involution on a Frobenius `*`-algebra

A **spin involution** on a Frobenius `*`-algebra `(A, τ, star)` is
an `R`-linear map `σ : A → A` that is

1. involutive (`σ ∘ σ = id`),
2. anti-multiplicative (`σ (a*b) = σ b * σ a`),
3. trace-invariant (`τ ∘ σ = τ`),
4. `*`-compatible (`σ (star a) = star (σ a)`).

The `±1`-eigenspaces of `σ` give the spin grading
`A = A₊ ⊕ A₋`; `A₊` is the spin-singlet sector and `A₋` the
spin-doublet sector. The isospin third-component `T₃` is read off
the `σ`-eigenvalue.

This sibling packages the four spin-involution axioms as a
structure and records the projection identity used downstream.

-- Ref: [leitner2026] def:spin-involution
-- Ref: [kassel1995] Kassel, "Quantum Groups," GTM 155, Springer (1995)
-/

namespace QOU.BraidKnot

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Module R A]

/-- A **spin involution** on a Frobenius `*`-algebra: an `R`-linear,
involutive, anti-multiplicative, trace- and `*`-compatible map. -/
structure SpinInvolution
    (τ : A → R) (star : A → A) where
  /-- The underlying map `σ : A → A`. -/
  σ : A → A
  /-- `σ` is `R`-linear. -/
  map_smul : ∀ (r : R) (a : A), σ (r • a) = r • σ a
  /-- `σ` is additive. -/
  map_add : ∀ a b : A, σ (a + b) = σ a + σ b
  /-- Involution: `σ ∘ σ = id`. -/
  involutive : ∀ a : A, σ (σ a) = a
  /-- Anti-multiplicative: `σ (a*b) = σ b * σ a`. -/
  anti_mul : ∀ a b : A, σ (a * b) = σ b * σ a
  /-- Trace-invariant: `τ (σ a) = τ a`. -/
  trace_inv : ∀ a : A, τ (σ a) = τ a
  /-- `*`-compatible: `σ (star a) = star (σ a)`. -/
  star_compat : ∀ a : A, σ (star a) = star (σ a)

/-- A spin involution is bijective: it is its own two-sided inverse,
directly from the involution axiom. -/
theorem spin_involution_bijective
    {τ : A → R} {star : A → A} (S : SpinInvolution τ star) :
    Function.Bijective S.σ :=
  Function.bijective_iff_has_inverse.2
    ⟨S.σ, S.involutive, S.involutive⟩

/-! ## Additivity helpers: `σ` is an additive group homomorphism

From `map_add` alone we derive `map_zero`, `map_neg`, `map_sub`. These are
needed for the `A₋` projection (which involves subtraction). -/

section Additive
variable {τ : A → R} {star : A → A} (S : SpinInvolution τ star)

/-- `σ 0 = 0`. -/
theorem SpinInvolution.map_zero : S.σ 0 = 0 := by
  have h : S.σ 0 + S.σ 0 = S.σ 0 + 0 := by
    rw [add_zero, ← S.map_add, add_zero]
  exact add_left_cancel h

/-- `σ (-a) = -(σ a)`. -/
theorem SpinInvolution.map_neg (a : A) : S.σ (-a) = -(S.σ a) := by
  have h : S.σ a + S.σ (-a) = 0 := by
    rw [← S.map_add, add_neg_cancel, S.map_zero]
  linear_combination (norm := abel) h

/-- `σ (a - b) = σ a - σ b`. -/
theorem SpinInvolution.map_sub (a b : A) : S.σ (a - b) = S.σ a - S.σ b := by
  rw [sub_eq_add_neg, S.map_add, S.map_neg, ← sub_eq_add_neg]

end Additive

/-! ## The spin grading `A = A₊ ⊕ A₋` (needs `½ ∈ R`) -/

section Projections
variable {τ : A → R} {star : A → A} [Invertible (2 : R)]

/-- The **spin-singlet projection** `a₊ = ½ (a + σ a) ∈ A₊`. -/
def SpinInvolution.plusProj (S : SpinInvolution τ star) (a : A) : A :=
  (⅟(2 : R)) • (a + S.σ a)

/-- The **spin-doublet projection** `a₋ = ½ (a - σ a) ∈ A₋`. -/
def SpinInvolution.minusProj (S : SpinInvolution τ star) (a : A) : A :=
  (⅟(2 : R)) • (a - S.σ a)

variable (S : SpinInvolution τ star)

/-- `a₊` lies in the `+1`-eigenspace: `σ (a₊) = a₊`. -/
theorem SpinInvolution.sigma_plusProj (a : A) :
    S.σ (S.plusProj a) = S.plusProj a := by
  unfold SpinInvolution.plusProj
  rw [S.map_smul, S.map_add, S.involutive, add_comm (S.σ a) a]

/-- `a₋` lies in the `-1`-eigenspace: `σ (a₋) = -a₋`. -/
theorem SpinInvolution.sigma_minusProj (a : A) :
    S.σ (S.minusProj a) = -(S.minusProj a) := by
  unfold SpinInvolution.minusProj
  rw [S.map_smul, S.map_sub, S.involutive, ← smul_neg, neg_sub]

/-- The spin decomposition `a = a₊ + a₋`. -/
theorem SpinInvolution.plus_add_minus (a : A) :
    S.plusProj a + S.minusProj a = a := by
  unfold SpinInvolution.plusProj SpinInvolution.minusProj
  rw [← smul_add]
  have h : a + S.σ a + (a - S.σ a) = (2 : R) • a := by
    rw [two_smul]; abel
  rw [h, smul_smul, invOf_mul_self, one_smul]

/-- The two sectors intersect only in `0`: an element that is both
`σ`-fixed and `σ`-negated is zero (uses `2` invertible). -/
theorem SpinInvolution.plus_inter_minus_eq_zero {x : A}
    (hplus : S.σ x = x) (hminus : S.σ x = -x) : x = 0 := by
  have hxx : x = -x := hplus.symm.trans hminus
  have hsum : x + x = 0 := by rw [add_eq_zero_iff_eq_neg]; exact hxx
  have h2 : (2 : R) • x = 0 := by rw [two_smul]; exact hsum
  calc x = (⅟(2 : R)) • ((2 : R) • x) := by
              rw [smul_smul, invOf_mul_self, one_smul]
    _ = (⅟(2 : R)) • (0 : A) := by rw [h2]
    _ = 0 := smul_zero _

/-- The spin decomposition is `σ`-diagonalising: `σ a = a₊ - a₋`. -/
theorem SpinInvolution.sigma_eq_plus_sub_minus (a : A) :
    S.σ a = S.plusProj a - S.minusProj a := by
  unfold SpinInvolution.plusProj SpinInvolution.minusProj
  rw [← smul_sub]
  have h : a + S.σ a - (a - S.σ a) = (2 : R) • S.σ a := by
    rw [two_smul]; abel
  rw [h, smul_smul, invOf_mul_self, one_smul]

end Projections

/-! ## Isospin third component `T₃ = ½ · sgn_σ`

The isospin third component is `T₃(a) = ½ · sgn_σ(a)`, where `sgn_σ ∈
{-1, 0, +1}` is `0` on the spin-singlet sector `A₊` and `±1` on the two
components of the spin-doublet sector `A₋`. Hence `T₃ = 0` on `A₊` and
`T₃ = ±½` on `A₋`. -/

section Isospin
variable [Invertible (2 : R)]

/-- Isospin third component from the three-valued spin sign
`sgn ∈ {-1, 0, +1}`: `T₃ = ½ · sgn`. -/
def isospinT3 (sgn : ℤ) : R := (sgn : R) * ⅟(2 : R)

/-- On the **spin-singlet** sector (`sgn = 0`) the isospin third component
vanishes: `T₃ = 0`. -/
theorem isospinT3_singlet : isospinT3 (R := R) 0 = 0 := by
  unfold isospinT3; simp

/-- On the **positive** spin-doublet component (`sgn = +1`): `T₃ = +½`. -/
theorem isospinT3_doublet_pos : isospinT3 (R := R) 1 = ⅟(2 : R) := by
  unfold isospinT3; simp

/-- On the **negative** spin-doublet component (`sgn = -1`): `T₃ = -½`. -/
theorem isospinT3_doublet_neg : isospinT3 (R := R) (-1) = -⅟(2 : R) := by
  unfold isospinT3; simp

/-- Doubled isospin `2·T₃ = sgn_σ` recovers the integer spin sign. -/
theorem two_mul_isospinT3 (sgn : ℤ) :
    (2 : R) * isospinT3 (R := R) sgn = (sgn : R) := by
  unfold isospinT3
  rw [← mul_assoc, mul_comm (2 : R), mul_assoc, mul_invOf_self, mul_one]

end Isospin

end QOU.BraidKnot
