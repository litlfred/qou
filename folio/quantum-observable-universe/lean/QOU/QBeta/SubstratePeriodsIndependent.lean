/-
# The substrate periods `ib`, `i/b` are ℝ-linearly independent (Faddeev–Volkov lattice)

The `DoublyPeriodicLiouville` reduction proved that a holomorphic function periodic
under two `ℝ`-linearly **independent** complex periods is constant, and thereby
reduced the standing-open `QOU.QBeta.CyclicDilogPentagon.PentagonRigidity` hypothesis
to **two** named analytic facts: (i) the ratio `Φ₁/Φ₂` of two `FaddeevPhi` solutions
is entire (the zeros of the two `Φ_b` coincide); and (ii) the two periods `ib` and
`i/b` of that ratio are `ℝ`-independent at the substrate modulus `b`.

This file discharges **(ii)**. The two periods span `ℂ` over `ℝ` exactly when their
`ℝ`-ratio is not real, i.e. when `b² = (ib)/(i/b)` has nonzero imaginary part. At the
substrate the modulus is `b = √β · e^{iπ/4}` (the `PhiBProd` convergence branch), so
`b² = iβ` and `Im(b²) = β > 0` — the periods are independent, and the doubly-periodic
Liouville step applies. What remains of `PentagonRigidity` is then exactly the single
analytic fact (i) (zeros coincide / ratio entire) — the formalize-first shrink.

Nothing here is conjectural: the independence is an unconditional linear-algebra fact
given `Im(b²) ≠ 0`. It removes one of the two open inputs to the pentagon; the other
(and the pentagon's downstream `A_ω` value) stay honestly open. Generic complex field
throughout; no archimedean substrate value is hardcoded (the caller supplies
`Im(b²) ≠ 0`). §7c: `ℂ` is intrinsic to the Faddeev quantum dilogarithm — not a
gratuitous `ℝ`.

-- Ref: [leitner2026] docs/workplans/2026-07-13-phib-combinatorial-fibre-lean-workplan.md (L4, period-independence leg)
-/
import Mathlib.LinearAlgebra.LinearIndependent.Defs
import Mathlib.LinearAlgebra.LinearIndependent.Lemmas
import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.LinearAlgebra.FiniteDimensional.Basic
import Mathlib.LinearAlgebra.Complex.FiniteDimensional

namespace QOU.QBeta.SubstratePeriods

open Complex

/-- **The two Faddeev–Volkov periods are `ℝ`-linearly independent** whenever
`Im(b²) ≠ 0`. Proof: an `ℝ`-relation `s•(ib) + t•(i/b) = 0` factors through `I`
and, after clearing `b`, gives `s·b² + t = 0`; taking imaginary parts (`t` real)
yields `s·Im(b²) = 0`, so `s = 0`, whence `t = 0`. -/
theorem periods_linearIndependent (b : ℂ) (hb : b ≠ 0) (himb2 : (b ^ 2).im ≠ 0) :
    LinearIndependent ℝ ![Complex.I * b, Complex.I / b] := by
  rw [LinearIndependent.pair_iff]
  intro s t hst
  -- ℝ-smul on ℂ is coercion-multiplication.
  have hI : Complex.I ≠ 0 := Complex.I_ne_zero
  -- s•(I*b) + t•(I/b) = I * (s*b + t/b) = 0  ⇒  s*b + t/b = 0.
  have e1 : (s : ℂ) * b + (t : ℂ) / b = 0 := by
    have : Complex.I * ((s : ℂ) * b + (t : ℂ) / b) = 0 := by
      have := hst
      simp only [Complex.real_smul] at this
      ring_nf
      ring_nf at this
      linear_combination this
    exact (mul_eq_zero.mp this).resolve_left hI
  -- multiply by b (≠0): s*b² + t = 0.
  have e2 : (s : ℂ) * b ^ 2 + (t : ℂ) = 0 := by
    have := congrArg (· * b) e1
    field_simp at this
    linear_combination this
  -- take imaginary parts: s*Im(b²) = 0 ⇒ s = 0.
  have him : (s : ℝ) * (b ^ 2).im = 0 := by
    have h := congrArg Complex.im e2
    simp only [Complex.add_im, Complex.mul_im, Complex.ofReal_re, Complex.ofReal_im,
               Complex.zero_im, zero_mul, add_zero] at h
    exact h
  have hs : s = 0 := by
    rcases mul_eq_zero.mp him with h | h
    · exact h
    · exact absurd h himb2
  -- back-substitute: t = 0.
  refine ⟨hs, ?_⟩
  have : (t : ℂ) = 0 := by
    rw [hs] at e2; simpa using e2
  exact_mod_cast this

/-- The two periods span `ℂ` over `ℝ`: being `ℝ`-independent and of cardinality
`2 = finrank ℝ ℂ`, they form a `Basis (Fin 2) ℝ ℂ` — the exact input
`DoublyPeriodicLiouville.ratio_const_of_doublyPeriodic` consumes. The `Basis`
follows from `periods_linearIndependent` by the standard "independent family of
size `finrank` is a basis" constructor; only the independence content is proved
here (it is the load-bearing fact — the basis is its mechanical corollary). -/
theorem periods_card_eq_finrank :
    (Fintype.card (Fin 2) : ℕ) = Module.finrank ℝ ℂ := by
  simp [Complex.finrank_real_complex]

end QOU.QBeta.SubstratePeriods
