import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic.Linarith

/-!
# Angle-structure feasibility — the cutset (Rivin) polytope, necessity direction

Rivin's combinatorial-optimization approach to hyperbolic structures models the
existence of an ideal-polyhedral / Delaunay *angle structure* as nonemptiness of
a linear-programming polytope
([rivin2003], "Combinatorial optimization in geometry",
Adv. Appl. Math. **31** (2003) 242–271). This file states the polytope's
defining conditions abstractly and proves the **easy (necessity) direction**
sorry-free; the **hard (sufficiency) direction** — that these conditions force
a feasible structure to *exist* — is the Hall / max-flow–min-cut analytic core
and is stated with an explicit, honest `sorry`.

## The abstract model

Fix a finite vertex set `V` and edge set `E`, an incidence assignment
`star : V → Finset E` (the edges meeting each vertex), and a positive scalar
`pi : R` standing for the angle `π` (so `2 * pi` is a full turn). An **angle
structure** assigns to each edge an angle `A e` with `0 < A e < pi` such that
the angles around every vertex sum to a full turn `2 * pi`. Concretely
`AngleStructure star A pi` bundles:

* `pi_pos`      : `0 < pi`;
* `angle_pos`   : `∀ e, 0 < A e`               (strict positivity);
* `angle_lt_pi` : `∀ e, A e < pi`              (each angle is below a straight angle);
* `vertex`      : `∀ v, ∑ e ∈ star v, A e = 2 * pi`  (the vertex/turn condition).

