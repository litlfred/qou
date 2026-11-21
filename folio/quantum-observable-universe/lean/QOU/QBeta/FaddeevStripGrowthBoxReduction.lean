/-
Copyright (c) 2026 litlfred. All rights reserved.

# Strip-growth reduces to a fundamental-domain bound (doubly-periodic norm)

Front-2 brick for the Faddeev–Volkov A_ω uniqueness leg
(`FaddeevPhiFullUniqueness`, bean `qou-mz4f`/`qou-7xvy`). The remaining open
input of that leg is `FaddeevPhiStripGrowth` — that a *second* Faddeev shift
solution `Φ` is comparable in modulus to `phiBProd`. The shift equations alone do
not give it (elliptic freedom), so it is the physical (Faddeev–Kashaev) asymptotic
content.

This file supplies the **domain reduction** that makes that physical input
**local**: the ratio `Φ/phiBProd` is **doubly-periodic** (the FaddeevPhi shift
prefactors cancel — `CyclicDilogPentagon.ratio_ib_periodic`/`ratio_ibinv_periodic`),
and a doubly-periodic function that is bounded on **one fundamental parallelogram**
(the closed ball of radius `‖bas 0‖+‖bas 1‖`) is bounded **everywhere**. So the
global comparability bound reduces to a bound on a **compact** fundamental domain —
exactly where the Faddeev asymptotic is a finite, checkable estimate rather than a
global one.

This is the *non-holomorphic* companion to `DoublyPeriodicLiouville.const_of_doublyPeriodic`
(which needs analyticity to conclude *constancy*): here we need only periodicity to
propagate a **modulus bound** from the fundamental domain to `ℂ`, which is what the
`comparable` field of `FaddeevPhiStripGrowth` is about (a norm inequality, not a
holomorphic statement). The reduction uses the same `Int.fract`/`periodic_zsmul`
lattice machinery.

**Scope (reduction, not closure).** This reduces the *global* strip-growth axiom to
a *fundamental-domain* bound; it does not *prove* that bound for a second solution
(that remains the physical Faddeev asymptotic + divisor matching at `phiBProd`'s
zeros). It converts a global analytic axiom into a local one — the standard,
tractable form. No fit; nothing wired; §7c: the reduction is over `ℂ` (the archimedean
strip is genuinely `ℂ`-analytic, so `ℝ`/`ℂ` here is correct, not gratuitous). Uses
only on-`main` `DoublyPeriodicLiouville`. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-31-faddeev-stripgrowth-box-reduction.md
-/
import Mathlib.LinearAlgebra.Basis.Defs
import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.Analysis.Complex.Basic
import QOU.MathlibExt.DoublyPeriodicLiouville

namespace QOU.QBeta.FaddeevStripGrowthBoxReduction

open Module
open QOU.MathlibExt.DoublyPeriodicLiouville

/-- **A doubly-periodic function bounded on the fundamental ball is bounded
everywhere.** If `r : ℂ → ℂ` is periodic under both vectors of an `ℝ`-basis `bas`
of `ℂ`, and `‖r w‖ ≤ C` for every `w` in the closed ball of radius
`‖bas 0‖ + ‖bas 1‖`, then `‖r z‖ ≤ C` for *all* `z`. Reducing the two `ℝ`-coordinates
of `z` modulo `1` (`Int.fract`) lands `z`, up to a lattice translation `r` ignores, in
that ball. The non-holomorphic modulus-bound analogue of
`const_of_doublyPeriodic`. -/
theorem norm_le_of_periodic_ballBound {r : ℂ → ℂ} {bas : Basis (Fin 2) ℝ ℂ} {C : ℝ}
    (hper : ∀ (i : Fin 2) (z : ℂ), r (z + bas i) = r z)
    (hball : ∀ w : ℂ, ‖w‖ ≤ ‖bas 0‖ + ‖bas 1‖ → ‖r w‖ ≤ C)
    (z : ℂ) : ‖r z‖ ≤ C := by
  set r0 := bas.repr z 0 with hr0
  set r1 := bas.repr z 1 with hr1
  set z0 : ℂ := Int.fract r0 • bas 0 + Int.fract r1 • bas 1 with hz0
  have hfract0 : |Int.fract r0| ≤ 1 :=
    abs_le.mpr ⟨by linarith [Int.fract_nonneg r0], le_of_lt (Int.fract_lt_one r0)⟩
  have hfract1 : |Int.fract r1| ≤ 1 :=
    abs_le.mpr ⟨by linarith [Int.fract_nonneg r1], le_of_lt (Int.fract_lt_one r1)⟩
  have hz0norm : ‖z0‖ ≤ ‖bas 0‖ + ‖bas 1‖ := by
    calc ‖Int.fract r0 • bas 0 + Int.fract r1 • bas 1‖
        ≤ ‖Int.fract r0 • bas 0‖ + ‖Int.fract r1 • bas 1‖ := norm_add_le _ _
      _ = |Int.fract r0| * ‖bas 0‖ + |Int.fract r1| * ‖bas 1‖ := by
          rw [norm_smul, norm_smul, Real.norm_eq_abs, Real.norm_eq_abs]
      _ ≤ 1 * ‖bas 0‖ + 1 * ‖bas 1‖ :=
          add_le_add (mul_le_mul_of_nonneg_right hfract0 (norm_nonneg _))
            (mul_le_mul_of_nonneg_right hfract1 (norm_nonneg _))
      _ = ‖bas 0‖ + ‖bas 1‖ := by rw [one_mul, one_mul]
  have hzsum : z0 + ((⌊r0⌋ : ℤ) • bas 0 + (⌊r1⌋ : ℤ) • bas 1) = z := by
    rw [hz0]
    have hrepr : r0 • bas 0 + r1 • bas 1 = z := by
      rw [hr0, hr1, ← Fin.sum_univ_two (fun i => bas.repr z i • bas i), bas.sum_repr z]
    rw [← hrepr, ← fract_smul_add_floor_zsmul r0 (bas 0),
      ← fract_smul_add_floor_zsmul r1 (bas 1)]
    abel
  have hrz : r z = r z0 := by
    rw [← hzsum, ← add_assoc,
      periodic_zsmul (hper 1) ⌊r1⌋ (z0 + (⌊r0⌋ : ℤ) • bas 0),
      periodic_zsmul (hper 0) ⌊r0⌋ z0]
  rw [hrz]; exact hball z0 hz0norm

