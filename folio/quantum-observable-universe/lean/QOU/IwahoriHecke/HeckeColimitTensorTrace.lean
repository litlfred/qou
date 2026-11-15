/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.HeckeColimit
import QOU.IwahoriHecke.TensorMarkovModel
import QOU.MathlibExt.OcneanuTrace
import QOU.MathlibExt.HeckeSandwichReduces

/-!
# The tensor-model Markov trace on the Hecke colimit, over any field

Bean `qou-0fmb` ("wire the `IwahoriHecke` algebra to the `BraidedTower` theorem").

`QOU.SchurWeyl.HeckeColimitMarkovTrace` already builds a `MarkovTrace` on the colimit
`HeckeLim K q q⁻¹` of the type-`A` Hecke tower, but only over `ℝ` and only for
`q` not a root of unity: its trace is `MarkovTraceInstance.wtrace`, a weighted sum of
seminormal characters, whose construction needs semisimplicity.

This file builds a **second** trace on the **same** carrier, over an arbitrary field `K`,
from `QOU.IwahoriHecke.TensorMarkovModel`: the normalised quantum trace
`τ_N(x) = (1+q²)^{-(N+1)} tr(W x)` on the centraliser of the site weight in
`End(V^{⊗(N+1)})`, `dim V = 2`. Its only hypotheses are `q ≠ 0` and `q² + 1 ≠ 0`; no
genericity, no ordering, no `ℝ`.

## What is proved (sorry-free)

* `toModel n : Hecke K q q⁻¹ n →ₐ[K] TensorMarkovModel.A q n` — the Hecke algebra maps
  to the tensor model, `σᵢ ↦ sᵢ` (universal property `Hecke.lift`, relations from
  `sA_heckeFamily`).
* `levelTrace n := τ_n ∘ toModel n`, with `levelTrace_one`, `levelTrace_cyc`,
  `levelTrace_markov` (Markov at every intermediate level `k < n`, with
  `z = zD q = q³/(q²+1)`).
* `levelTrace_incl` — **tower compatibility**,
  `levelTrace (n+1) (heckeIncl x) = levelTrace n x`. Proved by **uniqueness**
  (`JonesNormalForm.markov_unique_of_adjoin_eq_top`): both sides are normalised cyclic
  Markov traces on `Hecke K q q⁻¹ n` with the same `z`. No matrix computation.
* `trT` — the trace on the colimit (`DirectLimit.Module.lift`), with `trT_one`,
  `trT_cyclic`, `trT_markov`, `trT_markov_inv` (`zinv = zD q − (q − q⁻¹)`, derived from
  `σ⁻¹ = σ − (q − q⁻¹)·1`).
* `tensorColimitMarkovTrace : MarkovTrace K (HeckeLim K q q⁻¹)`.
* `braidedTower_tensorColimit` — the `BraidedTower` instance (`quad` with
  `h = q − q⁻¹`, `far`, `braid`, transported from `HeckeColimit`), and its two payoffs
  `towerSpan_tensorColimit`, `disjointBlock_tensorColimit`.

## What is NOT proved here

* Faithfulness. The tensor model factors through the Temperley–Lieb quotient (two-row
  partitions), so this trace kills the convention-D radical; it is not faithful on
  `H_∞(q)`, and nothing here claims it is.
* `H n` is the image of level `n` in the colimit (as in `HeckeColimit`); injectivity of
  `ofLim n` is not used.
* That this trace equals `HeckeColimitMarkovTrace.trLim` over `ℝ` at generic `q`. It
  should, by uniqueness, but the level-`k < n` Markov property of `wtrace` in
  `HeckeFamily` form is not available in this file, so the identification is not
  stated.
-/

namespace QOU.IwahoriHecke.HeckeColimitTensorTrace

open QOU.SchurWeyl QOU.SchurWeyl.Hecke QOU.SchurWeyl.HeckeInclusion
open QOU.SchurWeyl.HeckeDirectedSystem QOU.SchurWeyl.HeckeColimit
open QOU.IwahoriHecke.JonesNormalForm
open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.HeckeSandwichReduces
open QOU.MathlibExt.TowerSpanReduction QOU.MathlibExt.DisjointBlockTrace