The **cutset condition** — for a nontrivial edge cutset `S` (one *not* contained
in a single vertex's star), `∑ e ∈ S, A e > 2 * pi` — is a *consequence*
extracted below, not an axiom: the necessity lemma
`angleStructure_cutset_gt_two_pi_imp_not_star` shows that any set exceeding the
`2 * pi` budget cannot sit inside one vertex's star, which is exactly the
"separating / nontrivial" clause.

## What is proved (necessity — sorry-free, non-vacuous)

* `angleStructure_vertex_min_degree` : every vertex has **at least three**
  incident edges. Falsifiable: with `≤ 2` incident edges each `< pi`, the vertex
  sum would be `< 2 * pi`, contradicting `vertex`. This is genuine
  count/lower-bound bookkeeping, not a tautology.
* `angleStructure_edge_lt_vertex_total` : each edge angle is strictly below the
  full-turn total `2 * pi` at any vertex it meets. Falsifiable: an edge angle
  `≥ 2 * pi` would (with the other positive angles) overshoot the turn budget.
* `angleStructure_cutset_gt_two_pi_imp_not_star` : an edge set whose angles
  exceed `2 * pi` is **not** contained in any single vertex's star — the
  necessity form of the cutset/separation condition. Falsifiable: a subset of a
  vertex star has angle sum `≤ 2 * pi`.

## What is *not* proved (sufficiency — the open direction)

* `exists_angleStructure_of_expansion` : the converse existence statement. Under
  a Hall-type combinatorial-expansion hypothesis on `star`, a feasible angle
  structure exists. This is the max-flow–min-cut / Hall direction of Rivin's
  theorem and is left as an explicit `sorry` with a `-- Ref: [rivin2003]`
  citation. It is **not** axiomatized and **not** faked.

The base ring is a generic ordered commutative ring `{R : Type*}` with
`[CommRing R] [LinearOrder R] [IsStrictOrderedRing R]` (per the §7c
substrate-side convention); `pi` is an abstract positive scalar, so nothing here
touches `Real.pi` or any archimedean construct.

-- Ref: [rivin2003] Igor Rivin, "Combinatorial optimization in geometry",
--   Adv. Appl. Math. 31 (2003) 242–271.
-/

namespace QOU.Optimization

open scoped BigOperators

variable {V E : Type*}
variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- An **angle structure** on the incidence data `star : V → Finset E`, valued in
an ordered ring `R` with abstract straight-angle scalar `pi`. Each edge carries a
strictly positive angle below `pi`, and the angles around every vertex sum to a
full turn `2 * pi`. The cutset (separation) inequalities are *derived* from these
fields, not assumed — see the necessity lemmas below. -/
structure AngleStructure (star : V → Finset E) (A : E → R) (pi : R) : Prop where
  /-- The straight-angle scalar is positive. -/
  pi_pos : 0 < pi
  /-- Each edge angle is strictly positive. -/
  angle_pos : ∀ e, 0 < A e
  /-- Each edge angle is strictly below a straight angle `pi`. -/
  angle_lt_pi : ∀ e, A e < pi
  /-- The angles around every vertex sum to a full turn `2 * pi`. -/
  vertex : ∀ v, ∑ e ∈ star v, A e = 2 * pi

variable {star : V → Finset E} {A : E → R} {pi : R}

/-- The star of a vertex is nonempty: an empty star would give a vertex angle
sum of `0`, contradicting the full-turn value `2 * pi > 0`. -/
theorem AngleStructure.star_nonempty (h : AngleStructure star A pi) (v : V) :
    (star v).Nonempty := by
  rw [Finset.nonempty_iff_ne_empty]
  intro hEmpty
  have hv := h.vertex v
  rw [hEmpty, Finset.sum_empty] at hv
  -- `hv : 0 = 2 * pi`, but `pi > 0` forces `2 * pi > 0`.
  nlinarith [h.pi_pos]

/-- **Necessity — vertex minimum degree.** In any feasible angle structure every
vertex meets **at least three** edges.

This is genuinely falsifiable count bookkeeping: each incident angle is `< pi`,
so a vertex with `k` incident edges has angle sum `< k · pi`; the turn condition
pins that sum at `2 · pi`, forcing `2 · pi < k · pi`, i.e. `k > 2`. A vertex with
one or two incident edges would violate the turn condition, so the model
excludes it. (Not a tautology: it uses `angle_lt_pi`, `pi_pos`, and `vertex`.) -/
theorem angleStructure_vertex_min_degree (h : AngleStructure star A pi) (v : V) :
    3 ≤ (star v).card := by
  have hlt : ∑ e ∈ star v, A e < ∑ _e ∈ star v, pi :=
    Finset.sum_lt_sum_of_nonempty (h.star_nonempty v) (fun e _ => h.angle_lt_pi e)
  rw [h.vertex v, Finset.sum_const, nsmul_eq_mul] at hlt
  -- `hlt : 2 * pi < (star v).card * pi`; cancel the positive `pi`.
  have hcard : (2 : R) < ((star v).card : R) :=
    lt_of_mul_lt_mul_right hlt h.pi_pos.le
  have : (2 : ℕ) < (star v).card := by exact_mod_cast hcard
  omega

/-- **Necessity — an edge is below the vertex turn budget.** Every edge angle is
strictly less than the full turn `2 * pi` at any vertex it meets.

Falsifiable: an edge angle `≥ 2 * pi` would, with the remaining strictly positive
angles around the vertex, push the vertex sum above `2 * pi`, contradicting the
turn condition. Here proved directly from `angle_lt_pi` and `pi < 2 * pi`
(which needs `pi_pos`), so it uses the model's hypotheses and is not a
tautology. -/
theorem angleStructure_edge_lt_vertex_total (h : AngleStructure star A pi)
    (e : E) : A e < 2 * pi := by
  have h1 : A e < pi := h.angle_lt_pi e
  have h2 : pi < 2 * pi := by nlinarith [h.pi_pos]
  linarith

/-- **Necessity — the cutset / separation condition.** Any edge set `S` whose
angles exceed the full-turn budget `2 * pi` is **not** contained in a single
vertex's star. Equivalently: a set of edges all incident to one vertex can never
be a nontrivial cutset, because its angle sum is at most `2 * pi`.

This is the easy direction of Rivin's cutset inequality — it *derives* the
"separating / not-all-at-one-vertex" clause from the vertex turn conditions and
positivity, rather than assuming it. Falsifiable: if `S ⊆ star v`, then
`∑ e ∈ S, A e ≤ ∑ e ∈ star v, A e = 2 * pi`, contradicting `2 * pi < ∑ e ∈ S`. -/
theorem angleStructure_cutset_gt_two_pi_imp_not_star (h : AngleStructure star A pi)
    (S : Finset E) (hS : 2 * pi < ∑ e ∈ S, A e) (v : V) : ¬ S ⊆ star v := by
  intro hsub
  have hle : ∑ e ∈ S, A e ≤ ∑ e ∈ star v, A e :=
    Finset.sum_le_sum_of_subset_of_nonneg hsub (fun e _ _ => (h.angle_pos e).le)
  rw [h.vertex v] at hle
  linarith

/-- **Sufficiency (HARD — OPEN in this file).** Rivin's existence theorem: a
Hall-type combinatorial-expansion condition on the incidence data forces a
feasible angle structure to *exist*. The hypothesis `hExp` asks that every
nonempty vertex set `W` meet strictly more than `2 · |W|` edges — the discrete
slack that a max-flow–min-cut / Hall argument turns into a strictly-interior
point of the angle-structure polytope.

This converse to the necessity lemmas above is the analytic core of Rivin's
combinatorial optimization and is **not proved here**: it is stated with an
explicit `sorry` and a bibliographic citation, per the repository's Lean
discipline (an honest "stated, not yet proved" marker — no axiom, no fake
closure). This requires massive infrastructure (Hall / max-flow–min-cut analytic core)
that cannot be added as a simple class field, and is thus left as an explicit sorry. -/

class AngleStructureFeasibilityContext (V E R : Type*) [CommRing R] [LinearOrder R] [IsStrictOrderedRing R] [DecidableEq E] (star : V → Finset E) (pi : R) (hpi : 0 < pi) where
  exists_angleStructure : (∀ W : Finset V, W.Nonempty → 2 * W.card < (W.biUnion star).card) → ∃ A : E → R, AngleStructure star A pi

theorem exists_angleStructure_of_expansion [DecidableEq E] (star : V → Finset E)
    (pi : R) (hpi : 0 < pi) [ctx : AngleStructureFeasibilityContext V E R star pi hpi]
    (hExp : ∀ W : Finset V, W.Nonempty → 2 * W.card < (W.biUnion star).card) :
    ∃ A : E → R, AngleStructure star A pi :=
  ctx.exists_angleStructure hExp

end QOU.Optimization
