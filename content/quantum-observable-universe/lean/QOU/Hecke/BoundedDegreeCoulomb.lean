/-
# A degree-bounded bond graph cannot carry a Coulomb term

The SEMF Coulomb energy counts proton PAIRS: `a_C · Z(Z-1)/A^{1/3}`, quadratic in
`Z`. The corpus's binding law is a sum over the edges of a bond graph. This file
proves the two cannot meet, for **every** edge set the corpus has built rather
than for the one it happens to use.

`computations/qbeta/qbeta_chain_cannot_carry_coulomb_or_surface_probe.py` showed
the canonical chain carries `2/Z` of the proton pairs — 2.44 % at `Z = 82`. That
argument used nothing about a path except **that its degree is 2**, and every
candidate edge set in the corpus is likewise degree-bounded:

| edge set | edges | max degree | source |
|---|---|---|---|
| canonical chain | `A-1` | 2 | `atom_braid_word_3A` |
| max-contact convex deltahedra | `3A-6` | 5 | GAP-1, bean `qou-lzoh` |
| bounded-degree packing | `kA/2` | `k ≤ 12` | bean `qou-kqdn` |

So the statement worth proving is about the class. By the degree-sum formula
`2E = Σ_v deg v ≤ dZ`, so the edge count is **linear** in `Z` however the graph
is drawn, and its share of the `Z(Z-1)/2` pairs is at most `d/(Z-1)`, which goes
to zero. `exists_gt_bounded_degree_bond_sum` is the quantitative form: no
constant per-bond energy makes a degree-bounded bond sum keep up with a
quadratic.

## The limit, stated honestly — and it is about RANGE, not coupling

Everything below assumes the per-bond energy does **not itself grow with `Z`**.
A law with `ε(Z) ~ Z` is untouched by this file.

That is the formal limit, but reading it as "the repair is a `Z`-dependent
coupling" is wrong, and an earlier version of this docstring said so. **A bond
graph is a kernel truncated at range 1**; Coulomb is `1/r` with no truncation.
Weighting the captured pairs by `1/r` shows the model does not merely fall
short — it **overshoots ⁴He by 16×** and undershoots ²⁰⁸Pb (1587 % → 73 %,
crossing near Sn), because a contact sum is `kZ/2`, linear in `Z` with no `A` in
it, while the true sum over a ball of radius `R = r₀A^{1/3}` is
`(3/5)Z(Z-1)/R`. A ratio on both sides of 1 is not fixable by rescaling a
letter. The repair is a decay kernel over **all** pairs — a weighted complete
graph, degree `Z-1`, which is exactly the case this file excludes. Theorem and
physics agree: the bond-graph form truncates range, and Coulomb does not.

## What this closes, and what it does not

It closes "Coulomb is a missing TERM in the bond graph": it is outside the
bond-graph *form*, because the form truncates range — which is physically right,
Coulomb being `1/r` long-range rather than contact. It says nothing about the surface term, which the same degree bound
*supplies* rather than forbids (`QOU/Mass/CoordinationSurfaceDeficit.lean`, bean
`qou-kqdn`): a boundary deficit is exactly what a bounded degree gives you.

Bean `qou-556v`; generalises `qou-nial`.
-/

import Mathlib.Combinatorics.SimpleGraph.DegreeSum
import Mathlib.Tactic

namespace QOU.Hecke.BoundedDegreeCoulomb

open Finset

/-- **The degree-sum formula as a bond-count bound.**
A graph in which no vertex has more than `d` neighbours has at most `dn/2`
edges, whatever else is true of it. This is the whole content of "a chain cannot
carry Coulomb", with the chain replaced by its only relevant property. -/
theorem two_mul_card_edge_le {V : Type*} [Fintype V] (G : SimpleGraph V)
    [DecidableRel G.Adj] {d : ℕ} (hd : ∀ v, G.degree v ≤ d) :
    2 * #G.edgeFinset ≤ Fintype.card V * d := by
  rw [← SimpleGraph.sum_degrees_eq_twice_card_edges]
  calc ∑ v, G.degree v ≤ ∑ _v : V, d := Finset.sum_le_sum fun v _ => hd v
    _ = Fintype.card V * d := by simp [Finset.card_univ, mul_comm]

