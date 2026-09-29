/-
# A constant-residue holonomy character obeys a doubling identity — for every `c`

Beans `qou-pdix` / `qou-cds1`, route 5. The **hyperbolic mirror** of
`QOU/QBeta/PhaseFailsLogFunctionalEquation.lean`.

## Why this exists

Kohno–Drinfeld fixes the scale rather than leaving it free: braiding is
`P exp(ħ t/2)` with `t` eigenvalues `±1`, matching the Hecke eigenvalues
`{q, −1/q}` exactly when `q = e^{ħ/2}`. So `ħ = 2 ln q`, and a
**constant-residue** generator eigenvalue is `c · ln q` for some constant `c`.

`PhaseFailsLogFunctionalEquation` excludes such a holonomy on the **elliptic**
reading, where the angle itself is `c · ln q`, using `ln(q²) = 2 ln q` — so
every `c · ln` satisfies `f(q²) = 2 f(q)`, and the corpus's algebraic `α` does
not.

The **hyperbolic** reading needs a different identity, because there the
observable is the *character* `cosh(c · ln q)`, not the angle. The analogue is
the cosh double-angle law: `cosh 2a = 2 cosh²a − 1`, so every constant-residue
character satisfies

    χ(q²) = 2 χ(q)² − 1

whatever `c` is. `not_constant_residue_character_of_doubling_fails` is the
contrapositive, quantified over all `c` at once exactly as its elliptic sibling
is.

## Why the hyperbolic branch needs excluding at all

Route 5's step-18 obstruction (`HolonomySpectrumSignObstruction`) excluded the
real-spectrum holonomy from the hypothesis `κ < 1`, since `cosh ≥ 1`. On the
base the owner ruled on 2026-09-08 that hypothesis is **false** — `κ` is
`1.7593646` at the `z_D` order-zero `E₀` and `1.2002494` on the dashboard's
scored cell — so that exclusion does not fire and the branch re-opens. These
lemmas close the constant-residue part of it by a different route, and leave
open exactly what its elliptic sibling leaves open: a `q`-dependent residue, a
non-flat construction, or a genuinely `q`-dependent-parameter transcendental
object.

## Scope

Scope-(b) for *"no constant-residue real-spectrum holonomy supplies the
requirement AS A FUNCTION of q"*, citing the proved identity above. It is
**not** an exclusion at a point: at a single `q₀` the free `c` reaches any
`κ ≥ 1`, so a pointwise match is always available and says nothing.

The numerical companion is
`computations/qbeta/qbeta_constant_residue_character_doubling_probe.py`, which
measures the defect (59–70 % across `q ∈ {q₀, 1.5, 2, 3}`) and checks that no
rescaling `λ` rescues it (`λ(q)` spreads 28.9 %, against `λ ≡ 1` for a genuine
character).

Verified `lean`-direct with `-DautoImplicit=false -s 65536`: exit 0, no
diagnostics, no `sorry`, no `axiom`.
-/

import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic

namespace QOU.QBeta.CharacterDoubling

/-- The cosh double-angle law in the form the character test uses. -/
theorem cosh_doubling (a : ℝ) : Real.cosh (2 * a) = 2 * Real.cosh a ^ 2 - 1 := by
  have h := Real.cosh_sq_sub_sinh_sq a
  rw [Real.cosh_two_mul]
  linarith

/-- Every constant-residue character satisfies the doubling identity, for every
`c`. This is the hyperbolic analogue of `ln(q²) = 2 ln q`. -/
theorem char_doubling_of_constant_residue (c q : ℝ) :
    Real.cosh (c * Real.log (q ^ 2))
      = 2 * Real.cosh (c * Real.log q) ^ 2 - 1 := by
  have hlog : Real.log (q ^ 2) = 2 * Real.log q := by
    rw [Real.log_pow]; norm_num
  rw [hlog, show c * (2 * Real.log q) = 2 * (c * Real.log q) by ring, cosh_doubling]

/-- The contrapositive, quantified over all `c` at once: a function failing the
doubling identity at a single positive point is the character of no
constant-residue holonomy. -/
theorem not_constant_residue_character_of_doubling_fails
    {K : ℝ → ℝ} {q : ℝ} (hq : 0 < q)
    (hfail : K (q ^ 2) ≠ 2 * K q ^ 2 - 1) :
    ¬ ∃ c : ℝ, ∀ x : ℝ, 0 < x → K x = Real.cosh (c * Real.log x) := by
  rintro ⟨c, hc⟩
  apply hfail
  rw [hc (q ^ 2) (by positivity), hc q hq, char_doubling_of_constant_residue c q]

/-! ## The second survivor is vacuous

Excluding the *constant*-residue case leaves "a `q`-dependent residue" as a
survivor. It carries no content: `cosh` is onto `[1, ∞)`, so wherever the
requirement satisfies `1 ≤ κ` a residue reproducing it exists by construction —
one defines `a(q) := arcosh(κ(q))` from the answer. Measured, `κ` on the `z_D`
base is `≥ 1` throughout `q ∈ (1, 10]` (1.5333 at `q → 1⁺`, rising monotonically
to 8.0243 at `q = 10`), so the vacuity is not conditional in the physical
domain.

This is the same disposition `EigenphaseCarrierVacuity` gives the elliptic
trichotomy's middle branch ("`M` arbitrary — CIRCULAR"), reached independently
on the hyperbolic side. Only the third branch — a residue whose `q`-dependence
is *derived* rather than read off the requirement — can carry content. -/

/-- `cosh` is onto `[1, ∞)`, witnessed explicitly. -/
theorem cosh_arcosh (y : ℝ) (hy : 1 ≤ y) :
    Real.cosh (Real.log (y + Real.sqrt (y ^ 2 - 1))) = y := by
  have hy0 : (0:ℝ) ≤ y ^ 2 - 1 := by nlinarith
  set s := Real.sqrt (y ^ 2 - 1) with hs
  have hs2 : s ^ 2 = y ^ 2 - 1 := Real.sq_sqrt hy0
  have hsnn : 0 ≤ s := Real.sqrt_nonneg _
  have hpos : (0:ℝ) < y + s := by linarith
  have hmul : (y + s) * (y - s) = 1 := by nlinarith [hs2]
  have hinv : (y + s)⁻¹ = y - s := inv_eq_of_mul_eq_one_right hmul
  rw [Real.cosh_eq, Real.exp_log hpos, Real.exp_neg, Real.exp_log hpos, hinv]
  ring

/-- So a `q`-dependent residue reproducing any requirement `≥ 1` exists by
construction: the second survivor is vacuous, not open. -/
theorem exists_q_dependent_residue_of_one_le
    {K : ℝ → ℝ} (hK : ∀ x : ℝ, 1 ≤ K x) :
    ∃ a : ℝ → ℝ, ∀ x : ℝ, Real.cosh (a x) = K x :=
  ⟨fun x => Real.log (K x + Real.sqrt (K x ^ 2 - 1)), fun x => cosh_arcosh (K x) (hK x)⟩

end QOU.QBeta.CharacterDoubling
