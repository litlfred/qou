/-
  Torus-knot dictionary: leptons at H₂ vs mesons at H₃.

  The lepton mass tower is indexed by torus knots T(2,n) for
  n = 3,5,7 (electron, muon, tau). The meson sector uses the
  same torus-knot indices for quark flavors, with total crossings
  n₁ + n₂ for quark-antiquark pairs.

  -- Ref: [jones1987] https://doi.org/10.1090/S0273-0979-1985-15304-2
  -- Ref: [kashaev1997] https://doi.org/10.1007/s100529801020
-/

import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Omega

namespace QOU.ParticleInteractions

-- ═══════════════════════════════════════════════════════════════
-- §1  TORUS-KNOT GENERATION INDEX
-- ═══════════════════════════════════════════════════════════════

/-- Lepton generation → torus-knot crossing number. -/
def leptonTorusKnotIndex : Fin 3 → ℕ
  | 0 => 3   -- electron: trefoil T(2,3)
  | 1 => 5   -- muon: cinquefoil T(2,5)
  | 2 => 7   -- tau: septafoil T(2,7)

/-- All lepton torus-knot indices are odd. -/
theorem leptonIndex_odd (g : Fin 3) :
    ¬ 2 ∣ leptonTorusKnotIndex g := by
  fin_cases g <;> omega

/-- Consecutive generations differ by 2 crossings. -/
theorem leptonIndex_step :
    leptonTorusKnotIndex 1 - leptonTorusKnotIndex 0 = 2 ∧
    leptonTorusKnotIndex 2 - leptonTorusKnotIndex 1 = 2 := by
  constructor <;> rfl

-- ═══════════════════════════════════════════════════════════════
-- §2  MESON CROSSING COUNTS
-- ═══════════════════════════════════════════════════════════════

/-- Quark flavor → torus-knot crossing number.
  u,d quarks have n=3; s quark has n=5; c quark has n=7. -/
def quarkTorusKnotIndex : Fin 4 → ℕ
  | 0 => 3   -- u (up)
  | 1 => 3   -- d (down)
  | 2 => 5   -- s (strange)
  | 3 => 7   -- c (charm)

/-- Meson total crossings = quark + antiquark torus-knot indices. -/
def mesonCrossingCount (q1 q2 : Fin 4) : ℕ :=
  quarkTorusKnotIndex q1 + quarkTorusKnotIndex q2

/-- Pion (ūd): 3 + 3 = 6 crossings. -/
theorem pion_crossings : mesonCrossingCount 0 1 = 6 := rfl

/-- Kaon (ūs): 3 + 5 = 8 crossings. -/
theorem kaon_crossings : mesonCrossingCount 0 2 = 8 := rfl

/-- Phi (s̄s): 5 + 5 = 10 crossings. -/
theorem phi_crossings : mesonCrossingCount 2 2 = 10 := rfl

/-- D meson (ūc): 3 + 7 = 10 crossings. -/
theorem d_meson_crossings : mesonCrossingCount 0 3 = 10 := rfl

/-- The kaon-pion crossing difference equals the lepton generation step. -/
theorem kaon_pion_crossing_diff :
    mesonCrossingCount 0 2 - mesonCrossingCount 0 1 = 2 := rfl

-- ═══════════════════════════════════════════════════════════════
-- §3  HECKE NORMAL FORM STRUCTURE
-- ═══════════════════════════════════════════════════════════════

/-- The H₃(q) basis has 6 elements: 1, σ₀, σ₁, L₊, L₋, e⁻.
  A meson NF has 4 non-zero coefficients (σ₁, L₊, L₋, e⁻),
  with the constant and σ₀ terms vanishing. -/
structure MesonNF where
  coeff_sigma1 : ℤ → ℤ    -- coefficient of σ₁ as polynomial in h
  coeff_Lplus  : ℤ → ℤ    -- coefficient of L₊
  coeff_Lminus : ℤ → ℤ    -- coefficient of L₋
  coeff_eminus : ℤ → ℤ    -- coefficient of e⁻

/-- The canonical meson NF M₊ = h·σ₁ + (h²+1)·L₊ + h²·L₋ + (h³+h)·e⁻.
  At h=0 (q=1): M₊ = L₊ (pure Hopf link binding). -/
def canonicalMesonNF : MesonNF where
  coeff_sigma1 := fun h => h
  coeff_Lplus  := fun h => h^2 + 1
  coeff_Lminus := fun h => h^2
  coeff_eminus := fun h => h^3 + h

/-- At h=0, the meson NF reduces to the pure Hopf link L₊. -/
theorem meson_nf_classical_limit :
    canonicalMesonNF.coeff_sigma1 0 = 0 ∧
    canonicalMesonNF.coeff_Lplus 0 = 1 ∧
    canonicalMesonNF.coeff_Lminus 0 = 0 ∧
    canonicalMesonNF.coeff_eminus 0 = 0 := by
  unfold canonicalMesonNF
  simp

/-- At h=0 (classical limit), L₊ has coefficient 1 while all
  other basis elements have coefficient 0. The Hopf binding
  topology dominates the meson NF in the classical limit. -/
theorem Lplus_is_sole_classical_contribution :
    canonicalMesonNF.coeff_Lplus 0 = 1 ∧
    canonicalMesonNF.coeff_sigma1 0 = 0 ∧
    canonicalMesonNF.coeff_Lminus 0 = 0 ∧
    canonicalMesonNF.coeff_eminus 0 = 0 := by
  unfold canonicalMesonNF; simp

-- ═══════════════════════════════════════════════════════════════
-- §4  HIGHEST-WEIGHT / LOWEST-WEIGHT DUALITY
-- ═══════════════════════════════════════════════════════════════

/-- The kaon-pion crossing difference equals the muon-electron
  torus-knot step: both transitions add 2 crossings.
  Kaon = pion + 2 crossings; muon = electron + 2 crossings. -/
theorem flavor_transition_matches_lepton_step :
    mesonCrossingCount 0 2 - mesonCrossingCount 0 1 =
    leptonTorusKnotIndex 1 - leptonTorusKnotIndex 0 := rfl

end QOU.ParticleInteractions