/-- **Two-sided (comparability) form.** If the ratio `r` is doubly-periodic and both
`‖r‖ ≤ C` and `1/C ≤ ‖r‖` hold on the fundamental ball, they hold globally. This is
the `FaddeevPhiStripGrowth.comparable` shape (upper + lower modulus bound) reduced to
the compact fundamental domain — the local Faddeev-asymptotic input that discharges
the global strip-growth axiom (off `phiBProd`'s zeros; divisor matching there is the
separate same-divisor input). -/
theorem comparable_of_periodic_ballBound {r : ℂ → ℂ} {bas : Basis (Fin 2) ℝ ℂ} {C : ℝ}
    (hper : ∀ (i : Fin 2) (z : ℂ), r (z + bas i) = r z)
    (hballU : ∀ w : ℂ, ‖w‖ ≤ ‖bas 0‖ + ‖bas 1‖ → ‖r w‖ ≤ C)
    (hballL : ∀ w : ℂ, ‖w‖ ≤ ‖bas 0‖ + ‖bas 1‖ → 1 / C ≤ ‖r w‖)
    (z : ℂ) : ‖r z‖ ≤ C ∧ 1 / C ≤ ‖r z‖ := by
  refine ⟨norm_le_of_periodic_ballBound hper hballU z, ?_⟩
  -- lower bound: apply the upper-bound reduction to the *reciprocal* target 1/C ≤ ‖r‖,
  -- i.e. show ‖r z‖ is bounded below by reducing z to the fundamental ball.
  set r0 := bas.repr z 0 with hr0
  set r1 := bas.repr z 1 with hr1
  set z0 : ℂ := Int.fract r0 • bas 0 + Int.fract r1 • bas 1 with hz0
  have hfract0 : |Int.fract r0| ≤ 1 :=
    abs_le.mpr ⟨by linarith [Int.fract_nonneg r0], le_of_lt (Int.fract_lt_one r0)⟩
  have hfract1 : |Int.fract r1| ≤ 1 :=
    abs_le.mpr ⟨by linarith [Int.fract_nonneg r1], le_of_lt (Int.fract_lt_one r1)⟩
  have hz0norm : ‖z0‖ ≤ ‖bas 0‖ + ‖bas 1‖ := by
    calc ‖Int.fract r0 • bas 0 + Int.fract r1 • bas 1‖
        ≤ ‖Int.fract r0 • bas 0‖ + ‖Int.fract r1 • bas 1‖ := norm_add_le _ _
      _ = |Int.fract r0| * ‖bas 0‖ + |Int.fract r1| * ‖bas 1‖ := by
          rw [norm_smul, norm_smul, Real.norm_eq_abs, Real.norm_eq_abs]
      _ ≤ 1 * ‖bas 0‖ + 1 * ‖bas 1‖ :=
          add_le_add (mul_le_mul_of_nonneg_right hfract0 (norm_nonneg _))
            (mul_le_mul_of_nonneg_right hfract1 (norm_nonneg _))
      _ = ‖bas 0‖ + ‖bas 1‖ := by rw [one_mul, one_mul]
  have hzsum : z0 + ((⌊r0⌋ : ℤ) • bas 0 + (⌊r1⌋ : ℤ) • bas 1) = z := by
    rw [hz0]
    have hrepr : r0 • bas 0 + r1 • bas 1 = z := by
      rw [hr0, hr1, ← Fin.sum_univ_two (fun i => bas.repr z i • bas i), bas.sum_repr z]
    rw [← hrepr, ← fract_smul_add_floor_zsmul r0 (bas 0),
      ← fract_smul_add_floor_zsmul r1 (bas 1)]
    abel
  have hrz : r z = r z0 := by
    rw [← hzsum, ← add_assoc,
      periodic_zsmul (hper 1) ⌊r1⌋ (z0 + (⌊r0⌋ : ℤ) • bas 0),
      periodic_zsmul (hper 0) ⌊r0⌋ z0]
  rw [hrz]; exact hballL z0 hz0norm

end QOU.QBeta.FaddeevStripGrowthBoxReduction
