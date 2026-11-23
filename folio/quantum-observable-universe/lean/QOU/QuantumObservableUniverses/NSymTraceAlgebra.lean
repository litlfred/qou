import QOU.QuantumObservableUniverses.HiggsVacuumResidual
import Mathlib.CategoryTheory.Preadditive.Biproducts
import Mathlib.Tactic.Ring

/-!
# QOU.QuantumObservableUniverses.NSymTraceAlgebra — what `tr_F(e_sym^EW · e_H)` can be

Content block: `conj:g-action-on-substrate`
(`quantum-observable-universes/g-action-on-substrate.md`), section
"The closed form for 𝒩_sym(q): an open identification".

The block writes `𝒩_sym = tr_F(e_sym^EW · e_H)` and records two readings of the
host. This file proves what the trace algebra allows, for any additive,
`K`-homogeneous, cyclic trace (`CyclicTrace`, from `HiggsVacuumResidual.lean`) on a
`K`-linear category, `K` a field (§7c: no archimedean input).

* **Direct sums.** `tr (𝟙 (X ⊞ Y)) = tr (𝟙 X) + tr (𝟙 Y)`
  (`CyclicTrace.tr_id_biprod`), derived from cyclicity alone. An endomorphism
  supported on one summand keeps its trace (`tr_onLeft`, `tr_onRight`), and two
  endomorphisms supported on different summands compose to `0`, so the trace of
  their composite is `0` (`onLeft_comp_onRight`, `tr_onLeft_comp_onRight`).

* **The composite with `e_H`.** For a vacuum point / copoint pair through `U`
  (`e_H = t⁻¹ • (ϱ* ≫ ϱ)`) and any endomorphism `f` of the same object with
  `ϱ ≫ f ≫ ϱ* = s • 𝟙 U`, `tr (f ≫ e_H) = t⁻¹ * s * tr (𝟙 U)`
  (`PointCopoint.tr_comp_proj`): the vacuum matrix element of `f`, independent of
  `tr (𝟙 X)`. If `f` is an idempotent commuting with `e_H` and `𝟙 U ≠ 0`, then
  `s = 0` or `s = t` (`PointCopoint.vacuum_coeff_dichotomy`), so
  `tr (f ≫ e_H) ∈ {0, tr (𝟙 U)}`, which is `{0, 1}` for the Higgs datum with a
  unit-normalised trace (`VacuumPairing.tr_comp_proj_zero_or_one`).

* **Tensor products.** For a trace that is in addition multiplicative on `⊗`
  (`MonoidalCyclicTrace`, a hypothesis, which `Matrix.trace` satisfies via
  `Matrix.trace_kronecker`), `tr (𝟙 (X ⊗ Y)) = tr (𝟙 X) * tr (𝟙 Y)` and, for the
  unit-normalised Higgs datum, `tr (f ⊗ e_H) = tr f`
  (`VacuumPairing.tr_tensor_proj`).

Consequence (stated in the write-up
`docs/audits/2026-11-20-nsym-host-trace-route.md`, proved here only in the form
above): read as a composite, `tr_F(e_sym^EW · e_H)` is a vacuum expectation
value and lies in `{0, 1}` whenever the two idempotents commute; it is never a
product or a sum of host `q`-dimensions. A `q`-dimension of the electroweak image
arises only from the tensor reading, and then it equals `tr_F(e_sym^EW)`, whose
value is additive or multiplicative according to whether the electroweak host is
a direct sum or a tensor product. That second choice is not decided here.

The trace is a hypothesis; the pivotal trace of `Rep(SU_q(2))` is not constructed.
-/

namespace QOU.QuantumObservableUniverses

open CategoryTheory CategoryTheory.Limits CategoryTheory.MonoidalCategory

universe v u

section Biprod

variable {K : Type*} [Field K] {C : Type u} [Category.{v} C] [Preadditive C] [Linear K C]
variable (T : CyclicTrace K C)

namespace CyclicTrace

theorem tr_zero {Y : C} : T.tr (0 : Y ⟶ Y) = 0 := by
  have h := T.tr_smul (0 : K) (0 : Y ⟶ Y)
  rwa [zero_smul, zero_mul] at h

/-- `dim` is additive on biproducts, from cyclicity alone. -/
theorem tr_id_biprod (X Y : C) [HasBinaryBiproduct X Y] :
    T.tr (𝟙 (X ⊞ Y)) = T.tr (𝟙 X) + T.tr (𝟙 Y) := by
  rw [← biprod.total, T.tr_add, T.tr_comp_comm biprod.fst biprod.inl,
    T.tr_comp_comm biprod.snd biprod.inr, biprod.inl_fst, biprod.inr_snd]

end CyclicTrace

variable {X Y : C} [HasBinaryBiproduct X Y]

/-- An endomorphism of `X`, extended by `0` to `X ⊞ Y`. -/
noncomputable def onLeft (e : X ⟶ X) : X ⊞ Y ⟶ X ⊞ Y := biprod.fst ≫ e ≫ biprod.inl

