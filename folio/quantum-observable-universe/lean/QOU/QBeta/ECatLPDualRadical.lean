/-
  FORMALIZE-FIRST for the operator-selection LP on a geometric cost against the
  Hecke Gram: what the dual price must be, and the single scalar that decides
  in advance whether running the program can tell us anything.

  WHY THIS FILE COMES BEFORE THE COMPUTE. AGENTS.md §"Formalize-first probe
  discipline" says: state the hypothesis class, find the invariant the whole
  class must satisfy, formalize it, and let the result narrow the probe. The
  class here is "run `min Σ tᵢxᵢ s.t. Σxᵢ = n_target, Gx ≥ 0` with the
  discretised-`E_cat` per-block cost `t_λ` in place of the Hecke one". The
  invariant is §2 below, and it collapses the probe to a two-line measurement.

  THE SETTING, for a reader who was not in the session. The corpus's
  operator-selection program is

      primal:  min Σ tᵢ xᵢ   s.t.  Σ xᵢ = n_target,  G x ≥ 0,  xᵢ ≥ -M
      dual:    max n_target · y₀   s.t.  y₀·1 + G y = t,  yᵢ ≥ 0

  with `G` the Frobenius/Gram matrix and `y₀` the shadow price of the net
  constraint -- the quantity `prop:operator-selection-lp` calls the
  binding-energy density. Two facts about the IMPLEMENTED (Hecke) instance are
  already on the record and are what motivate replacing the cost:

    * `G` is singular. Its radical is spanned by the q-antisymmetriser
      `v = (-q³, q², q², -q, -q, 1)`, exactly (`operator_selection_lp.lean`,
      `y_0_eq_zero_of_radical`, over any commutative ring without zero
      divisors).
    * The Hecke cost is a row of that Gram: `t_j = tr_M(b₀b_j) = G_{0j}`.
      Hence `t·x = (Gx)₀` is CONSTANT on the feasible set -- there is nothing
      to optimise -- and `y₀ = 0` is forced.

  `computations/confinement_lp_braid_gram_probe.py` draws the conclusion in
  its own words: *"a surviving formulation has to break (a): change the
  OBJECTIVE, not the Gram."*

  §2 IS THE RESULT, AND IT IS SHARPER THAN "THE DEGENERACY MIGHT NOT APPLY".
  Pairing the dual equality with any radical vector `v` kills the `G y` term,
  because `⟨Gy, v⟩ = ⟨y, Gv⟩ = 0`. What survives is a single scalar equation
  that DETERMINES the shadow price before any solver runs:

      y₀ · ⟨1, v⟩ = ⟨t, v⟩        so        y₀ = ⟨t, v⟩ / ⟨1, v⟩

  Three consequences, all proved below:

    * `dual_price_zero_of_cost_orthogonal_to_radical` -- the recorded Hecke
      collapse, recovered as a special case. A cost orthogonal to the radical
      forces `y₀ = 0`. Nothing about feasibility, symmetry or sign is needed.
    * `dual_price_ne_zero_of_cost_not_orthogonal` -- THE ESCAPE, and the
      formalize-first payoff. If `⟨t, v⟩ ≠ 0` the shadow price is forced
      NON-zero. So the question "can the geometric cost give a live dual?" is
      answered by ONE inner product, computable without an LP solver, without
      a feasible point, and without `n_target`.
    * `dual_price_is_solver_independent` -- and the value is then pinned, not
      merely nonzero: every dual-feasible `y₀` equals the same ratio. A solver
      that returned anything else would be wrong, which makes this a CHECK on
      the eventual compute rather than a prediction to be confirmed by it.

  WHAT THE PROBE SHOULD THEREFORE MEASURE, and it is two numbers:

      ⟨t_geometric, v⟩     and     ⟨1, v⟩

  If the first is zero the geometric cost collapses exactly as the Hecke one
  does and the route is dead without running anything. If it is nonzero, `y₀`
  is already known and the LP is worth solving for the primal.

  🛑 WHAT THIS DOES NOT SAY.

  * It does NOT say the geometric cost is non-orthogonal to the radical. That
    is a measurement, deliberately not made here -- making it here, and then
    keeping the cost because the answer came out well, would be selection
    against the target.
  * It does NOT say a nonzero `y₀` selects any word. The dual price is one
    number; selection is a primal question, and §3's
    `cost_from_gram_makes_objective_a_constraint_readout` shows exactly which
    costs make the primal vacuous.
  * `⟨1, v⟩ ≠ 0` is a HYPOTHESIS here. For the H₃ six-basis the corpus records
    `⟨1, v⟩ = -(q-1)(q²-q+1) ≠ 0` for `q ≠ 1`, but that is a fact about that
    basis, not about every Gram, so it is carried as an assumption rather than
    silently assumed.
  * No claim about `Gv = 0` holding for the Gram the geometric cost pairs
    with. The radical is an input.

  Sorry-free. No `axiom`, no conditional class, no `native_decide`. Stated over
  a generic field with no ordering, so nothing here depends on the archimedean
  structure of the LP -- only on its linear algebra.

  -- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/.../operator_selection_lp.lean
  --      (y_0_eq_zero_of_radical -- the recorded Hecke collapse)
  -- Ref: [leitner2026] computations/confinement_lp_braid_gram_probe.py
  -- Ref: [leitner2026] tools/pyhecke/python/pyhecke/lp_dual_solver.py
  -- Ref: [leitner2026] QOU/QBeta/ECatBlockDecomposition.lean  (the cost being proposed)
  -- Ref: [leitner2026] .beans/qou-99qc
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Lemmas
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta.ECatLPDualRadical

