import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Linarith
import Mathlib.Data.Real.Basic

/-!
# QOU.MathlibExt.PlancherelRestrictionIncoherent — `d_q(λ)²` weights do not restrict from `n = 4` to `n = 3`

A trace on `H_4(q)` of the form `tr = Σ_{λ ⊢ 4} ω_λ χ^λ` restricts to `H_3(q)` with weights
`ω'_μ = Σ_{λ ⊃ μ} ω_λ`, because `χ^λ|_{H_3} = Σ_{μ ⊂ λ} χ^μ` (multiplicity-free branching).
Any trace family on the tower `H_3 ⊂ H_4` — in particular every Markov trace, at every
parameter `z` — has this property: its `H_4` weights restrict to its `H_3` weights.

The quantum Plancherel candidate puts `μ_λ ∝ d_q(λ)²`, i.e. per-character weights
`ω_λ ∝ d_q(λ)² / f^λ`, with `d_q(λ) = [n]_q! / ∏_x [h(x)]_q` (balanced `q`-integers).
This file proves that its `H_4` weights restrict to its `H_3` weights **only when**

  `[3]_q · (q − q⁻¹)⁴ = 0`,

so for real `q > 0` exactly at `q = 1`.  Hence for real `q > 0`, `q ≠ 1`, no trace family on the
tower — no Markov trace at any `z` — has quantum-Plancherel weights at both `n = 3` and `n = 4`.

This is a scope-(b) exclusion in the sense of AGENTS.md §"Before declaring refuted": the
invariant is restriction coherence of a tower trace.  It says nothing about `d_q²/D²` as a
weight on a single `H_n`, where any positive weight vector defines a trace; it excludes it as a
weight **system along the tower**.

## The data (balanced `[m] = (q^m − q^{−m})/(q − q^{−1})`)

| `λ ⊢ 4` | `f^λ` | `d_q(λ)` |       | `μ ⊢ 3` | `f^μ` | `d_q(μ)` |
|---|---|---|---|---|---|---|
| (4) | 1 | 1 | | (3) | 1 | 1 |
| (3,1) | 3 | `[3]` | | (2,1) | 2 | `[2]` |
| (2,2) | 2 | `[4]/[2]` | | (1,1,1) | 1 | 1 |
| (2,1,1) | 3 | `[3]` | | | | |
| (1⁴) | 1 | 1 | | | | |

Restricting: `ω'_(3) = ω_(4) + ω_(3,1)`, `ω'_(2,1) = ω_(3,1) + ω_(2,2) + ω_(2,1,1)`,
`ω'_(1,1,1) = ω_(2,1,1) + ω_(1⁴)`.  Coherence asks `ω'` to be a multiple of the `n = 3` weights.

Numerically at the proton `q₀ ≈ 1.10998` the mismatch is small (`[3]_{q₀} − 3 ≈ 0.044`),
which is why it is easy to miss at low working precision.
-/

namespace QOU.MathlibExt.PlancherelRestriction

variable {K : Type*} [Field K]

/-- Balanced `q`-integers `[2]`, `[3]`, `[4]`. -/
def b2 (q : K) : K := q + q⁻¹
def b3 (q : K) : K := q ^ 2 + 1 + q⁻¹ ^ 2
def b4 (q : K) : K := q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3

/-- Per-character Plancherel weights `d_q(λ)² / f^λ` on `λ ⊢ 4` (unnormalised). -/
def w4 (q : K) : Fin 5 → K
  | 0 => 1                          -- (4)
  | 1 => b3 q ^ 2 / 3               -- (3,1)
  | 2 => (b4 q / b2 q) ^ 2 / 2      -- (2,2)
  | 3 => b3 q ^ 2 / 3               -- (2,1,1)
  | 4 => 1                          -- (1⁴)

/-- Per-character Plancherel weights `d_q(μ)² / f^μ` on `μ ⊢ 3` (unnormalised). -/
def w3 (q : K) : Fin 3 → K
  | 0 => 1                          -- (3)
  | 1 => b2 q ^ 2 / 2               -- (2,1)
  | 2 => 1                          -- (1,1,1)

/-- Restriction of the `n = 4` weights to `n = 3` by the branching rule. -/
def restrict (w : Fin 5 → K) : Fin 3 → K
  | 0 => w 0 + w 1
  | 1 => w 1 + w 2 + w 3
  | 2 => w 3 + w 4

/-- The `n = 4` Plancherel weights restrict to a multiple of the `n = 3` ones. -/
def Coherent (q : K) : Prop :=
  ∃ c : K, ∀ μ, restrict (w4 q) μ = c * w3 q μ

/-- **Restriction coherence holds iff `[3]_q · (q − q⁻¹)⁴ = 0`.** -/
theorem coherent_iff [CharZero K] (q : K) (hq : q ≠ 0) (h2 : b2 q ≠ 0) :
    Coherent q ↔ b3 q * (q - q⁻¹) ^ 4 = 0 := by
  have h4 : b4 q / b2 q = b3 q - 1 := by
    rw [div_eq_iff h2]; unfold b2 b3 b4; field_simp; ring
  have key : restrict (w4 q) 1 - restrict (w4 q) 0 * w3 q 1
      = - (b3 q * (q - q⁻¹) ^ 4) / 6 := by
    simp only [restrict, w4, w3, h4]
    unfold b2 b3
    field_simp
    ring
  constructor
  · rintro ⟨c, hc⟩
    have h0 := hc 0
    have h1 := hc 1
    simp only [w3, mul_one] at h0
    have : restrict (w4 q) 1 - restrict (w4 q) 0 * w3 q 1 = 0 := by
      rw [h1, h0]; simp [w3]
    rw [key] at this
    have h6 : (6 : K) ≠ 0 := by norm_num
    have := (div_eq_zero_iff.mp this).resolve_right h6
    exact neg_eq_zero.mp this
  · intro h
    refine ⟨restrict (w4 q) 0, fun μ => ?_⟩
    fin_cases μ
    · simp [w3]
    · have : restrict (w4 q) 1 - restrict (w4 q) 0 * w3 q 1 = 0 := by rw [key, h]; simp
      exact sub_eq_zero.mp this
    · simp [restrict, w4, w3]; ring

/-- **For real `q > 0`, the Plancherel weights are restriction-coherent only at `q = 1`.**
    So for `q > 0`, `q ≠ 1`, no trace family on `H_3 ⊂ H_4` — no Markov trace at any
    parameter — carries quantum-Plancherel weights at both levels. -/
theorem not_coherent_of_pos_of_ne_one (q : ℝ) (hq : 0 < q) (h1 : q ≠ 1) :
    ¬ Coherent q := by
  have hq0 : q ≠ 0 := hq.ne'
  have h2 : b2 q ≠ 0 := by unfold b2; positivity
  rw [coherent_iff q hq0 h2]
  have hb3 : b3 q ≠ 0 := by unfold b3; positivity
  have hd : q - q⁻¹ ≠ 0 := by
    intro h
    have hsq : q ^ 2 = 1 := by
      have := sub_eq_zero.mp h
      field_simp at this
      linarith [this]
    have : (q - 1) * (q + 1) = 0 := by ring_nf; linarith
    rcases mul_eq_zero.mp this with h' | h'
    · exact h1 (by linarith)
    · linarith
  exact mul_ne_zero hb3 (pow_ne_zero 4 hd)

end QOU.MathlibExt.PlancherelRestriction