/-- An endomorphism of `Y`, extended by `0` to `X ⊞ Y`. -/
noncomputable def onRight (e : Y ⟶ Y) : X ⊞ Y ⟶ X ⊞ Y := biprod.snd ≫ e ≫ biprod.inr

theorem tr_onLeft (e : X ⟶ X) : T.tr (onLeft (Y := Y) e) = T.tr e := by
  unfold onLeft
  rw [T.tr_comp_comm, Category.assoc, biprod.inl_fst, Category.comp_id]

theorem tr_onRight (e : Y ⟶ Y) : T.tr (onRight (X := X) e) = T.tr e := by
  unfold onRight
  rw [T.tr_comp_comm, Category.assoc, biprod.inr_snd, Category.comp_id]

/-- Endomorphisms supported on different summands compose to `0`. -/
theorem onLeft_comp_onRight (e : X ⟶ X) (e' : Y ⟶ Y) :
    onLeft (Y := Y) e ≫ onRight (X := X) e' = 0 := by
  simp [onLeft, onRight]

/-- **Direct-sum reading.** The composite trace of endomorphisms (in particular
idempotents) on different summands is `0`, whatever their own traces are. -/
theorem tr_onLeft_comp_onRight (e : X ⟶ X) (e' : Y ⟶ Y) :
    T.tr (onLeft (Y := Y) e ≫ onRight (X := X) e') = 0 := by
  rw [onLeft_comp_onRight, CyclicTrace.tr_zero]

end Biprod

section Vacuum

variable {K : Type*} [Field K] {C : Type u} [Category.{v} C] [Preadditive C] [Linear K C]
variable (T : CyclicTrace K C)

namespace PointCopoint

variable {U X : C} (P : PointCopoint K U X)

/-- **Composite reading.** `tr (f ≫ e_H)` is the vacuum matrix element of `f`
times `t⁻¹ tr (𝟙 U)`; `tr (𝟙 X)` does not enter. -/
theorem tr_comp_proj (f : X ⟶ X) (s : K) (hs : P.pt ≫ f ≫ P.copt = s • 𝟙 U) :
    T.tr (f ≫ P.proj) = P.scalar⁻¹ * s * T.tr (𝟙 U) := by
  unfold proj
  rw [Linear.comp_smul, T.tr_smul, ← Category.assoc, T.tr_comp_comm, ← Category.assoc,
    Category.assoc, hs, T.tr_smul, mul_assoc]

theorem pt_ne_zero (hU : (𝟙 U : U ⟶ U) ≠ 0) : P.pt ≠ 0 := by
  intro h
  have := P.pt_comp_copt
  rw [h, zero_comp] at this
  exact hU ((smul_eq_zero.mp this.symm).resolve_left P.scalar_ne_zero)

theorem proj_ne_zero (hU : (𝟙 U : U ⟶ U) ≠ 0) : P.proj ≠ 0 := by
  intro h
  have := P.pt_comp_proj
  rw [h, comp_zero] at this
  exact P.pt_ne_zero hU this.symm

/-- **Dichotomy.** If `f` is idempotent, commutes with `e_H`, and has vacuum
matrix element `s`, then `s = 0` or `s = t`. -/
theorem vacuum_coeff_dichotomy (hU : (𝟙 U : U ⟶ U) ≠ 0) (f : X ⟶ X) (hf : f ≫ f = f)
    (hc : f ≫ P.proj = P.proj ≫ f) (s : K) (hs : P.pt ≫ f ≫ P.copt = s • 𝟙 U) :
    s = 0 ∨ s = P.scalar := by
  have ht : P.scalar ≠ 0 := P.scalar_ne_zero
  -- `e_H ≫ f ≫ e_H = (t⁻¹ s) • e_H`.
  have hsand : P.proj ≫ f ≫ P.proj = (P.scalar⁻¹ * s) • P.proj := by
    simp only [proj, Linear.smul_comp, Linear.comp_smul, Category.assoc, smul_smul]
    have : P.copt ≫ P.pt ≫ f ≫ P.copt ≫ P.pt = s • (P.copt ≫ P.pt) := by
      rw [← Category.assoc P.pt, ← Category.assoc (P.pt ≫ f), Category.assoc P.pt, hs]
      simp
    rw [this, smul_smul]
    congr 1
    ring
  -- `f ≫ e_H` is idempotent and equals `e_H ≫ f ≫ e_H`.
  have hfe : f ≫ P.proj = P.proj ≫ f ≫ P.proj := by
    rw [← Category.assoc, ← hc, Category.assoc, P.proj_idem]
  have hidem : (f ≫ P.proj) ≫ (f ≫ P.proj) = f ≫ P.proj := by
    rw [Category.assoc, ← Category.assoc P.proj, ← hc, Category.assoc, P.proj_idem,
      ← Category.assoc, hf]
  rw [hfe, hsand, Linear.smul_comp, Linear.comp_smul, P.proj_idem, smul_smul] at hidem
  have h0 : ((P.scalar⁻¹ * s) * (P.scalar⁻¹ * s) - P.scalar⁻¹ * s) • P.proj = 0 := by
    rw [sub_smul, hidem, sub_self]
  have ha := (smul_eq_zero.mp h0).resolve_right (P.proj_ne_zero hU)
  have ha' : (P.scalar⁻¹ * s) * ((P.scalar⁻¹ * s) - 1) = 0 := by rw [mul_sub, mul_one]; exact ha
  rcases mul_eq_zero.mp ha' with h | h
  · left
    rcases mul_eq_zero.mp h with h | h
    · exact absurd (inv_eq_zero.mp h) ht
    · exact h
  · right
    have h' : P.scalar⁻¹ * s = 1 := sub_eq_zero.mp h
    calc s = P.scalar * (P.scalar⁻¹ * s) := by rw [← mul_assoc, mul_inv_cancel₀ ht, one_mul]
      _ = P.scalar := by rw [h', mul_one]

/-- **Composite reading, value.** For a commuting idempotent,
`tr (f ≫ e_H) ∈ {0, tr (𝟙 U)}`. -/
theorem tr_comp_proj_dichotomy (hU : (𝟙 U : U ⟶ U) ≠ 0) (f : X ⟶ X) (hf : f ≫ f = f)
    (hc : f ≫ P.proj = P.proj ≫ f) (s : K) (hs : P.pt ≫ f ≫ P.copt = s • 𝟙 U) :
    T.tr (f ≫ P.proj) = 0 ∨ T.tr (f ≫ P.proj) = T.tr (𝟙 U) := by
  rw [P.tr_comp_proj T f s hs]
  rcases P.vacuum_coeff_dichotomy hU f hf hc s hs with h | h
  · left; rw [h, mul_zero, zero_mul]
  · right; rw [h, inv_mul_cancel₀ P.scalar_ne_zero, one_mul]

end PointCopoint

/-- **Higgs case.** With a unit-normalised trace, the composite reading of
`tr_F(e_sym · e_H)` takes the value `0` or `1` for every idempotent `e_sym`
commuting with `e_H`. -/
theorem VacuumPairing.tr_comp_proj_zero_or_one [MonoidalCategory C] {X : C}
    (P : VacuumPairing K X) (h1 : T.tr (𝟙 (𝟙_ C)) = 1) (f : X ⟶ X) (hf : f ≫ f = f)
    (hc : f ≫ P.proj = P.proj ≫ f) (s : K) (hs : P.pt ≫ f ≫ P.copt = s • 𝟙 (𝟙_ C)) :
    T.tr (f ≫ P.proj) = 0 ∨ T.tr (f ≫ P.proj) = 1 := by
  have hU : (𝟙 (𝟙_ C) : 𝟙_ C ⟶ 𝟙_ C) ≠ 0 := by
    intro h; rw [h, CyclicTrace.tr_zero] at h1; exact zero_ne_one h1
  rw [← h1]
  exact P.tr_comp_proj_dichotomy T hU f hf hc s hs

end Vacuum

section Tensor

variable (K : Type*) [Field K] (C : Type u) [Category.{v} C] [Preadditive C] [Linear K C]
  [MonoidalCategory C]

/-- A cyclic trace that is multiplicative on `⊗` (the property of the categorical
trace of a spherical `K`-linear category). A hypothesis, not a construction. -/
structure MonoidalCyclicTrace extends CyclicTrace K C where
  /-- Multiplicativity on tensor products of endomorphisms. -/
  tr_tensor : ∀ {Y Z : C} (f : Y ⟶ Y) (g : Z ⟶ Z), tr (f ⊗ₘ g) = tr f * tr g

variable {K C}
variable (T : MonoidalCyclicTrace K C)

/-- `dim` is multiplicative on `⊗`. -/
theorem MonoidalCyclicTrace.tr_id_tensor (X Y : C) :
    T.tr (𝟙 (X ⊗ Y)) = T.tr (𝟙 X) * T.tr (𝟙 Y) := by
  rw [← id_tensorHom_id, T.tr_tensor]

/-- **Tensor reading.** With a unit-normalised trace, `tr (f ⊗ e_H) = tr f`:
the Higgs factor contributes `1`, and the value is the trace of `f` on its own
host. -/
theorem VacuumPairing.tr_tensor_proj {X Y : C} (P : VacuumPairing K X)
    (h1 : T.tr (𝟙 (𝟙_ C)) = 1) (f : Y ⟶ Y) :
    T.tr (f ⊗ₘ P.proj) = T.tr f := by
  rw [T.tr_tensor, VacuumPairing.tr_proj_eq_one P T.toCyclicTrace h1, mul_one]

end Tensor

end QOU.QuantumObservableUniverses