open BigOperators

variable {ι R : Type*} [Fintype ι] [Field R]

/-! ### 1. Pairing the dual equality with a radical vector -/

/-- **The radical pairing.**

`Gy` is the image `G y` of the dual variables; `v` spans the radical of `G`, so
`⟨Gy, v⟩ = ⟨y, Gv⟩ = 0` -- carried here as the hypothesis `hGy`, since it is a
fact about `G` and `v` and not about the LP. Pairing the dual equality
`y₀·1 + Gy = t` with `v` leaves one scalar equation.

Everything below is a corollary of this line. -/
theorem radical_pairing (t one v Gy : ι → R) (y₀ : R)
    (hdual : ∀ j, y₀ * one j + Gy j = t j)
    (hGy : ∑ i, Gy i * v i = 0) :
    ∑ i, t i * v i = y₀ * ∑ i, one i * v i := by
  calc ∑ i, t i * v i
      = ∑ i, (y₀ * one i + Gy i) * v i := by simp_rw [hdual]
    _ = ∑ i, (y₀ * (one i * v i) + Gy i * v i) := by
        refine Finset.sum_congr rfl ?_; intros; ring
    _ = y₀ * (∑ i, one i * v i) + ∑ i, Gy i * v i := by
        rw [Finset.sum_add_distrib, ← Finset.mul_sum]
    _ = y₀ * ∑ i, one i * v i := by rw [hGy, add_zero]

/-! ### 2. The shadow price is DETERMINED before any solver runs -/

/-- **`y₀ = ⟨t, v⟩ / ⟨1, v⟩`.**

The shadow price of the net constraint is fixed by two inner products against
the radical vector. No feasible point, no `n_target`, no solver, no ordering.

This is the formalize-first payoff: whether the geometric cost gives a live
dual is decided by ONE number, `⟨t, v⟩`, and the probe that follows has to
compute that and nothing else to know whether the LP is worth running. -/
theorem dual_price_determined_by_radical (t one v Gy : ι → R) (y₀ : R)
    (hdual : ∀ j, y₀ * one j + Gy j = t j)
    (hGy : ∑ i, Gy i * v i = 0)
    (hone : ∑ i, one i * v i ≠ 0) :
    y₀ = (∑ i, t i * v i) / (∑ i, one i * v i) := by
  rw [radical_pairing t one v Gy y₀ hdual hGy, mul_div_assoc, div_self hone,
      mul_one]

/-- **The recorded Hecke collapse, as a special case.**

A cost orthogonal to the radical forces `y₀ = 0`. This is
`y_0_eq_zero_of_radical`'s conclusion reached from the same pairing, and it
holds with no hypothesis about feasibility, symmetry, or signs -- which is why
the collapse cannot be escaped by adjusting the constraints. -/
theorem dual_price_zero_of_cost_orthogonal_to_radical
    (t one v Gy : ι → R) (y₀ : R)
    (hdual : ∀ j, y₀ * one j + Gy j = t j)
    (hGy : ∑ i, Gy i * v i = 0)
    (hone : ∑ i, one i * v i ≠ 0)
    (ht : ∑ i, t i * v i = 0) :
    y₀ = 0 := by
  rw [dual_price_determined_by_radical t one v Gy y₀ hdual hGy hone, ht,
      zero_div]

/-- **THE ESCAPE.** A cost NOT orthogonal to the radical forces a nonzero
shadow price.

So the geometric cost's fate is settled by `⟨t, v⟩` alone. This is the
statement that makes running the LP on `t_λ` a decidable question rather than
a hopeful one — and note the direction: this does not say the geometric cost
clears the bar, only that clearing it is exactly `⟨t, v⟩ ≠ 0`. -/
theorem dual_price_ne_zero_of_cost_not_orthogonal
    (t one v Gy : ι → R) (y₀ : R)
    (hdual : ∀ j, y₀ * one j + Gy j = t j)
    (hGy : ∑ i, Gy i * v i = 0)
    (hone : ∑ i, one i * v i ≠ 0)
    (ht : ∑ i, t i * v i ≠ 0) :
    y₀ ≠ 0 := by
  rw [dual_price_determined_by_radical t one v Gy y₀ hdual hGy hone]
  exact div_ne_zero ht hone

