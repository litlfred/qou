import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.Ring.Basic
import Mathlib.Tactic


/-!
# Topological decomposition of vortex mass (conjectural)

This file axiomatizes the vortex mass decomposition conjecture
(`conj:topological-decomposition-mass`) as a `class` and proves four
downstream structural results **unconditionally** from the class axioms.

The conjecture asserts that for a closed cycle ϱ (vortex) in a quantum
observable universe, the categorical mass decomposes as:

    m(ϱ) = ‖Hol_∇(ϱ₀; G)‖ + Σᵢ₌₁ᴺ ‖Φ_q(zᵢ)‖

where:
- `Hol_∇(ϱ₀; G)` is the gauge holonomy along the unknot core ϱ₀,
- `Φ_q(zᵢ)` are the quantum-dilogarithm values at the N blow-up
  centres zᵢ of the brane boundary (`def:brane-boundary`).

**Note:** The conjecture differs from the proved theorem
(`thm:topological-mass`) in that `thm:topological-mass` uses the
categorical descent trace on the recursive brane tower, whereas this
conjecture expresses the descent piece as a gauge holonomy.  Bridging
the two formulations is the main open proof obligation.

All results below are purely algebraic — no quantum-dilogarithm
evaluation, no numerical approximation.

## Results

1. `mass_unique`                    — decomposition uniquely determines mass
2. `mass_nonneg`                    — mass is non-negative
3. `mass_gt_holonomy_of_dilog_pos`  — blow-ups increase mass beyond holonomy
4. `mass_eq_holonomy_of_flat`       — in the flat case (N=0) mass = holonomy
5. `mass_add_dilog`                 — adding one more blow-up increases mass

## References

- [leitner2026] conj:topological-decomposition-mass
- [leitner2026] thm:topological-mass
- [leitner2026] cor:quantum-dilogarithm
- [leitner2026] def:brane-boundary
-/

open Finset BigOperators

namespace QOU.TopologicalMass

-- Ref: [leitner2026] conj:topological-decomposition-mass

/-- **Vortex mass decomposition conjecture** (axiomatized as a class).

    An instance `TopologicalDecompositionMass R vortex` asserts that
    the mass of `vortex` decomposes as
        mass = holonomy + Σᵢ dilog i,
    where:
    - `holonomy` is the gauge-holonomy norm ‖Hol_∇(ϱ₀; G)‖ ≥ 0,
    - `dilog i` is the quantum-dilogarithm norm ‖Φ_q(zᵢ)‖ ≥ 0
      at the i-th blow-up centre,
    - `N` is the number of exceptional divisors.

    The `decomp` field is the conjecture itself; instances supply it
    as an axiomatic hypothesis.  All theorems below are sorry-free. -/
-- Ref: [leitner2026] conj:topological-decomposition-mass
class TopologicalDecompositionMass (R : Type*) [AddCommMonoid R] [PartialOrder R] [IsOrderedAddMonoid R]
    (vortex : Type*) where
  /-- Gauge-holonomy contribution ‖Hol_∇(ϱ₀; G)‖. -/
  holonomy : R
  holonomy_nonneg : 0 ≤ holonomy
  /-- Number of exceptional divisors (blow-up centres). -/
  N : ℕ
  /-- Quantum-dilogarithm values ‖Φ_q(zᵢ)‖ at each blow-up centre. -/
  dilog : Fin N → R
  /-- Each dilogarithm value is non-negative. -/
  dilog_nonneg : ∀ i, 0 ≤ dilog i
  /-- The total categorical mass. -/
  mass : R
  /-- **The decomposition equation** (the conjecture). -/
  decomp : mass = holonomy + ∑ i, dilog i

-- ────────────────────────────────────────────────────────────────────────────
-- Downstream conditional theorems — all proved from `decomp` alone.
-- ────────────────────────────────────────────────────────────────────────────

/-- **Mass is uniquely determined by the decomposition.**

    Any element m agreeing with holonomy + Σ dilog equals the class mass.
    In other words, the decomposition `decomp` has at most one solution
    for `mass` given the holonomy and dilogarithm data. -/
-- Ref: [leitner2026] conj:topological-decomposition-mass §"Proof obligations"
theorem mass_unique {R : Type*} [AddCommMonoid R] [PartialOrder R] [IsOrderedAddMonoid R] (vortex : Type*)
    [M : TopologicalDecompositionMass R vortex]
    (m : R) (h : m = M.holonomy + ∑ i, M.dilog i) :
    m = M.mass := by
  rw [h, M.decomp]

/-- **Mass is non-negative.**

    Both the holonomy and all dilogarithm values are non-negative, so
    their sum is non-negative.  This is the physical content that
    mass ≥ 0 follows purely from the categorical structure. -/
-- Ref: [leitner2026] conj:topological-decomposition-mass
theorem mass_nonneg {R : Type*} [AddCommMonoid R] [PartialOrder R] [IsOrderedAddMonoid R] (vortex : Type*)
    [M : TopologicalDecompositionMass R vortex] :
    0 ≤ M.mass := by
  rw [M.decomp]
  apply add_nonneg M.holonomy_nonneg
  apply sum_nonneg
  intro i _
  exact M.dilog_nonneg i

