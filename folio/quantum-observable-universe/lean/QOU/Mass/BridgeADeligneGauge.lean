import Mathlib.RingTheory.Derivation.Basic
import Mathlib.Algebra.Ring.Action.Basic
import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.Defs

/-!
# Bridge A, route B — conjugate monodromy + Deligne full faithfulness ⇒ algebraic gauge equivalence

Mass-pipeline gap 3.  The 2026-11-15 audit (`docs/audits/2026-11-15-bridge-a2-lagrangian-kz.md`,
last section) kept two assumptions between the categorical braiding and the KZ connection:

1. Riemann–Hilbert in Deligne's form;
2. triviality of the resulting algebraic vector bundle on `Conf_n`.

Item 2 is settled on paper by commutative algebra (route A of
`/mnt/project-files/qou-mass-pipeline-gaps-3-4/gaps-3-4-seminormal-and-bridge-a.md`):
`K₀(ℂ[z][1/Δ]) = ℤ`, so every bundle is stably free, and Bass cancellation makes a stably free
module of rank `Nⁿ > n = dim` free.  So both connections below live on the trivial bundle.

This file proves the **algebraic skeleton of item 1**, and shows that only the *uniqueness* half of
Riemann–Hilbert is needed: existence is supplied by KZ itself, whose monodromy is the Jimbo braiding
(`QOU.Mass.KohnoAssembly.kz_conj_jimbo_complex`).

## Setting (all algebraic)

* `R` — the algebraic functions (for `Conf_n`: `ℂ[z][1/Δ]`), inside a commutative ring `S` of
  multivalued analytic functions (functions on the universal cover).  `algebraMap R S` is injective.
* `D : ι → Derivation ℤ S S` — the partial derivatives `∂/∂z_j`.
* `Γ` — the deck group (`π₁`, the pure braid group), acting on `S` by ring automorphisms.
* `K` — the constants: `D` kills them and `Γ` fixes them.
* A connection on the trivial rank-`N` bundle is a family `ω : ι → Matrix n n R`; a *fundamental
  solution* is an invertible `Φ` over `S` with `∂_j Φ = ω_j Φ` and deck behaviour
  `γ • Φ = Φ · M(γ)`, `M(γ)` constant: `M` is the monodromy.

## The one analytic input, isolated

`DeligneFullyFaithful ω₁ ω₂`: a **deck-invariant** (single-valued) matrix `h` over `S` that is
horizontal for `Hom(∇₁, ∇₂)` — `∂_j h = ω₂_j h − h ω₁_j` — has entries in `R`.  For regular-singular
connections on a smooth quasi-projective variety this is Deligne's theorem (moderate growth +
GAGA); it is the only place analysis enters, and it is a hypothesis here, never proved.

The existence of fundamental solutions with monodromy is the ODE half; it is also carried as data
(`FundamentalSolution`), not proved.

## Result

`gauge_of_conj_monodromy`: if the monodromies are conjugate by a constant invertible `C`
(`M₂(γ)·C = C·M₁(γ)`), and full faithfulness holds in both directions, then there is
`g ∈ GL_N(R)` with `ω₂ = (∂g + g ω₁) g⁻¹` — the connections are **algebraically** gauge
equivalent.  With `∇₁ = KZ` and `∇₂` the Lagrangian connection, and `C` from
`kz_conj_jimbo_complex`, this gives `∇ ≅ KZ` without postulating two-body locality (P2).

## What this does NOT give

* It does not prove Deligne's theorem, nor the existence of fundamental solutions.
* It does not connect `S`, `Γ`, `D` to the concrete transport in `KZHolonomy`; that instantiation
  is open.  Route A (bundle triviality) is not formalised (needs Bass cancellation, absent from
  Mathlib).
* Gauge equivalence by a non-constant `g` does not preserve the Arnold form, so "P2 follows"
  means "P2 holds up to algebraic gauge".

