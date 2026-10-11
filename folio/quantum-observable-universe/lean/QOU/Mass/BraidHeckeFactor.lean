import QOU.MathlibExt.BraidGroup
import QOU.SchurWeyl.HeckeAlgebra

/-!
# A braid representation with one quadratic generator factors through the Hecke algebra

Let `K` be a commutative ring, `A` a `K`-algebra and `θ : B_{m+1} →* Aˣ` a representation of
the braid group on `m + 1` strands (Artin presentation, `QOU.MathlibExt.Braid.BraidGroup m`).
Fix scalars `s, q, qi : K`. Say that `x ∈ A` is **`(s, q, qi)`-Hecke** if `β = s • x` satisfies
the Hecke quadratic of `QOU.SchurWeyl.Hecke K q qi m`:

    β * β = (q − qi) • β + (q * qi) • 1.

This file proves, over an arbitrary commutative ring:

* `isHeckeQuad_conj` — the condition is invariant under conjugation by a unit;
* `σ_succ_eq_conj` — in `B_{m+1}`, `σ_{i+1} = w σ_i w⁻¹` with `w = σ_i σ_{i+1}`;
* `isHeckeQuad_all_of_zero` — hence **if the first generator `θ(σ₀)` is Hecke, every generator
  is**. All Artin generators are conjugate, so one local computation suffices;
* `heckeOfBraidRep` — if every generator is Hecke, `θ` factors through the Hecke algebra: there
  is a `K`-algebra map `H_m(q) →ₐ[K] A` with `σ_j ↦ s • θ(σ_j)` (the `RingQuot` lift
  `QOU.SchurWeyl.Hecke.lift`; the braid and far-commutation relations are inherited from the
  braid group).

Nothing here is analytic. Its use in the Kohno comparison (`QOU.Mass.KZTwoStrandHecke`,
docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §5) is to reduce the factorisation of
the KZ holonomy representation through `H_n(q)` to the quadratic relation for **one**
generator.
-/

namespace QOU.Mass.BraidHeckeFactor

open QOU.MathlibExt.Braid

/-! ## Relations in the braid group -/

section BraidRelations

variable {m : ℕ}

/-- The braid relation `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}` in `BraidGroup m`. -/
theorem σ_braid_rel (i : Fin m) (h : (i : ℕ) + 1 < m) :
    σ i * σ ⟨(i : ℕ) + 1, h⟩ * σ i = σ ⟨(i : ℕ) + 1, h⟩ * σ i * σ ⟨(i : ℕ) + 1, h⟩ := by
  have hmem : FreeGroup.of i * FreeGroup.of ⟨(i : ℕ) + 1, h⟩ * FreeGroup.of i *
      (FreeGroup.of ⟨(i : ℕ) + 1, h⟩ * FreeGroup.of i * FreeGroup.of ⟨(i : ℕ) + 1, h⟩)⁻¹ ∈
      braidRelators m := Or.inr ⟨i, h, rfl⟩
  have := PresentedGroup.mk_eq_mk_of_mul_inv_mem hmem
  simpa only [map_mul] using this

/-- Far commutation `σ_i σ_j = σ_j σ_i` for `i + 2 ≤ j` in `BraidGroup m`. -/
theorem σ_comm_rel (i j : Fin m) (h : (i : ℕ) + 2 ≤ (j : ℕ)) :
    σ i * σ j = σ j * σ i := by
  have hmem : FreeGroup.of i * FreeGroup.of j * (FreeGroup.of i)⁻¹ * (FreeGroup.of j)⁻¹ ∈
      braidRelators m := Or.inl ⟨i, j, h, rfl⟩
  have h1 := PresentedGroup.one_of_mem hmem
  simp only [map_mul, map_inv] at h1
  have h2 : (σ i * σ j) * (σ j * σ i)⁻¹ = 1 := by
    rw [mul_inv_rev]
    simpa only [σ, PresentedGroup.of, mul_assoc] using h1
  exact mul_inv_eq_one.mp h2

/-- **All Artin generators are conjugate.** `σ_{i+1} = w σ_i w⁻¹` with `w = σ_i σ_{i+1}`. -/
theorem σ_succ_eq_conj (i : Fin m) (h : (i : ℕ) + 1 < m) :
    σ ⟨(i : ℕ) + 1, h⟩ = (σ i * σ ⟨(i : ℕ) + 1, h⟩) * σ i * (σ i * σ ⟨(i : ℕ) + 1, h⟩)⁻¹ := by
  rw [eq_mul_inv_iff_mul_eq, σ_braid_rel i h, mul_assoc]

end BraidRelations

/-! ## The Hecke quadratic condition -/

section Quad

variable {K : Type*} [CommRing K] {A : Type*} [Ring A] [Algebra K A]

/-- `x` is `(s, q, qi)`-Hecke: `β = s • x` satisfies `β² = (q − qi)β + q·qi`. -/
def IsHeckeQuad (s q qi : K) (x : A) : Prop :=
  (s • x) * (s • x) = (q - qi) • (s • x) + (q * qi) • (1 : A)

