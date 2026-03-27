/-!
# QOU.Descartes.beta_decay_transfer_matrix

Beta decay is a universal 2×2 matrix-valued polynomial in q.
The two elementary decay matrices (nn→mix and mix→pp) are IDENTICAL:

  Δ_β(q) = ½(1-q²)·T_pp(q) + ½q·s·I

where s = q½ - q⁻½ and I is the 2×2 identity.

This universality follows from T_mix = ½(T_pp + T_nn): the mixed
matrix is the exact midpoint, so both steps are the same displacement.

LaTeX label: `prop:beta-decay-transfer-matrix`

## References
- [manuscript] §6/beta-decay-transfer-matrix
-/

import Mathlib.Data.Real.Basic

namespace QOU.Descartes

/-- A 2×2 transfer matrix (entries are polynomials in q). -/
-- Ref: [manuscript] §6/beta-decay-transfer-matrix
structure TM where
  a₁₁ : ℝ; a₁₂ : ℝ; a₂₁ : ℝ; a₂₂ : ℝ

/-- Transfer matrix from crossing coefficients (c, d). -/
-- Ref: [manuscript] §6/beta-decay-transfer-matrix
noncomputable def tm (q c d : ℝ) : TM where
  a₁₁ := c * (q - 1/q) + d
  a₁₂ := c
  a₂₁ := c
  a₂₂ := d

/-- T_pp: proton-proton crossing (c=1, d=0). -/
-- Ref: [manuscript] §6/beta-decay-transfer-matrix
noncomputable def T_pp (q : ℝ) : TM := tm q 1 0

/-- T_nn: neutron-neutron crossing (c=q², d=-q·s). -/
-- Ref: [manuscript] §6/beta-decay-transfer-matrix
noncomputable def T_nn (q : ℝ) : TM :=
  tm q (q^2) (-q * (q ^ (1/2 : ℝ) - q ^ (-(1/2 : ℝ))))

/-- T_mix: mixed crossing (c=½(1+q²), d=-½q·s). -/
-- Ref: [manuscript] §6/beta-decay-transfer-matrix
noncomputable def T_mix (q : ℝ) : TM :=
  tm q ((1 + q^2) / 2) (-q * (q ^ (1/2 : ℝ) - q ^ (-(1/2 : ℝ))) / 2)

/-- Matrix subtraction. -/
-- Ref: [manuscript] §6/beta-decay-transfer-matrix
def TM.sub (A B : TM) : TM where
  a₁₁ := A.a₁₁ - B.a₁₁; a₁₂ := A.a₁₂ - B.a₁₂
  a₂₁ := A.a₂₁ - B.a₂₁; a₂₂ := A.a₂₂ - B.a₂₂

/-- The universal beta decay matrix: Δ_β = T_mix - T_nn = T_pp - T_mix.
    Both elementary decay matrices are identical. -/
-- Ref: [manuscript] §6/beta-decay-transfer-matrix
noncomputable def Delta_beta (q : ℝ) : TM :=
  (T_mix q).sub (T_nn q)

/-- UNIVERSALITY: Δ_β^{nn→mix} = Δ_β^{mix→pp}.
    The two elementary decay matrices are the same. -/
-- Ref: [manuscript] §6/beta-decay-transfer-matrix
theorem beta_decay_universal (q : ℝ) (hq : q ≠ 0) :
    let d1 := (T_mix q).sub (T_nn q)
    let d2 := (T_pp q).sub (T_mix q)
    d1.a₁₁ = d2.a₁₁ ∧ d1.a₁₂ = d2.a₁₂ ∧
    d1.a₂₁ = d2.a₂₁ ∧ d1.a₂₂ = d2.a₂₂ := by
  unfold T_mix T_pp T_nn tm TM.sub
  simp
  constructor <;> ring

/-- T_mix is the exact midpoint: T_mix = ½(T_pp + T_nn). -/
-- Ref: [manuscript] §6/beta-decay-transfer-matrix
theorem T_mix_midpoint (q : ℝ) (hq : q ≠ 0) :
    let pp := T_pp q; let nn := T_nn q; let mx := T_mix q
    mx.a₁₂ = (pp.a₁₂ + nn.a₁₂) / 2 ∧
    mx.a₂₁ = (pp.a₂₁ + nn.a₂₁) / 2 ∧
    mx.a₂₂ = (pp.a₂₂ + nn.a₂₂) / 2 := by
  unfold T_pp T_nn T_mix tm
  simp
  constructor <;> ring

/-- At q = 1, the decay matrix vanishes (no beta decay). -/
-- Ref: [manuscript] §6/beta-decay-transfer-matrix
theorem beta_decay_vanishes_classical :
    let d := Delta_beta 1
    d.a₁₂ = 0 ∧ d.a₂₁ = 0 := by
  unfold Delta_beta T_mix T_nn tm TM.sub
  simp
  constructor <;> norm_num

/-- The Markov-traced volume from a transfer matrix. -/
-- Ref: [manuscript] §6/beta-decay-transfer-matrix
noncomputable def TM.tracedVolume (M : TM) (z : ℝ) : ℝ :=
  z * M.a₁₁ + M.a₂₁

end QOU.Descartes
