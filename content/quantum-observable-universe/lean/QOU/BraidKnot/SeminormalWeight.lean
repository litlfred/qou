/-
# Seminormal weights — the `a_ρ = h/(1 − q^{−2ρ})` sum infrastructure

Foundational Mathlib-gap infra for the **Young seminormal character sum** that the
corpus repeatedly cites as *"not in Mathlib"* (e.g. `symbolic_character_table`,
`QHeckeSeminormalCharacterClosure`). Mathlib carries `YoungDiagram` and
`SemistandardTableau` but **no** standard-tableau seminormal representation, so
the single-generator character

  χ_λ(σ) = Σ_{T ∈ SYT(λ)}  a_{ρ(T)},        a_ρ = h / (1 − q^{−2ρ}),  h = q − q⁻¹

has no home. This file supplies the **weight layer** (bean `qou-mcbf`, Infra 2):
the reduced weight `g_ρ = 1/(1 − q^{−2ρ})`, the factorisation `a_ρ = h · g_ρ`
(the algebraic *source* of the `· h` in the closed form `χ_λ(σ) = c_λ · h`), and
the **pairing identity** `g_ρ + g_{−ρ} = 1` — the structural fact that makes a sum
of reduced weights over a ρ ↔ −ρ symmetric tableau set an **integer** `c_λ`.

Base ring (§7c): pure algebra over a generic `[Field R]` with `q ≠ 0` — no
archimedean structure (`Real.sqrt`, ordering) is used, so this is *not* `ℝ`-locked.
The `q₀`-evaluation lives downstream, past the substrate→archimedean wall.

-- Ref: [sagan2001] The Symmetric Group, §3.3 (Young's seminormal form)
-- Ref: [manuscript] quantum-observable-universe/mass-theory/symbolic-character-table.md
-/
import Mathlib.Tactic

namespace QOU.BraidKnot.SeminormalWeight

variable {R : Type*} [Field R]

/-- **Reduced seminormal weight** `g_ρ = 1/(1 − q^{−2ρ})` — the dimensionless part
    of the axial-distance weight, `ρ : ℤ` the axial distance between the boxes
    holding `i` and `i+1` in a standard tableau. -/
noncomputable def reducedWeight (q : R) (ρ : ℤ) : R := (1 - q ^ (-2 * ρ))⁻¹

/-- **Seminormal weight** `a_ρ = h / (1 − q^{−2ρ})`, `h = q − q⁻¹` the Hecke
    parameter (AGENTS.md §7a). -/
noncomputable def seminormalWeight (q h : R) (ρ : ℤ) : R := h * reducedWeight q ρ

/-- **The `h` factors out.** `a_ρ = h · g_ρ`. This is the algebraic source of the
    `· h` in the character closed form `χ_λ(σ) = c_λ · h`: every summand carries a
    single factor of `h`, so the whole character does. -/
theorem seminormalWeight_eq_h_mul (q h : R) (ρ : ℤ) :
    seminormalWeight q h ρ = h * reducedWeight q ρ := rfl

/-- Rewriting `q^{−2ρ}` as `(q^{2ρ})⁻¹`. -/
theorem reducedWeight_eq (q : R) (ρ : ℤ) :
    reducedWeight q ρ = (1 - (q ^ (2 * ρ))⁻¹)⁻¹ := by
  unfold reducedWeight
  rw [show (-2 * ρ) = -(2 * ρ) by ring, zpow_neg]

/-- **The pairing identity** `g_ρ + g_{−ρ} = 1`.

    With `x = q^{2ρ}`: `g_ρ = (1 − x⁻¹)⁻¹ = x/(x−1)` and `g_{−ρ} = (1 − x)⁻¹ =
    −1/(x−1)`, so the sum telescopes to `1`. This is *why* a reduced-weight sum
    over a ρ ↔ −ρ symmetric standard-tableau set is an **integer** `c_λ`: the
    off-diagonal boxes pair up, each pair contributing `1`. Hypotheses: `q ≠ 0`
    (so `zpow` inverts) and `q^{2ρ} ≠ 1` (so no box sits on the diagonal, i.e.
    `i, i+1` are neither same-row nor same-column). -/
theorem reducedWeight_add_neg (q : R) (ρ : ℤ) (hq : q ≠ 0)
    (hx : q ^ (2 * ρ) ≠ 1) :
    reducedWeight q ρ + reducedWeight q (-ρ) = 1 := by
  rw [reducedWeight_eq, show reducedWeight q (-ρ) = (1 - q ^ (2 * ρ))⁻¹ by
        unfold reducedWeight; rw [show (-2 * -ρ) = 2 * ρ by ring]]
  set x := q ^ (2 * ρ) with hxdef
  have hx0 : x ≠ 0 := zpow_ne_zero _ hq
  clear_value x
  have hxinv : x⁻¹ ≠ 1 := fun h => hx (inv_eq_one.mp h)
  have h2 : (1 : R) - x⁻¹ ≠ 0 := sub_ne_zero.mpr (Ne.symm hxinv)
  have hx1 : x - 1 ≠ 0 := sub_ne_zero.mpr hx
  have A : (1 - x⁻¹)⁻¹ = x / (x - 1) := by
    have hnum : 1 - x⁻¹ = (x - 1) / x := by field_simp
    rw [hnum, inv_div]
  have B : (1 - x)⁻¹ = -(1 / (x - 1)) := by
    rw [show (1 : R) - x = -(x - 1) by ring, ← neg_inv, one_div]
  rw [A, B]
  field_simp
  ring