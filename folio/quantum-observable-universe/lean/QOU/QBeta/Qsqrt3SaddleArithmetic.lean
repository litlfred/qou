import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith

/-!
# QOU.QBeta.Qsqrt3SaddleArithmetic

**The even-channel resurgence action's arithmetic home is ℚ(√3).**

The 4₁ (figure-eight) Kashaev sum `Σ_k exp(2 Σ_{j≤k} log(2 sin(πj/N)))` localises,
in the `N → ∞` volume-conjecture limit, at the saddle `x* = 5/6` (the maximum of
`G(x) = ∫₀ˣ log(2 sin πs) ds`, where `G'(x*) = log(2 sin(5π/6)) = log 1 = 0`). The
perturbative expansion around that saddle is built from the Taylor derivatives of
`log(2 sin πx)` at `x*`, and **those derivatives are exact elements of
`ℚ(√3)·π^k`** — real quadratic data. The invariant trace field of 4₁ is the
*imaginary* quadratic field `ℚ(√−3)` (Eisenstein / hexagonal); it is a **distinct**
number field from the totally real `ℚ(√3)` that carries the certified saddle data.
Both sit inside the cyclotomic field `ℚ(ζ₁₂)`, and `√−3 = i·√3` relates the two
generators, but the fields themselves are not equal (one totally real, one
imaginary quadratic). This file certifies the real `ℚ(√3)` saddle arithmetic; the
`ℚ(√−3)` trace field is the ambient classical fact it refracts.

This file certifies that arithmetic, sorry-free:

* `sin_saddle` / `grad_saddle_zero` — `x* = 5/6` is a critical point.
* `cot_saddle` / `hessian_eq` — the Hessian `G''(x*) = π·cot(5π/6) = −√3·π ∈ ℚ(√3)·π`.
* `laplaceB1_at_saddle` — the leading saddle-Laplace coefficient
  `b₁ = g₄/(8 g₂²) + 5 g₃²/(24 |g₂|³)` evaluated at the exact **exponent** Taylor
  data `g_k = 2·G^{(k)}(x*)` (the sum is `exp(2N·G)`, so the Laplace exponent is
  `2G`), i.e. `(g₂, g₃, g₄) = (−2√3π, −8π², −16√3π³)`, equals
  **`√3·π/54 ∈ ℚ(√3)·π`** — an exact arithmetic object, replacing the
  entropy-blocked numerical PSLQ of #3571.
* `ohtsukiKappa1` / `ohtsukiKappa1_eq_eleven_halves_b1` — the observable leading
  coefficient `κ₁ = 11·√3·π/108 = (11/2)·b₁` (numerically identified; Lean proves
  the `(11/2)` algebra), also in `ℚ(√3)·π` (`ohtsukiKappa1_mem_qsqrt3`).

## Honest scope (anti-laundering): arithmetic *home*, NOT a closed action value

