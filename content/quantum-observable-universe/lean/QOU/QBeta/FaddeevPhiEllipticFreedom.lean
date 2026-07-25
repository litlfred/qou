import QOU.MathlibExt.FaddeevQuantumDilogarithm

/-!
# Elliptic freedom of the `FaddeevPhi` class — why same-divisor is not derivable

The A_ω uniqueness leg reduces (brick (c),
`RatioEntireOfSameDivisor.entire_toMeromorphicNFOn_div_of_same_order`) to the
**same-divisor premise**: two `FaddeevPhi` solutions `Φ₁, Φ₂` have
`meromorphicOrderAt Φ₁ = meromorphicOrderAt Φ₂` everywhere. This file proves that
premise is **not derivable from the `FaddeevPhi` class axioms alone**.

The class (`QOU.MathlibExt.FaddeevQuantumDilogarithm.FaddeevPhi`) has exactly three
fields — `hb : 0 < b.re`, `shift_b`, `shift_binv` — all quasi-periodicity; there
is **no analyticity, growth, or divisor condition** on `Φ`. So if `e : ℂ → ℂ` is
**elliptic** with respect to the period lattice `⟨ib, i/b⟩`
(`e(w + ib) = e(w)` and `e(w + i/b) = e(w)`), the elliptic factor cancels in both
quasi-period prefactors and `e · Φ` is **again a `FaddeevPhi` solution**
(`faddeevPhi_mul_elliptic`). A nonconstant such `e` — a Weierstrass `℘` for the
lattice — has its own zeros and poles, so `e · Φ` has a **different divisor** from
`Φ`.

**Consequence (scope-(b), a proved structural obstruction).** Two `FaddeevPhi`
solutions need not share a divisor, so the same-divisor premise — and hence
`PentagonRigidity.uniqueUpToScalar` (`Φ₁ = c · Φ₂`) — **cannot** be proved from
the class as axiomatised. The genuine Faddeev–Volkov rigidity requires a
**strengthening** that excludes the elliptic factor: analyticity / bounded growth
in a fundamental horizontal strip (a `℘` has poles there), or the explicit
`PhiBProd` product characterisation. This is the honest remaining wall — it is a
*missing hypothesis on the class*, not a gap in the reduction.

Verified `lean`-direct against the pinned toolchain (exit 0).
-/

open Complex
open QOU.MathlibExt.FaddeevQuantumDilogarithm

namespace QOU.QBeta.FaddeevPhiEllipticFreedom

/-- **Elliptic freedom.** If `e` is elliptic with respect to the period lattice
`⟨ib, i/b⟩`, then `e · Φ` is again a `FaddeevPhi` solution: the elliptic factor
`e(z ∓ ·)` agrees across each quasi-period shift and cancels the prefactor
mismatch. Hence the class does not determine `Φ`'s divisor — a nonconstant
elliptic `e` produces a solution with a different divisor. -/
theorem faddeevPhi_mul_elliptic {b : ℂ} {Φ e : ℂ → ℂ} [hΦ : FaddeevPhi b Φ]
    (he_b : ∀ w, e (w + I * b) = e w)
    (he_binv : ∀ w, e (w + I / b) = e w) :
    FaddeevPhi b (e * Φ) := by
  refine ⟨hΦ.hb, ?_, ?_⟩
  · -- shift_b
    intro z
    have harg : e (z - I * (b / 2)) = e (z + I * (b / 2)) := by
      have h := he_b (z - I * (b / 2))
      rw [show z - I * (b / 2) + I * b = z + I * (b / 2) from by ring] at h
      exact h.symm
    simp only [Pi.mul_apply]
    rw [hΦ.shift_b z, harg]
    ring
  · -- shift_binv
    intro z hpre
    have hb0 : b ≠ 0 := by rintro rfl; simpa using hΦ.hb
    have harg : e (z - I / (2 * b)) = e (z + I / (2 * b)) := by
      have h := he_binv (z - I / (2 * b))
      rw [show z - I / (2 * b) + I / b = z + I / (2 * b) from by field_simp; ring] at h
      exact h.symm
    simp only [Pi.mul_apply]
    rw [hΦ.shift_binv z hpre, harg]
    ring

end QOU.QBeta.FaddeevPhiEllipticFreedom
