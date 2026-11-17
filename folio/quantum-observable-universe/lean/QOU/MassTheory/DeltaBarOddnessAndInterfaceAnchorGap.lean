import Mathlib.Tactic

/-!
# Delta Bar-Oddness and Interface Anchor Offset (`qou-gw96`, `qou-nlw5`)

This module formalizes two nuclear-binding structural results under `qou-v2om`:

1. **Bar-oddness of `Δ_S` forces the `h²/2` even constant (`qou-gw96`)**:
   On the diagram-symmetric `H₃` ansatz `x = c · 1 + d (σ₀ + σ₁)`, the Kazhdan–Lusztig
   bar involution (`bar(q) = q⁻¹`, `bar(h) = -h`, `bar(σ_i) = σ_i - h`) maps `x` to
   `(c̄ - 2 h d̄) · 1 + d̄ (σ₀ + σ₁)`. When `d = -h/2` (`d̄ = h/2 = -d`), the bar-oddness
   condition `bar(x) = -x` reduces to `c + c̄ = h²`, forcing the bar-even part of `c`
   to be `h²/2` and yielding the counit `net(Δ_S) = c + 2d = h²/2 - h = ε_{NP,q}` at `c = h²/2`.

2. **Interface `d` offset vs colour-blind midpoint and implied `h` shift (`qou-nlw5`)**:
   The colour-weighted `p-n` interface offset `d_cw(h, δ) = -h (1/2 - δ/4)` differs from
   the colour-blind midpoint `-h/2` by `+h δ / 4`, so its implied Hecke parameter
   `h_implied = -2 d_cw = h (1 - δ/2)` is shifted below `h` by `-h δ / 2`.
-/

namespace QOU.MassTheory

/-- Constant (`1`) coordinate `c̄ - 2 h d̄` of `bar(c · 1 + d (σ₀ + σ₁))` in `H₃(q)` (`qou-gw96`). -/
def barConstCoord (c_bar h d_bar : ℚ) : ℚ :=
  c_bar - 2 * h * d_bar

/-- Counit `net(c · 1 + d (σ₀ + σ₁)) = c + 2d` (`qou-gw96`). -/
def counitNet (c d : ℚ) : ℚ :=
  c + 2 * d

/-- At `d = -h/2` (`d̄ = h/2`), bar-oddness `barConstCoord c_bar h (h/2) = -c` holds iff
`c + c_bar = h²`, and at the pure bar-even choice `c = c_bar = h²/2` the counit equals
`h²/2 - h` (`qou-gw96`). -/
theorem barOdd_iff_sum_eq_h_sq_and_counit (c c_bar h : ℚ) :
    (barConstCoord c_bar h (h / 2) = -c ↔ c + c_bar = h ^ 2) ∧
    barConstCoord (h ^ 2 / 2) h (h / 2) = -(h ^ 2 / 2) ∧
    counitNet (h ^ 2 / 2) (-h / 2) = h ^ 2 / 2 - h := by
  unfold barConstCoord counitNet
  refine ⟨⟨fun h1 => by linarith, fun h2 => by linarith⟩, by ring, by ring⟩

/-- Colour-weighted `p-n` interface offset `-h (1/2 - δ/4)` (`qou-nlw5`). -/
def colourWeightedOffset (h delta : ℚ) : ℚ :=
  -h * (1 / 2 - delta / 4)

/-- Colour-blind midpoint offset `-h/2` (`qou-nlw5`). -/
def colourBlindMidpoint (h : ℚ) : ℚ :=
  -h / 2

/-- Implied Hecke parameter `-2d` under the midpoint inversion (`qou-nlw5`). -/
def impliedHeckeH (d : ℚ) : ℚ :=
  -2 * d

/-- Exact offset `d_cw - (-h/2) = h δ / 4` and implied-`h` shift
`h_implied - h = -h δ / 2`, with strict ordering when `h > 0` and `δ > 0` (`qou-nlw5`). -/
theorem colourWeighted_vs_midpoint_and_impliedH (h delta : ℚ)
    (hh : 0 < h) (hdelta : 0 < delta) :
    colourWeightedOffset h delta - colourBlindMidpoint h = h * delta / 4 ∧
    impliedHeckeH (colourWeightedOffset h delta) = h * (1 - delta / 2) ∧
    impliedHeckeH (colourWeightedOffset h delta) - h = -(h * delta / 2) ∧
    colourBlindMidpoint h < colourWeightedOffset h delta ∧
    impliedHeckeH (colourWeightedOffset h delta) < h := by
  unfold colourWeightedOffset colourBlindMidpoint impliedHeckeH
  have hprod : 0 < h * delta := mul_pos hh hdelta
  refine ⟨by ring, by ring, by ring, by linarith, by linarith⟩

end QOU.MassTheory
