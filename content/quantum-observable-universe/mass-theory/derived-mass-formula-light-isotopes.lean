import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Choose.Basic


/-!
# Derived-only mass formula for light isotopes

The strict derived mass formula (no fitting):

  M(Z, N) = Z·m_p + N·m_n + Z·m_e
          + α·(Φ₁ - 2[3]_q·Φ₂ + H_A²·Φ₃)         [paper 3-term]
          + Δ_W                                   [paper Wigner T=0]
          + Δ_T1                                  [natural T=1 extension]

with α = m_e · 8G, Δ_W = -m_e · H_q((2,2)) · min(Z,N)/A,
Δ_T1 = -m_e · H_q((2,2)) · (n_pp + n_nn)/A.

Empirical scorecard (light isotopes through ⁷Li):
  Atomic masses: sub-percent (-0.049% to +0.576% across A = 2..7)
  Bindings:     under-predicted by 30-76% (structural gap)

-- Ref: [manuscript] prop:derived-mass-formula-light-isotopes
-- Triggering hash update for AI sweep
-/

namespace QOU.WedderburnMass

/-- The derived-only mass formula contributions. -/
structure DerivedFormulaParams where
  m_e   : ℝ      -- electron mass (CODATA)
  m_p   : ℝ      -- proton mass (CODATA)
  m_n   : ℝ      -- neutron mass (CODATA)
  α     : ℝ      -- m_e · 8G (Borromean prefactor)
  Hq22  : ℝ      -- H_q((2,2)) at q_0 (Wigner unit factor)
  q3_q  : ℝ      -- [3]_q
  H_A   : ℝ      -- q - q⁻¹

/-- The three Wedderburn log-functionals from the paper. -/
structure ThreeFunctionals where
  Φ₁ : ℝ        -- Σ log|trace M_i| over inter-gen direct
  Φ₂ : ℝ        -- Σ log|det M_i|
  Φ₃ : ℝ        -- Σ log|sym/alt|

/-- Wigner T=0 np-pairing correction (paper). -/
noncomputable def deltaWigner (p : DerivedFormulaParams) (Z N A : ℕ) : ℝ :=
  if A ≥ 2 ∧ Z ≥ 1 ∧ N ≥ 1 then
    -p.m_e * p.Hq22 * (Nat.min Z N : ℝ) / (A : ℝ)
  else 0

/-- T=1 isovector same-flavor pair correction (natural extension of
    Wigner using the same self-conjugate partition (2,2) ⊢ 4). -/
noncomputable def deltaT1 (p : DerivedFormulaParams) (Z N A : ℕ) : ℝ :=
  let n_pp : ℕ := Z.choose 2
  let n_nn : ℕ := N.choose 2
  if A ≥ 2 ∧ (n_pp + n_nn) > 0 then
    -p.m_e * p.Hq22 * ((n_pp + n_nn : ℕ) : ℝ) / (A : ℝ)
  else 0

/-- The derived-only atomic mass formula. -/
noncomputable def derivedLightIsotopeFormula
    (p : DerivedFormulaParams) (Z N : ℕ) (Φ : ThreeFunctionals) : ℝ :=
  let A : ℕ := Z + N
  (Z : ℝ) * p.m_p + (N : ℝ) * p.m_n + (Z : ℝ) * p.m_e
  + p.α * (Φ.Φ₁ - 2 * p.q3_q * Φ.Φ₂ + p.H_A^2 * Φ.Φ₃)
  + deltaWigner p Z N A
  + deltaT1 p Z N A

/-- For the free proton (Z=1, N=0, A=1), the formula returns
    m_p + m_e (the hydrogen atomic mass) exactly when Φ = 0. -/
theorem free_proton_exact
    (p : DerivedFormulaParams)
    (Φ : ThreeFunctionals) (hΦ : Φ.Φ₁ = 0 ∧ Φ.Φ₂ = 0 ∧ Φ.Φ₃ = 0) :
    derivedLightIsotopeFormula p 1 0 Φ = p.m_p + p.m_e := by
  -- A = 1 + 0 = 1, so deltaWigner returns 0 (A ≥ 2 fails),
  -- deltaT1 returns 0 (n_pp = 0, n_nn = 0).
  -- The Φ-correction is α·(0 - 2·q3·0 + H_A²·0) = 0.
  unfold derivedLightIsotopeFormula deltaWigner deltaT1
  obtain ⟨h1, h2, h3⟩ := hΦ
  rw [h1, h2, h3]
  -- A = 1, so the conditions A ≥ 2 fail, gates return 0.
  simp [Nat.choose, show (1 + 0 : ℕ) = 1 by rfl]
  ring

/-- For the free neutron (Z=0, N=1, A=1), the formula returns
    m_n exactly when Φ = 0. -/
theorem free_neutron_exact
    (p : DerivedFormulaParams)
    (Φ : ThreeFunctionals) (hΦ : Φ.Φ₁ = 0 ∧ Φ.Φ₂ = 0 ∧ Φ.Φ₃ = 0) :
    derivedLightIsotopeFormula p 0 1 Φ = p.m_n := by
  unfold derivedLightIsotopeFormula deltaWigner deltaT1
  obtain ⟨h1, h2, h3⟩ := hΦ
  rw [h1, h2, h3]
  simp [Nat.choose, show (0 + 1 : ℕ) = 1 by rfl]
  ring

/-- The proton-neutron mass splitting (bare) equals the CODATA
    constituent difference exactly under inter-gen direct convention. -/
theorem np_splitting_exact
    (p : DerivedFormulaParams)
    (Φp Φn : ThreeFunctionals)
    (hp : Φp.Φ₁ = 0 ∧ Φp.Φ₂ = 0 ∧ Φp.Φ₃ = 0)
    (hn : Φn.Φ₁ = 0 ∧ Φn.Φ₂ = 0 ∧ Φn.Φ₃ = 0) :
    derivedLightIsotopeFormula p 0 1 Φn
      - (derivedLightIsotopeFormula p 1 0 Φp - p.m_e)
    = p.m_n - p.m_p := by
  rw [free_neutron_exact p Φn hn, free_proton_exact p Φp hp]
  ring

end QOU.WedderburnMass
