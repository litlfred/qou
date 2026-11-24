/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.QuantumGLHWRestrict
import BraidKnotOctonion.QuantumGLHWDensity
import BraidKnotOctonion.HeckeWedderburnGeneral
import HeckeTemperleyLieb.SeminormalCharBranching
import Mathlib.Data.Matrix.Basis
import Mathlib.LinearAlgebra.Dual.Lemmas

/-!
# Each highest-weight space has a single seminormal character

G3.4c (bean `qou-gl343`), identification step D.

Let `W : H_{m+1}(q) ≃ ∏_{λ ⊢ m+1} End(S_λ)` be the Wedderburn isomorphism
(`heckeWedderburn`), and `e_λ = W⁻¹(1_λ)` its central block idempotents.  On a nonzero `HW_μ`
each `e_λ` acts by an idempotent commuting with the whole Hecke action, which by density
(`exists_jimbo_restrict_eq`) is all of `End(HW_μ)`; so it acts by `0` or `1`
(`eq_zero_or_one_of_isIdempotentElem_of_comm`).  Some `e_π` acts by `1`.  Then `HW_μ` only
sees the block `π`, and a trace functional on a matrix algebra is a multiple of the trace
(`exists_eq_mul_trace_of_comm`), so

`tr(z | HW_μ) = c · χ^π(z)`  for all `z`  (`exists_hwTrace_eq_mul_trace`).

Pinning `π = λ(μ)` and `c = 1` is the induction of step E, using the two branching rules.

## Base ring (§7c)

The two abstract lemmas: any field.  The rest: a linearly ordered field, `q` not a root of
unity (density and the Wedderburn split need it).
-/

namespace QOU.SchurWeyl.QuantumGL

open QOU.SchurWeyl.JimboGL QOU.SchurWeyl.HeckeInclusion Matrix

section Abstract

variable {K : Type*} [Field K]

/-- **A trace functional on a matrix algebra is a multiple of the trace.** -/
theorem exists_eq_mul_trace_of_comm {n : Type*} [Fintype n] [DecidableEq n]
    (τ : Matrix n n K →ₗ[K] K) (hτ : ∀ A B, τ (A * B) = τ (B * A)) :
    ∃ c : K, ∀ X, τ X = c * X.trace := by
  classical
  rcases isEmpty_or_nonempty n with hn | ⟨⟨i0⟩⟩
  · exact ⟨0, fun X => by rw [Subsingleton.elim X 0, map_zero, zero_mul]⟩
  refine ⟨τ (single i0 i0 1), fun X => ?_⟩
  have hs : ∀ i j, τ (single i j (1 : K)) = if i = j then τ (single i0 i0 1) else 0 := by
    intro i j
    have h1 : single i j (1 : K) = single i i0 1 * single i0 j 1 := by
      rw [single_mul_single_same, one_mul]
    rw [h1, hτ]
    by_cases hij : i = j
    · subst hij; rw [single_mul_single_same, one_mul, if_pos rfl]
    · rw [single_mul_single_of_ne 1 i0 j i (Ne.symm hij) 1, map_zero, if_neg hij]
  have hsm : ∀ i j, τ (single i j (X i j)) = X i j * τ (single i j 1) := by
    intro i j
    rw [show single i j (X i j) = X i j • single i j (1 : K) by
      rw [smul_single, smul_eq_mul, mul_one], map_smul, smul_eq_mul]
  conv_lhs => rw [matrix_eq_sum_single X]
  rw [map_sum, Matrix.trace, Finset.mul_sum]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [map_sum, Finset.sum_eq_single i]
  · rw [hsm, hs, if_pos rfl, Matrix.diag_apply, mul_comm]
  · intro j _ hj; rw [hsm, hs, if_neg (Ne.symm hj), mul_zero]
  · intro h; exact absurd (Finset.mem_univ i) h

/-- **A central idempotent of `End V` is `0` or `1`.** -/
theorem eq_zero_or_one_of_isIdempotentElem_of_comm {V : Type*} [AddCommGroup V] [Module K V]
    (P : Module.End K V) (hP : IsIdempotentElem P) (hc : ∀ f : Module.End K V, P * f = f * P) :
    P = 0 ∨ P = 1 := by
  by_cases h0 : P = 0
  · exact Or.inl h0
  right
  obtain ⟨v, hv⟩ : ∃ v, P v ≠ 0 := by
    by_contra hh; push_neg at hh; exact h0 (LinearMap.ext hh)
  obtain ⟨φ, hφ⟩ : ∃ φ : Module.Dual K V, φ (P v) ≠ 0 := by
    by_contra hh; push_neg at hh
    exact hv ((Module.forall_dual_apply_eq_zero_iff K (P v)).mp hh)
  refine LinearMap.ext fun w => ?_
  set f : Module.End K V := (φ (P v))⁻¹ • φ.smulRight w with hfdef
  have hf : f (P v) = w := by
    rw [hfdef, LinearMap.smul_apply, LinearMap.smulRight_apply, smul_smul, inv_mul_cancel₀ hφ,
      one_smul]
  have hPP : P (P v) = P v := congrArg (fun g : Module.End K V => g v) hP
  have h := congrArg (fun g : Module.End K V => g (P v)) (hc f)
  simp only [Module.End.mul_apply, hPP, hf] at h
  rw [h]; rfl