/-- **The price is solver-independent**: any two dual-feasible shadow prices
agree. So the ratio above is a CHECK the eventual compute must satisfy, not a
prediction the compute confirms — a solver returning anything else is wrong. -/
theorem dual_price_is_solver_independent
    (t one v Gy Gy' : ι → R) (y₀ y₀' : R)
    (hdual : ∀ j, y₀ * one j + Gy j = t j)
    (hdual' : ∀ j, y₀' * one j + Gy' j = t j)
    (hGy : ∑ i, Gy i * v i = 0)
    (hGy' : ∑ i, Gy' i * v i = 0)
    (hone : ∑ i, one i * v i ≠ 0) :
    y₀ = y₀' := by
  rw [dual_price_determined_by_radical t one v Gy y₀ hdual hGy hone,
      dual_price_determined_by_radical t one v Gy' y₀' hdual' hGy' hone]

/-! ### 3. The primal side: exactly which costs make the objective vacuous -/

/-- **A cost drawn from the Gram makes the objective a read-out of the
constraints.**

If the cost is obtained by pairing each basis vector against a fixed `u`
through the Gram — `tⱼ = ⟨G eⱼ, u⟩` — then

    ⟨t, x⟩ = ⟨G x, u⟩

so the objective reports a linear functional OF THE CONSTRAINT DATA `G x` and
carries no information the constraints do not already fix. Taking `u = eₖ`
recovers the recorded Hecke defect exactly: `tⱼ = G_{kj}` gives
`⟨t, x⟩ = (Gx)ₖ`, which is `t·x = u₀` at `k = 0` — constant on a feasible set
that pins that coordinate.

Read with §2 this says precisely what a replacement objective must avoid, and
it is two independent conditions, both checkable before solving: *not drawn
from the Gram it is paired with*, and *not orthogonal to that Gram's radical*.
Being merely "different from the Hecke cost" is neither. -/
theorem cost_from_gram_makes_objective_a_constraint_readout
    (x u : ι → R) (Grow : ι → ι → R) (t : ι → R)
    (ht : ∀ j, t j = ∑ i, Grow j i * u i) :
    ∑ j, t j * x j = ∑ j, (∑ i, Grow j i * u i) * x j := by
  refine Finset.sum_congr rfl ?_
  intro j _
  rw [ht j]

/-- **A DIAGONAL Gram kills every cost built on its own diagonal.**

This is the general form of the negative measured in
`qbeta_ecat_lp_radical_pairing_probe` (5/5), and it is stated for the diagonal
case because that is the case measured -- the dense-Gram version needs a sum
swap this file does not carry, and claiming it would be asserting more than is
proved.

Setting: `G = diag g`, so `t_j = g_j * u_j` for a cost built from the diagonal,
and `v` is in the radical, i.e. `g_j * v_j = 0` for every `j`. Then
`⟨t, v⟩ = 0` — so by §2 the shadow price collapses.

**The block-basis instance.** There `g_λ = y_λ * dim_λ` and the cost is
`t_λ = y_λ * f(λ)`, which is `g_λ * u_λ` with `u_λ = f(λ)/dim_λ` wherever
`dim_λ ≠ 0`. So the measured collapse was an instance of this and not a
coincidence of convention D: the SAME `y_λ` that makes the Gram entry vanish
makes the cost component vanish, for every `f`.

**The design constraint for whoever builds the next cost:** against a diagonal
Gram, no cost proportional to that diagonal escapes. Escaping requires a
component where the Gram has none — on the six-operator basis, a component
along the q-antisymmetriser `(-q³, q², q², -q, -q, 1)`. Being geometric is not
sufficient and being non-Hecke is not sufficient. -/
theorem diagonal_gram_kills_every_cost_on_its_diagonal
    (g u v : ι → R) (t : ι → R)
    (hrad : ∀ j, g j * v j = 0)
    (ht : ∀ j, t j = g j * u j) :
    ∑ j, t j * v j = 0 := by
  refine Finset.sum_eq_zero ?_
  intro j _
  rw [ht j]
  calc g j * u j * v j = u j * (g j * v j) := by ring
    _ = 0 := by rw [hrad j, mul_zero]

/-- Against a diagonal Gram with radical vector `v`, any cost `t j = g j * u j`
built from the diagonal is orthogonal to `v` and therefore forces the dual
shadow price `y₀ = 0`. -/
theorem dual_price_zero_of_diagonal_gram_cost
    (g u one v Gy t : ι → R) (y₀ : R)
    (hdual : ∀ j, y₀ * one j + Gy j = t j)
    (hGy : ∑ i, Gy i * v i = 0)
    (hone : ∑ i, one i * v i ≠ 0)
    (hrad : ∀ j, g j * v j = 0)
    (ht : ∀ j, t j = g j * u j) :
    y₀ = 0 := by
  have horth : ∑ i, t i * v i = 0 :=
    diagonal_gram_kills_every_cost_on_its_diagonal g u v t hrad ht
  exact dual_price_zero_of_cost_orthogonal_to_radical t one v Gy y₀ hdual hGy hone horth

end QOU.QBeta.ECatLPDualRadical