/-- **In the flat case (no blow-ups), mass equals the holonomy.**

    When N = 0 the brane boundary has no exceptional divisors, so the
    transient (dilogarithm) piece vanishes and mass = holonomy. -/
-- Ref: [leitner2026] conj:topological-decomposition-mass §"Proof obligations"
theorem mass_eq_holonomy_of_flat {R : Type*} [AddCommMonoid R] [PartialOrder R] [IsOrderedAddMonoid R]
    (vortex : Type*) [M : TopologicalDecompositionMass R vortex]
    (hN : M.N = 0) : M.mass = M.holonomy := by
  rw [M.decomp]
  have : ∑ i : Fin M.N, M.dilog i = 0 := by
    apply Finset.sum_eq_zero
    intro i _
    exact absurd i.isLt (by omega)
  rw [this, add_zero]

/-- **Blow-ups strictly increase mass above the holonomy.**

    When N ≥ 1 and all dilogarithm values are strictly positive,
    the mass strictly exceeds the holonomy contribution. -/
-- Ref: [leitner2026] conj:topological-decomposition-mass
theorem mass_gt_holonomy_of_dilog_pos {R : Type*}
    [AddCommMonoid R] [PartialOrder R] [IsOrderedCancelAddMonoid R]
    (vortex : Type*) [M : TopologicalDecompositionMass R vortex]
    (hN : 0 < M.N) (hd : ∀ i, 0 < M.dilog i) :
    M.holonomy < M.mass := by
  rw [M.decomp]
  apply lt_add_of_le_of_pos (le_refl _)
  apply sum_pos (fun i _ => hd i)
  exact univ_nonempty_iff.mpr ⟨⟨0, hN⟩⟩

/-- **Adding a blow-up centre does not decrease mass.**

    If two vortices share the same holonomy and all but one dilogarithm
    value, the one with the extra blow-up centre has mass ≥ the other. -/
-- Ref: [leitner2026] conj:topological-decomposition-mass §"Proof obligations"
theorem mass_mono_of_extra_dilog {R : Type*} [AddCommMonoid R] [PartialOrder R] [IsOrderedAddMonoid R]
    (vortex₁ vortex₂ : Type*)
    [M₁ : TopologicalDecompositionMass R vortex₁]
    [M₂ : TopologicalDecompositionMass R vortex₂]
    (hN : M₂.N = M₁.N + 1)
    (hhol : M₁.holonomy = M₂.holonomy)
    (hd : ∀ i : Fin M₁.N, M₁.dilog i = M₂.dilog ⟨i.val, by omega⟩)
    (hextra_nonneg : 0 ≤ M₂.dilog ⟨M₁.N, by omega⟩) :
    M₁.mass ≤ M₂.mass := by
  rw [M₁.decomp, M₂.decomp, ← hhol]
  gcongr
  -- Need: Σᵢ<N₁ M₁.dilog i ≤ Σᵢ<N₁+1 M₂.dilog i
  -- Reduce to: Σᵢ<N₁ M₂.dilog i + M₂.dilog N₁ ≥ Σᵢ<N₁ M₁.dilog i
  calc ∑ i : Fin M₁.N, M₁.dilog i
      = ∑ i : Fin M₁.N, M₂.dilog (Fin.cast hN.symm i.castSucc) := by
        refine Finset.sum_congr rfl fun i _ => ?_
        exact hd i
    _ ≤ ∑ i : Fin (M₁.N + 1), M₂.dilog (Fin.cast hN.symm i) := by
        rw [Fin.sum_univ_castSucc]
        exact le_add_of_nonneg_right hextra_nonneg
    _ = ∑ i : Fin M₂.N, M₂.dilog i := Fin.sum_congr' _ hN.symm

/-- **Flat-vortex satisfiability witness** (a `def`, deliberately NOT an
    `instance`).  The data `holonomy = 0`, `N = 0`, `mass = 0` satisfies
    `decomp` by `simp`.  It shows only that the class is consistent; it
    encodes none of the conjectural content.

    This was a global `instance` until 2026-10-10 (bean `tmvac`).  As an
    instance over an arbitrary `vortex` it was found by typeclass resolution
    for every vortex type, so any `[TopologicalDecompositionMass ℝ vortex]`
    binder was discharged with all-zero data and `M.mass` resolved to `0`.
    That preempted the §3b-cond hypothesis rather than witnessing it.  Use
    it explicitly, e.g. `@mass_nonneg ℝ _ _ _ v (flatVortex v)`, where a
    consistency check is wanted.

    Note that `mass` is itself a field of the class, so `decomp` relates
    fields of one instance to each other.  It does not tie `mass` to a mass
    defined independently of the instance. -/
-- Ref: [leitner2026] conj:topological-decomposition-mass §"Skeleton"
def flatVortex (vortex : Type*) :
    TopologicalDecompositionMass ℝ vortex where
  holonomy := 0
  holonomy_nonneg := le_refl 0
  N := 0
  dilog := fun i => i.elim0
  dilog_nonneg := fun i => i.elim0
  mass := 0
  decomp := by simp

end QOU.TopologicalMass
