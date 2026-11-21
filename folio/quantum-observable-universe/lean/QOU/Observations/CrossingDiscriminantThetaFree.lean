/-
# The crossing-energy discriminant does not depend on the substrate phase

Bean `qou-hjs8`; issue #7278.

`conj:complex-chirality-rotation` writes a substrate phase `θ` into `q = |q|e^{iθ}`
and reads off an "experimental discriminant"

  δ_CP = (|S_c(T)| − |S_c(T^σ)|) / (|S_c(T)| + |S_c(T^σ)|) ∼ O(θ²),

said to vanish to first order and so to "match electron-positron mass equality".

This file formalises why **no** such quantity can depend on `θ`, and what it
equals instead.  The mathematical content is one observation: the discriminant
is a function of the two **moduli**, and a phase has modulus one.  So `θ` cannot
enter through a phase — and the thing that does enter is the corpus's own mirror
rule, which inverts the modulus rather than conjugating a phase
(`prop:antiparticle-crossing-reversal` item 2:
`𝔈_cross(𝔥^σ) = −𝔈_cross(𝔥)|_{q ↔ q⁻¹}`).

Nothing here proves anything about electrons, crossing energies, or CP.  It
proves two facts about the *shape* of the discriminant, which is what the
disagreement between the blocks is actually about.  The numerical evaluation at
the substrate anchor lives in
`computations/cp/delta_cp_theta_order_and_mass_asymmetry_probe.py`, per §7c —
nothing below needs an anchor, so nothing below mentions one.

-- Ref: [leitner2026] `conj:complex-chirality-rotation`,
--      `prop:antiparticle-crossing-reversal`, `def:crossing-energy`
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.Observations.CrossingDiscriminantThetaFree

open scoped Real

/-- The discriminant the block forms, as a function of the two **moduli**.
This is the whole point: it is a function of `‖·‖` alone, so it is blind to
every phase by construction. -/
noncomputable def crossingDisc (a b : ℝ) : ℝ := (a - b) / (a + b)

/-- **Item 1's reading, carried to its conclusion.**  `conj:complex-chirality-
rotation` item 1 says the mirror multiplies `S_c` by `e^{-i n_c θ}` where the
particle carries `e^{+i n_c θ}`.  A phase has modulus one, so the two moduli
coincide and the discriminant is **identically zero** — to all orders, not to
first.  The block's own item 1 therefore contradicts its own `O(θ²)`. -/
theorem crossingDisc_self (a : ℝ) : crossingDisc a a = 0 := by
  simp [crossingDisc]

/-- **The corpus's reading.**  Under `prop:antiparticle-crossing-reversal` the
mirror sends the modulus `c·r` to `c/r`.  The discriminant is then
`(r² − 1)/(r² + 1)` — and note the overall factor `c` **cancels**, so it is
independent of the crossing count as well as of the phase. -/
theorem crossingDisc_scale_inv {c r : ℝ} (hc : c ≠ 0) (hr : 0 < r) :
    crossingDisc (c * r) (c / r) = (r ^ 2 - 1) / (r ^ 2 + 1) := by
  have hr' : r ≠ 0 := ne_of_gt hr
  have hden : r ^ 2 + 1 ≠ 0 := by positivity
  unfold crossingDisc
  rw [div_eq_div_iff (by
        field_simp
        positivity) hden]
  field_simp

/-- `(r² − 1)/(r² + 1) = tanh (log r)` — the closed form the probe reports. -/
theorem disc_eq_tanh_log {r : ℝ} (hr : 0 < r) :
    (r ^ 2 - 1) / (r ^ 2 + 1) = Real.tanh (Real.log r) := by
  have hr' : r ≠ 0 := ne_of_gt hr
  rw [Real.tanh_eq_sinh_div_cosh, Real.sinh_eq, Real.cosh_eq,
    Real.exp_log hr, Real.exp_neg, Real.exp_log hr]
  field_simp

/-- **The θ-free statement, with the phase present and explicit.**  Write the
particle's crossing energy as `n·q` and the mirror's as `−n/q` with
`q = r·e^{iθ}` — which is `def:crossing-energy` on an all-positive braid
together with `prop:antiparticle-crossing-reversal` item 2.  Then the
discriminant of their norms equals `(r² − 1)/(r² + 1)` **for every** `θ`.

`θ` is bound on the left and absent on the right: that is the refutation of the
`O(θ²)` claim, and it is not an approximation. -/
theorem crossingDisc_norm_theta_free {n r : ℝ} (hn : 0 < n) (hr : 0 < r) (θ : ℝ) :
    crossingDisc ‖(n : ℂ) * ((r : ℂ) * Complex.exp ((θ : ℂ) * Complex.I))‖
      ‖-(n : ℂ) / ((r : ℂ) * Complex.exp ((θ : ℂ) * Complex.I))‖
      = (r ^ 2 - 1) / (r ^ 2 + 1) := by
  have hexp : ‖Complex.exp ((θ : ℂ) * Complex.I)‖ = 1 :=
    Complex.norm_exp_ofReal_mul_I θ
  have hnorm₁ : ‖(n : ℂ) * ((r : ℂ) * Complex.exp ((θ : ℂ) * Complex.I))‖ = n * r := by
    rw [norm_mul, norm_mul, hexp, Complex.norm_real, Complex.norm_real,
      Real.norm_of_nonneg hn.le, Real.norm_of_nonneg hr.le, mul_one]
  have hnorm₂ : ‖-(n : ℂ) / ((r : ℂ) * Complex.exp ((θ : ℂ) * Complex.I))‖ = n / r := by
    rw [norm_div, norm_neg, norm_mul, hexp, Complex.norm_real, Complex.norm_real,
      Real.norm_of_nonneg hn.le, Real.norm_of_nonneg hr.le, mul_one]
  rw [hnorm₁, hnorm₂]
  exact crossingDisc_scale_inv (ne_of_gt hn) hr

/-- For a substrate with `|q| > 1` the discriminant is **strictly positive** —
so the `q ↔ q⁻¹` asymmetry the mirror introduces is not merely nonzero at some
orders, it never vanishes.  This is the direction that does work: no choice of
phase can make the two crossing energies agree in magnitude. -/
theorem crossingDisc_pos_of_one_lt {r : ℝ} (hr : 1 < r) :
    0 < (r ^ 2 - 1) / (r ^ 2 + 1) := by
  have h1 : (0 : ℝ) < r ^ 2 - 1 := by nlinarith
  have h2 : (0 : ℝ) < r ^ 2 + 1 := by positivity
  exact div_pos h1 h2

end QOU.Observations.CrossingDiscriminantThetaFree