Base ring (§7c): any commutative rings, any field-free setting; no `ℝ`/`ℂ`.
-/

set_option linter.unusedSectionVars false

namespace QOU.Mass.BridgeADeligneGauge

open Matrix

variable {S : Type*} [CommRing S] {n : Type*} [Fintype n] [DecidableEq n]

/-- Matrix Leibniz rule for an additive derivation applied entrywise. -/
theorem map_mul_der (d : Derivation ℤ S S) (A B : Matrix n n S) :
    (A * B).map d = A.map d * B + A * B.map d := by
  ext i k
  simp only [Matrix.map_apply, Matrix.mul_apply, Matrix.add_apply, map_sum,
    Derivation.leibniz, smul_eq_mul, ← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl fun l _ => by ring

theorem map_one_der (d : Derivation ℤ S S) : (1 : Matrix n n S).map d = 0 := by
  ext i k
  by_cases h : i = k
  · subst h; simp
  · simp [Matrix.one_apply_ne h]

section Setting

variable {ι : Type*} (D : ι → Derivation ℤ S S)
variable {K : Type*} [CommRing K] [Algebra K S]
variable {Γ : Type*} [Monoid Γ] [MulSemiringAction Γ S]

/-- Entrywise deck action on matrices. -/
def actM (γ : Γ) (M : Matrix n n S) : Matrix n n S := M.map (fun s => γ • s)

theorem actM_mul (γ : Γ) (A B : Matrix n n S) : actM γ (A * B) = actM γ A * actM γ B :=
  Matrix.map_mul (f := MulSemiringAction.toRingHom Γ S γ)

theorem actM_one (γ : Γ) : actM γ (1 : Matrix n n S) = 1 :=
  Matrix.map_one (fun s => γ • s) (smul_zero γ) (smul_one γ)

/-- The constants embedded in `S`. -/
abbrev cst (C : Matrix n n K) : Matrix n n S := C.map (algebraMap K S)

/-- A fundamental solution of `∂_j Φ = ω_j Φ` with constant monodromy `M`. -/
structure FundamentalSolution (ω : ι → Matrix n n S) where
  Φ : Matrix n n S
  Φinv : Matrix n n S
  mul_inv : Φ * Φinv = 1
  inv_mul : Φinv * Φ = 1
  horiz : ∀ j, Φ.map (D j) = ω j * Φ
  M : Γ → Matrix n n K
  deck : ∀ γ : Γ, actM γ Φ = Φ * cst (M γ)

/-- **Deligne full faithfulness** (the isolated analytic input): a single-valued horizontal
section of `Hom(∇₁, ∇₂)` is algebraic. -/
def DeligneFullyFaithful (R : Type*) [CommRing R] [Algebra R S] (Γ : Type*) [Monoid Γ]
    [MulSemiringAction Γ S] (ω₁ ω₂ : ι → Matrix n n S) : Prop :=
  ∀ h : Matrix n n S, (∀ γ : Γ, actM γ h = h) →
    (∀ j, h.map (D j) = ω₂ j * h - h * ω₁ j) → ∃ h' : Matrix n n R, h = h'.map (algebraMap R S)

variable {D}

/-- The inverse of a fundamental solution satisfies `∂Φ⁻¹ = −Φ⁻¹ ω`. -/
theorem horiz_inv {ω : ι → Matrix n n S} (F : FundamentalSolution (Γ := Γ) (K := K) D ω) (j : ι) :
    F.Φinv.map (D j) = -(F.Φinv * ω j) := by
  have h0 : (F.Φ * F.Φinv).map (D j) = 0 := by rw [F.mul_inv, map_one_der]
  rw [map_mul_der, F.horiz j] at h0
  -- ωΦΦ⁻¹ + Φ ∂Φ⁻¹ = 0, multiply by Φ⁻¹ on the left
  have h1 : F.Φinv * (ω j * F.Φ * F.Φinv + F.Φ * F.Φinv.map (D j)) = 0 := by rw [h0, mul_zero]
  rw [mul_add, Matrix.mul_assoc (ω j), F.mul_inv, Matrix.mul_one, ← Matrix.mul_assoc F.Φinv F.Φ,
    F.inv_mul, Matrix.one_mul] at h1
  exact eq_neg_of_add_eq_zero_right h1

/-- The deck action on `Φ⁻¹`: `γ • Φ⁻¹ = M(γ)⁻¹ Φ⁻¹`, written without inverting `M`:
`Φ · M(γ) · (γ • Φ⁻¹) = 1`. -/
theorem deck_inv {ω : ι → Matrix n n S} (F : FundamentalSolution (Γ := Γ) (K := K) D ω) (γ : Γ) :
    F.Φ * cst (F.M γ) * actM γ F.Φinv = 1 := by
  rw [← F.deck γ, ← actM_mul, F.mul_inv, actM_one]

/-- The candidate intertwiner `h = Φ₂ C Φ₁⁻¹`. -/
def intertwiner {ω₁ ω₂ : ι → Matrix n n S} (F₁ : FundamentalSolution (Γ := Γ) (K := K) D ω₁)
    (F₂ : FundamentalSolution (Γ := Γ) (K := K) D ω₂) (C : Matrix n n K) : Matrix n n S :=
  F₂.Φ * cst C * F₁.Φinv

variable (hDK : ∀ j (c : K), D j (algebraMap K S c) = 0)
variable (hΓK : ∀ (γ : Γ) (c : K), γ • algebraMap K S c = algebraMap K S c)
include hDK

theorem cst_der (C : Matrix n n K) (j : ι) : (cst C).map (D j) = (0 : Matrix n n S) := by
  ext i k; simp [hDK]

/-- `h = Φ₂ C Φ₁⁻¹` is horizontal for `Hom(∇₁, ∇₂)`, for any constant `C`. -/
theorem intertwiner_horiz {ω₁ ω₂ : ι → Matrix n n S}
    (F₁ : FundamentalSolution (Γ := Γ) (K := K) D ω₁)
    (F₂ : FundamentalSolution (Γ := Γ) (K := K) D ω₂) (C : Matrix n n K) (j : ι) :
    (intertwiner F₁ F₂ C).map (D j)
      = ω₂ j * intertwiner F₁ F₂ C - intertwiner F₁ F₂ C * ω₁ j := by
  unfold intertwiner
  rw [map_mul_der, map_mul_der, F₂.horiz j, cst_der hDK, horiz_inv F₁ j]
  simp only [Matrix.mul_zero, add_zero, Matrix.mul_neg, Matrix.mul_assoc]
  abel

omit hDK in
include hΓK in
/-- `h` is deck-invariant (single-valued) exactly when `C` intertwines the monodromies. -/
theorem intertwiner_invariant {ω₁ ω₂ : ι → Matrix n n S}
    (F₁ : FundamentalSolution (Γ := Γ) (K := K) D ω₁)
    (F₂ : FundamentalSolution (Γ := Γ) (K := K) D ω₂) (C : Matrix n n K)
    (hC : ∀ γ, F₂.M γ * C = C * F₁.M γ) (γ : Γ) :
    actM γ (intertwiner F₁ F₂ C) = intertwiner F₁ F₂ C := by
  have hcst : actM γ (cst (S := S) C) = cst C := by ext i k; simp [actM, hΓK]
  have hmul : ∀ A B : Matrix n n K, (cst (S := S) (A * B)) = cst A * cst B := fun A B =>
    Matrix.map_mul (f := algebraMap K S)
  unfold intertwiner
  rw [actM_mul, actM_mul, F₂.deck γ, hcst, Matrix.mul_assoc F₂.Φ, ← hmul, hC γ, hmul]
  -- Φ₂ (C M₁) (γΦ₁⁻¹) = Φ₂ C Φ₁⁻¹ · (Φ₁ M₁ γΦ₁⁻¹)
  have h1 := deck_inv F₁ γ
  calc F₂.Φ * (cst C * cst (F₁.M γ)) * actM γ F₁.Φinv
      = F₂.Φ * cst C * (F₁.Φinv * F₁.Φ) * cst (F₁.M γ) * actM γ F₁.Φinv := by
        rw [F₁.inv_mul, Matrix.mul_one]; simp only [Matrix.mul_assoc]
    _ = F₂.Φ * cst C * F₁.Φinv * (F₁.Φ * cst (F₁.M γ) * actM γ F₁.Φinv) := by
        simp only [Matrix.mul_assoc]
    _ = F₂.Φ * cst C * F₁.Φinv := by rw [h1, Matrix.mul_one]

include hΓK in
/-- **Route B of Bridge A.**  Conjugate monodromy plus Deligne full faithfulness (both directions)
gives an algebraic gauge transformation `g ∈ GL_N(R)` with `∂g = ω₂ g − g ω₁`, i.e.
`ω₂ = (∂g + g ω₁) g⁻¹`. -/
theorem gauge_of_conj_monodromy (R : Type*) [CommRing R] [Algebra R S]
    (hinj : Function.Injective (algebraMap R S)) {ω₁ ω₂ : ι → Matrix n n S}
    (F₁ : FundamentalSolution (Γ := Γ) (K := K) D ω₁)
    (F₂ : FundamentalSolution (Γ := Γ) (K := K) D ω₂) (C Cinv : Matrix n n K)
    (hCC : C * Cinv = 1) (hCC' : Cinv * C = 1)
    (hC : ∀ γ, F₂.M γ * C = C * F₁.M γ)
    (hFF₁₂ : DeligneFullyFaithful D R Γ ω₁ ω₂) (hFF₂₁ : DeligneFullyFaithful D R Γ ω₂ ω₁) :
    ∃ g gInv : Matrix n n R, g * gInv = 1 ∧ gInv * g = 1 ∧
      ∀ j, (g.map (algebraMap R S)).map (D j)
        = ω₂ j * g.map (algebraMap R S) - g.map (algebraMap R S) * ω₁ j := by
  have hmul : ∀ A B : Matrix n n K, (cst (S := S) (A * B)) = cst A * cst B := fun A B =>
    Matrix.map_mul (f := algebraMap K S)
  have hone : cst (S := S) (1 : Matrix n n K) = 1 := Matrix.map_one _ (map_zero _) (map_one _)
  -- the reverse intertwining
  have hC' : ∀ γ, F₁.M γ * Cinv = Cinv * F₂.M γ := fun γ => by
    calc F₁.M γ * Cinv = Cinv * (C * F₁.M γ) * Cinv := by
          rw [← Matrix.mul_assoc, hCC', Matrix.one_mul]
      _ = Cinv * (F₂.M γ * C) * Cinv := by rw [hC γ]
      _ = Cinv * F₂.M γ := by rw [Matrix.mul_assoc, Matrix.mul_assoc, hCC, Matrix.mul_one]
  obtain ⟨g, hg⟩ := hFF₁₂ (intertwiner F₁ F₂ C)
    (intertwiner_invariant hΓK F₁ F₂ C hC) (intertwiner_horiz hDK F₁ F₂ C)
  obtain ⟨gi, hgi⟩ := hFF₂₁ (intertwiner F₂ F₁ Cinv)
    (intertwiner_invariant hΓK F₂ F₁ Cinv hC') (intertwiner_horiz hDK F₂ F₁ Cinv)
  have hprod : intertwiner F₁ F₂ C * intertwiner F₂ F₁ Cinv = 1 := by
    unfold intertwiner
    calc F₂.Φ * cst C * F₁.Φinv * (F₁.Φ * cst Cinv * F₂.Φinv)
        = F₂.Φ * cst C * (F₁.Φinv * F₁.Φ) * cst Cinv * F₂.Φinv := by simp only [Matrix.mul_assoc]
      _ = F₂.Φ * cst (C * Cinv) * F₂.Φinv := by
          rw [F₁.inv_mul, Matrix.mul_one, hmul, Matrix.mul_assoc F₂.Φ]
      _ = 1 := by rw [hCC, hone, Matrix.mul_one, F₂.mul_inv]
  have hprod' : intertwiner F₂ F₁ Cinv * intertwiner F₁ F₂ C = 1 := by
    unfold intertwiner
    calc F₁.Φ * cst Cinv * F₂.Φinv * (F₂.Φ * cst C * F₁.Φinv)
        = F₁.Φ * cst Cinv * (F₂.Φinv * F₂.Φ) * cst C * F₁.Φinv := by simp only [Matrix.mul_assoc]
      _ = F₁.Φ * cst (Cinv * C) * F₁.Φinv := by
          rw [F₂.inv_mul, Matrix.mul_one, hmul, Matrix.mul_assoc F₁.Φ]
      _ = 1 := by rw [hCC', hone, Matrix.mul_one, F₁.mul_inv]
  have hmulR : ∀ A B : Matrix n n R, (A * B).map (algebraMap R S)
      = A.map (algebraMap R S) * B.map (algebraMap R S) := fun A B =>
    Matrix.map_mul (f := algebraMap R S)
  have hinjM : Function.Injective (fun A : Matrix n n R => A.map (algebraMap R S)) :=
    fun A B hAB => by ext i k; exact hinj (congrFun (congrFun hAB i) k)
  have honeR : (1 : Matrix n n R).map (algebraMap R S) = 1 :=
    Matrix.map_one _ (map_zero _) (map_one _)
  refine ⟨g, gi, ?_, ?_, ?_⟩
  · apply hinjM; simp only; rw [hmulR, ← hg, ← hgi, hprod, honeR]
  · apply hinjM; simp only; rw [hmulR, ← hg, ← hgi, hprod', honeR]
  · intro j; rw [← hg]; exact intertwiner_horiz hDK F₁ F₂ C j

end Setting

/-! ## Non-vacuity: the hypotheses are jointly satisfiable

`S = R = K = ℚ`, `Γ = Unit` acting trivially, zero derivations, `ω₁ = ω₂ = 0`, `Φ = 1`, `M = 1`, `C = 1`.  This
only shows the structure and the full-faithfulness predicate can be inhabited; it is not the KZ
instance. -/

section NonVacuity

/-- The trivial deck group acting trivially. -/
local instance trivialAction : MulSemiringAction Unit ℚ where
  smul _ x := x
  one_smul _ := rfl
  mul_smul _ _ _ := rfl
  smul_zero _ := rfl
  smul_add _ _ _ := rfl
  smul_one _ := rfl
  smul_mul _ _ _ := rfl

example : DeligneFullyFaithful (n := Fin 2) (S := ℚ) (fun _ : Unit => (0 : Derivation ℤ ℚ ℚ)) ℚ (Unit)
    (fun _ => 0) (fun _ => 0) := fun h _ _ => ⟨h, by ext i k; simp⟩

example : FundamentalSolution (n := Fin 2) (S := ℚ) (K := ℚ) (Γ := Unit)
    (fun _ : Unit => (0 : Derivation ℤ ℚ ℚ)) (fun _ => 0) where
  Φ := 1
  Φinv := 1
  mul_inv := Matrix.mul_one 1
  inv_mul := Matrix.mul_one 1
  horiz := fun _ => by rw [map_one_der, Matrix.zero_mul]
  M := fun _ => 1
  deck := fun γ => by rw [actM_one, Matrix.one_mul]; ext i k; simp [cst, Matrix.one_apply]

end NonVacuity

end QOU.Mass.BridgeADeligneGauge
