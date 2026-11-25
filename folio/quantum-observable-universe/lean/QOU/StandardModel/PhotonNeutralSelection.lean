/-
  Which factorisation of the Borromean core into two photons survives linking neutrality
  (audit `docs/audits/2026-11-25-photon-jet-and-hearing-the-shape.md` §13).

  Over `ℚ(h)`, `γ(φ)γ(ψ) = V³` has 8 solutions: the corpus pair and an irreducible degree-6
  component (Singular, §11.2). Expand `γ(φ)γ(ψ)` formally in the group algebra `ℤ[B₃]` and
  collect by braid-group element. Four of the group elements that occur are not linking-neutral
  (`QOU.PhotonU1NeutralCut.table`): `σ₀` (coefficient `φ₀ + ψ₀ + φ₀₁ψ₁`, since `Vσ₁ = σ₀` in
  `B₃`), `σ₁` (`φ₁ + ψ₁`), `σ₀V` (`φ₀ψ₀₁`) and `σ₁V` (`φ₁ψ₀₁`). Requiring those four
  coefficients to vanish, term-wise linking neutrality, leaves only the corpus pair
  (`neutral_selects_corpus`), in the concrete model of `H₃(q)`, over any domain with
  `h ≠ 0` and `h² + 2 ≠ 0`.

  Scope: `QOU.PhotonU1NeutralCut` leaves open whether neutrality is imposed term by term or on
  the whole product braid. This theorem uses the term-wise reading. The whole-product reading
  cannot separate the factorisations, since all of them have the same product `V³`.

  -- Ref: [leitner2026] predicted-spectra, def:photon
-/
import QOU.StandardModel.HeckeH3Model

namespace QOU.PhotonNeutralSelection

open QOU.Mass.BorromeanPhotonFactorisation QOU.HeckeH3Model

variable {R : Type*} [CommRing R]

/-- `V` applied to a vector, explicitly. -/
theorem modelV_apply (h : R) (v : Fin 6 → R) :
    modelV h v = ![v 4 - h * v 1, v 2 - h * v 0 + h * (v 4 - h * v 1), v 5 - h * v 3,
      v 0 + h * (v 5 - h * v 3), v 3, v 1 + h * v 3] := by
  funext i
  fin_cases i <;> simp [vertex, Module.End.mul_apply] <;> ring

/-- A photon applied to a vector, explicitly. -/
theorem gamma_apply (h c₀ c₁ c₂ : R) (v : Fin 6 → R) :
    (1 + c₀ • heckeL0 h + c₁ • heckeL1 h + c₂ • modelV h) v =
      ![v 0 + c₀ * v 1 + c₁ * v 2 + c₂ * (v 4 - h * v 1),
        v 1 + c₀ * (v 0 + h * v 1) + c₁ * v 4 + c₂ * (v 2 - h * v 0 + h * (v 4 - h * v 1)),
        v 2 + c₀ * v 3 + c₁ * (v 0 + h * v 2) + c₂ * (v 5 - h * v 3),
        v 3 + c₀ * (v 2 + h * v 3) + c₁ * v 5 + c₂ * (v 0 + h * (v 5 - h * v 3)),
        v 4 + c₀ * v 5 + c₁ * (v 1 + h * v 4) + c₂ * v 3,
        v 5 + c₀ * (v 4 + h * v 5) + c₁ * (v 3 + h * v 5) + c₂ * (v 1 + h * v 3)] := by
  have hv := modelV_apply h v
  funext i
  simp only [LinearMap.add_apply, LinearMap.smul_apply, Module.End.one_apply, Pi.add_apply,
    Pi.smul_apply, smul_eq_mul, hv, heckeL0_apply, heckeL1_apply]
  fin_cases i <;> simp <;> ring

