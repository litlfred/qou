import QOU.QBeta.CyclicDilogPentagon
import QOU.Common.EllipticLiouville

/-!
# Faddeev–Volkov rigidity reduces to holomorphicity of the ratio

The executable scope of the G3 keystone's remaining gap. Combines the two proved
periods (`ratio_ib_periodic`, `ratio_ibinv_periodic`,
`QOU/QBeta/CyclicDilogPentagon.lean`) with the proved elliptic-Liouville theorem
(`doublyPeriodic_entire_const`, `QOU/Common/EllipticLiouville.lean`) to show that
`PentagonRigidity.uniqueUpToScalar` follows from **exactly three explicit
hypotheses**, isolating precisely what "the holomorphicity endowment" must
supply. Nothing here is axiomatized; the three hypotheses are honest open input.

**The endowment, decomposed.** The load-bearing hypothesis is `hratio` — the
ratio `Ψ/Φ` is entire. This is NOT "`Φ_b` is entire" (false: the true `Φ_b` is
meromorphic, with poles on the dual `1/b`-lattice and zeros on the `b`-lattice).
It decomposes into (i) `Φ_b` holomorphic/meromorphic (the `FaddeevPhi` class
currently axiomatizes only the difference equations — the contour-integral `Φ_b`
and its analyticity are open), and (ii) **divisor cancellation**: two solutions
of the same functional equations have identical zeros and poles, so the ratio has
only removable singularities and extends to an entire, nowhere-zero function.
The other two hypotheses are lighter: `hspan` is the algebraic non-degeneracy
`b² ∉ ℝ` (the substrate branch `arg b = π/4`; it FAILS for real `b`, where both
periods are imaginary and the lattice collapses), and `hibinv` is derivable off
the dual pole lattice from `ratio_ibinv_periodic`, needing only the identity
theorem to extend across that discrete set.

Verified `lean`-direct against pinned Mathlib (exit 0).

Ref: [manuscript] docs/audits/2026-07-18-g3-stokes-keystone-evidence-base.md §8
-/

open Complex
open QOU.MathlibExt.FaddeevQuantumDilogarithm
open QOU.QBeta.CyclicDilogPentagon
open QOU.Common

namespace QOU.QBeta.FaddeevRigidityReduction

/-- **Reduction of Faddeev–Volkov rigidity to holomorphicity of the ratio.**
For two `FaddeevPhi` solutions `Ψ, Φ` at the same `b` with `Φ` nowhere zero, the
`uniqueUpToScalar` conclusion (`∃ c, Ψ = c·Φ`) follows from three explicit inputs,
each an honest open hypothesis:

* `hratio` — the ratio `Ψ/Φ` is **entire** (the holomorphicity endowment: `Φ_b`
  holomorphic AND the two solutions' poles/zeros cancel in the ratio);
* `hspan` — the lattice `⟨ib, i/b⟩` **ℝ-spans** `ℂ` (non-degeneracy `b² ∉ ℝ`);
* `hibinv` — the `i/b`-periodicity of the ratio holds **everywhere**.

The `ib`-periodicity is **derived** (nowhere-zero forces the quasiperiod prefactor
nonzero), then `doublyPeriodic_entire_const` finishes. -/
theorem uniqueUpToScalar_of_ratio_entire
    {b : ℂ} {Φ Ψ : ℂ → ℂ} [FaddeevPhi b Φ] [FaddeevPhi b Ψ]
    (hΦ0 : ∀ z, Φ z ≠ 0)
    (hratio : Differentiable ℂ (fun z => Ψ z / Φ z))
    (hspan : ∀ w : ℂ, ∃ s t : ℝ, w = s • (I * b) + t • (I / b))
    (hibinv : ∀ z, Ψ (z + I / b) / Φ (z + I / b) = Ψ z / Φ z) :
    ∃ c, ∀ z, Ψ z = c * Φ z := by
  -- ib-periodicity of the ratio, unconditional because Φ is nowhere zero
  have hib : ∀ z, Ψ (z + I * b) / Φ (z + I * b) = Ψ z / Φ z := by
    intro z
    have hP : (1 : ℂ) + Complex.exp (I * (Real.pi : ℂ) * (b : ℂ) ^ 2)
                * Complex.exp (2 * (Real.pi : ℂ) * b * z) ≠ 0 := by
      intro hP0
      have hq := phi_b_quasiperiod (b := b) (Φ := Φ) z
      rw [hP0, zero_mul] at hq
      exact hΦ0 z hq
    exact (ratio_ib_periodic (b := b) (Φ₁ := Ψ) (Φ₂ := Φ) z hP).symm
  -- elliptic Liouville on the entire, doubly-periodic ratio
  obtain ⟨c, hc⟩ := doublyPeriodic_entire_const (fun z => Ψ z / Φ z) (I * b) (I / b)
      hratio hib hibinv hspan
  exact ⟨c, fun z => (div_eq_iff (hΦ0 z)).mp (hc z)⟩

end QOU.QBeta.FaddeevRigidityReduction