/-- **The trace of an idempotent is its rank.** -/
theorem trace_eq_finrank_range_of_isIdempotentElem {V : Type*} [AddCommGroup V] [Module K V]
    [FiniteDimensional K V] (P : Module.End K V) (h : IsIdempotentElem P) :
    LinearMap.trace K V P = (Module.finrank K (LinearMap.range P) : K) :=
  (LinearMap.IsIdempotentElem.isProj_range P h).trace

end Abstract

section Action

variable {K : Type*} [Field K] {d : ℕ} [NeZero d]

/-- The Hecke action on `HW_μ`, as an algebra map. -/
noncomputable def hwAct (q : K) (hq : q ≠ 0) (m : ℕ) (μ : Fin d → ℕ) :
    Hecke K q q⁻¹ m →ₐ[K] Module.End K (hwSpace q m μ) where
  toFun z := (Matrix.mulVecLin (jimbo d q hq m z)).restrict fun _ hv =>
    mulVec_mem_hwSpace (jimbo_mem_commutant q hq m z) hv
  map_one' := LinearMap.ext fun v => Subtype.ext (by simp)
  map_mul' x y := LinearMap.ext fun v => Subtype.ext (by simp [Matrix.mulVec_mulVec])
  map_zero' := LinearMap.ext fun v => Subtype.ext (by simp)
  map_add' x y := LinearMap.ext fun v => Subtype.ext (by simp)
  commutes' r := LinearMap.ext fun v => Subtype.ext (by
    simp [Algebra.algebraMap_eq_smul_one])

omit [NeZero d] in
theorem hwTrace_eq_trace_hwAct (q : K) (hq : q ≠ 0) (m : ℕ) (μ : Fin d → ℕ)
    (z : Hecke K q q⁻¹ m) :
    hwTrace q hq m μ z = LinearMap.trace K _ (hwAct q hq m μ z) := rfl

end Action

section Specht

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L] {d : ℕ} [NeZero d]

open QOU.Mathlib (StandardYoungTableau partitionShape)
open QOU.SchurWeyl.SeminormalRep

omit [LinearOrder L] [IsStrictOrderedRing L] [NeZero d] in
/-- A nonzero highest-weight space has an occurring weight. -/
theorem mem_occWeights_of_ne_bot {q : L} {m : ℕ} {μ : Fin d → ℕ} (h : hwSpace q m μ ≠ ⊥) :
    μ ∈ occWeights d m := by
  obtain ⟨v, hv, hv0⟩ := Submodule.exists_mem_ne_zero_of_ne_bot h
  obtain ⟨a, ha⟩ : ∃ a, v a ≠ 0 := by
    by_contra hh; push_neg at hh; exact hv0 (funext hh)
  have h1 := congrFun hv.1 a
  rw [weightProj_mulVec_apply] at h1
  split_ifs at h1 with hc
  · exact Finset.mem_image.mpr ⟨a, Finset.mem_univ _, hc⟩
  · exact absurd h1.symm ha

