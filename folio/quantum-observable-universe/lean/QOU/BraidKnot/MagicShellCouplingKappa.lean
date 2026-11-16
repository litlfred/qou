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

/-! ## The `v`-level passage (`q = v²`) and `1/g = 5g(1 + x/5)` criticality identity (`qou-xajh`)

Operationalizes the half-power (`v = √q`, `q = v²`) passage connecting the substrate deformation
`h = q - q⁻¹` to the `v`-level symmetric quantum integer `[2]_v = v + v⁻¹` and deformation
parameter `x = (v - v⁻¹)²`:
1. `q - q⁻¹ = v² - v⁻² = (v - v⁻¹) · [2]_v`.
2. `(q - q⁻¹)² = x · (4 + x)` where `x = (v - v⁻¹)²` and `[2]_v² = 4 + x`.
3. Under the fusion-frame criticality relation `g² · (5 + x) = 1`, the reciprocal deformation `g⁻¹`
   and the classical-count deformation `5g` satisfy the exact resummed identity
   `g⁻¹ = (5g) · (1 + x/5)` and `g⁻¹ - 5g = g · x`. -/

/-- **The `v`-level passage identity (`qou-xajh`):** for `q = v²` (`v ≠ 0`),
`q - q⁻¹ = (v - v⁻¹) · (v + v⁻¹) = (v - v⁻¹) · [2]_v`. -/
theorem q_sub_qinv_eq_v_level {R : Type*} [Field R] (v : R) (hv : v ≠ 0) :
    v ^ 2 - (v ^ 2)⁻¹ = (v - v⁻¹) * (v + v⁻¹) := by
  field_simp
  ring

/-- **Squared `v`-level passage (`qou-xajh`):** with `x = (v - v⁻¹)²`, the squared `q`-deformation
`(v² - v⁻²)²` equals `(v - v⁻¹)² · (4 + (v - v⁻¹)²) = x(4 + x)`. -/
theorem q_sub_qinv_sq_eq_x_mul_four_plus_x {R : Type*} [Field R] (v : R) (hv : v ≠ 0) :
    (v ^ 2 - (v ^ 2)⁻¹) ^ 2 = (v - v⁻¹) ^ 2 * (4 + (v - v⁻¹) ^ 2) := by
  field_simp
  ring

/-- **Resummed `1/g = 5g(1 + x/5)` criticality identity (`qou-xajh`):** whenever `g² · (5 + x) = 1`
in a field of characteristic ≠ 5 (`(5 : R) ≠ 0`, `g ≠ 0`), `g⁻¹ = (5 * g) * (1 + x / 5)`. -/
theorem inv_g_eq_five_g_mul_one_plus_x_div_five {R : Type*} [Field R]
    (g x : R) (hg : g ≠ 0) (h5 : (5 : R) ≠ 0) (hcrit : g ^ 2 * (5 + x) = 1) :
    g⁻¹ = (5 * g) * (1 + x / 5) := by
  apply mul_left_cancel₀ hg
  rw [mul_inv_cancel₀ hg, ← hcrit]
  field_simp
  ring

/-- **First-order difference `1/g - 5g = g · x` (`qou-xajh`):** whenever `g² · (5 + x) = 1`
and `g ≠ 0`, the shift between the `1/g` and `5g` readings is `g * x`. -/
theorem inv_g_sub_five_g_eq_g_mul_x {R : Type*} [Field R]
    (g x : R) (hg : g ≠ 0) (hcrit : g ^ 2 * (5 + x) = 1) :
    g⁻¹ - 5 * g = g * x := by
  apply mul_left_cancel₀ hg
  have hgi : g * g⁻¹ = g ^ 2 * (5 + x) := by
    rw [mul_inv_cancel₀ hg, hcrit]
  calc
    g * (g⁻¹ - 5 * g) = g * g⁻¹ - 5 * g ^ 2 := by ring
    _ = g ^ 2 * (5 + x) - 5 * g ^ 2 := by rw [hgi]
    _ = g * (g * x) := by ring

end QOU.BraidKnot

