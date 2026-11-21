import QOU.QBeta.CyclicDilogPentagon
import QOU.QBeta.PeriodLatticeBasis
import QOU.MathlibExt.DoublyPeriodicLiouville

/-!
# Faddeev–Volkov rigidity reduces to holomorphicity of the ratio (FaddeevPhi-specific)

The `FaddeevPhi`-specific bridge into the generic doubly-periodic Liouville result
`QOU.MathlibExt.DoublyPeriodicLiouville.ratio_const_of_doublyPeriodic` (which proves:
two entire functions with nowhere-zero denominator and a ratio periodic under an
`ℝ`-basis are proportional). That generic lemma takes *both* period identities as
input; this file supplies the extra `FaddeevPhi`-specific content — the compact
`ib`-period of the ratio is **not** an assumption, it is **derived** from
nowhere-zero via the quasi-period prefactor (`phi_b_quasiperiod`,
`ratio_ib_periodic`). So a caller need only supply the *dual* `i/b`-period, the
entireness, and the basis.

**Convergence note.** The generic elliptic-Liouville step
(`const_of_doublyPeriodic`) and its ratio bridge were landed independently on
`origin/main` (`DoublyPeriodicLiouville.lean`) while this branch developed a
parallel `EllipticLiouville.lean`; per the reuse-and-simplify discipline the
duplicate was removed and this file now consumes the upstream lemma. The two
independent proofs of the same Liouville step are a confirmation, not waste.

**What remains open (anti-laundering, explicit).** Unchanged: (i) `Φ_b`
holomorphic + divisor cancellation so the solutions are entire (the true `Φ_b` is
meromorphic — this is the idealized nowhere-zero-entire setting), (ii) the basis
non-degeneracy `b² ∉ ℝ` (substrate `arg b = π/4`; fails for real `b`), (iii) the
`i/b`-period everywhere (identity theorem off the dual pole lattice). Nothing here
is axiomatized.

Verified `lean`-direct against pinned Mathlib (exit 0).

Ref: [leitner2026] docs/audits/2026-07-18-g3-stokes-keystone-evidence-base.md §8
-/

open Complex Module
open QOU.MathlibExt.FaddeevQuantumDilogarithm
open QOU.QBeta.CyclicDilogPentagon
open QOU.QBeta.PeriodLatticeBasis
open QOU.MathlibExt.DoublyPeriodicLiouville

namespace QOU.QBeta.FaddeevRigidityReduction

/-- **Reduction of Faddeev–Volkov rigidity to entireness of the two solutions.**
For two `FaddeevPhi` solutions `Ψ, Φ` at the same `b` with `Φ` nowhere zero and
both entire, `∃ c, Ψ = c·Φ` follows from a basis `bas` of `ℂ` realizing the two
periods `⟨ib, i/b⟩` plus the dual `i/b`-periodicity of the ratio. The compact
`ib`-periodicity is **derived** here (nowhere-zero forces the quasi-period
prefactor nonzero), then upstream `ratio_const_of_doublyPeriodic` finishes. -/
theorem uniqueUpToScalar_of_entire
    {b : ℂ} {Φ Ψ : ℂ → ℂ} [FaddeevPhi b Φ] [FaddeevPhi b Ψ]
    (hΦe : Differentiable ℂ Φ) (hΨe : Differentiable ℂ Ψ)
    (hΦ0 : ∀ z, Φ z ≠ 0)
    (bas : Basis (Fin 2) ℝ ℂ) (hb0 : bas 0 = I * b) (hb1 : bas 1 = I / b)
    (hibinv : ∀ z, Ψ (z + I / b) / Φ (z + I / b) = Ψ z / Φ z) :
    ∃ c, ∀ z, Ψ z = c * Φ z := by
  -- ib-periodicity of the ratio, DERIVED (nowhere-zero ⇒ prefactor nonzero)
  have hib : ∀ z, Ψ (z + I * b) / Φ (z + I * b) = Ψ z / Φ z := by
    intro z
    have hP : (1 : ℂ) + Complex.exp (I * (Real.pi : ℂ) * (b : ℂ) ^ 2)
                * Complex.exp (2 * (Real.pi : ℂ) * b * z) ≠ 0 := by
      intro hP0
      have hq := phi_b_quasiperiod (b := b) (Φ := Φ) z
      rw [hP0, zero_mul] at hq
      exact hΦ0 z hq
    exact (ratio_ib_periodic (b := b) (Φ₁ := Ψ) (Φ₂ := Φ) z hP).symm
  -- feed both periods to the upstream doubly-periodic ratio Liouville lemma
  refine ratio_const_of_doublyPeriodic (b := bas) hΦe hΨe hΦ0 ?_
  rw [Fin.forall_fin_two]
  exact ⟨fun z => by rw [hb0]; exact hib z, fun z => by rw [hb1]; exact hibinv z⟩

/-- **Cleaner form — the basis is discharged by the substrate non-degeneracy.**
Given `b² ∉ ℝ` (the substrate branch `arg b = π/4`; fails for real `b`), the
period lattice `⟨ib, i/b⟩` is automatically a basis
(`PeriodLatticeBasis.exists_period_basis`), so Faddeev–Volkov rigidity reduces to
just **two** open inputs: the two solutions are entire, and the ratio is
`i/b`-periodic everywhere. (The `ib`-period is still derived from nowhere-zero.) -/
theorem uniqueUpToScalar_of_entire_of_sq_not_real
    {b : ℂ} {Φ Ψ : ℂ → ℂ} [FaddeevPhi b Φ] [FaddeevPhi b Ψ]
    (hΦe : Differentiable ℂ Φ) (hΨe : Differentiable ℂ Ψ)
    (hΦ0 : ∀ z, Φ z ≠ 0) (hb2 : (b ^ 2).im ≠ 0)
    (hibinv : ∀ z, Ψ (z + I / b) / Φ (z + I / b) = Ψ z / Φ z) :
    ∃ c, ∀ z, Ψ z = c * Φ z := by
  obtain ⟨bas, hb0, hb1⟩ := exists_period_basis hb2
  exact uniqueUpToScalar_of_entire hΦe hΨe hΦ0 bas hb0 hb1 hibinv

end QOU.QBeta.FaddeevRigidityReduction
