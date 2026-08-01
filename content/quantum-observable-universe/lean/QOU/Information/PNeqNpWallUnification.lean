import QOU.Information.SkeinGradeConnective
import QOU.Information.CountingModuliGrade

/-!
# QOU.Information.PNeqNpWallUnification — one super-poly-cost lemma, two P-vs-NP formulations

The merged infra gives two P-vs-NP cost separations:

* the **Skein bridge** horizon separation `not_polyObservable_family_of_horizon_cost`
  (`SkeinGradeConnective`), keyed on `3^{len}`;
* the **moduli** counting separation `not_familyPolyBounded_of_physical_point`
  (`CountingModuliGrade`), keyed on `physicalCost n = 3^{3n}`.

This file shows they are **the same statement** — both are instances of one
general fact: *a super-polynomial cost beats every polynomial budget on a
size-indexed family*. The bridge case is `cost = 3^n`; the moduli case is
`cost = physicalCost`. Nothing here is new mathematics; it is the honest
unification that concentrates each leg's open content into a single ingredient.

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

/-- **The general super-poly-cost separation (sorry-free).**  For any
    `SkeinObservationSystem`, a size-indexed family `P n` at filtration level `n`
    whose observation is reached only at a **super-polynomial** cost `cost n`
    (`hcost`, `hcost_sp`) is not `PolyObservable` for all `n` under any polynomial
    budget — `cost` eventually exceeds every polynomial.  This subsumes
    `not_polyObservable_family_of_horizon_cost` (the `cost = 3^n` case) and the
    moduli `physicalCost` case below: one lemma, both P-vs-NP formulations. -/
theorem not_polyObservable_family_of_superPoly {S : Type u} {V : Type v}
    (sys : SkeinObservationSystem S V) (P : ℕ → S)
    (hlen : ∀ n, sys.len (P n) = n)
    (cost : ℕ → ℕ) (hcost_sp : SuperPolynomial cost)
    (hcost : ∀ n k, sys.obs (sys.step^[k] (P n)) = sys.obs sys.normalForm →
        cost n ≤ k)
    (poly : ℕ → ℕ) (hpoly : PolyBounded poly) :
    ∃ n, ¬ sys.PolyObservable poly (P n) := by
  obtain ⟨c, K, hb⟩ := hpoly
  obtain ⟨n, _, hn⟩ := hcost_sp c K
  refine ⟨n, ?_⟩
  rintro ⟨k, hk, hobs⟩
  rw [hlen] at hk
  have hck := hcost n k hobs
  have hpn : poly n < cost n := lt_of_le_of_lt (hb n) hn
  omega

/-- The bridge horizon cost `3^n` is the `cost = 3^n` instance of the general
    lemma (`superPoly_three_pow`) — recovering
    `not_polyObservable_family_of_horizon_cost`. -/
theorem not_polyObservable_family_horizon {S : Type u} {V : Type v}
    (sys : SkeinObservationSystem S V) (P : ℕ → S)
    (hlen : ∀ n, sys.len (P n) = n)
    (hcost : ∀ n k, sys.obs (sys.step^[k] (P n)) = sys.obs sys.normalForm →
        3 ^ n ≤ k)
    (poly : ℕ → ℕ) (hpoly : PolyBounded poly) :
    ∃ n, ¬ sys.PolyObservable poly (P n) :=
  not_polyObservable_family_of_superPoly sys P hlen (fun n => 3 ^ n)
    superPoly_three_pow hcost poly hpoly

/-- `physicalCost n = 3^{3n}` — the moduli counting cost is a bridge horizon cost
    at filtration level `3n`. -/
theorem physicalCost_eq_three_pow (n : ℕ) : physicalCost n = 3 ^ (3 * n) := rfl

/-- **The moduli `physicalCost` drives the same bridge separation (sorry-free).**
    The `3^{3n}` resolution-tree cost of `CountingModuliGrade` is another instance
    of the general super-poly-cost lemma (`physicalCost_superPoly`).  So the
    moduli `not_familyPolyBounded_of_physical_point` and the bridge
    `not_polyObservable_family_of_horizon_cost` are one wall in two
    formulations. -/
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