namespace TM
export QOU.IwahoriHecke.TensorMarkovModel (A sA tau zD sA_heckeFamily tau_one tau_cyc tau_markov)
end TM

/-! ## A general membership transport -/

/-- An algebra map that sends the first `k` members of one family to the first `k`
members of another maps the generated subalgebras into each other. -/
theorem map_mem_adjoin_Iio {R B C : Type*} [CommRing R] [Ring B] [Algebra R B] [Ring C]
    [Algebra R C] (φ : B →ₐ[R] C) {s : ℕ → B} {s' : ℕ → C} {k : ℕ}
    (h : ∀ i, i < k → φ (s i) = s' i) {x : B}
    (hx : x ∈ Algebra.adjoin R (s '' Set.Iio k)) :
    φ x ∈ Algebra.adjoin R (s' '' Set.Iio k) := by
  have himg : φ '' (s '' Set.Iio k) = s' '' Set.Iio k := by
    rw [Set.image_image]
    exact Set.image_congr fun i hi => h i (Set.mem_Iio.mp hi)
  rw [← himg, Algebra.adjoin_image]
  exact ⟨x, hx, rfl⟩

variable {K : Type*} [Field K] (q : K)

/-! ## The ℕ-indexed generator family of `Hecke K q q⁻¹ n` -/

/-- The generators of `Hecke K q q⁻¹ n`, indexed by `ℕ` (`0` from `n` on). -/
noncomputable def sw (n : ℕ) (i : ℕ) : Hecke K q q⁻¹ n :=
  if h : i < n then σ K q q⁻¹ n ⟨i, h⟩ else 0

theorem sw_of_lt {n i : ℕ} (h : i < n) : sw q n i = σ K q q⁻¹ n ⟨i, h⟩ := by
  simp [sw, h]

variable {q}

/-- The generators of `Hecke K q q⁻¹ n` form a `HeckeFamily` with `s² = (q − q⁻¹)s + 1`. -/
theorem sw_heckeFamily (hq : q ≠ 0) (n : ℕ) : HeckeFamily n (q - q⁻¹) 1 (sw q n) where
  quad i hi := by
    rw [sw_of_lt q hi, σ_quadratic, mul_inv_cancel₀ hq]
  braid i hi := by
    rw [sw_of_lt q (show i < n by omega), sw_of_lt q hi]
    exact σ_braid K q q⁻¹ n ⟨i, by omega⟩ hi
  comm i j hij hj := by
    rw [sw_of_lt q (show i < n by omega), sw_of_lt q hj]
    exact (σ_commute K q q⁻¹ n ⟨j, hj⟩ ⟨i, by omega⟩ (by simpa using hij)).symm

variable (q) in
theorem adjoin_sw_eq_top (n : ℕ) : Algebra.adjoin K (sw q n '' Set.Iio n) = ⊤ := by
  have : sw q n '' Set.Iio n = Set.range (σ K q q⁻¹ n) := by
    ext x
    constructor
    · rintro ⟨i, hi, rfl⟩
      exact ⟨⟨i, hi⟩, (sw_of_lt q hi).symm⟩
    · rintro ⟨i, rfl⟩
      exact ⟨i, i.isLt, sw_of_lt q i.isLt⟩
  rw [this]
  exact adjoin_range_σ_eq_top K q q⁻¹ n

variable (q) in
/-- The inclusion sends the `ℕ`-indexed generators below `n` to themselves. -/
theorem heckeIncl_sw (n : ℕ) {i : ℕ} (hi : i < n) :
    heckeIncl K q q⁻¹ n (sw q n i) = sw q (n + 1) i := by
  rw [sw_of_lt q hi, heckeIncl_σ, sw_of_lt q (by omega)]
  rfl

/-! ## The Hecke algebra maps to the tensor model -/

/-- `Hecke K q q⁻¹ n → End(V^{⊗(n+1)})^W`, `σᵢ ↦ sᵢ`. -/
noncomputable def toModel (hq : q ≠ 0) (n : ℕ) : Hecke K q q⁻¹ n →ₐ[K] TM.A q n :=
  Hecke.lift K q q⁻¹ n (fun i => TM.sA q n i)
    (fun i => by
      rw [mul_inv_cancel₀ hq, (TM.sA_heckeFamily hq n).quad i i.isLt])
    (fun i hi => (TM.sA_heckeFamily hq n).braid i hi)
    (fun i j hij => ((TM.sA_heckeFamily hq n).comm j i (by simpa using hij) i.isLt).symm)

theorem toModel_sw (hq : q ≠ 0) (n : ℕ) {i : ℕ} (hi : i < n) :
    toModel hq n (sw q n i) = TM.sA q n i := by
  rw [sw_of_lt q hi, toModel, Hecke.lift_σ]

/-! ## The level traces -/

/-- The Markov trace at level `n`: the normalised quantum trace pulled back to
`Hecke K q q⁻¹ n`. -/
noncomputable def levelTrace (hq : q ≠ 0) (n : ℕ) : Hecke K q q⁻¹ n →ₗ[K] K :=
  TM.tau q n ∘ₗ (toModel hq n).toLinearMap

theorem levelTrace_apply (hq : q ≠ 0) (n : ℕ) (x : Hecke K q q⁻¹ n) :
    levelTrace hq n x = TM.tau q n (toModel hq n x) := rfl

theorem levelTrace_one (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) (n : ℕ) :
    levelTrace hq n 1 = 1 := by
  rw [levelTrace_apply, map_one, TM.tau_one hq1]

theorem levelTrace_cyc (hq : q ≠ 0) (n : ℕ) (x y : Hecke K q q⁻¹ n) :
    levelTrace hq n (x * y) = levelTrace hq n (y * x) := by
  rw [levelTrace_apply, levelTrace_apply, map_mul (toModel hq n) x y,
    map_mul (toModel hq n) y x]
  exact TM.tau_cyc q n _ _

/-- Markov stabilisation at every intermediate level. -/
theorem levelTrace_markov (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) (n : ℕ) :
    ∀ k, k < n → ∀ x ∈ Algebra.adjoin K (sw q n '' Set.Iio k),
      levelTrace hq n (x * sw q n k) = TM.zD q * levelTrace hq n x := by
  intro k hk x hx
  rw [levelTrace_apply, levelTrace_apply, map_mul, toModel_sw hq n hk]
  refine TM.tau_markov hq hq1 n k hk _ ?_
  exact map_mem_adjoin_Iio (toModel hq n)
    (fun i hi => toModel_sw hq n (lt_trans hi hk)) hx

/-- **Tower compatibility**, by uniqueness of the Markov trace on `Hecke K q q⁻¹ n`. -/
theorem levelTrace_incl (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) (n : ℕ) (x : Hecke K q q⁻¹ n) :
    levelTrace hq (n + 1) (heckeIncl K q q⁻¹ n x) = levelTrace hq n x := by
  have h := markov_unique_of_adjoin_eq_top (sw_heckeFamily hq n) (adjoin_sw_eq_top q n)
    (TM.zD q) (levelTrace hq (n + 1) ∘ₗ (heckeIncl K q q⁻¹ n).toLinearMap) (levelTrace hq n)
    (by simp [levelTrace_one hq hq1])
    (by intro x y; simp only [LinearMap.coe_comp, Function.comp_apply,
          AlgHom.toLinearMap_apply, map_mul]; exact levelTrace_cyc hq (n + 1) _ _)
    (by
      intro k hk x hx
      simp only [LinearMap.coe_comp, Function.comp_apply, AlgHom.toLinearMap_apply, map_mul,
        heckeIncl_sw q n hk]
      refine levelTrace_markov hq hq1 (n + 1) k (by omega) _ ?_
      exact map_mem_adjoin_Iio (heckeIncl K q q⁻¹ n)
        (fun i hi => heckeIncl_sw q n (lt_trans hi hk)) hx)
    (levelTrace_one hq hq1 n) (levelTrace_cyc hq n) (levelTrace_markov hq hq1 n)
  exact LinearMap.congr_fun h x

theorem levelTrace_inclLE (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) (i j : ℕ) (hij : i ≤ j)
    (x : Hecke K q q⁻¹ i) :
    levelTrace hq j (heckeInclLE K q q⁻¹ i j hij x) = levelTrace hq i x := by
  induction j, hij using Nat.le_induction with
  | base => rw [heckeInclLE_self]; rfl
  | succ n hn ih =>
      rw [heckeInclLE_succ K q q⁻¹ i n hn, AlgHom.comp_apply, levelTrace_incl hq hq1 n, ih]

/-! ## The trace on the colimit -/

/-- **The tensor-model Markov trace on the Hecke colimit.** -/
noncomputable def trT (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) : HeckeLim K q q⁻¹ →ₗ[K] K :=
  DirectLimit.Module.lift K ℕ (Hecke K q q⁻¹) (heckeF K q q⁻¹)
    (levelTrace hq) (fun i j hij x => levelTrace_inclLE hq hq1 i j hij x)

@[simp] theorem trT_ofLim (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) (n : ℕ) (x : Hecke K q q⁻¹ n) :
    trT hq hq1 (ofLimₐ K q q⁻¹ n x) = levelTrace hq n x :=
  DirectLimit.Module.lift_of (f := heckeF K q q⁻¹) _ _ x

theorem trT_cyclic (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) (a b : HeckeLim K q q⁻¹) :
    trT hq hq1 (a * b) = trT hq hq1 (b * a) := by
  induction a, b using DirectLimit.induction₂ (f := heckeF K q q⁻¹) with
  | _ i x y =>
    show trT hq hq1 (ofLimₐ K q q⁻¹ i x * ofLimₐ K q q⁻¹ i y)
      = trT hq hq1 (ofLimₐ K q q⁻¹ i y * ofLimₐ K q q⁻¹ i x)
    rw [← map_mul, ← map_mul, trT_ofLim, trT_ofLim]
    exact levelTrace_cyc hq i x y

theorem trT_one (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) : trT hq hq1 1 = 1 := by
  have h1 : (1 : HeckeLim K q q⁻¹) = ofLimₐ K q q⁻¹ 0 1 := (map_one _).symm
  rw [h1, trT_ofLim]
  exact levelTrace_one hq hq1 0

/-- **(T3)** Markov stabilisation on the colimit, with `z = q³/(q²+1)`. -/
theorem trT_markov (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) (n : ℕ) (a : HeckeLim K q q⁻¹)
    (ha : a ∈ H K q q⁻¹ n) :
    trT hq hq1 (a * gLim K q q⁻¹ n) = TM.zD q * trT hq hq1 a := by
  obtain ⟨y, rfl⟩ := ha
  show trT hq hq1 (ofLimₐ K q q⁻¹ n y * gLim K q q⁻¹ n)
    = TM.zD q * trT hq hq1 (ofLimₐ K q q⁻¹ n y)
  have hstep : ofLimₐ K q q⁻¹ n y
      = ofLimₐ K q q⁻¹ (n + 1) (heckeIncl K q q⁻¹ n y) := by
    have := ofLimₐ_comp K q q⁻¹ (Nat.le_succ n) y
    rw [← this, heckeInclLE_succ K q q⁻¹ n n le_rfl, AlgHom.comp_apply, heckeInclLE_self]
    rfl
  have hgen : σ K q q⁻¹ (n + 1) ⟨n, Nat.lt_succ_self n⟩ = sw q (n + 1) n :=
    (sw_of_lt q (Nat.lt_succ_self n)).symm
  nth_rewrite 1 [hstep]
  rw [gLim, hgen, ← map_mul, trT_ofLim, trT_ofLim, ← levelTrace_incl hq hq1 n y]
  refine levelTrace_markov hq hq1 (n + 1) n (Nat.lt_succ_self n) _ ?_
  refine map_mem_adjoin_Iio (heckeIncl K q q⁻¹ n) (fun i hi => heckeIncl_sw q n hi) ?_
  rw [adjoin_sw_eq_top q n]
  trivial

/-- **(T3')** Markov stabilisation by the inverse generator; `zinv` is derived from
`σ⁻¹ = σ − (q − q⁻¹)·1`. -/
theorem trT_markov_inv (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) (n : ℕ) (a : HeckeLim K q q⁻¹)
    (ha : a ∈ H K q q⁻¹ n) :
    trT hq hq1 (a * ginvLim K q q⁻¹ n) = (TM.zD q - (q - q⁻¹)) * trT hq hq1 a := by
  have hsplit : a * ginvLim K q q⁻¹ n = a * gLim K q q⁻¹ n - (q - q⁻¹) • a := by
    rw [ginvLim, gLim, σInv, map_sub, map_smul, map_one, mul_sub, mul_smul_comm, mul_one]
  rw [hsplit, map_sub, map_smul, trT_markov hq hq1 n a ha]
  simp only [smul_eq_mul]
  ring

/-- **The `IwahoriHecke` tensor-model trace as an abstract `MarkovTrace`**, over any
field, at `z = q³/(q²+1)`. -/
noncomputable def tensorColimitMarkovTrace (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) :
    MarkovTrace K (HeckeLim K q q⁻¹) where
  H := H K q q⁻¹
  H_mono := H_mono K q q⁻¹
  g := gLim K q q⁻¹
  g_mem := gLim_mem K q q⁻¹
  ginv := ginvLim K q q⁻¹
  ginv_mem := ginvLim_mem K q q⁻¹
  ginv_mul n := ginvLim_mul_gLim K q q⁻¹ (mul_inv_cancel₀ hq) n
  mul_ginv n := gLim_mul_ginvLim K q q⁻¹ (mul_inv_cancel₀ hq) n
  tr := trT hq hq1
  tr_mul_comm := trT_cyclic hq hq1
  tr_one := trT_one hq hq1
  z := TM.zD q
  zinv := TM.zD q - (q - q⁻¹)
  markov := trT_markov hq hq1
  markov_inv := trT_markov_inv hq hq1

/-- The tensor-model colimit trace is a **braided tower**, with `h = q − q⁻¹`. -/
instance braidedTower_tensorColimit (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) :
    BraidedTower (tensorColimitMarkovTrace hq hq1) where
  quad m := ⟨q - q⁻¹, by
    have h := gLim_quadratic K q q⁻¹ m
    rw [mul_inv_cancel₀ hq, one_smul] at h
    exact h⟩
  far m k hk := gLim_far K q q⁻¹ m k hk
  braid m := gLim_braid K q q⁻¹ m

/-- The quadratic scalar `h = q − q⁻¹` is non-zero exactly when `q² ≠ 1`. -/
theorem quad_scalar_ne_zero (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) : q - q⁻¹ ≠ 0 := by
  intro h
  apply hq2
  have : q = q⁻¹ := sub_eq_zero.mp h
  calc q ^ 2 = q * q⁻¹ := by rw [sq]; nth_rewrite 2 [this]; rfl
    _ = 1 := mul_inv_cancel₀ hq

/-- **`TowerSpan`** on the tensor-model Hecke colimit. -/
theorem towerSpan_tensorColimit (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) :
    TowerSpan (tensorColimitMarkovTrace hq hq1) :=
  towerSpan_of_braided _

/-- **The disjoint-block trace law** on the tensor-model Hecke colimit, over any field. -/
theorem disjointBlock_tensorColimit (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) :
    DisjointBlockMultiplicative (tensorColimitMarkovTrace hq hq1) :=
  disjointBlock_of_braided _

end QOU.IwahoriHecke.HeckeColimitTensorTrace