/-- Coordinates of `γ(φ)γ(ψ) − V³` as a vector equation. -/
theorem coord_factorisation (h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ : R)
    (hfac : (1 + φ₀ • heckeL0 h + φ₁ • heckeL1 h + φ₀₁ • modelV h)
      * (1 + ψ₀ • heckeL0 h + ψ₁ • heckeL1 h + ψ₀₁ • modelV h)
      = modelV h * modelV h * modelV h) (i : Fin 6) :
    (1 + φ₀ • heckeL0 h + φ₁ • heckeL1 h + φ₀₁ • modelV h)
      ((1 + ψ₀ • heckeL0 h + ψ₁ • heckeL1 h + ψ₀₁ • modelV h) te) i
      = modelV h (modelV h (modelV h te)) i := by
  have := congrArg (fun X : M6 R => X te i) hfac
  simpa [Module.End.mul_apply] using this

theorem coord_eq0 (h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ : R)
    (hfac : (1 + φ₀ • heckeL0 h + φ₁ • heckeL1 h + φ₀₁ • modelV h)
      * (1 + ψ₀ • heckeL0 h + ψ₁ • heckeL1 h + ψ₀₁ • modelV h)
      = modelV h * modelV h * modelV h) :
    h ^ 4 + h ^ 2 * φ₀₁ * ψ₀₁ - h * φ₀ * ψ₀₁ - h * φ₀₁ * ψ₀ + φ₀ * ψ₀ + φ₁ * ψ₁ = 0 := by
  have e := coord_factorisation h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ hfac 0
  rw [gamma_apply, gamma_apply, modelV_apply, modelV_apply, modelV_apply] at e
  simp [te] at e
  linear_combination e

theorem coord_eq1 (h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ : R)
    (hfac : (1 + φ₀ • heckeL0 h + φ₁ • heckeL1 h + φ₀₁ • modelV h)
      * (1 + ψ₀ • heckeL0 h + ψ₁ • heckeL1 h + ψ₀₁ • modelV h)
      = modelV h * modelV h * modelV h) :
    h ^ 5 + h ^ 3 * φ₀₁ * ψ₀₁ + h ^ 3 - h ^ 2 * φ₀ * ψ₀₁ - h ^ 2 * φ₀₁ * ψ₀ + h * φ₀ * ψ₀
      - h * φ₀₁ - h * ψ₀₁ + φ₀ + φ₀₁ * ψ₁ + ψ₀ = 0 := by
  have e := coord_factorisation h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ hfac 1
  rw [gamma_apply, gamma_apply, modelV_apply, modelV_apply, modelV_apply] at e
  simp [te] at e
  linear_combination e

theorem coord_eq2 (h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ : R)
    (hfac : (1 + φ₀ • heckeL0 h + φ₁ • heckeL1 h + φ₀₁ • modelV h)
      * (1 + ψ₀ • heckeL0 h + ψ₁ • heckeL1 h + ψ₀₁ • modelV h)
      = modelV h * modelV h * modelV h) :
    -h ^ 3 + h * φ₁ * ψ₁ - h * φ₀₁ * ψ₀₁ + φ₀ * ψ₀₁ + φ₁ + ψ₁ = 0 := by
  have e := coord_factorisation h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ hfac 2
  rw [gamma_apply, gamma_apply, modelV_apply, modelV_apply, modelV_apply] at e
  simp [te] at e
  linear_combination e

theorem coord_eq3 (h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ : R)
    (hfac : (1 + φ₀ • heckeL0 h + φ₁ • heckeL1 h + φ₀₁ • modelV h)
      * (1 + ψ₀ • heckeL0 h + ψ₁ • heckeL1 h + ψ₀₁ • modelV h)
      = modelV h * modelV h * modelV h) :
    -h ^ 4 - h ^ 2 * φ₀₁ * ψ₀₁ - h ^ 2 + h * φ₀ * ψ₀₁ + φ₀ * ψ₁ + φ₀₁ + ψ₀₁ = 0 := by
  have e := coord_factorisation h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ hfac 3
  rw [gamma_apply, gamma_apply, modelV_apply, modelV_apply, modelV_apply] at e
  simp [te] at e
  linear_combination e

theorem coord_eq4 (h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ : R)
    (hfac : (1 + φ₀ • heckeL0 h + φ₁ • heckeL1 h + φ₀₁ • modelV h)
      * (1 + ψ₀ • heckeL0 h + ψ₁ • heckeL1 h + ψ₀₁ • modelV h)
      = modelV h * modelV h * modelV h) :
    h ^ 2 - h * φ₁ * ψ₀₁ + φ₁ * ψ₀ + φ₀₁ * ψ₀₁ = 0 := by
  have e := coord_factorisation h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ hfac 4
  rw [gamma_apply, gamma_apply, modelV_apply, modelV_apply, modelV_apply] at e
  simp [te] at e
  linear_combination e

