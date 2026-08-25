import QOU.SchurWeyl.HeckeDim3Dim

/-!
# QOU.SchurWeyl.HeckeWedderburn3 — the Wedderburn iso `H_3(q) ≅ ℝ × ℝ × M₂(ℝ)` (SW-7, R2-inst at n=3)

The three irreducible representations of `H_3(q) = Hecke ℝ q q⁻¹ 2` (`q ≠ 0`) —
the trivial `rhoTriv`, the sign `rhoSign`, and the `(2,1)` seminormal
`seminormalRep21` — assemble into a single algebra map

  `ρ = (rhoTriv, rhoSign, seminormalRep21) : H_3(q) →ₐ[ℝ] ℝ × ℝ × M₂(ℝ)`.

* **injective** (`rho_injective`): `ρ x = 0` gives the three representation images
  of `x` are zero; expanding `x` in the six-word basis reduces to the component
  core `sixCoeffs_zero`, so every coordinate — hence `x` — vanishes;
* **bijective** (`rho_bijective`): both sides have `finrank = 6`
  (`finrank_hecke3`; `1 + 1 + 2·2` on the right), so an injective ℝ-linear map
  between them is surjective.

Hence `wedderburn3 : H_3(q) ≃ₐ[ℝ] ℝ × ℝ × M₂(ℝ)` — the Artin–Wedderburn
decomposition of the semisimple algebra `H_3(q)` at `n = 3`, matching
`1² + 1² + 2² = 6 = 3!`.  This is **R2-inst at n = 3**.

Base ring `ℝ` (the seminormal rep is archimedean, §7c).

LaTeX label: `prop:hecke3-wedderburn`
-/

namespace QOU.SchurWeyl

open Hecke Matrix

section Wedderburn

variable (q : ℝ)

local notation3 "t₀" => σ ℝ q q⁻¹ 2 0
local notation3 "t₁" => σ ℝ q q⁻¹ 2 1

/-- The **product representation** `ρ = (rhoTriv, rhoSign, seminormalRep21)` of
`H_3(q)` into `ℝ × ℝ × M₂(ℝ)` (`q ≠ 0`). -/
noncomputable def rho (hq : q ≠ 0) :
    Hecke ℝ q q⁻¹ 2 →ₐ[ℝ] ℝ × ℝ × Matrix (Fin 2) (Fin 2) ℝ :=
  (rhoTriv ℝ q q⁻¹ 2).prod ((rhoSign ℝ q q⁻¹ 2).prod (seminormalRep21 q hq))

@[simp] theorem rho_apply (hq : q ≠ 0) (x : Hecke ℝ q q⁻¹ 2) :
    rho q hq x = (rhoTriv ℝ q q⁻¹ 2 x, rhoSign ℝ q q⁻¹ 2 x, seminormalRep21 q hq x) := by
  simp [rho, AlgHom.prod_apply]

/-- `finrank_ℝ (ℝ × ℝ × M₂(ℝ)) = 6`. -/
theorem finrank_rhs :
    Module.finrank ℝ (ℝ × ℝ × Matrix (Fin 2) (Fin 2) ℝ) = 6 := by
  rw [Module.finrank_prod, Module.finrank_prod, Module.finrank_self, Module.finrank_matrix]
  simp

/-- **`ρ` is injective** (`q ≠ 0`): the three irreps jointly separate points, via the
six-word basis and the component core `sixCoeffs_zero`. -/
theorem rho_injective (hq : q ≠ 0) : Function.Injective (rho q hq) := by
  rw [injective_iff_map_eq_zero]
  intro x hx
  set b := sixBasis q hq with hb
  -- `x` expanded in the six-word basis, in the exact shape `sixCoeffs_zero` expects.
  have key : ∑ i, b.repr x i • sixFamily q i = x := by
    have h := b.sum_repr x
    simpa only [hb, sixBasis, Module.Basis.mk_apply] using h
  have hexp : (∑ i, b.repr x i • sixFamily q i)
      = b.repr x 0 • (1 : Hecke ℝ q q⁻¹ 2) + b.repr x 1 • t₀ + b.repr x 2 • t₁
        + b.repr x 3 • (t₀ * t₁) + b.repr x 4 • (t₁ * t₀) + b.repr x 5 • (t₀ * t₁ * t₀) := by
    simp [Fin.sum_univ_six, sixFamily]
  have hxe : x = b.repr x 0 • (1 : Hecke ℝ q q⁻¹ 2) + b.repr x 1 • t₀ + b.repr x 2 • t₁
        + b.repr x 3 • (t₀ * t₁) + b.repr x 4 • (t₁ * t₀) + b.repr x 5 • (t₀ * t₁ * t₀) :=
    key.symm.trans hexp
  -- The three representation images of `x` vanish.
  rw [rho_apply] at hx
  obtain ⟨hT0, hS0, hM0⟩ := by simpa only [Prod.ext_iff] using hx
  rw [hxe] at hT0 hS0 hM0
  obtain ⟨e1, e2, e3, e4, e5, e6⟩ :=
    sixCoeffs_zero q hq _ _ _ _ _ _ hT0 hS0 hM0
  rw [hxe, e1, e2, e3, e4, e5, e6]
  simp

/-- **`ρ` is bijective** (`q ≠ 0`): injective + equal finrank (`6 = 6`). -/
theorem rho_bijective (hq : q ≠ 0) : Function.Bijective (rho q hq) := by
  haveI : FiniteDimensional ℝ (Hecke ℝ q q⁻¹ 2) :=
    FiniteDimensional.of_fintype_basis (sixBasis q hq)
  have hfin : Module.finrank ℝ (Hecke ℝ q q⁻¹ 2)
      = Module.finrank ℝ (ℝ × ℝ × Matrix (Fin 2) (Fin 2) ℝ) := by
    rw [finrank_hecke3 q hq, finrank_rhs]
  refine ⟨rho_injective q hq, ?_⟩
  have hsurj : Function.Surjective ((rho q hq).toLinearMap) :=
    (LinearMap.injective_iff_surjective_of_finrank_eq_finrank hfin).mp (rho_injective q hq)
  exact hsurj

/-- **The Wedderburn isomorphism** `H_3(q) ≅ ℝ × ℝ × M₂(ℝ)** (`q ≠ 0`) — the
Artin–Wedderburn decomposition of the semisimple Iwahori–Hecke algebra at `n = 3`,
matching `1² + 1² + 2² = 6 = 3!`.  R2-inst at `n = 3`. -/
noncomputable def wedderburn3 (hq : q ≠ 0) :
    Hecke ℝ q q⁻¹ 2 ≃ₐ[ℝ] ℝ × ℝ × Matrix (Fin 2) (Fin 2) ℝ :=
  AlgEquiv.ofBijective (rho q hq) (rho_bijective q hq)

end Wedderburn

end QOU.SchurWeyl
