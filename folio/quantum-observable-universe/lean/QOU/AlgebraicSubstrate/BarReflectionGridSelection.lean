/-
# Bar-reflection selection on the theta-grid continuum — the two-point
# narrowing of the extension-circle question (generic group core)

The fibre-level open content of the computational-time conjecture is,
after the 2026-08-01 representability + kernel-selection campaigns, the
choice of a distinguished self-adjoint extension of the derived Jacobi
operator; the atomic representing kernels are the theta-grid kernels
supported on `u · q̃^ℤ`, one per translate class
`u ∈ ℝ_{>0} / q̃^ℤ`, and the identified derivation route is the action
of the bar reflection `s ↦ q̃⁻¹/s` on this continuum.

This module proves, sorry-free, the STRUCTURAL leg of that route:

* the bar reflection is an involution and maps the grid through `u` to
  the grid through `u⁻¹` (`barReflect_mem_grid_iff`) — so it acts on
  translate classes by `u ↦ u⁻¹`;
* a grid class is bar-invariant iff `u² ∈ q̃^ℤ`
  (`grid_barInvariant_iff`);
* given a half-step `w` with `w² = q̃` (and 2-torsion-freeness, true in
  `ℝ_{>0}`), the bar-invariant classes are EXACTLY the two named
  candidates: the unit class `u ≡ 1` and the half-step class
  `u ≡ q̃^{1/2}` (`grid_barInvariant_classification`).

Scope (honest): this is a conditional two-point narrowing — IF the
distinguished kernel is atomic and bar-invariant (bar-invariance being
the selection principle, motivated by the exact bar-invariance of the
balanced moment functional), THEN its grid class lies in the two-point
set `{1, q̃^{1/2}}` — the pair whose half-`q̃`-step separation is the
KSel-1 discriminant. It does NOT select between the two, and it does
not prove the distinguished extension is atomic or bar-invariant;
those remain the conjecture's open fibre content.

Base ring (§7c): the grid/reflection algebra is pure multiplicative
group theory, so the core is stated over a generic `CommGroup G`; the
archimedean instantiation at `G = {x : ℝ // 0 < x}` lives in
`QOU.Archimedean.BarReflectionGridSelectionReal`.

-- Ref: [leitner2026] predicted-spectra, conj:schwinger-measure-computational-time
--      (State after the representability and kernel-selection campaigns, 2026-08-01);
--      docs/audits/2026-08-01-ksel2-gns-favard-canonicity.md;
--      docs/audits/2026-08-01-ksel1-singularity-selection.md.
-/

import Mathlib.Algebra.Group.Basic
import Mathlib.Data.Set.Basic
import Mathlib.Tactic.Group
import Mathlib.Algebra.Group.Int.Even

namespace QOU.AlgebraicSubstrate.BarReflectionGridSelection

variable {G : Type*} [CommGroup G]

/-- The **theta grid** through `u` with multiplicative step `v`
(archimedean reading: `v = q̃ = √q`, the balanced half-step; the grid is
the support `u · q̃^ℤ` of an atomic representing kernel). -/
def grid (u v : G) : Set G :=
  {s | ∃ k : ℤ, s = u * v ^ k}

theorem mem_grid_self (u v : G) : u ∈ grid u v :=
  ⟨0, by simp⟩

/-- The **bar reflection** `s ↦ v⁻¹ · s⁻¹` (archimedean reading:
`s ↦ q̃⁻¹/s`, the fibre bar involution on the Schwinger variable). -/
def barReflect (v s : G) : G := v⁻¹ * s⁻¹

theorem barReflect_involutive (v : G) :
    Function.Involutive (barReflect v) := by
  intro s
  unfold barReflect
  rw [mul_inv_rev, inv_inv, inv_inv, mul_comm s v, inv_mul_cancel_left]

/-- The bar reflection maps the grid through `u` into the grid through
`u⁻¹`: `barReflect v (u · v^k) = u⁻¹ · v^(−k−1)`. -/
theorem barReflect_mem_grid (u v : G) {s : G} (h : s ∈ grid u v) :
    barReflect v s ∈ grid u⁻¹ v := by
  obtain ⟨k, rfl⟩ := h
  refine ⟨-k - 1, ?_⟩
  unfold barReflect
  rw [mul_inv_rev, show (-k - 1 : ℤ) = -k + -1 by ring, zpow_add,
    zpow_neg v k, zpow_neg_one v]
  simp [mul_comm, mul_left_comm]

/-- The bar reflection acts on translate classes by `u ↦ u⁻¹`:
membership form, both directions. -/
theorem barReflect_mem_grid_iff (u v s : G) :
    barReflect v s ∈ grid u⁻¹ v ↔ s ∈ grid u v := by
  constructor
  · intro h
    have h2 := barReflect_mem_grid u⁻¹ v h
    rwa [inv_inv, barReflect_involutive v s] at h2
  · exact barReflect_mem_grid u v

/-- Grid equality is translate equivalence: `grid u v = grid w v` iff
`w = u · v^k` for some `k : ℤ`. -/
theorem grid_eq_grid_iff (u w v : G) :
    grid u v = grid w v ↔ ∃ k : ℤ, w = u * v ^ k := by
  constructor
  · intro h
    have : w ∈ grid u v := h ▸ mem_grid_self w v
    exact this
  · rintro ⟨k, rfl⟩
    ext s
    constructor
    · rintro ⟨j, rfl⟩
      exact ⟨j - k, by rw [mul_assoc, ← zpow_add]; ring_nf⟩
    · rintro ⟨j, rfl⟩
      exact ⟨k + j, by rw [mul_assoc, ← zpow_add]⟩

