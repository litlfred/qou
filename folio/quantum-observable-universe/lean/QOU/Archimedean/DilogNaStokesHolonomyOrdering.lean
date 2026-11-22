import QOU.MathlibExt.YekutieliIntegration
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# Na-Stokes holonomy-ordering dichotomy for Dilog Part B (bean qou-zbcj)

This file supplies the **structural justification**, previously prose-only, for the
na-Stokes *ordering selection* of the dilog Part-B closure — the honest open bridge
recorded as bean `qou-zbcj` in the coordination ledger
[`docs/coordination/dilog-part-b-cusp-attack.md`](../../../../../docs/coordination/dilog-part-b-cusp-attack.md)
(2026-07-26 owner insight: "limits need to follow na-Stokes, which I guess is
path-ordered exponential").

## Where this sits

* **Closed already (sorry-free).**  W-P2 (`euler_tail_asymptotic`, #4191); the W-P1
  iterated-limit machinery + closure (`wp1_bulk_tendsto` / `wp1_outer_tendsto`,
  #4262/#4343); and the conditional class `NaStokesPartBOrdering`
  (`DilogNaStokesOrdering.lean`), which *derives* the Part-B total `Li₂ x − π²/3` from
  the two proved bricks under the na-Stokes hypothesis.

* **The gap this file addresses.**  `NaStokesPartBOrdering`'s hypothesis fields are
  *flat archimedean `Tendsto` claims* — the actual na-Stokes structural content ("the
  observable is the τ-shadow of a **path-ordered holonomy**, so its refinement is
  intrinsically *iterated*; the joint/symmetric limit is legal **only** in the abelian
  degeneration") lived only in the docstring prose and in
  [`docs/audits/2026-07-26-nastokes-curvature-yekutieli-coefficient.md`](../../../../../docs/audits/2026-07-26-nastokes-curvature-yekutieli-coefficient.md)
  §3.  Here that prose becomes a **proved dichotomy** over the corpus `holonomy` layer.

## What is proved (all sorry-free, real content)

1. `partBHolonomy_eq_prod` — **Φ_n IS an ordered holonomy.**  The Part-B partial
   product `∏_{k<n}(1 − x qᵏ)⁻¹` equals the discrete Yekutieli holonomy (ordered
   `List.prod`, `QOU.MathlibExt.YekutieliIntegration.holonomy`) of its scalar segment
   transports.  This is the τ-shadow identification half of qou-zbcj: the recognisable
   Part-B observable literally *is* an ordered product of segment transports.
2. `partBHolonomy_reorder_free` — **abelian collapse / τ-shadow order-freedom.**  In the
   commutative τ-shadow (`ℝ`) the holonomy value is invariant under any reordering of
   its segments (`holonomy_perm`); so the *value* of the multiplicative integral is
   independent of the refinement order.
3. `holonomy_growth_order_dependent` — **fibre-level obstruction.**  An explicit
   non-abelian group and two single-segment paths with
   `holonomy (p ++ q) ≠ holonomy (q ++ p)`: on the non-commutative fibre `𝒫exp` the
   joint/symmetric limit is genuinely *illegal*.  This is the structural reason
   na-Stokes selects the **iterated** (not joint) ordering for Part B — the joint limit
   would scramble the path-ordering of a holonomy, which is only harmless in the
   abelian degeneration realised by the scalar τ-shadow (fact 2).

## What this does NOT claim (anti-laundering, AGENTS.md "Axiomatization is NOT a Proof")

It does **not** discharge the physics bridge that the specific `Φ_n` *is* the Yekutieli
multiplicative integral of *the specific* `𝐂`-connection with the `(ρ then q)`
refinement order — that identification remains the honest open conjectural input of
qou-zbcj.  This file proves the **abstract ordering dichotomy** the bridge invokes,
plus the concrete "Φ_n is an ordered product" τ-shadow fact.  It also does **not** claim
`−π²/3` is a curvature/commutator term (that is a `no-match`; the audit above).  Nothing
is wired to production; the landed `NaStokesPartBOrdering` class is untouched.

## Base ring (§7c)

`partBSeg` / `partBHolonomy` are archimedean (`ℝ`): the scalar `(1 − x qᵏ)⁻¹` is the
τ-shadow, past the substrate→archimedean wall.  The dichotomy's abelian half uses the
`CommMonoid ℝ` structure; its non-abelian half lives over a generic `Group`
(`Equiv.Perm (Fin 3)`), the fibre side.  The purely-algebraic `holonomy` primitives it
builds on (`YekutieliIntegration.lean`) are over a generic `Monoid` / `Group`.

-- Ref: [leitner2026] docs/coordination/dilog-part-b-cusp-attack.md (2026-07-26 na-Stokes insight); bean qou-zbcj
-- Ref: [yekutieli2015] https://doi.org/10.1142/9537
-/

namespace QOU.Archimedean.NaStokesHolonomy

open QOU.MathlibExt.YekutieliIntegration

/-- The `k`-th Part-B scalar segment transport, `(1 − x qᵏ)⁻¹` — the τ-shadow of the
    `k`-th local parallel transport of the path-ordered holonomy. -/
noncomputable def partBSeg (x q : ℝ) (k : ℕ) : ℝ := (1 - x * q ^ k)⁻¹

/-- The Part-B partial product `Φ_n` presented as a **discrete Yekutieli holonomy**: the
    ordered `List.prod` of the first `n` scalar segment transports, in path order. -/
noncomputable def partBHolonomy (x q : ℝ) (n : ℕ) : ℝ :=
  holonomy ((List.range n).map (partBSeg x q))

/-- **Φ_n IS an ordered holonomy.**  The Part-B partial product `∏_{k<n}(1 − x qᵏ)⁻¹`
    equals the discrete holonomy (ordered product) of its scalar segment transports.
    The τ-shadow identification half of qou-zbcj — the recognisable observable *is* an
    ordered product of segment transports. -/
theorem partBHolonomy_eq_prod (x q : ℝ) (n : ℕ) :
    partBHolonomy x q n = ∏ k ∈ Finset.range n, (1 - x * q ^ k)⁻¹ := by
  induction n with
  | zero => simp [partBHolonomy, holonomy]
  | succ k ih =>
      unfold partBHolonomy at ih ⊢
      rw [List.range_succ, List.map_append, holonomy_append, ih,
        Finset.prod_range_succ]
      simp [holonomy, partBSeg]

/-- **τ-shadow ordering-freedom (abelian collapse).**  Reordering the segments leaves the
    scalar Part-B holonomy unchanged — the classical (abelian) limit of Yekutieli's
    non-abelian Stokes, where the surface-ordering is irrelevant (`holonomy_perm`).  So in
    the commutative τ-shadow the *value* of the multiplicative integral is independent of
    the refinement order. -/
theorem partBHolonomy_reorder_free (x q : ℝ) {n : ℕ} {l : List ℕ}
    (h : l.Perm (List.range n)) :
    holonomy (l.map (partBSeg x q)) = partBHolonomy x q n :=
  holonomy_perm (h.map (partBSeg x q))

/-- **Fibre-level: growth ordering is NOT free.**  There is a (non-abelian) group and two
    single-segment paths whose two growth (concatenation) orders give *different*
    holonomies: `holonomy (p ++ q) ≠ holonomy (q ++ p)`.

    So on the non-commutative fibre `𝒫exp` the joint / symmetric limit is **illegal** —
    it would scramble the path-ordering of the holonomy — whereas the abelian τ-shadow is
    order-free (`partBHolonomy_reorder_free`).  This is the structural reason the na-Stokes
    path-ordering **selects the iterated (not joint) limit** for Part B: the two limits are
    interchangeable only in the abelian degeneration, and the physical observable is a
    path-ordered holonomy. -/
theorem holonomy_growth_order_dependent :
    ∃ (G : Type) (_ : Group G) (p q : List G),
      holonomy (p ++ q) ≠ holonomy (q ++ p) := by
  refine ⟨Equiv.Perm (Fin 3), inferInstance,
    [Equiv.swap 0 1], [Equiv.swap 1 2], ?_⟩
  simp only [holonomy, List.cons_append, List.nil_append, List.prod_cons, List.prod_nil,
    mul_one]
  decide

end QOU.Archimedean.NaStokesHolonomy
