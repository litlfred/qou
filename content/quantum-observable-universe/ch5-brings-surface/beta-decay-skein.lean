/-!
# QOU.Descartes.BetaDecaySkein — Beta decay as Skein crossing change

Beta decay is the Skein relation applied to one crossing of the
Gröbner normal form of a nuclear link.

β⁻: N̄(p,n) → N̄(p+1, n-1) ⊔ L₀⁻  (electron + antineutrino)
β⁺: N̄(p,n) → N̄(p-1, n+1) ⊔ L₀⁺  (positron + neutrino)

The Z/2 symmetry q ↔ q⁻¹ exchanges β⁻ ↔ β⁺.

LaTeX label: `def:beta-decay-skein`

## References
- [manuscript] §6/beta-decay-skein
-/

import Mathlib.Data.Real.Basic

namespace QOU.Descartes

-- ═══════════════════════════════════════════════════════════════════
-- Nuclear link type (abstract)
-- ═══════════════════════════════════════════════════════════════════

/-- A nuclear link configuration: proton count, neutron count, and
    the Gröbner normal form data. -/
-- Ref: [manuscript] §6/beta-decay-skein
structure NuclearLink where
  /-- Number of protons. -/
  p : ℕ
  /-- Number of neutrons. -/
  n : ℕ
  /-- Mass number A = p + n. -/
  A : ℕ := p + n
  /-- The categorical action S_q evaluated on this normal form. -/
  action : ℝ
  /-- The action is positive. -/
  action_pos : 0 < action

-- ═══════════════════════════════════════════════════════════════════
-- Beta decay as a Skein operation
-- ═══════════════════════════════════════════════════════════════════

/-- A beta-minus decay: the Skein crossing change d → u at one
    generator of the Gröbner normal form.

    Produces: daughter nucleus + electron T_{2,3} + antineutrino K_{0_1}. -/
-- Ref: [manuscript] §6/beta-decay-skein
structure BetaMinusDecay where
  /-- The parent nucleus. -/
  parent : NuclearLink
  /-- The daughter nucleus. -/
  daughter : NuclearLink
  /-- The daughter has one more proton. -/
  p_inc : daughter.p = parent.p + 1
  /-- The daughter has one fewer neutron. -/
  n_dec : daughter.n = parent.n - 1
  /-- Mass number is preserved. -/
  A_preserved : daughter.A = parent.A
  /-- The electron mass (trefoil T_{2,3}). -/
  m_e : ℝ
  /-- Electron mass is positive. -/
  m_e_pos : 0 < m_e
  /-- The 𝒬_q-value: categorical action difference (NOT classical energy conservation).
      𝒬_q = S_q(parent) - S_q(daughter) - S_q(electron).
      This differs from T_e + T_ν̄ + T_recoil by the q-anomaly δ_q. -/
  Q_q : ℝ := parent.action - daughter.action - m_e
  /-- The Skein relation: q[parent] - q⁻¹[daughter] = (q^½ - q^⁻½)[L₀]. -/
  skein_coefficient : ℝ  -- = q^½ - q^⁻½

/-- A beta-plus decay: the mirror Skein crossing change u → d.

    Produces: daughter nucleus + positron σ(T_{2,3}) + neutrino K_{0_1}. -/
-- Ref: [manuscript] §6/beta-decay-skein
structure BetaPlusDecay where
  /-- The parent nucleus. -/
  parent : NuclearLink
  /-- The daughter nucleus. -/
  daughter : NuclearLink
  /-- The daughter has one fewer proton. -/
  p_dec : daughter.p = parent.p - 1
  /-- The daughter has one more neutron. -/
  n_inc : daughter.n = parent.n + 1
  /-- Mass number is preserved. -/
  A_preserved : daughter.A = parent.A
  /-- The positron mass (mirror trefoil σ(T_{2,3})); same as electron mass. -/
  m_e : ℝ
  m_e_pos : 0 < m_e
  /-- The Q-value. -/
  Q : ℝ := parent.action - daughter.action - m_e

-- ═══════════════════════════════════════════════════════════════════
-- The Z/2 symmetry: q ↔ q⁻¹ exchanges β⁻ ↔ β⁺
-- ═══════════════════════════════════════════════════════════════════

/-- The weak asymmetry: S_ab(q) - S_ba(q) = (q - q⁻¹)(μ_a - μ_b)/(q^½ + q^⁻½).
    This vanishes at q = 1 (no weak force in classical limit)
    and vanishes when μ_a = μ_b (no flavour asymmetry). -/
-- Ref: [manuscript] §6/beta-decay-skein
noncomputable def weakAsymmetry (q mu_a mu_b : ℝ) (hq : 0 < q) : ℝ :=
  (q - 1/q) * (mu_a - mu_b) / (q ^ (1/2 : ℝ) + q ^ (-(1/2 : ℝ)))

/-- The weak asymmetry vanishes at q = 1. -/
-- Ref: [manuscript] §6/beta-decay-skein
theorem weakAsymmetry_classical (mu_a mu_b : ℝ) :
    weakAsymmetry 1 mu_a mu_b (by norm_num) = 0 := by
  unfold weakAsymmetry
  norm_num

/-- The weak asymmetry vanishes when μ_a = μ_b. -/
-- Ref: [manuscript] §6/beta-decay-skein
theorem weakAsymmetry_equal_mass (q mu : ℝ) (hq : 0 < q) :
    weakAsymmetry q mu mu hq = 0 := by
  unfold weakAsymmetry
  ring_nf
  simp [sub_self]

/-- The Q-value of β⁻ decay is positive when the parent action exceeds
    the daughter action plus the electron mass. -/
-- Ref: [manuscript] §6/beta-decay-skein
theorem beta_minus_Q_pos (d : BetaMinusDecay)
    (h : d.daughter.action + d.m_e < d.parent.action) :
    0 < d.Q := by
  unfold BetaMinusDecay.Q
  linarith

/-- Top-level alias matching the manifest declaration. -/
-- Ref: [manuscript] §6/beta-decay-skein
def BetaDecaySkein := BetaMinusDecay

end QOU.Descartes
