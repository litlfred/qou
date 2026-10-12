/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.IwahoriHecke.CoxeterCarrierEquiv
import QOU.IwahoriHecke.HeckeColimitTensorTrace
import QOU.MathlibExt.AlgebraTowerColimit

/-!
# The Coxeter-presentation Hecke tower, and its braided Markov trace

Bean `qou-0fmb`, titled *"wire the IwahoriHecke algebra to the BraidedTower theorem"*.

`QOU.IwahoriHecke.CoxeterCarrier.skeinBalancedEquiv` identifies each level of the skein
tower `QOU.SchurWeyl.Hecke K q q⁻¹ n` with the **Coxeter-presentation** Iwahori–Hecke
algebra `HeckeAlgebra K (q*q) (Aₙ n)` (= `Balanced.BalancedHecke (Aₙ n) q`, the algebra
`QOU/IwahoriHecke/` is built on, over Mathlib's `CoxeterMatrix.Aₙ`). It did not supply
what a tower needs: an inclusion between the levels on the Coxeter side. This file
supplies it and transports the braided Markov trace across.

## What is proved (sorry-free)

* `coxIncl Q n : HeckeAlgebra K Q (Aₙ n) →ₐ[K] HeckeAlgebra K Q (Aₙ (n+1))`, `Tᵢ ↦ T_{i}`
  (`castSucc`), by the universal property; the braid clause transfers because the
  `Aₙ` entries depend only on index values (`AMat_castSucc`). Any `CommRing K`, any `Q`.
* `skeinBalancedEquiv_σ` — the equivalence sends `σᵢ ↦ q⁻¹ • Tᵢ`.
* `skeinBalancedEquiv_heckeIncl` — **the inclusions agree**:
  `e_{n+1} ∘ heckeIncl = coxIncl ∘ e_n` (and `skeinBalancedEquiv_inclLE` for the
  iterates).
* `CoxLim q` — the colimit of the Coxeter tower (via `MathlibExt.AlgebraTowerColimit`),
  and `colimEquiv hq : HeckeLim K q q⁻¹ ≃ₐ[K] CoxLim q`, the induced equivalence of
  colimits, with `colimEquiv_ofLim` (it is `e_n` on level `n`).
* Generic: `transportMarkovTrace T e` moves an `OcneanuTrace.MarkovTrace` along an algebra
  equivalence, and `braidedTower_transport` moves the `BraidedTower` instance with it.
* `coxeterMarkovTrace hq hq1 : MarkovTrace K (CoxLim q)` — the tensor-model Markov trace
  of `HeckeColimitTensorTrace`, on the Coxeter tower; `coxeterMarkovTrace_H`
  (`H n` is the image of level `n` of the Coxeter tower), `coxeterMarkovTrace_g`
  (`g n` is the §7a balanced generator `Balanced.sigma = q⁻¹·T_n` at level `n+1`),
  `coxeterMarkovTrace_tr_ofₐ` (on level `n` the trace is the level trace through `e_n⁻¹`),
  `coxeterMarkovTrace_z` (`z = q³/(q²+1)`).
* `braidedTower_coxeter` (`h = q − q⁻¹`), `towerSpan_coxeter`, `disjointBlock_coxeter`.

Hypotheses: `[Field K]`, `q ≠ 0`, `q² + 1 ≠ 0`.

## What is NOT proved here

* Faithfulness (the tensor-model trace is the two-row quotient; not faithful).
* Injectivity of the level maps into `CoxLim` (`H n` is an image).
* Anything about the `Set.univ`-indexed `QOU.IwahoriHecke.Defn.IwahoriHecke` or
  `TypeA.IwahoriHeckeOfSn`; this is the `HeckeAlgebra K Q (Aₙ n)` family only.
-/

namespace QOU.IwahoriHecke.CoxeterTower

open QOU.MathlibExt.IwahoriHecke QOU.IwahoriHecke.CoxeterCarrier
open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.HeckeSandwichReduces
open QOU.MathlibExt.TowerSpanReduction QOU.MathlibExt.DisjointBlockTrace
open QOU.MathlibExt.AlgebraTowerColimit

/-! ## Transporting a Markov trace along an algebra equivalence -/

section Transport

variable {R A B : Type*} [CommRing R] [Ring A] [Algebra R A] [Ring B] [Algebra R B]

/-- A `MarkovTrace` on `A` gives one on any `B ≃ₐ[R] A`-equivalent algebra. -/
noncomputable def transportMarkovTrace (T : MarkovTrace R A) (e : A ≃ₐ[R] B) :
    MarkovTrace R B where
  H n := (T.H n).map e.toAlgHom
  H_mono _ _ h := Subalgebra.map_mono (T.H_mono h)
  g n := e (T.g n)
  g_mem n := Subalgebra.mem_map.mpr ⟨T.g n, T.g_mem n, rfl⟩
  ginv n := e (T.ginv n)
  ginv_mem n := Subalgebra.mem_map.mpr ⟨T.ginv n, T.ginv_mem n, rfl⟩
  ginv_mul n := by rw [← map_mul, T.ginv_mul, map_one]
  mul_ginv n := by rw [← map_mul, T.mul_ginv, map_one]
  tr := T.tr ∘ₗ e.symm.toLinearMap
  tr_mul_comm a b := by
    simp only [LinearMap.coe_comp, Function.comp_apply, AlgEquiv.toLinearMap_apply, map_mul]
    exact T.tr_mul_comm _ _
  tr_one := by
    simp only [LinearMap.coe_comp, Function.comp_apply, AlgEquiv.toLinearMap_apply, map_one]
    exact T.tr_one
  z := T.z
  zinv := T.zinv
  markov n a ha := by
    obtain ⟨a', ha', rfl⟩ := Subalgebra.mem_map.mp ha
    show T.tr (e.symm (e a' * e (T.g n))) = T.z * T.tr (e.symm (e a'))
    rw [← map_mul, AlgEquiv.symm_apply_apply, AlgEquiv.symm_apply_apply]
    exact T.markov n a' ha'
  markov_inv n a ha := by
    obtain ⟨a', ha', rfl⟩ := Subalgebra.mem_map.mp ha
    show T.tr (e.symm (e a' * e (T.ginv n))) = T.zinv * T.tr (e.symm (e a'))
    rw [← map_mul, AlgEquiv.symm_apply_apply, AlgEquiv.symm_apply_apply]
    exact T.markov_inv n a' ha'

/-- The braid-tower relations move along the equivalence. -/
instance braidedTower_transport (T : MarkovTrace R A) (e : A ≃ₐ[R] B) [hbt : BraidedTower T] :
    BraidedTower (transportMarkovTrace T e) where
  quad m := by
    obtain ⟨h, hh⟩ := hbt.quad m
    refine ⟨h, ?_⟩
    show e (T.g m) * e (T.g m) = h • e (T.g m) + 1
    rw [← map_mul, hh, map_add, map_smul, map_one]
  far m k hk := by
    show e (T.g m) * e (T.g k) = e (T.g k) * e (T.g m)
    rw [← map_mul, ← map_mul, hbt.far m k hk]
  braid m := by
    show e (T.g (m + 1)) * e (T.g m) * e (T.g (m + 1)) = e (T.g m) * e (T.g (m + 1)) * e (T.g m)
    rw [← map_mul, ← map_mul, ← map_mul, ← map_mul, hbt.braid m]

end Transport

/-! ## The level inclusion on the Coxeter side -/

/-- The `Aₙ` entries depend only on index values, so they are stable under `castSucc`. -/
theorem AMat_castSucc (n : ℕ) (i j : Fin n) :
    AMat (n + 1) i.castSucc j.castSucc = AMat n i j := by
  simp only [AMat, CoxeterMatrix.Aₙ, Matrix.of_apply, Fin.castSucc_inj, Fin.coe_castSucc]

variable (K : Type*) [CommRing K]

/-- **The Coxeter-side tower map** `HeckeAlgebra K Q (Aₙ n) →ₐ HeckeAlgebra K Q (Aₙ (n+1))`,
`Tᵢ ↦ T_{castSucc i}`. -/
noncomputable def coxIncl (Q : K) (n : ℕ) :
    HeckeAlgebra K Q (AMat n) →ₐ[K] HeckeAlgebra K Q (AMat (n + 1)) :=
  lift K Q (AMat n) (fun i => T K Q (AMat (n + 1)) i.castSucc)
    (fun i => T_quadratic i.castSucc)
    (fun i j => by
      rw [← AMat_castSucc n i j, ← AMat_castSucc n j i]
      exact T_braid i.castSucc j.castSucc)

@[simp] theorem coxIncl_T (Q : K) (n : ℕ) (i : Fin n) :
    coxIncl K Q n (T K Q (AMat n) i) = T K Q (AMat (n + 1)) i.castSucc :=
  lift_T K Q (AMat n) _ _ _ i

/-! ## The inclusions agree under `skeinBalancedEquiv` -/

variable {K}

theorem skeinBalancedEquiv_σ {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (n : ℕ)
    (i : Fin n) :
    skeinBalancedEquiv q hq n (QOU.SchurWeyl.Hecke.σ K q q⁻¹ n i)
      = q⁻¹ • T K (q * q) (AMat n) i := by
  simp only [skeinBalancedEquiv, AlgEquiv.trans_apply, QOU.SchurWeyl.carrierEquiv,
    AlgEquiv.ofAlgHom_apply, QOU.SchurWeyl.toIwahori, QOU.SchurWeyl.Hecke.lift_σ, map_smul,
    coxeterCarrierEquiv_σ]

/-- **The inclusions agree**: `e_{n+1} ∘ heckeIncl = coxIncl ∘ e_n`. -/
theorem skeinBalancedEquiv_heckeIncl {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (n : ℕ)
    (x : QOU.SchurWeyl.Hecke K q q⁻¹ n) :
    skeinBalancedEquiv q hq (n + 1) (QOU.SchurWeyl.HeckeInclusion.heckeIncl K q q⁻¹ n x)
      = coxIncl K (q * q) n (skeinBalancedEquiv q hq n x) := by
  have h : (skeinBalancedEquiv q hq (n + 1)).toAlgHom.comp
        (QOU.SchurWeyl.HeckeInclusion.heckeIncl K q q⁻¹ n)
      = (coxIncl K (q * q) n).comp (skeinBalancedEquiv q hq n).toAlgHom := by
    apply QOU.SchurWeyl.Hecke.hom_ext
    intro i
    simp only [AlgHom.comp_apply, AlgEquiv.toAlgHom_eq_coe, AlgHom.coe_coe,
      QOU.SchurWeyl.HeckeInclusion.heckeIncl_σ, skeinBalancedEquiv_σ, map_smul, coxIncl_T]
  exact AlgHom.congr_fun h x

/-! ## The Coxeter colimit and the equivalence of colimits -/

section Colimit

variable {K : Type*} [Field K] (q : K)

/-- The levels of the Coxeter tower, `HeckeAlgebra K (q*q) (Aₙ n)` (= `BalancedHecke`). -/
abbrev CoxLevel (n : ℕ) : Type _ := HeckeAlgebra K (q * q) (AMat n)

/-- The colimit of the Coxeter-presentation Hecke tower. -/
noncomputable abbrev CoxLim : Type _ :=
  Lim (CoxLevel q) (fun n => coxIncl K (q * q) n)

variable {q}

open QOU.SchurWeyl.HeckeDirectedSystem QOU.SchurWeyl.HeckeColimit in
theorem skeinBalancedEquiv_inclLE (hq : q ≠ 0) (i j : ℕ) (hij : i ≤ j)
    (x : QOU.SchurWeyl.Hecke K q q⁻¹ i) :
    skeinBalancedEquiv q hq j (heckeInclLE K q q⁻¹ i j hij x)
      = inclLE (CoxLevel q) (fun n => coxIncl K (q * q) n) i j hij
          (skeinBalancedEquiv q hq i x) := by
  induction j, hij using Nat.le_induction with
  | base => rw [heckeInclLE_self, inclLE_self]; rfl
  | succ n hn ih =>
      rw [heckeInclLE_succ K q q⁻¹ i n hn, inclLE_succ (CoxLevel q) (fun n => coxIncl K (q * q) n) i n hn, AlgHom.comp_apply,
        AlgHom.comp_apply, skeinBalancedEquiv_heckeIncl, ih]

open QOU.SchurWeyl.HeckeDirectedSystem QOU.SchurWeyl.HeckeColimit in
/-- The forward map of colimits, as a ring map. -/
noncomputable def colimFwd (hq : q ≠ 0) : HeckeLim K q q⁻¹ →+* CoxLim q :=
  DirectLimit.Ring.lift (QOU.SchurWeyl.Hecke K q q⁻¹) (heckeF K q q⁻¹) (CoxLim q)
    (fun i => (ofₐ (CoxLevel q) (fun n => coxIncl K (q * q) n) i).toRingHom.comp
      (skeinBalancedEquiv q hq i).toRingEquiv.toRingHom)
    (fun i j hij x => by
      show ofₐ (CoxLevel q) (fun n => coxIncl K (q * q) n) j
          (skeinBalancedEquiv q hq j (heckeInclLE K q q⁻¹ i j hij x))
        = ofₐ (CoxLevel q) (fun n => coxIncl K (q * q) n) i (skeinBalancedEquiv q hq i x)
      rw [skeinBalancedEquiv_inclLE, ofₐ_comp])

open QOU.SchurWeyl.HeckeDirectedSystem QOU.SchurWeyl.HeckeColimit in
/-- The backward map of colimits, as a ring map. -/
noncomputable def colimBwd (hq : q ≠ 0) : CoxLim q →+* HeckeLim K q q⁻¹ :=
  DirectLimit.Ring.lift (CoxLevel q) (inclLE (CoxLevel q) (fun n => coxIncl K (q * q) n))
    (HeckeLim K q q⁻¹)
    (fun i => (ofLimₐ K q q⁻¹ i).toRingHom.comp
      (skeinBalancedEquiv q hq i).symm.toRingEquiv.toRingHom)
    (fun i j hij y => by
      show ofLimₐ K q q⁻¹ j ((skeinBalancedEquiv q hq j).symm
          (inclLE (CoxLevel q) (fun n => coxIncl K (q * q) n) i j hij y))
        = ofLimₐ K q q⁻¹ i ((skeinBalancedEquiv q hq i).symm y)
      have h := skeinBalancedEquiv_inclLE hq i j hij ((skeinBalancedEquiv q hq i).symm y)
      rw [AlgEquiv.apply_symm_apply] at h
      rw [← h, AlgEquiv.symm_apply_apply, ofLimₐ_comp])

open QOU.SchurWeyl.HeckeColimit in
theorem colimFwd_ofLim (hq : q ≠ 0) (n : ℕ) (x : QOU.SchurWeyl.Hecke K q q⁻¹ n) :
    colimFwd hq (ofLimₐ K q q⁻¹ n x)
      = ofₐ (CoxLevel q) (fun n => coxIncl K (q * q) n) n (skeinBalancedEquiv q hq n x) :=
  rfl

open QOU.SchurWeyl.HeckeColimit in
theorem colimBwd_ofₐ (hq : q ≠ 0) (n : ℕ) (y : CoxLevel q n) :
    colimBwd hq (ofₐ (CoxLevel q) (fun n => coxIncl K (q * q) n) n y)
      = ofLimₐ K q q⁻¹ n ((skeinBalancedEquiv q hq n).symm y) :=
  rfl

open QOU.SchurWeyl.HeckeColimit in
/-- **The colimit of the skein tower is the colimit of the Coxeter tower.** -/
noncomputable def colimEquiv (hq : q ≠ 0) : HeckeLim K q q⁻¹ ≃ₐ[K] CoxLim q :=
  AlgEquiv.ofAlgHom
    (AlgHom.mk' (colimFwd hq) (fun c x => by
      induction x using DirectLimit.induction (f := heckeF K q q⁻¹) with
      | ih i x =>
        show colimFwd hq (c • ofLimₐ K q q⁻¹ i x) = c • colimFwd hq (ofLimₐ K q q⁻¹ i x)
        rw [← map_smul, colimFwd_ofLim, colimFwd_ofLim, map_smul, map_smul]))
    (AlgHom.mk' (colimBwd hq) (fun c y => by
      induction y using DirectLimit.induction
          (f := inclLE (CoxLevel q) (fun n => coxIncl K (q * q) n)) with
      | ih i y =>
        show colimBwd hq (c • ofₐ (CoxLevel q) (fun n => coxIncl K (q * q) n) i y)
          = c • colimBwd hq (ofₐ (CoxLevel q) (fun n => coxIncl K (q * q) n) i y)
        rw [← map_smul, colimBwd_ofₐ, colimBwd_ofₐ, map_smul, map_smul]))
    (by
      apply AlgHom.ext
      intro y
      induction y using DirectLimit.induction
          (f := inclLE (CoxLevel q) (fun n => coxIncl K (q * q) n)) with
      | ih i y =>
        show colimFwd hq (colimBwd hq (ofₐ (CoxLevel q) (fun n => coxIncl K (q * q) n) i y))
          = ofₐ (CoxLevel q) (fun n => coxIncl K (q * q) n) i y
        rw [colimBwd_ofₐ, colimFwd_ofLim, AlgEquiv.apply_symm_apply])
    (by
      apply AlgHom.ext
      intro x
      induction x using DirectLimit.induction (f := heckeF K q q⁻¹) with
      | ih i x =>
        show colimBwd hq (colimFwd hq (ofLimₐ K q q⁻¹ i x)) = ofLimₐ K q q⁻¹ i x
        rw [colimFwd_ofLim, colimBwd_ofₐ, AlgEquiv.symm_apply_apply])

open QOU.SchurWeyl.HeckeColimit in
@[simp] theorem colimEquiv_ofLim (hq : q ≠ 0) (n : ℕ) (x : QOU.SchurWeyl.Hecke K q q⁻¹ n) :
    colimEquiv hq (ofLimₐ K q q⁻¹ n x)
      = ofₐ (CoxLevel q) (fun n => coxIncl K (q * q) n) n (skeinBalancedEquiv q hq n x) :=
  rfl

end Colimit

/-! ## The braided Markov trace on the Coxeter tower -/

section Trace

open QOU.IwahoriHecke.HeckeColimitTensorTrace QOU.SchurWeyl.HeckeColimit

variable {K : Type*} [Field K] {q : K} (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0)

/-- **The Ocneanu (tensor-model) Markov trace on the Coxeter-presentation Hecke tower.** -/
noncomputable def coxeterMarkovTrace : MarkovTrace K (CoxLim q) :=
  transportMarkovTrace (tensorColimitMarkovTrace hq hq1) (colimEquiv hq)

instance braidedTower_coxeter : BraidedTower (coxeterMarkovTrace hq hq1) :=
  braidedTower_transport _ _

/-- `H n` is the image of level `n` of the **Coxeter** tower. -/
theorem coxeterMarkovTrace_H (n : ℕ) :
    (coxeterMarkovTrace hq hq1).H n
      = (ofₐ (CoxLevel q) (fun n => coxIncl K (q * q) n) n).range := by
  ext y
  constructor
  · intro hy
    obtain ⟨a, ⟨x, rfl⟩, rfl⟩ := Subalgebra.mem_map.mp hy
    exact ⟨skeinBalancedEquiv q hq n x, (colimEquiv_ofLim hq n x).symm⟩
  · rintro ⟨y, rfl⟩
    refine Subalgebra.mem_map.mpr ⟨ofLimₐ K q q⁻¹ n ((skeinBalancedEquiv q hq n).symm y),
      ⟨_, rfl⟩, ?_⟩
    show colimEquiv hq (ofLimₐ K q q⁻¹ n ((skeinBalancedEquiv q hq n).symm y)) = _
    rw [colimEquiv_ofLim, AlgEquiv.apply_symm_apply]
    rfl

/-- `g n` is the §7a balanced generator `σ_n = q⁻¹·T_n` of `HeckeAlgebra K (q*q) (Aₙ (n+1))`. -/
theorem coxeterMarkovTrace_g (n : ℕ) :
    (coxeterMarkovTrace hq hq1).g n
      = ofₐ (CoxLevel q) (fun n => coxIncl K (q * q) n) (n + 1)
          (Balanced.sigma (AMat (n + 1)) q q⁻¹ ⟨n, Nat.lt_succ_self n⟩) := by
  show colimEquiv hq (gLim K q q⁻¹ n) = _
  rw [gLim, colimEquiv_ofLim, skeinBalancedEquiv_σ, Balanced.sigma, Algebra.smul_def]

/-- On level `n` of the Coxeter tower the trace is the level trace pulled back along `e_n`. -/
theorem coxeterMarkovTrace_tr_ofₐ (n : ℕ) (y : CoxLevel q n) :
    (coxeterMarkovTrace hq hq1).tr (ofₐ (CoxLevel q) (fun n => coxIncl K (q * q) n) n y)
      = levelTrace hq n ((skeinBalancedEquiv q hq n).symm y) := by
  show trT hq hq1 ((colimEquiv hq).symm (ofₐ _ _ n y)) = _
  have : (colimEquiv hq).symm (ofₐ (CoxLevel q) (fun n => coxIncl K (q * q) n) n y)
      = ofLimₐ K q q⁻¹ n ((skeinBalancedEquiv q hq n).symm y) := by
    rw [AlgEquiv.symm_apply_eq, colimEquiv_ofLim, AlgEquiv.apply_symm_apply]
  rw [this, trT_ofLim]

theorem coxeterMarkovTrace_z :
    (coxeterMarkovTrace hq hq1).z = q ^ 3 / (q ^ 2 + 1) := rfl

/-- **`TowerSpan`** on the Coxeter-presentation Hecke tower. -/
theorem towerSpan_coxeter : TowerSpan (coxeterMarkovTrace hq hq1) :=
  towerSpan_of_braided _

/-- **The disjoint-block trace law** on the Coxeter-presentation Hecke tower. -/
theorem disjointBlock_coxeter : DisjointBlockMultiplicative (coxeterMarkovTrace hq hq1) :=
  disjointBlock_of_braided _

end Trace

end QOU.IwahoriHecke.CoxeterTower
