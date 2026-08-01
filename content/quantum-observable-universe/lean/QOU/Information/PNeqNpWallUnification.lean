import QOU.Information.SkeinGradeConnective
import QOU.Information.CountingModuliGrade

/-!
# QOU.Information.PNeqNpWallUnification — one super-poly-cost lemma, two P-vs-NP formulations

The merged infra states the P-vs-NP horizon separation in two places, over
different filtration levels:

* the **Skein bridge** `not_polyObservable_family_of_horizon_cost`
  (`SkeinGradeConnective`), keyed on the horizon cost `3^{len}`;
* the **moduli** counting cost `physicalCost n = 3^{3n}`
  (`CountingModuliGrade`), the resolution-tree cost of the boundary family.

This file shows the two **`PolyObservable` separations** are one statement —
both are instances of a single general fact
(`SkeinGradeConnective.not_polyObservable_family_of_superPoly`): *a
super-polynomial cost beats every polynomial budget on a size-indexed family*.
The bridge case is `cost = 3^n`; the moduli case (added here) is
`cost = physicalCost`. What is shared is the
**super-polynomial cost witness**: `physicalCost_superPoly` is the same
ingredient that drives the moduli `FamilyPolyBounded` separation
(`not_familyPolyBounded_of_physical_point`) — a *distinct* predicate over
moduli, not equated here. So the unification is of the *cost object* (`3^{3n}`
super-poly), which each wall consumes; it is not new mathematics, it
concentrates each leg's open content into a single ingredient.

**How far the new machinery attacks (honest scope).** The grade squeeze *proves*
the P-vs-NP **counting/cost** leg (the resolution-tree cost out-grades every
polynomial budget) and, with `MagnitudeTraceCommutator` / `MagnitudeAxisBoundary`,
*explains* why no magnitude/trace/birthday invariant can cross to the decision
side. It does **not** cross any of the three Millennium walls — those need the
genuinely-open ingredients (a descent measure `μ` for q-Collatz — `v_[2]` refuted
scope-(a); a smoothness Lyapunov for q-NS; the faithfulness/`χ(A)` residue for
P-vs-NP, gated by algebrization). So this unification is a **pruning attack**: it
rules out the grade/trace routes across the wall and localizes the one missing
ingredient per leg. All sorry-free; ℕ-valued.
-/

universe u v

namespace QOU.Information

open SkeinObservationSystem

/-- `physicalCost n = 3^{3n}` — the moduli counting cost is a bridge horizon cost
    at filtration level `3n`. -/
theorem physicalCost_eq_three_pow (n : ℕ) : physicalCost n = 3 ^ (3 * n) := rfl

/-- **The moduli `physicalCost` drives the same bridge separation (sorry-free).**
    The `3^{3n}` resolution-tree cost of `CountingModuliGrade` is another instance
    of the general super-poly-cost lemma (via `physicalCost_superPoly`).  So the
    same super-polynomial cost witness that powers the moduli
    `FamilyPolyBounded` separation (`not_familyPolyBounded_of_physical_point`)
    also powers this bridge `PolyObservable` separation — the two walls consume
    one shared ingredient (`physicalCost_superPoly`), though the predicates
    (`FamilyPolyBounded` vs `PolyObservable`) are distinct. -/
theorem not_polyObservable_family_of_physicalCost {S : Type u} {V : Type v}
    (sys : SkeinObservationSystem S V) (P : ℕ → S)
    (hlen : ∀ n, sys.len (P n) = n)
    (hcost : ∀ n k, sys.obs (sys.step^[k] (P n)) = sys.obs sys.normalForm →
        physicalCost n ≤ k)
    (poly : ℕ → ℕ) (hpoly : PolyBounded poly) :
    ∃ n, ¬ sys.PolyObservable poly (P n) :=
  not_polyObservable_family_of_superPoly sys P hlen physicalCost
    physicalCost_superPoly hcost poly hpoly

end QOU.Information