theorem coord_eq5 (h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ : R)
    (hfac : (1 + φ₀ • heckeL0 h + φ₁ • heckeL1 h + φ₀₁ • modelV h)
      * (1 + ψ₀ • heckeL0 h + ψ₁ • heckeL1 h + ψ₀₁ • modelV h)
      = modelV h * modelV h * modelV h) :
    φ₁ * ψ₀₁ + φ₀₁ * ψ₀ = 0 := by
  have e := coord_factorisation h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ hfac 5
  rw [gamma_apply, gamma_apply, modelV_apply, modelV_apply, modelV_apply] at e
  simp [te] at e
  linear_combination e

/-- **Term-wise linking neutrality selects the corpus pair.** If `γ(φ)γ(ψ) = V³` and the
coefficients of the non-neutral group elements `σ₀, σ₁, σ₀V, σ₁V` in the formal expansion
vanish, then both photons are pure vertex photons with the corpus weights `qh`, `−q⁻¹h`. -/
theorem neutral_selects_corpus [IsDomain R] {q q' : R} (hqq : q * q' = 1)
    (hh : q - q' ≠ 0) (hh2 : (q - q') ^ 2 + 2 ≠ 0) {φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ : R}
    (hfac : (1 + φ₀ • heckeL0 (q - q') + φ₁ • heckeL1 (q - q') + φ₀₁ • modelV (q - q'))
      * (1 + ψ₀ • heckeL0 (q - q') + ψ₁ • heckeL1 (q - q') + ψ₀₁ • modelV (q - q'))
      = modelV (q - q') * modelV (q - q') * modelV (q - q'))
    (n1 : φ₀ + ψ₀ + φ₀₁ * ψ₁ = 0) (n2 : φ₁ + ψ₁ = 0)
    (n3 : φ₀ * ψ₀₁ = 0) (n4 : φ₁ * ψ₀₁ = 0) :
    φ₀ = 0 ∧ φ₁ = 0 ∧ ψ₀ = 0 ∧ ψ₁ = 0 ∧
      ((φ₀₁ = q * (q - q') ∧ ψ₀₁ = -(q' * (q - q'))) ∨
        (φ₀₁ = -(q' * (q - q')) ∧ ψ₀₁ = q * (q - q'))) := by
  set h := q - q' with hdef
  have e0 := coord_eq0 h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ hfac
  have e1 := coord_eq1 h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ hfac
  have e2 := coord_eq2 h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ hfac
  have e3 := coord_eq3 h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ hfac
  have e4 := coord_eq4 h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ hfac
  by_cases hs : ψ₀₁ = 0
  · exfalso
    subst hs
    have key : h ^ 3 * (h ^ 2 + 2) = 0 := by
      linear_combination (h - ψ₁ ^ 2 * h) * e0 + (ψ₁ ^ 2 - 1) * e1 + (ψ₁ ^ 2 - 1) * e2
        + (-h) * e3 + h * e4 + (-ψ₁ ^ 2 + ψ₁ * h + 1) * n1 + (-ψ₁ ^ 2 - ψ₀ * h + 1) * n2
    rcases mul_eq_zero.mp key with k | k
    · exact hh (pow_eq_zero_iff (by norm_num) |>.mp k)
    · exact hh2 k
  · have k0 : φ₀ = 0 := (mul_eq_zero.mp n3).resolve_right hs
    have k1 : φ₁ = 0 := (mul_eq_zero.mp n4).resolve_right hs
    have k4 : ψ₁ = 0 := by rw [k1] at n2; linear_combination n2
    have k3 : ψ₀ = 0 := by rw [k0, k4] at n1; linear_combination n1
    refine ⟨k0, k1, k3, k4, ?_⟩
    rw [k0, k1, k3, k4] at hfac
    simp only [zero_smul, add_zero] at hfac
    exact borromean_weights_forced_model hqq hfac

end QOU.PhotonNeutralSelection
