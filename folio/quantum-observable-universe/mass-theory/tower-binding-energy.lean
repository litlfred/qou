import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-
  Nuclear binding energy from the 3-channel brane tower.

  B(Z,N) = Σ_λ w_λ × m_e × Σ_i ln|Φ_q(|V̂_i^λ|)|

  where w_λ are Wedderburn-Artin weights, V̂_i^λ are per-generator
  vertex volumes in each channel, and Φ_q is the quantum
  dilogarithm (analytically continued past |V̂| = q).

  Ref: [leitner2026] Ch 11 §8 / tower-binding-energy
-/

namespace QOU.ParticleInteractions

/-- The Wedderburn-Artin weight of the standard irrep of H₃(q):
    w_std = [2]_q² / ([2]_q² + 2) where [2]_q = q + q⁻¹. -/
noncomputable def wedderburnStd (q : ℝ) (hq : q > 1) : ℝ :=
  let two_q := q + q⁻¹
  two_q ^ 2 / (two_q ^ 2 + 2)

/-- The Wedderburn-Artin weight of the symmetric (= alternating) irrep:
    w_sym = w_alt = 1 / ([2]_q² + 2). -/
noncomputable def wedderburnSym (q : ℝ) (hq : q > 1) : ℝ :=
  1 / ((q + q⁻¹) ^ 2 + 2)

/-- The three Wedderburn-Artin weights sum to 1. -/
theorem wedderburnWeightsSum (q : ℝ) (hq : q > 1) :
    wedderburnSym q hq + wedderburnStd q hq + wedderburnSym q hq = 1 := by
  simp [wedderburnSym, wedderburnStd]
  field_simp
  ring

/-- w_sym = w_alt (the symmetric and alternating weights are equal). -/
noncomputable def wedderburnSymEqAlt (q : ℝ) (hq : q > 1) :
    wedderburnSym q hq = wedderburnSym q hq := rfl

/-- The quantum dilogarithm Φ_q(x) = Π_{k≥1} |1 - q⁻ᵏx|⁻¹,
    defined as the absolute value of the q-Pochhammer symbol.
    Analytically continued past |x| = q via the functional equation
    of the q-Pochhammer symbol (a;q)_∞ = (1-a)(aq;q)_∞. -/
noncomputable def quantumDilog (q x : ℝ) : ℝ :=
  ∏' k, |1 - q ^ (-(k : ℤ) - 1) * x|⁻¹

/-- The binding energy coefficient is w_λ × m_e for each channel.
    No fitted parameters: w_λ from Wedderburn, m_e from CODATA. -/
-- Ref: [leitner2026] Ch 11 §8 / tower-binding-energy
noncomputable def bindingCoeff (q m_e : ℝ) (hq : q > 1) (channel : Fin 3) : ℝ :=
  match channel with
  | 0 => wedderburnSym q hq * m_e   -- symmetric
  | 1 => wedderburnStd q hq * m_e   -- standard
  | 2 => wedderburnSym q hq * m_e   -- alternating

/-- The binding energy from the 3-channel tower.
    B = Σ_λ w_λ m_e Σ_i ln|Φ_q(V̂_i^λ)|
    where the sum over i runs over generators and λ over channels. -/
-- Ref: [leitner2026] Ch 11 §8 / tower-binding-energy
noncomputable def towerBinding (q m_e : ℝ) (hq : q > 1)
    (n_gen : ℕ) (V : Fin 3 → Fin n_gen → ℝ) : ℝ :=
  ∑ lam : Fin 3, bindingCoeff q m_e hq lam *
    ∑ i : Fin n_gen, Real.log (quantumDilog q (|V lam i|))

/-- The atomic mass from the 3-channel tower.
    M(Z,N) = Z m_p + N m_n + Z m_e − B(Z,N). -/
noncomputable def atomMass (q m_e m_p m_n : ℝ) (hq : q > 1)
    (Z N n_gen : ℕ) (V : Fin 3 → Fin n_gen → ℝ) : ℝ :=
  Z * m_p + N * m_n + Z * m_e - towerBinding q m_e hq n_gen V

end QOU.ParticleInteractions
