import QOU.MathlibExt.DoublyPeriodicLiouville

/-!
# Global boundedness of a doubly-periodic function localizes to a fundamental domain

The Faddeev–Volkov uniqueness capstone
(`FaddeevUniquenessBoundedCapstone.faddeevPhi_proportional_of_bounded_ratio`, wired to
the concrete `Φ_b` in `PhiBProdUniquenessAssembly`) leaves one analytic input open: the
**global** strip-boundedness `hbdd : ∀ z, ‖r z‖ ≤ C` of the prefactor-cancelled ratio `r`.
That ratio is **doubly periodic** (elliptic) under the substrate lattice `⟨ib, i/b⟩`
(route-B step 2, `MeromorphicSameOrder` + `FaddeevRigidityMeromorphic`).

This file supplies the periodicity half of `hbdd`: a doubly-periodic function bounded on the
**closed fundamental parallelepiped** (a compact set) is bounded on all of `ℂ`. So the
global `hbdd` reduces to a **local, compact-domain** bound — `‖r‖ ≤ C` on one fundamental
domain — a strictly weaker analytic obligation than the global one. The `℘`-freedom that
would violate boundedness lives entirely inside the fundamental domain (its poles), so this
is the honest localization of the remaining input, not a cosmetic restatement.

The reduction uses **only** periodicity (no differentiability): reducing each `ℝ`-coordinate
of `z` modulo `1` (`Int.fract`) lands `z`, up to a lattice translation `f` ignores, in the
closed ball of radius `‖b 0‖ + ‖b 1‖` — the same `Int.fract`/`⌊·⌋` construction as
`DoublyPeriodicLiouville.const_of_doublyPeriodic`, but ending in the supplied compact-domain
bound instead of Liouville. Verified `lean`-direct against the pinned Mathlib. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-25-faddeev-uniqueness-keystone-state.md
-/

open QOU.MathlibExt.DoublyPeriodicLiouville
open Complex Module

namespace QOU.QBeta.DoublyPeriodicBoundedLocalization

variable {f : ℂ → ℂ}

/-- **Boundedness localizes to the fundamental domain.** A function `f` periodic under both
vectors of an `ℝ`-basis `b` of `ℂ` and bounded by `C` on the closed ball of radius
`‖b 0‖ + ‖b 1‖` (which contains a fundamental parallelepiped) is bounded by `C` everywhere:
every `z` is, up to a lattice translation `f` ignores, congruent to a point of that ball. -/
theorem bounded_of_doublyPeriodic_of_bounded_on_ball {b : Basis (Fin 2) ℝ ℂ} {C : ℝ}
    (h : ∀ i, ∀ z, f (z + b i) = f z)
    (hball : ∀ w ∈ Metric.closedBall (0 : ℂ) (‖b 0‖ + ‖b 1‖), ‖f w‖ ≤ C) (z : ℂ) :
    ‖f z‖ ≤ C := by
  set M : ℝ := ‖b 0‖ + ‖b 1‖ with hM
  set r0 := b.repr z 0 with hr0
  set r1 := b.repr z 1 with hr1
  set z0 : ℂ := Int.fract r0 • b 0 + Int.fract r1 • b 1 with hz0
  have hfract0 : |Int.fract r0| ≤ 1 :=
    abs_le.mpr ⟨by linarith [Int.fract_nonneg r0], le_of_lt (Int.fract_lt_one r0)⟩
  have hfract1 : |Int.fract r1| ≤ 1 :=
    abs_le.mpr ⟨by linarith [Int.fract_nonneg r1], le_of_lt (Int.fract_lt_one r1)⟩
  have hmem : z0 ∈ Metric.closedBall (0 : ℂ) M := by
    rw [Metric.mem_closedBall, dist_zero_right, hz0]
    calc ‖Int.fract r0 • b 0 + Int.fract r1 • b 1‖
        ≤ ‖Int.fract r0 • b 0‖ + ‖Int.fract r1 • b 1‖ := norm_add_le _ _
      _ = |Int.fract r0| * ‖b 0‖ + |Int.fract r1| * ‖b 1‖ := by
          rw [norm_smul, norm_smul, Real.norm_eq_abs, Real.norm_eq_abs]
      _ ≤ 1 * ‖b 0‖ + 1 * ‖b 1‖ :=
          add_le_add (mul_le_mul_of_nonneg_right hfract0 (norm_nonneg _))
            (mul_le_mul_of_nonneg_right hfract1 (norm_nonneg _))
      _ = M := by rw [one_mul, one_mul, hM]
  have hfz0 : f z0 = f z := by
    have hzsum : z0 + ((⌊r0⌋ : ℤ) • b 0 + (⌊r1⌋ : ℤ) • b 1) = z := by
      rw [hz0]
      have hrepr : r0 • b 0 + r1 • b 1 = z := by
        rw [hr0, hr1, ← Fin.sum_univ_two (fun i => b.repr z i • b i), b.sum_repr z]
      rw [← hrepr, ← fract_smul_add_floor_zsmul r0 (b 0),
        ← fract_smul_add_floor_zsmul r1 (b 1)]
      abel
    rw [← hzsum, ← add_assoc,
      periodic_zsmul (h 1) ⌊r1⌋ (z0 + (⌊r0⌋ : ℤ) • b 0),
      periodic_zsmul (h 0) ⌊r0⌋ z0]
  rw [← hfz0]
  exact hball z0 hmem

end QOU.QBeta.DoublyPeriodicBoundedLocalization