/-- **Density**, as surjectivity of the action map onto `End(HW_μ)`. -/
theorem hwAct_surjective (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    (m : ℕ) {μ : Fin d → ℕ} (hμ : μ ∈ occWeights d m) :
    Function.Surjective (hwAct (d := d) q hq m μ) := by
  intro f
  obtain ⟨x, hx, -⟩ := exists_jimbo_restrict_eq q hq hgen m ⟨μ, hμ⟩ f
  exact ⟨x, LinearMap.ext fun v => Subtype.ext (hx v.1 v.2 v.2)⟩

/-- **A nonzero `HW_μ` sees exactly one Wedderburn block.**  There is a partition `π ⊢ m + 1`
and a scalar `c` such that the block map `A ↦ ρ(W⁻¹(A_π))` is onto `End(HW_μ)`, its trace is
`c · tr A`, and `tr(z | HW_μ) = c · χ^π(z)`. -/
theorem exists_hwBlock (q : L) (hq : q ≠ 0)
    (hgen : GenericParameter.NotRootOfUnity q) (m : ℕ) (μ : Fin d → ℕ)
    (hne : hwSpace q m μ ≠ ⊥) :
    ∃ (π : Partition (m + 1)) (c : L),
      (∀ z : Hecke L q q⁻¹ m, hwTrace q hq m μ z
        = c * (seminormalRep q hq hgen m (partitionShape_card_succ π) z).trace) ∧
      (∀ A, LinearMap.trace L _
          (hwAct (d := d) q hq m μ ((heckeWedderburn q hq hgen m).symm (Pi.single π A)))
        = c * A.trace) ∧
      Function.Surjective (fun A => hwAct (d := d) q hq m μ
        ((heckeWedderburn q hq hgen m).symm (Pi.single π A))) := by
  set W := heckeWedderburn q hq hgen m with hW
  set ρ := hwAct (d := d) q hq m μ with hρ
  have hsurj := hwAct_surjective q hq hgen m (mem_occWeights_of_ne_bot hne)
  let e : Partition (m + 1) → Hecke L q q⁻¹ m := fun π => W.symm (Pi.single π 1)
  have hWe : ∀ π, W (e π) = Pi.single π 1 := fun π => W.apply_symm_apply _
  have he_idem : ∀ π, IsIdempotentElem (e π) := fun π => W.injective (by
    rw [map_mul, hWe, ← Pi.single_mul, one_mul])
  have hcen : ∀ π x, e π * x = x * e π := fun π x => W.injective (by
    rw [map_mul, map_mul, hWe]; funext lam
    simp only [Pi.mul_apply]
    by_cases h : lam = π
    · subst h; simp
    · simp [Pi.single_eq_of_ne h])
  have hsum : ∑ π, e π = 1 := W.injective (by
    rw [map_sum, map_one]; simp only [hWe]
    simpa using Finset.univ_sum_single
      (1 : ∀ lam : Partition (m + 1), Matrix (StandardYoungTableau (partitionShape lam))
        (StandardYoungTableau (partitionShape lam)) L))
  have hdich : ∀ π, ρ (e π) = 0 ∨ ρ (e π) = 1 := fun π =>
    eq_zero_or_one_of_isIdempotentElem_of_comm _ ((he_idem π).map ρ) fun f => by
      obtain ⟨x, rfl⟩ := hsurj f
      rw [← map_mul, ← map_mul, hcen]
  obtain ⟨π, hπ⟩ : ∃ π, ρ (e π) = 1 := by
    by_contra hh; push_neg at hh
    have h0 : ρ 1 = 0 := by
      rw [← hsum, map_sum]
      exact Finset.sum_eq_zero fun π _ => (hdich π).resolve_right (hh π)
    obtain ⟨v, hv, hv0⟩ := Submodule.exists_mem_ne_zero_of_ne_bot hne
    have := congrArg (fun g : Module.End L (hwSpace q m μ) =>
      ((g ⟨v, hv⟩ : hwSpace q m μ) : (Fin (m + 1) → Fin d) → L)) h0
    simp only [map_one, Module.End.one_apply, LinearMap.zero_apply,
      Submodule.coe_zero] at this
    exact hv0 this
  let τ : Matrix (StandardYoungTableau (partitionShape π))
      (StandardYoungTableau (partitionShape π)) L →ₗ[L] L :=
    LinearMap.trace L _ ∘ₗ ρ.toLinearMap ∘ₗ W.symm.toLinearMap ∘ₗ
      LinearMap.single L (fun lam : Partition (m + 1) =>
        Matrix (StandardYoungTableau (partitionShape lam))
          (StandardYoungTableau (partitionShape lam)) L) π
  have hτ : ∀ A, τ A = LinearMap.trace L _ (ρ (W.symm (Pi.single π A))) := fun _ => rfl
  obtain ⟨c, hc⟩ := exists_eq_mul_trace_of_comm τ fun A B => by
    rw [hτ, hτ, Pi.single_mul, map_mul, map_mul, LinearMap.trace_mul_comm,
      ← map_mul, ← map_mul, ← Pi.single_mul]
  have hez : ∀ z, e π * z = W.symm (Pi.single π (W z π)) := fun z => W.injective (by
    rw [map_mul, hWe, W.apply_symm_apply]; funext lam
    simp only [Pi.mul_apply]
    by_cases h : lam = π
    · subst h; simp
    · simp [Pi.single_eq_of_ne h])
  have hρz : ∀ z, ρ z = ρ (e π * z) := fun z => by rw [map_mul, hπ, one_mul]
  refine ⟨π, c, fun z => ?_, fun A => by rw [← hτ, hc], fun f => ?_⟩
  · rw [hwTrace_eq_trace_hwAct, ← hρ, hρz, hez, ← hτ, hc]
    rfl
  · obtain ⟨x, rfl⟩ := hsurj f
    exact ⟨W x π, by show ρ _ = ρ x; rw [hρz x, hez]⟩

/-- **A nonzero `HW_μ` carries a single seminormal character**, up to a scalar:
`tr(z | HW_μ) = c · χ^π(z)` for one partition `π ⊢ m + 1` and one `c`. -/
theorem exists_hwTrace_eq_mul_trace (q : L) (hq : q ≠ 0)
    (hgen : GenericParameter.NotRootOfUnity q) (m : ℕ) (μ : Fin d → ℕ)
    (hne : hwSpace q m μ ≠ ⊥) :
    ∃ (π : Partition (m + 1)) (c : L), ∀ z : Hecke L q q⁻¹ m,
      hwTrace q hq m μ z
        = c * (seminormalRep q hq hgen m (partitionShape_card_succ π) z).trace := by
  obtain ⟨π, c, h, -⟩ := exists_hwBlock q hq hgen m μ hne
  exact ⟨π, c, h⟩

/-- **The scalar is `1`: a nonzero `HW_μ` carries exactly one seminormal character.**
`tr(z | HW_μ) = χ^π(z)` for one partition `π ⊢ m + 1`.

The trace of the block map on a matrix unit `E_{TT}` is the rank `k` of an idempotent, so
`c = k ∈ ℕ`.  Evaluating at `z = 1` gives `dim HW_μ = k · f^π`, and surjectivity of the block
map gives `(dim HW_μ)² ≤ (f^π)²`; since `dim HW_μ > 0`, `k = 1`. -/
theorem exists_hwTrace_eq_trace (q : L) (hq : q ≠ 0)
    (hgen : GenericParameter.NotRootOfUnity q) (m : ℕ) (μ : Fin d → ℕ)
    (hne : hwSpace q m μ ≠ ⊥) :
    ∃ π : Partition (m + 1), ∀ z : Hecke L q q⁻¹ m,
      hwTrace q hq m μ z
        = (seminormalRep q hq hgen m (partitionShape_card_succ π) z).trace := by
  obtain ⟨π, c, hz, hblock, hsurj⟩ := exists_hwBlock q hq hgen m μ hne
  set W := heckeWedderburn q hq hgen m
  set ρ := hwAct (d := d) q hq m μ
  set S := StandardYoungTableau (partitionShape π)
  have hf0 : 0 < Fintype.card S := by
    rw [← Nat.card_eq_fintype_card]; exact QOU.Mathlib.numStandardYoungTableaux_pos _
  obtain ⟨T0⟩ := Fintype.card_pos_iff.mp hf0
  -- `c` is the rank of an idempotent
  set E : Matrix S S L := Matrix.single T0 T0 1
  set P := ρ (W.symm (Pi.single π E))
  have hP : IsIdempotentElem P := by
    show P * P = P
    rw [← map_mul, ← map_mul, ← Pi.single_mul, single_mul_single_same, one_mul]
  have hk : c = (Module.finrank L (LinearMap.range P) : L) := by
    have h1 := hblock E
    rw [trace_single_eq_same, mul_one] at h1
    rw [← h1]
    exact trace_eq_finrank_range_of_isIdempotentElem P hP
  set k := Module.finrank L (LinearMap.range P)
  set n := Module.finrank L (hwSpace q m μ)
  set f := Fintype.card S
  -- `n = k · f`
  have hnkf : n = k * f := by
    have h1 := hz 1
    rw [hwTrace_eq_trace_hwAct, map_one, LinearMap.trace_one, map_one, Matrix.trace_one,
      hk] at h1
    exact_mod_cast h1
  -- `n² ≤ f²`
  have hle : n * n ≤ f * f := by
    let B : Matrix S S L →ₗ[L] Module.End L (hwSpace q m μ) :=
      ρ.toLinearMap ∘ₗ W.symm.toLinearMap ∘ₗ
        LinearMap.single L (fun lam : Partition (m + 1) =>
          Matrix (StandardYoungTableau (partitionShape lam))
            (StandardYoungTableau (partitionShape lam)) L) π
    have hB : Function.Surjective B := hsurj
    have := LinearMap.finrank_range_le B
    rw [LinearMap.range_eq_top.mpr hB, finrank_top, Module.finrank_linearMap,
      Module.finrank_matrix, Module.finrank_self, mul_one] at this
    exact this
  have hn0 : 0 < n := Nat.pos_of_ne_zero fun h => hne (Submodule.finrank_eq_zero.mp h)
  have hk1 : k = 1 := by
    rw [hnkf] at hle hn0
    have hk0 : 0 < k := Nat.pos_of_mul_pos_right hn0
    by_contra hne1
    have : 2 ≤ k := by omega
    have : 2 * f ≤ k * f := Nat.mul_le_mul_right f this
    nlinarith
  refine ⟨π, fun z => ?_⟩
  rw [hz, hk, hk1, Nat.cast_one, one_mul]

end Specht

end QOU.SchurWeyl.QuantumGL
