/-
# The `Q_β` functional from the categorical quantum trace: one closed form for every rank

Bean `qou-99qc`. Owner request 2026-11-20: walk the chain from the Frobenius pairing,
the categorical Lagrangian and the non-abelian holonomy, and see where `Q_β` lands.

The mass identity (`def:mass-identity`) reads a braid with the Frobenius form `∫_A`,
which `prop:feynman-categorical-trace` identifies, for `C = Rep(SU_q(N))` acting on
`V^{⊗n}`, with the quantum trace normalised by `dim_q(V^{⊗n})`. Its block weights are
`y_λ = dim_q(V_λ)/[N]^n`. Writing `a = q^N`, a quantum integer shifted by `N` is
`[N + k] = (a q^k - (a q^k)⁻¹)/(q - q⁻¹)`.

`QBetaChiralityReduction.lean` shows that on the typed-crossing difference `Δ_S` the
two-row block `(2,1)` is invisible, so the functional is
`(h[2]/2)·(y_(3) - y_(1³))`, `h = q - q⁻¹`, `[2] = q + q⁻¹`.

## What is proved (generic field, no `ℝ`, no `sorry`)

* `qtrace_family_closed_form`: `(h[2]/2)(y_(3) - y_(1³)) = (h²/2)·(a² + 1)/(a² - 1)`.
  With `q = e^λ`, `a = e^{Nλ}` this is `(h²/2)·coth(Nλ)`: one function of the rank.
* `qtrace_family_rank_one`: at `a = q` (rank 1) the value is `h[2]/2`, the augmentation.
* `qtrace_family_rank_two`: at `a = q²` (rank 2) the value is
  `(h[2]/2)·(q⁴+1)/(q²+1)²`, i.e. the convention-D trace `z_D = q³/(q²+1)` already ruled.
* `framed_sigma_eq_framed_sigmaInv`: the framing-corrected trace of `def:mass-identity`
  gives `σ` and `σ⁻¹` the same value `q/(q²+1)` at `z_D`.

## What is NOT proved

Which rank the decay channel uses. `C = Rep(SU_q(2))` is the corpus's `C`, which gives
`z_D`. The energy scale `E₀` is not touched here. Nothing here selects a rank by its
residual against CODATA (AGENTS.md §NO FITTING).

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [reshetikhin-turaev1990] (quantum trace of Rep(U_q g))
-/
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.QBeta.QuantumTraceFamilyCoth

variable {K : Type*} [Field K]

/-- The quantum number `(x - x⁻¹)/(q - q⁻¹)`; with `x = q^k` it is `[k]_q`. -/
def qnum (q x : K) : K := (x - x⁻¹) / (q - q⁻¹)

/-- Weight of the symmetric block `(3)` in `V^{⊗3}`, `V` the rank-`N` fundamental, `a = q^N`. -/
def ySym (q a : K) : K :=
  qnum q (a * q) * qnum q (a * q ^ 2) / (qnum q (q ^ 2) * qnum q (q ^ 3) * qnum q a ^ 2)

/-- Weight of the sign block `(1³)`. -/
def yAlt (q a : K) : K :=
  qnum q (a / q) * qnum q (a / q ^ 2) / (qnum q (q ^ 2) * qnum q (q ^ 3) * qnum q a ^ 2)

section Family

variable {q a : K} (h2 : (2 : K) ≠ 0) (hq : q ≠ 0) (ha : a ≠ 0) (hq2 : q ^ 2 - 1 ≠ 0)
  (ha2 : a ^ 2 - 1 ≠ 0) (hn : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0)
include h2 hq ha hq2 ha2 hn h3

theorem qtrace_family_closed_form :
    (q - q⁻¹) * (q + q⁻¹) / 2 * (ySym q a - yAlt q a) =
      (q - q⁻¹) ^ 2 / 2 * ((a ^ 2 + 1) / (a ^ 2 - 1)) := by
  have hqq : q - q⁻¹ ≠ 0 := by
    intro h; apply hq2
    have e : q ^ 2 - 1 = q * (q - q⁻¹) := by field_simp
    rw [e, h, mul_zero]
  have hD : (1 + (-q ^ 4 - q ^ 6) + q ^ 10 : K) ≠ 0 := by
    rw [show (1 + (-q ^ 4 - q ^ 6) + q ^ 10 : K)
        = ((q ^ 2 - 1) * (q ^ 2 + 1)) * ((q ^ 2 - 1) * (q ^ 4 + q ^ 2 + 1)) by ring]
    exact mul_ne_zero (mul_ne_zero hq2 hn) (mul_ne_zero hq2 h3)
  unfold ySym yAlt qnum
  field_simp
  ring_nf
  linear_combination (a ^ 4 - 1) * mul_inv_cancel₀ hD

end Family

theorem qtrace_family_rank_one {q : K} (hq : q ≠ 0) (hq2 : q ^ 2 - 1 ≠ 0) :
    (q - q⁻¹) ^ 2 / 2 * ((q ^ 2 + 1) / (q ^ 2 - 1)) = (q - q⁻¹) * (q + q⁻¹) / 2 := by
  field_simp

theorem qtrace_family_rank_two {q : K} (h2 : (2 : K) ≠ 0) (hq : q ≠ 0)
    (hq4 : (q ^ 2) ^ 2 - 1 ≠ 0) (hn : q ^ 2 + 1 ≠ 0) :
    (q - q⁻¹) ^ 2 / 2 * (((q ^ 2) ^ 2 + 1) / ((q ^ 2) ^ 2 - 1)) =
      (q - q⁻¹) * (q + q⁻¹) / 2 * ((q ^ 4 + 1) / (q ^ 2 + 1) ^ 2) := by
  have h4' : (-1 + q ^ 4 : K) ≠ 0 := by
    rw [show (-1 + q ^ 4 : K) = (q ^ 2) ^ 2 - 1 by ring]; exact hq4
  field_simp
  ring_nf
  field_simp
  ring

/-- Framing correction `q^{-2w}` at `z_D`: `σ` (writhe 1, trace `z_D`) and `σ⁻¹`
(writhe −1, trace `z_D - h`) get the same framed value `q/(q²+1)`. -/
theorem framed_sigma_eq_framed_sigmaInv {q : K} (hq : q ≠ 0) (hn : q ^ 2 + 1 ≠ 0) :
    (q ^ 2)⁻¹ * (q ^ 3 / (q ^ 2 + 1)) = q / (q ^ 2 + 1) ∧
      q ^ 2 * (q ^ 3 / (q ^ 2 + 1) - (q - q⁻¹)) = q / (q ^ 2 + 1) := by
  refine ⟨by field_simp, ?_⟩
  field_simp
  ring

end QOU.QBeta.QuantumTraceFamilyCoth
