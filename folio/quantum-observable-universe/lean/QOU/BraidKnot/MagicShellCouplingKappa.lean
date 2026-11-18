import Mathlib.Tactic

/-!
# QOU.BraidKnot.MagicShellCouplingKappa

**Canonical declaration** for content block at
[`quantum-observable-universe/particle-interactions/magic-shell-coupling-kappa-table-data.ts`](quantum-observable-universe/particle-interactions/magic-shell-coupling-kappa-table-data.ts).

Formalises the manuscript magic-shell coupling table: the shell scale
`E₀ = m_e/(q(q−1))`, `h = q − q⁻¹`, and the q-integers `[2]_q = q + q⁻¹`,
`[3]_q = q² + 1 + q⁻²`, together with the identity `[3]_q = [2]_q² − 1`.
Generic over any field (§7c: `q⁻¹` needs `Field`; no ordering used).
-/

namespace QOU.BraidKnot

/-- Data for the magic-shell coupling table at `q`.

    A `definition` carrier: `q ≠ 0`, the electron scale `m_e`, the shell
    scale `E₀`, the deformation `h`, and the q-integers `[2]_q`, `[3]_q`,
    each pinned to its manuscript value. -/
structure MagicShellCouplingKappa (R : Type*) [Field R] where
  /-- Substrate parameter `q`. -/
  q : R
  /-- `q ≠ 0`. -/
  q_ne : q ≠ 0
  /-- Electron scale `m_e`. -/
  m_e : R
  /-- Shell scale `E₀ = m_e/(q(q−1))`. -/
  E0 : R
  /-- Deformation `h = q − q⁻¹`. -/
  h : R
  /-- `[2]_q = q + q⁻¹`. -/
  br2 : R
  /-- `[3]_q = q² + 1 + q⁻²`. -/
  br3 : R
  /-- `E₀ = m_e/(q(q−1))`. -/
  E0_def : E0 = m_e / (q * (q - 1))
  /-- `h = q − q⁻¹`. -/
  h_def : h = q - q⁻¹
  /-- `[2]_q = q + q⁻¹`. -/
  br2_def : br2 = q + q⁻¹
  /-- `[3]_q = q² + 1 + q⁻²`. -/
  br3_def : br3 = q ^ 2 + 1 + q⁻¹ ^ 2

-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/magic-shell-coupling-kappa-table-data.ts

/-- The q-integer identity `[3]_q = [2]_q² − 1` (since
    `(q + q⁻¹)² = q² + 2 + q⁻²`). -/
theorem br3_eq_br2_sq_sub_one {R : Type*} [Field R]
    (M : MagicShellCouplingKappa R) : M.br3 = M.br2 ^ 2 - 1 := by
  rw [M.br3_def, M.br2_def]
  have hq : M.q ≠ 0 := M.q_ne
  field_simp
  ring

/-- Subtracting the squared second q-integer minus one from the third q-integer yields zero. -/
theorem br3_sub_br2_sq_sub_one_eq_zero {R : Type*} [Field R]
    (M : MagicShellCouplingKappa R) : M.br3 - (M.br2 ^ 2 - 1) = 0 := by
  rw [br3_eq_br2_sq_sub_one M, sub_self]

end QOU.BraidKnot
