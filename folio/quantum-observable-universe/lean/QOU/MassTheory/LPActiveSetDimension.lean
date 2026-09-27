import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Algebra.BigOperators.Fin

/-!
# QOU.MassTheory.LPActiveSetDimension

**The operator-selection LP's active set has cardinality at most `d - 1`, where
`d` is the size of the operator basis — whatever the Frobenius Gram is.**

Bean `qou-brng` (the linking-vs-self-energy amplitude assignment).

## Why this exists

`QOU.MassTheory.UICGateNotFromComplementarySlackness` established that the
operator-selection LP's active set is not the UIC Pass-2 gate, *for an
orthogonal basis*: Wedderburn block projectors give a diagonal Frobenius Gram
`G_lm = tr_M(P_l P_m) = δ_lm tr_M(P_l)`, complementary slackness decouples, and
the atom's traces never enter.  That diagnosis named an escape — use a
**non-orthogonal** basis, whose Gram is dense, and the LP "recovers
discriminating power".

The escape does not exist, and the reason is a dimension count rather than a
sparsity pattern.  The LP is (`pyhecke/lp_dual_solver.py:1147-1152`)

```
  max  tᵀ x    s.t.   1ᵀ x = n_target    (dual y₀)
                      G x ≥ 0            (dual y ≥ 0)
                      x ≥ -M
```

with `G_ij = tr_M(e_i e_j)`.  Complementary slackness reads `y_i · (G x)_i = 0`,
and `(G x)_i = ∑_j tr_M(e_i e_j) x_j = tr_M(e_i · Φ)` with `Φ = ∑_j x_j e_j` the
selected operator — so an active index is a basis element **Frobenius-orthogonal
to `Φ`**.  `exists_slack` then says not all of them can be, because `G x = 0`
would force `x = 0` and contradict the net constraint.

## What it forecloses

`activeSetCard_lt` bounds the active set by the **size of the basis**, with no
reference to the atom's traces `t`, to `n_target`, or to the Gram's density.  A
binding multiplier must depend on the nucleus; this quantity cannot, under any
basis.  Measured companion (all assertions pass):
`computations/probes/lp_active_set_is_pinned_by_dimension_probe.py`, which
sweeps a corpus-derived non-orthogonal basis from off-diagonal fraction `0.000`
to `1.000` at full rank and finds `|active| = d - 1` throughout.

**Scope (b)**, structural exclusion; invariant = invertibility of the Gram
together with a non-zero net constraint.  It holds over any field, hence for
every `n`, `q` and trace convention.  It excludes the **active set** only — the
LP's optimal value and `y₀*` are untouched, as is `qou-brng`'s real target, the
extensive term itself.

The two ways out are the two degenerate cases, and both are hypotheses here
rather than conclusions: a **singular** Gram (then `G x = 0` has a kernel, but
the operators are not a basis) and an **indefinite** one (then the LP is
unbounded and a solver returns a box corner —
`h6_block_selection_lp_probe.py` retracted exactly such a reading of the braid
sub-word basis on 2026-08-16).
-/

namespace QOU.MassTheory.LPActiveSetDimension

open Finset

variable {d : ℕ} {K : Type*} [Field K] [DecidableEq K]

/-- **Not every Frobenius constraint can be tight.**  If the Gram `G` is
invertible and the net constraint `∑ i, x i = n` is non-zero, some coordinate of
`G.mulVec x` is non-zero.

This is the whole content: `G x = 0` forces `x = 0` by injectivity, and then the
net constraint reads `0 = n`. -/
theorem exists_slack {G : Matrix (Fin d) (Fin d) K} (hG : IsUnit G)
    {x : Fin d → K} {n : K} (hn : n ≠ 0) (hx : ∑ i, x i = n) :
    ∃ i, G.mulVec x i ≠ 0 := by
  by_contra h
  push_neg at h
  have hzero : G.mulVec x = G.mulVec 0 := by
    funext i
    simp [h i]
  have hx0 : x = 0 := (Matrix.mulVec_injective_iff_isUnit.2 hG) hzero
  rw [hx0] at hx
  simp only [Pi.zero_apply, Finset.sum_const_zero] at hx
  exact hn hx.symm

/-- **The tight set is a proper subset of the index set**, hence has cardinality
`< d`. -/
theorem tightSetCard_lt {G : Matrix (Fin d) (Fin d) K} (hG : IsUnit G)
    {x : Fin d → K} {n : K} (hn : n ≠ 0) (hx : ∑ i, x i = n) :
    (univ.filter fun i => G.mulVec x i = 0).card < d := by
  obtain ⟨i, hi⟩ := exists_slack hG hn hx
  have hss : (univ.filter fun j => G.mulVec x j = 0) ⊂ (univ : Finset (Fin d)) := by
    refine ⟨filter_subset _ _, ?_⟩
    intro hcon
    have : i ∈ univ.filter fun j => G.mulVec x j = 0 := hcon (mem_univ i)
    exact hi (mem_filter.1 this).2
  simpa using card_lt_card hss

/-- **The LP's active set is bounded by the size of the operator basis.**

`hcs` is complementary slackness on the optimal primal-dual pair: a non-zero
dual multiplier forces its Frobenius constraint tight.  The conclusion mentions
neither the cost vector `t`, nor `n_target` beyond its non-vanishing, nor any
property of `G` beyond invertibility — in particular not its sparsity.  So
passing from an orthogonal basis to a non-orthogonal one cannot raise this
bound. -/
theorem activeSetCard_lt {G : Matrix (Fin d) (Fin d) K} (hG : IsUnit G)
    {x y : Fin d → K} {n : K} (hn : n ≠ 0) (hx : ∑ i, x i = n)
    (hcs : ∀ i, y i ≠ 0 → G.mulVec x i = 0) :
    (univ.filter fun i => y i ≠ 0).card < d := by
  have hsub : (univ.filter fun i => y i ≠ 0) ⊆ (univ.filter fun i => G.mulVec x i = 0) := by
    intro i hi
    exact mem_filter.2 ⟨mem_univ i, hcs i (mem_filter.1 hi).2⟩
  exact lt_of_le_of_lt (card_le_card hsub) (tightSetCard_lt hG hn hx)

/-- The same bound in the `≤ d - 1` form the probe reports. -/
theorem activeSetCard_le_pred {G : Matrix (Fin d) (Fin d) K} (hG : IsUnit G)
    {x y : Fin d → K} {n : K} (hn : n ≠ 0) (hx : ∑ i, x i = n)
    (hcs : ∀ i, y i ≠ 0 → G.mulVec x i = 0) :
    (univ.filter fun i => y i ≠ 0).card ≤ d - 1 :=
  Nat.le_sub_one_of_lt (activeSetCard_lt hG hn hx hcs)

end QOU.MassTheory.LPActiveSetDimension
