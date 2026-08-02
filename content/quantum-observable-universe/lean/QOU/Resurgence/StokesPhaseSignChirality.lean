/-
  QOU.Resurgence.StokesPhaseSignChirality

  Does the ±i imaginary Stokes phase supply the Δ_λ CHIRALITY SIGN?

  Companion to the descent+Ward scaffold (PR #4525,
  `StokesMatrixDescent.lean` / `WardFiltrationCounting.lean`), which proved
  sorry-free that the gauge-invariant Markov trace forces the |Δ_λ| MAGNITUDES
  but structurally cannot see the SIGN (`chiral_sign_cancels`), relocating the
  residual gap to `chiralPairs(n)` chirality signs.  That scaffold's open
  carrier `StokesPhaseSign` conjectured the sign is the real shadow of the ±i
  Stokes discontinuity, a sign that FLIPS under the bar-involution q ↦ q⁻¹.

  This file tests that conjecture — formalize-first, anti-fit.

  RESULT (honest negative, a full win): the ±i phase does NOT supply the sign.

  * (Part 1) The ±i imaginary discontinuity is REAL — proved sorry-free over ℂ:
    the alien / Stokes discontinuity across a simple Borel singularity is the
    Laplace-contour residue `2πi·ρ`, which is purely imaginary (`.re = 0`) and
    squares to a NEGATIVE real.  It is a π/2 (quarter-turn) monodromy.

  * (Part 2) It does NOT reproduce the mixed-sign Δ_λ pattern.  A ±i phase that
    is bar-covariant (q ↦ q⁻¹ acts as complex conjugation i ↦ −i) imprints a
    sign that must FLIP on every chiral (non-self-conjugate) pair — the
    `bar_flip` axiom of `StokesPhaseSign`.  The physical Δ_λ chirality sign
    provably FAILS this: at n = 5 the chiral pair (5) ↔ (1⁵) has EQUAL signs
    (+1, +1), not opposite.  Hence `¬ BarOdd deltaSign`, and no bar-covariant
    imaginary phase equals `deltaSign`.

  * (Part 3) The actual sign is a REAL π-phase, not an imaginary π/2 phase:
    `deltaSign λ = (-1)^{n(λ)}` = the Lusztig a-function / b-invariant parity =
    the sign-representation twist `sgn(w₀^{S_{λ'}})` (corpus
    `PartitionOf5.deltaSign_eq_nStat_parity`, PROBE-4 overturning audit
    2026-06-23).  It squares to +1 (a π-monodromy), a different monodromy order
    from the ±i discontinuity — which is exactly why the phase cannot source it.

  The apparent match at the two anchors named in the task (n = 3: 1+/2−; n = 6:
  6+/5−) is a SMALL-n COINCIDENCE: those are the only n ≤ 8 where every chiral
  pair happens to flip; the mechanism already fails at n = 4 (2/2 pairs do NOT
  flip) and at n = 5, 7, 8.  Full ladder in the audit doc + witness.

  -- Ref: [ecalle1981] Écalle, Les fonctions résurgentes (alien calculus)
  -- Ref: [macdonald1995] https://doi.org/10.1093/oso/9780198534891.001.0001
-/

import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Data.Complex.Basic
import QOU.BraidsAndKnots.S5SO3FiberAction

namespace QOU.Resurgence

open Complex

/-! ## Part 1 — the ±i imaginary Stokes discontinuity (proved sorry-free over ℂ)

The alien derivative `Δ_ω` across a Stokes line is the discontinuity of the
Laplace transform around the Borel singularity `ξ = A`.  For a simple singularity
the discontinuity is the contour residue `∮ dξ/(ξ−A)·ρ = 2πi·ρ` (`ρ` the real
residue) — intrinsically imaginary.  We encode the discontinuity value and prove
its imaginary-ness structurally (no fit, no free parameter: `2πi` is forced by
the monodromy). -/

/-- The Stokes / alien discontinuity value across a simple Borel singularity with
real residue `ρ`: the Laplace-contour monodromy `2πi·ρ`. -/
noncomputable def stokesDiscontinuity (ρ : ℝ) : ℂ :=
  ((2 * Real.pi * ρ : ℝ) : ℂ) * Complex.I

/-- **The Stokes discontinuity is purely imaginary** — zero real part.  This is
the `±i` signature of the alien derivative: the `2πi` Laplace-contour residue
has no real component. -/
theorem stokesDiscontinuity_re_zero (ρ : ℝ) : (stokesDiscontinuity ρ).re = 0 := by
  simp [stokesDiscontinuity, Complex.mul_re]

/-- The imaginary part is the full magnitude `2πρ`. -/
theorem stokesDiscontinuity_im (ρ : ℝ) :
    (stokesDiscontinuity ρ).im = 2 * Real.pi * ρ := by
  simp [stokesDiscontinuity, Complex.mul_im]