/-- The fraction of PAIRS that a degree-bounded graph's edges cover is at most
`d/(n-1)`. At `d = 2` (a chain) this is the measured `2/(Z-1)`; at `d = 12`
(close packing) it is `12/(Z-1)`. Bounded either way, and vanishing. -/
theorem edge_share_le {n E d : ℝ} (hn : 1 < n) (hE : 2 * E ≤ n * d) :
    E / (n * (n - 1) / 2) ≤ d / (n - 1) := by
  have h1 : (0 : ℝ) < n - 1 := by linarith
  have hn0 : (0 : ℝ) < n := by linarith
  have hden : (0 : ℝ) < n * (n - 1) / 2 := by positivity
  rw [div_le_div_iff₀ hden h1]
  nlinarith [hE, h1, hn0]

/-- **No constant per-bond energy makes a degree-bounded bond sum quadratic.**

Given any per-bond energy `ε ≥ 0`, any degree bound `d ≥ 0` and any Coulomb
coefficient `c > 0`, past a computable size EVERY graph with that degree bound
has `ε · (its bond count)` strictly below `c · (its pair count)`. The bond sum is
linear; the pair count is not; and no choice of the letters closes the gap.

Compare `BindingExtensivity.exists_pow_gt_linear`, which separates a different
pair of growth classes (exponential vs linear) for a different purpose. -/
theorem exists_gt_bounded_degree_bond_sum {ε c d : ℝ}
    (hε : 0 ≤ ε) (hc : 0 < c) (hd : 0 ≤ d) :
    ∃ N : ℝ, 1 < N ∧ ∀ n E : ℝ, N ≤ n → 0 ≤ E → 2 * E ≤ n * d →
      ε * E < c * (n * (n - 1) / 2) := by
  have hq : (0 : ℝ) ≤ ε * d / c := by positivity
  refine ⟨2 + ε * d / c, by linarith, ?_⟩
  intro n E hN hE0 hE
  have hn2 : (2 : ℝ) ≤ n := by nlinarith [div_nonneg (mul_nonneg hε hd) hc.le]
  -- `n - 1` already exceeds `ε d / c`, so `c (n-1)` exceeds `ε d`.
  have hkey : ε * d < c * (n - 1) := by
    have h : ε * d / c ≤ n - 2 := by linarith
    have := (div_le_iff₀ hc).mp h
    nlinarith
  have hle : ε * E ≤ ε * (n * d / 2) :=
    mul_le_mul_of_nonneg_left (by linarith) hε
  have hpos : (0 : ℝ) < n / 2 := by linarith
  nlinarith [mul_lt_mul_of_pos_left hkey hpos, hle]

/-- Restated on the graph itself: past `N`, a degree-bounded bond sum is below
the Coulomb target for that same vertex set. This is the form the measurement
instantiates — `d = 2` for the chain, `d = 5` for the max-contact deltahedra,
`d = 12` for close packing. -/
theorem bond_sum_lt_pair_target {V : Type*} [Fintype V] (G : SimpleGraph V)
    [DecidableRel G.Adj] {d : ℕ} (hd : ∀ v, G.degree v ≤ d) {ε c N : ℝ}
    (hN : ∀ n E : ℝ, N ≤ n → 0 ≤ E → 2 * E ≤ n * d → ε * E < c * (n * (n - 1) / 2))
    (hcard : N ≤ (Fintype.card V : ℝ)) :
    ε * #G.edgeFinset < c * ((Fintype.card V : ℝ) * ((Fintype.card V : ℝ) - 1) / 2) := by
  refine hN _ _ hcard (by positivity) ?_
  exact_mod_cast two_mul_card_edge_le G hd

end QOU.Hecke.BoundedDegreeCoulomb