/-- The Hecke condition is invariant under conjugation by a unit. -/
theorem isHeckeQuad_conj {s q qi : K} {x : A} (u : Aˣ) (hx : IsHeckeQuad s q qi x) :
    IsHeckeQuad s q qi ((u : A) * x * (u⁻¹ : Aˣ)) := by
  unfold IsHeckeQuad at *
  have hs : s • ((u : A) * x * (u⁻¹ : Aˣ)) = (u : A) * (s • x) * (u⁻¹ : Aˣ) := by
    rw [mul_smul_comm, smul_mul_assoc]
  rw [hs]
  calc (u : A) * (s • x) * (u⁻¹ : Aˣ) * ((u : A) * (s • x) * (u⁻¹ : Aˣ))
      = (u : A) * ((s • x) * (s • x)) * (u⁻¹ : Aˣ) := by
        simp only [mul_assoc, Units.inv_mul_cancel_left]
    _ = (u : A) * ((q - qi) • (s • x) + (q * qi) • (1 : A)) * (u⁻¹ : Aˣ) := by rw [hx]
    _ = (q - qi) • ((u : A) * (s • x) * (u⁻¹ : Aˣ)) + (q * qi) • (1 : A) := by
        rw [mul_add, add_mul]
        congr 1
        · rw [mul_smul_comm, smul_mul_assoc]
        · rw [mul_smul_comm, smul_mul_assoc, mul_one, Units.mul_inv]

variable {m : ℕ}

/-- **One generator suffices.** If `θ(σ₀)` is Hecke then every `θ(σ_j)` is: the generators
are conjugate in the braid group (`σ_succ_eq_conj`) and the condition is
conjugation-invariant (`isHeckeQuad_conj`). -/
theorem isHeckeQuad_all_of_zero {s q qi : K} (θ : BraidGroup m →* Aˣ)
    (h0 : ∀ hm : 0 < m, IsHeckeQuad s q qi ((θ (σ ⟨0, hm⟩) : Aˣ) : A)) :
    ∀ j : Fin m, IsHeckeQuad s q qi ((θ (σ j) : Aˣ) : A) := by
  rintro ⟨j, hj⟩
  induction j with
  | zero => exact h0 hj
  | succ k ih =>
      have hk : k < m := Nat.lt_of_succ_lt hj
      have hc := σ_succ_eq_conj (m := m) ⟨k, hk⟩ hj
      have hc' : (⟨k + 1, hj⟩ : Fin m) = ⟨((⟨k, hk⟩ : Fin m) : ℕ) + 1, hj⟩ := rfl
      rw [hc', hc, map_mul, map_mul, map_inv]
      exact isHeckeQuad_conj (θ (σ ⟨k, hk⟩ * σ ⟨k + 1, hj⟩)) (ih hk)

/-! ## The factorisation -/

/-- The scaled generator images `j ↦ s • θ(σ_j)`. -/
def scaledGen (θ : BraidGroup m →* Aˣ) (s : K) (j : Fin m) : A := s • ((θ (σ j) : Aˣ) : A)

lemma scaledGen_braid (θ : BraidGroup m →* Aˣ) (s : K) (i : Fin m) (h : (i : ℕ) + 1 < m) :
    scaledGen θ s i * scaledGen θ s ⟨(i : ℕ) + 1, h⟩ * scaledGen θ s i =
      scaledGen θ s ⟨(i : ℕ) + 1, h⟩ * scaledGen θ s i * scaledGen θ s ⟨(i : ℕ) + 1, h⟩ := by
  have hb := congrArg (fun b => ((θ b : Aˣ) : A)) (σ_braid_rel (m := m) i h)
  simp only [map_mul, Units.val_mul] at hb
  simp only [scaledGen, smul_mul_smul_comm]
  rw [hb]

lemma scaledGen_comm (θ : BraidGroup m →* Aˣ) (s : K) (i j : Fin m)
    (h : (j : ℕ) + 2 ≤ (i : ℕ)) :
    scaledGen θ s i * scaledGen θ s j = scaledGen θ s j * scaledGen θ s i := by
  have hb := congrArg (fun b => ((θ b : Aˣ) : A)) (σ_comm_rel (m := m) j i h)
  simp only [map_mul, Units.val_mul] at hb
  simp only [scaledGen, smul_mul_smul_comm]
  rw [hb]

/-- **Factorisation through the Hecke algebra.** A braid representation whose generators are
all `(s, q, qi)`-Hecke induces a `K`-algebra map `H_m(q) →ₐ[K] A`, `σ_j ↦ s • θ(σ_j)`. -/
noncomputable def heckeOfBraidRep {s q qi : K} (θ : BraidGroup m →* Aˣ)
    (hq : ∀ j : Fin m, IsHeckeQuad s q qi ((θ (σ j) : Aˣ) : A)) :
    QOU.SchurWeyl.Hecke K q qi m →ₐ[K] A :=
  QOU.SchurWeyl.Hecke.lift K q qi m (scaledGen θ s) hq (scaledGen_braid θ s)
    (scaledGen_comm θ s)

@[simp] theorem heckeOfBraidRep_σ {s q qi : K} (θ : BraidGroup m →* Aˣ)
    (hq : ∀ j : Fin m, IsHeckeQuad s q qi ((θ (σ j) : Aˣ) : A)) (j : Fin m) :
    heckeOfBraidRep θ hq (QOU.SchurWeyl.Hecke.σ K q qi m j) = s • ((θ (σ j) : Aˣ) : A) :=
  QOU.SchurWeyl.Hecke.lift_σ K q qi m (scaledGen θ s) hq (scaledGen_braid θ s)
    (scaledGen_comm θ s) j

/-- The factorisation from the first generator alone. -/
noncomputable def heckeOfBraidRepOfZero {s q qi : K} (θ : BraidGroup m →* Aˣ)
    (h0 : ∀ hm : 0 < m, IsHeckeQuad s q qi ((θ (σ ⟨0, hm⟩) : Aˣ) : A)) :
    QOU.SchurWeyl.Hecke K q qi m →ₐ[K] A :=
  heckeOfBraidRep θ (isHeckeQuad_all_of_zero θ h0)

end Quad

end QOU.Mass.BraidHeckeFactor