/-- **Bar-invariance criterion.** The grid class of `u` is fixed by the
bar reflection iff `u² ∈ v^ℤ`. -/
theorem grid_barInvariant_iff (u v : G) :
    grid u⁻¹ v = grid u v ↔ ∃ k : ℤ, u ^ 2 = v ^ k := by
  rw [grid_eq_grid_iff]
  constructor
  · rintro ⟨k, hk⟩
    refine ⟨k, ?_⟩
    have : u * u = u * (u⁻¹ * v ^ k) := by rw [← hk]
    rw [pow_two, this, ← mul_assoc, mul_inv_cancel, one_mul]
  · rintro ⟨k, hk⟩
    refine ⟨k, ?_⟩
    rw [← hk, pow_two, ← mul_assoc, inv_mul_cancel, one_mul]

/-- **The two-point classification.** Suppose the step has a half-step
`w` (`w² = v`) and `G` is 2-torsion-free (both hold in `ℝ_{>0}`). Then
a grid class is bar-invariant iff it is the unit class `grid 1 v` or
the half-step class `grid w v` — the two named candidates of the
extension-circle question, separated by exactly half a `q̃`-step
(the KSel-1 discriminant). -/
theorem grid_barInvariant_classification (u v w : G)
    (hw : w ^ 2 = v) (htf : ∀ x : G, x ^ 2 = 1 → x = 1) :
    grid u⁻¹ v = grid u v ↔ (grid u v = grid 1 v ∨ grid u v = grid w v) := by
  have hww : w * w = v := by rw [← pow_two, hw]
  rw [grid_barInvariant_iff]
  constructor
  · rintro ⟨k, hk⟩
    -- u² = v^k = (w·w)^k ⇒ (u · w^(−k))² = 1 ⇒ u = w^k
    have hval : u * u = w ^ k * w ^ k := by
      rw [← pow_two, hk, ← hww, mul_zpow]
    have hsq : (u * w ^ (-k)) ^ 2 = 1 := by
      rw [pow_two]
      calc (u * w ^ (-k)) * (u * w ^ (-k))
          = (u * u) * (w ^ (-k) * w ^ (-k)) := by
            simp [mul_comm, mul_left_comm, mul_assoc]
        _ = (w ^ k * w ^ k) * (w ^ (-k) * w ^ (-k)) := by rw [hval]
        _ = 1 := by
            rw [← zpow_add, ← zpow_add, ← zpow_add,
              show k + k + (-k + -k) = 0 by ring, zpow_zero]
    have hu : u = w ^ k := by
      have h1 : u * w ^ (-k) = 1 := htf _ hsq
      have h2 : u * w ^ (-k) * w ^ k = w ^ k := by rw [h1, one_mul]
      rwa [mul_assoc, ← zpow_add, show -k + k = 0 by ring, zpow_zero,
        mul_one] at h2
    rcases Int.even_or_odd k with ⟨m, hm⟩ | ⟨m, hm⟩
    · left
      rw [grid_eq_grid_iff]
      refine ⟨-m, ?_⟩
      have hum : u = v ^ m := by
        rw [hu, hm, zpow_add, ← hww, mul_zpow]
      rw [hum, ← zpow_add, show m + -m = 0 by ring, zpow_zero]
    · right
      rw [grid_eq_grid_iff]
      refine ⟨-m, ?_⟩
      have hum : u = v ^ m * w := by
        rw [hu, hm, show (2 * m + 1 : ℤ) = (m + m) + 1 by ring, zpow_add,
          zpow_add, zpow_one, ← hww, mul_zpow]
      rw [hum, mul_assoc, mul_comm w (v ^ (-m)), ← mul_assoc, ← zpow_add,
        show m + -m = 0 by ring, zpow_zero, one_mul]
  · rintro (h | h) <;> rw [grid_eq_grid_iff] at h
    · obtain ⟨k, hk⟩ := h
      -- 1 = u · v^k ⇒ u = v^(−k) ⇒ u² = v^(−(k+k))
      refine ⟨-(k + k), ?_⟩
      have hu' : u = v ^ (-k) := by
        have h2 : u * v ^ k * v ^ (-k) = 1 * v ^ (-k) := by rw [← hk]
        rwa [mul_assoc, ← zpow_add, show k + -k = 0 by ring, zpow_zero,
          mul_one, one_mul] at h2
      rw [pow_two, hu', ← zpow_add, show -k + -k = -(k + k) by ring]
    · obtain ⟨k, hk⟩ := h
      -- w = u · v^k ⇒ u = w · v^(−k) ⇒ u² = (w·w) · v^(−(k+k)) = v^(1−(k+k))
      refine ⟨1 - (k + k), ?_⟩
      have hu' : u = w * v ^ (-k) := by
        have h2 : u * v ^ k * v ^ (-k) = w * v ^ (-k) := by rw [← hk]
        rwa [mul_assoc, ← zpow_add, show k + -k = 0 by ring, zpow_zero,
          mul_one] at h2
      rw [pow_two, hu']
      calc (w * v ^ (-k)) * (w * v ^ (-k))
          = (w * w) * (v ^ (-k) * v ^ (-k)) := by
            simp [mul_comm, mul_left_comm, mul_assoc]
        _ = v * v ^ (-k + -k) := by rw [hww, ← zpow_add]
        _ = v ^ (1 - (k + k)) := by
            rw [show (1 - (k + k) : ℤ) = 1 + (-k + -k) by ring,
              zpow_add v 1 (-k + -k), zpow_one]

end QOU.AlgebraicSubstrate.BarReflectionGridSelection