/-- **A nonzero residue gives a nonzero (purely imaginary) discontinuity.**  So
the Stokes jump genuinely exists — it is not a removable artifact. -/
theorem stokesDiscontinuity_ne_zero (ρ : ℝ) (hρ : ρ ≠ 0) :
    stokesDiscontinuity ρ ≠ 0 := by
  intro h
  have him : (stokesDiscontinuity ρ).im = 0 := by rw [h]; simp
  rw [stokesDiscontinuity_im] at him
  have hpi : Real.pi ≠ 0 := Real.pi_ne_zero
  have hne : (2 : ℝ) * Real.pi * ρ ≠ 0 :=
    mul_ne_zero (mul_ne_zero (by norm_num) hpi) hρ
  exact hne him

/-- **The ±i discontinuity is a π/2 (quarter-turn) monodromy: its square is a
NEGATIVE real.**  `(2πi·ρ)² = −(2πρ)²`.  Contrast Part 3: the chirality sign
squares to `+1` (a π monodromy).  The two monodromy orders differ. -/
theorem stokesDiscontinuity_sq (ρ : ℝ) :
    (stokesDiscontinuity ρ) ^ 2 = ((-(2 * Real.pi * ρ) ^ 2 : ℝ) : ℂ) := by
  simp only [stokesDiscontinuity, mul_pow, Complex.I_sq]
  push_cast
  ring

/-! ## Part 2 — falsifiable test: the bar-odd ±i sign does NOT reproduce Δ_λ

`StokesPhaseSign.bar_flip` (the open carrier) posits `sign(conj μ) = − sign μ`
on chiral pairs — the mathematical signature of a ±i phase under the bar
involution q ↦ q⁻¹ (complex conjugation i ↦ −i).  We show the physical Δ_λ sign
`PartitionOf5.deltaSign` does NOT satisfy it. -/

open QOU.BraidsAndKnots

/-- A sign assignment is **bar-odd** when it flips under the bar-involution
(partition conjugation `λ ↦ λ'`) on every chiral (non-self-conjugate) pair.
This is exactly `StokesPhaseSign.bar_flip`: a bar-covariant ±i Stokes phase must
imprint a bar-odd sign. -/
def BarOdd (s : PartitionOf5 → ℤ) : Prop :=
  ∀ p : PartitionOf5, p.conjugate ≠ p → s p.conjugate = - s p

/-- **The physical Δ_λ chirality sign is NOT bar-odd** (proved by explicit
counterexample).  The chiral pair `(5) ↔ (1⁵)` is a genuine conjugate pair
(`(5).conjugate = (1⁵) ≠ (5)`) whose signs are EQUAL — `deltaSign (1⁵) = +1 =
deltaSign (5)` — not opposite.  So the bar-involution does not flip it, and the
`bar_flip` requirement of a ±i Stokes phase fails on the real target. -/
theorem deltaSign_not_barOdd : ¬ BarOdd PartitionOf5.deltaSign := by
  intro h
  have hpair : PartitionOf5.five.conjugate ≠ PartitionOf5.five := by decide
  have := h PartitionOf5.five hpair
  revert this
  decide

/-- **No bar-covariant imaginary Stokes phase supplies the Δ_λ chirality sign.**
Any sign imprinted by such a phase is bar-odd (Part 2 hypothesis); the physical
Δ_λ sign is not; therefore the ±i phase does not source it.  This is the honest
negative resolving the `StokesPhaseSign` carrier: the sign horn is NOT closed by
the Stokes phase. -/
theorem no_imaginary_phase_sources_deltaSign :
    ¬ ∃ s : PartitionOf5 → ℤ, BarOdd s ∧ s = PartitionOf5.deltaSign := by
  rintro ⟨s, hbar, rfl⟩
  exact deltaSign_not_barOdd hbar

/-! ## Part 3 — the actual sign source: a REAL π-phase (a-function parity)

Not an imaginary π/2 phase.  `deltaSign λ = (-1)^{n(λ)} = e^{iπ n(λ)}` is a π
(half-turn) real monodromy: the Lusztig a-function / b-invariant parity, equal to
the sign-representation twist `sgn(w₀^{S_{λ'}})` (corpus, PROBE-4 overturning
audit).  It squares to `+1`, a different monodromy order from the ±i
discontinuity (which squares to a negative real, Part 1) — the structural reason
the phase cannot be the source. -/

/-- **The chirality sign is the real π-phase `(-1)^{n(λ)}` with square `+1`** —
composing the two corpus facts `deltaSign_eq_nStat_parity` (the a-function-parity
identity) and `deltaSign_sq_one`.  A π-monodromy real ±1, categorically distinct
from the π/2 imaginary Stokes discontinuity of Part 1. -/
theorem chirality_sign_is_real_pi_phase (p : PartitionOf5) :
    PartitionOf5.deltaSign p = (-1 : ℤ) ^ p.nStat
      ∧ PartitionOf5.deltaSign p ^ 2 = 1 :=
  ⟨PartitionOf5.deltaSign_eq_nStat_parity p, PartitionOf5.deltaSign_sq_one p⟩

end QOU.Resurgence