`b₁` is the **naive integral-Laplace** coefficient. It does **not** equal the
*observable* action coefficient `c₁ ≈ 0.554` (numerically fitted in #3571):
`b₁ = √3π/54 ≈ 0.101` (`laplaceB1_at_saddle`), a rational multiple of `√3·π`
(`laplaceB1_saddle_mem_qsqrt3`). The observable adds the Euler–Maclaurin
sum-vs-integral correction of the discrete Kashaev *sum*: the leading observable
coefficient `κ₁ = [1/N] log J_N(4₁)` is (numerically, `qbeta_ohtsuki_kappa1_extract.py`,
≈23-digit + 33-digit PSLQ) the **exact** element `κ₁ = 11·√3·π/108 = (11/2)·b₁`
(`ohtsukiKappa1`, `ohtsukiKappa1_eq_eleven_halves_b1`) — the sum-correction is
exactly the factor `11/2` (Ohtsuki's figure-eight 2-loop numerator `11`,
`κ_1^Oht = (11/72)/√−3`). So both `b₁` and `κ₁` live in `ℚ(√3)·π`
(`…_mem_qsqrt3`); the observable's leading coefficient is now known exactly, and
`κ₁ ≠ b₁`. Higher-order `[1/N^k]` coefficients (the full ladder) remain
entropy-blocked (#3571). **Epistemic honesty:** the `κ₁ = 11√3π/108` *value* is
the numerical Ohtsuki identification, not proved here from the sum; Lean certifies
only the algebra `κ₁ = (11/2)·b₁` and the field membership. This file proves the
`ℚ(√3)` arithmetic of the even channel; it launders **no** Q_β action value — the
4₁-Kashaev ↔ Q_β bridge is the open keystone, nothing is wired.

Even-channel counterpart of the odd-channel `HopfCubicOddCarrier` (KC20, the
bar-odd carrier over the prime-19 cubic field). Companion audit
`docs/audits/2026-07-11-fmap-action-qsqrt3-saddle-entropy-block.md` (#3571).

-- Ref: [leitner2026] the 4₁ trace field ℚ(√−3); Kashaev saddle at x*=5/6
-/

namespace QOU.QBeta.Qsqrt3Saddle

open Real

/-- At the saddle `x* = 5/6`, `2·sin(5π/6) = 1` (so `G'(x*) = log 1 = 0`). -/
theorem sin_saddle : 2 * Real.sin (5 * π / 6) = 1 := by
  have h : (5 : ℝ) * π / 6 = π - π / 6 := by ring
  rw [h, Real.sin_pi_sub, Real.sin_pi_div_six]
  norm_num

/-- `sin(5π/6) = 1/2`. -/
theorem sin_saddle' : Real.sin (5 * π / 6) = 1 / 2 := by
  have := sin_saddle; linarith

/-- `cos(5π/6) = −√3/2`. -/
theorem cos_saddle : Real.cos (5 * π / 6) = -(Real.sqrt 3 / 2) := by
  have h : (5 : ℝ) * π / 6 = π - π / 6 := by ring
  rw [h, Real.cos_pi_sub, Real.cos_pi_div_six]

/-- **Critical point:** `G'(x*) = log(2 sin(5π/6)) = 0`. -/
theorem grad_saddle_zero : Real.log (2 * Real.sin (5 * π / 6)) = 0 := by
  rw [sin_saddle, Real.log_one]

/-- `cot(5π/6) = −√3` — the arithmetic that puts the Hessian in `ℚ(√3)`. -/
theorem cot_saddle : Real.cos (5 * π / 6) / Real.sin (5 * π / 6) = -Real.sqrt 3 := by
  rw [cos_saddle, sin_saddle']; ring

/-- **The Hessian `G''(x*) = π·cot(5π/6) = −√3·π ∈ ℚ(√3)·π`.** -/
theorem hessian_eq :
    π * (Real.cos (5 * π / 6) / Real.sin (5 * π / 6)) = -Real.sqrt 3 * π := by
  rw [cot_saddle]; ring

/-- The leading saddle-Laplace `1/N` coefficient as a function of the first three
    saddle Taylor data `(g₂, g₃, g₄)`:
    `b₁ = g₄/(8 g₂²) + 5 g₃²/(24 |g₂|³)`.

    **Domain: `g₂ < 0`.** A Laplace `1/N` expansion exists only at a *maximum* of
    the exponent, where the second derivative `g₂ = 2·G''(x*)` is strictly negative;
    there `|g₂| = −g₂`, which is what the `(−g2)^3` denominator encodes. This is the
    natural (non-misuse-prone) domain — the coefficient is meaningless at `g₂ ≥ 0`.
    The sole call site (`laplaceB1_at_saddle`) instantiates `g₂ = −2√3π < 0`
    concretely, so no separate hypothesis is threaded. -/
noncomputable def laplaceB1 (g2 g3 g4 : ℝ) : ℝ :=
  g4 / (8 * g2 ^ 2) + 5 * g3 ^ 2 / (24 * (-g2) ^ 3)

/-- **`b₁ = √3·π/54 ∈ ℚ(√3)·π`** at the exact 4₁ exponent (`2G`) saddle data
    `(g₂, g₃, g₄) = (−2√3π, −8π², −16√3π³)`. Exact arithmetic object (the numerical
    PSLQ of #3571 was entropy-blocked; this is the exact value). -/
theorem laplaceB1_at_saddle :
    laplaceB1 (-2 * Real.sqrt 3 * π) (-8 * π ^ 2) (-16 * Real.sqrt 3 * π ^ 3)
      = Real.sqrt 3 * π / 54 := by
  -- `field_simp` discharges the `π ≠ 0` / `√3 ≠ 0` denominator side-conditions
  -- itself, so no explicit nonzero hypotheses are needed.
  have h3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have e2 : (-2 * Real.sqrt 3 * π) ^ 2 = 12 * π ^ 2 := by
    linear_combination 4 * π ^ 2 * h3
  have e3 : (-(-2 * Real.sqrt 3 * π)) ^ 3 = 24 * Real.sqrt 3 * π ^ 3 := by
    linear_combination 8 * Real.sqrt 3 * π ^ 3 * h3
  unfold laplaceB1
  rw [e2, e3]
  field_simp
  linear_combination (-552960 : ℝ) * h3

/-- **The naive saddle `b₁` is a rational multiple of `√3·π` — i.e. it lives in
    `ℚ(√3)·π`** (`b₁ = (1/54)·√3π`). This is the exact arithmetic *home* of the
    even channel; it is NOT the observable action coefficient `c₁` (see the module
    docstring's honest-scope note). -/
theorem laplaceB1_saddle_mem_qsqrt3 :
    ∃ r : ℚ, laplaceB1 (-2 * Real.sqrt 3 * π) (-8 * π ^ 2) (-16 * Real.sqrt 3 * π ^ 3)
      = (r : ℝ) * (Real.sqrt 3 * π) := by
  refine ⟨1 / 54, ?_⟩
  rw [laplaceB1_at_saddle]
  push_cast
  ring

/-! ## The observable leading coefficient `κ₁ = 11·√3·π/108`

The naive saddle `b₁ = √3π/54` above is the **integral**-Laplace coefficient; it
omits the Euler–Maclaurin sum-vs-integral correction of the discrete Kashaev
*sum*. The **observable** even-channel leading coefficient — the `[1/N]`
coefficient of `log J_N(4₁)`, numerically `≈ 0.5542164724…` (matching the value
#3571 could only fit) — is identified (audit script
`qbeta_ohtsuki_kappa1_extract.py`, 10-point Vandermonde to ≈23 digits + 2-term
PSLQ to 33-digit agreement) as the **exact** element

  `κ₁ = 11·√3·π/108 ∈ ℚ(√3)·π`,

equivalently Ohtsuki's imaginary-coefficient form `κ_1^Oht = A/√−3` with the
rational `A = 11/72` — the classical figure-eight **2-loop numerator `11`**.

**Epistemic status.** The identification `κ₁ = 11√3π/108` is the *numerical*
Ohtsuki result (the audit script's PSLQ), NOT proved here from the sum. What
Lean certifies below is (i) the **exact algebraic relation** `κ₁ = (11/2)·b₁`
between the named observable value and the naive saddle (the sum-correction is
exactly the factor `11/2`), and (ii) the `ℚ(√3)·π` membership of `κ₁`. The
bridge from this 4₁-Kashaev fact to the physical Q_β observable action is the
open keystone; nothing here is wired to production, and no `c_k` value changes. -/

/-- The observable even-channel leading coefficient `κ₁ = 11·√3·π/108` (the exact
    value of the `[1/N]` coefficient of `log J_N(4₁)`; numerical Ohtsuki
    identification — see the section docstring). -/
noncomputable def ohtsukiKappa1 : ℝ := 11 * Real.sqrt 3 * π / 108

/-- **`κ₁ = (11/2)·b₁`.** The Euler–Maclaurin sum-vs-integral correction multiplies
    the naive integral-Laplace saddle `b₁ = √3π/54` by exactly `11/2`. Pure algebra
    over the certified `laplaceB1_at_saddle` value. -/
theorem ohtsukiKappa1_eq_eleven_halves_b1 :
    ohtsukiKappa1
      = (11 / 2) * laplaceB1 (-2 * Real.sqrt 3 * π) (-8 * π ^ 2)
          (-16 * Real.sqrt 3 * π ^ 3) := by
  rw [ohtsukiKappa1, laplaceB1_at_saddle]; ring

/-- **`κ₁ ∈ ℚ(√3)·π`** (`κ₁ = (11/108)·√3π`) — the exact even-channel observable
    leading coefficient lives in the same real quadratic field `ℚ(√3)` as the naive
    saddle `b₁`, not merely near it. -/
theorem ohtsukiKappa1_mem_qsqrt3 :
    ∃ r : ℚ, ohtsukiKappa1 = (r : ℝ) * (Real.sqrt 3 * π) := by
  refine ⟨11 / 108, ?_⟩
  rw [ohtsukiKappa1]; push_cast; ring

/-! ## Higher rungs `κ₂, κ₃, κ₄` — the √3-parity alternation

The higher-rung extraction (PR #3628; `qbeta_ohtsuki_higher_rungs.py`, confirmed at
N ≤ 6291456 to 19–36 digits per rung) identifies

  `κ₂ = (2/27)·π²`, `κ₃ = (1081/21870)·√3·π³`, `κ₄ = (98/729)·π⁴`,

with the structural **√3-parity alternation**: odd rungs carry `√3` (odd powers of
the imaginary `ℏ = 2πi/N` refract the `√−3` trace-field generator to real `√3`),
even rungs are pure rational multiples of `π^n`. Denominators are 3-power-dominated
(`27 = 3³`, `21870 = 2·3⁷·5`, `729 = 3⁶`) — the ℚ(√−3) torsion-3 signature.

**Epistemic status.** As with `κ₁`, the *values* are the numerical Ohtsuki
identifications (not proved from the sum here); Lean certifies the **field
membership** — each rung is a rational multiple of its parity generator — so the
alternation pattern (`ℚ·√3π^n` odd / `ℚ·π^n` even) is machine-checked arithmetic
over the named values. Nothing is wired; the 4₁↔Q_β bridge stays open. -/

/-- `κ₂ = (2/27)·π²` — the second even-channel rung (even rung: pure rational,
    NO `√3`). Numerical Ohtsuki identification, 30 confirmed digits. -/
noncomputable def ohtsukiKappa2 : ℝ := 2 * π ^ 2 / 27

/-- `κ₃ = (1081/21870)·√3·π³` — the third rung (odd rung: carries `√3`).
    Numerical Ohtsuki identification, 25 confirmed digits. -/
noncomputable def ohtsukiKappa3 : ℝ := 1081 * Real.sqrt 3 * π ^ 3 / 21870

/-- `κ₄ = (98/729)·π⁴` — the fourth rung (even rung: pure rational).
    Numerical Ohtsuki identification, 19 confirmed digits. -/
noncomputable def ohtsukiKappa4 : ℝ := 98 * π ^ 4 / 729

/-- **`κ₂ ∈ ℚ·π²`** — the even-rung parity: a rational multiple of `π²`,
    with no `√3` factor. -/
theorem ohtsukiKappa2_mem_q_pi_sq :
    ∃ r : ℚ, ohtsukiKappa2 = (r : ℝ) * π ^ 2 := by
  refine ⟨2 / 27, ?_⟩
  rw [ohtsukiKappa2]; push_cast; ring

/-- **`κ₃ ∈ ℚ·√3·π³`** — the odd-rung parity: a rational multiple of `√3·π³`,
    like `κ₁`. -/
theorem ohtsukiKappa3_mem_qsqrt3_pi_cube :
    ∃ r : ℚ, ohtsukiKappa3 = (r : ℝ) * (Real.sqrt 3 * π ^ 3) := by
  refine ⟨1081 / 21870, ?_⟩
  rw [ohtsukiKappa3]; push_cast; ring

/-- **`κ₄ ∈ ℚ·π⁴`** — the even-rung parity: a rational multiple of `π⁴`. -/
theorem ohtsukiKappa4_mem_q_pi_four :
    ∃ r : ℚ, ohtsukiKappa4 = (r : ℝ) * π ^ 4 := by
  refine ⟨98 / 729, ?_⟩
  rw [ohtsukiKappa4]; push_cast; ring

end QOU.QBeta.Qsqrt3Saddle
