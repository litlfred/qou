/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.QuantumGLHWDim

/-!
# The Hecke action on the highest-weight spaces is dense (G3.4c)

Bean `qou-gl343`. Over a linearly ordered field at `q` not a root of unity:

* `resHW_bijective`: restriction from the commutant `B'` of `uqGens` to the highest-weight spaces,
  `B' → ∏_μ End(HW_μ)`, is a linear bijection. It is injective by `resHW_injective` (F3), and the
  dimensions agree by `sum_sq_finrank_hwSpace_eq`.
* `exists_jimbo_restrict_eq`: for every occurring weight `μ` and every linear map
  `f : HW_μ → HW_μ`, some `x ∈ H_{m+1}(q)` acts on `HW_μ` as `f` and acts by zero on every other
  `HW_ν`. In particular each nonzero `HW_μ` is a simple `H_{m+1}(q)`-module (density), and distinct
  `HW_μ` are pairwise non-isomorphic.

This file does not prove which Specht module `HW_μ` is, i.e. `HW_μ ≅ S_{λ(μ)}`.

## Base ring (§7c)

A linearly ordered field, inherited from `range_jimbo_eq_commutant`.
-/

namespace QOU.SchurWeyl.QuantumGL

open Matrix QOU.SchurWeyl.JimboGL

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L] {d : ℕ} [NeZero d]

/-- **Wedderburn form of G3.4**: `B' ≅ ∏_μ End(HW_μ)` by restriction. -/
theorem resHW_bijective (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    (m : ℕ) : Function.Bijective (resHW (d := d) q m) := by
  have hinj := resHW_injective (d := d) q m
  refine ⟨hinj, ?_⟩
  haveI : FiniteDimensional L (commutant (uqGens (d := d) q m)) :=
    FiniteDimensional.finiteDimensional_submodule _
  have hr := LinearMap.finrank_range_of_inj hinj
  have htop : LinearMap.range (resHW (d := d) q m) = ⊤ := by
    haveI : ∀ μ : occWeights d m,
        Module.Finite L (hwSpace q m μ.1 →ₗ[L] hwSpace q m μ.1) := fun _ => inferInstance
    refine Submodule.eq_top_of_finrank_eq (K := L)
      (V := (μ : occWeights d m) → (hwSpace q m μ.1 →ₗ[L] hwSpace q m μ.1)) ?_
    rw [hr, Module.finrank_pi_fintype, ← range_jimbo_eq_commutant q hq hgen m,
      finrank_range_jimbo q hq hgen m, ← sum_sq_finrank_hwSpace_eq q hq hgen m,
      ← Finset.sum_coe_sort (occWeights d m)]
    refine Finset.sum_congr rfl fun μ _ => ?_
    rw [Module.finrank_linearMap, sq]
  exact LinearMap.range_eq_top.mp htop

/-- **Density**: every endomorphism of one highest-weight space is realised by the Hecke action,
which can moreover be chosen to vanish on every other highest-weight space. -/
theorem exists_jimbo_restrict_eq (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (μ : occWeights d m) (f : hwSpace q m μ.1 →ₗ[L] hwSpace q m μ.1) :
    ∃ x : Hecke L q q⁻¹ m,
      (∀ v ∈ hwSpace q m μ.1, ∀ hv : v ∈ hwSpace q m μ.1,
          jimbo d q hq m x *ᵥ v = (f ⟨v, hv⟩ : (Fin (m + 1) → Fin d) → L)) ∧
      ∀ ν : occWeights d m, ν ≠ μ → ∀ w ∈ hwSpace q m ν.1, jimbo d q hq m x *ᵥ w = 0 := by
  classical
  obtain ⟨Y, hY⟩ := (resHW_bijective (d := d) q hq hgen m).2 (Pi.single μ f)
  have hYr : Y.1 ∈ LinearMap.range (jimbo d q hq m).toLinearMap := by
    rw [range_jimbo_eq_commutant q hq hgen m]; exact Y.2
  obtain ⟨x, hx⟩ := hYr
  have hx' : jimbo d q hq m x = Y.1 := hx
  refine ⟨x, fun v _ hv => ?_, fun ν hν w hw => ?_⟩
  · have := congrArg (fun g => ((g μ) ⟨v, hv⟩ : (Fin (m + 1) → Fin d) → L)) hY
    simpa [resHW, hx'] using this
  · have := congrArg (fun g => ((g ν) ⟨w, hw⟩ : (Fin (m + 1) → Fin d) → L)) hY
    simpa [resHW, hx', Pi.single_eq_of_ne hν] using this

end QOU.SchurWeyl.QuantumGL
