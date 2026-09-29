import QOU.Information.SkeinObservationBridge
import QOU.Information.SurrealBudgetGrade

/-!
# QOU.Information.SkeinGradeConnective — the surreal grade meets the three-wall bridge

`SkeinObservationBridge` packages q-Collatz (`Halts`), q-NS (`Regular`/`BlowsUp`),
and P-vs-NP (`PolyObservable`) as three questions about one `len`-filtered
Skein orbit read through `obs = tr_M`.  Its P-vs-NP separation
(`not_polyObservable_id_of_horizon_cost`) is proved only for the **identity
(linear) budget** — `lt_three_pow` discharges the single gap `len P < 3^{len P}`.

This file **upgrades that separation to every polynomial budget** by routing it
through the surreal ω-grade squeeze (`SurrealBudgetGrade`): the horizon cost
`3^{len}` is genuinely *super-polynomial*, so no `PolyBounded` budget — not just
the linear one — observes a whole size-indexed family.  This is the exact
statement "the P-vs-NP leg's `3^c` resolution-tree cost out-grades every
polynomial," now as a grade fact rather than a per-instance `omega`.

Placement on the two axes (honest, per the categorical-dialogue roast): q-NS is
bounded-vs-unbounded *in time* (magnitude axis); q-Collatz / P-vs-NP are
reachability / reachability-at-polynomial-rate (quantifier axis).  Sharing the
`len` filtration does **not** reduce one to another — this file connects only the
P-vs-NP leg to the grade, which is where the grade legitimately lives.
All sorry-free; ℕ-valued (base ring N/A).
-/

universe u v

namespace QOU.Information

/-- **`3^n` is super-polynomial (sorry-free).**  `2^n ≤ 3^n` lifts
    `superPoly_two_pow` through `SuperPolynomial.of_le`; the resolution-tree
    horizon cost lives in the super-poly grade. -/
theorem superPoly_three_pow : SuperPolynomial (fun n => 3 ^ n) :=
  superPoly_two_pow.of_le (fun n => Nat.pow_le_pow_left (by norm_num) n)

/-- **The horizon cost `3^n` is not polynomially budgeted (sorry-free).**  The
    grade form of the bridge's P-vs-NP separation: the `3^c` resolution-tree cost
    out-grades every polynomial budget. -/
theorem horizon_cost_not_polyBounded : ¬ PolyBounded (fun n => 3 ^ n) :=
  not_polyBounded_of_superPoly superPoly_three_pow

/-- **The general super-poly-cost separation (sorry-free).**  For any
    `SkeinObservationSystem`, a size-indexed family `P n` at filtration level `n`
    whose observation is reached only at a **super-polynomial** cost `cost n`
    (`hcost`, `hcost_sp`) is not `PolyObservable` for all `n` under any polynomial
    budget — `cost` eventually exceeds every polynomial.  The horizon
    (`cost = 3^n`) and moduli (`cost = physicalCost = 3^{3n}`,
    `PNeqNpWallUnification`) separations are its two instances. -/
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

/-- **Every polynomial budget fails on a horizon-cost family (sorry-free).**
    Upgrades `SkeinObservationSystem.not_polyObservable_id_of_horizon_cost` from
    the identity budget to *any* `PolyBounded` budget.  For a size-indexed family
    `P n` with filtration level `n`, whose observation is reached only at the
    horizon cost `3^n` (`hcost`), no polynomial budget `poly` is
    `PolyObservable` for all `n` — because `3^n` is super-polynomial
    (`superPoly_three_pow`), so it eventually exceeds `poly`.  This is the
    surreal ω-grade squeeze applied to the Skein bridge's P-vs-NP leg.  It is the
    `cost = 3^n` instance of `not_polyObservable_family_of_superPoly` below. -/
theorem not_polyObservable_family_of_horizon_cost {S : Type u} {V : Type v}
    (sys : SkeinObservationSystem S V) (P : ℕ → S)
    (hlen : ∀ n, sys.len (P n) = n)
    (hcost : ∀ n k, sys.obs (sys.step^[k] (P n)) = sys.obs sys.normalForm →
        3 ^ n ≤ k)
    (poly : ℕ → ℕ) (hpoly : PolyBounded poly) :
    ∃ n, ¬ sys.PolyObservable poly (P n) :=
  not_polyObservable_family_of_superPoly sys P hlen (fun n => 3 ^ n)
    superPoly_three_pow hcost poly hpoly

end QOU.Information
