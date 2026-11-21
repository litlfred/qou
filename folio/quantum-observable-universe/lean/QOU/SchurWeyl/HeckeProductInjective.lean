/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.HeckeWedderburnGeneral

/-!
# The seminormal block family is faithful

Bean `qou-ejde`. `heckeProduct = ⊕_λ ρ_λ` is **injective**, so the seminormal
representations separate points of `H_{n+1}(q)`.

## Why this is not circular, and why it is one line

`HeckeProductSurjective.heckeProduct_surjective` proves the map is **onto**, and
`HeckeWedderburnGeneral` computes **both** dimensions as `(n+1)!` —
`finrank_hecke_eq_factorial` upstairs and `finrank_blocks_eq_factorial`
downstairs. A surjection between spaces of *equal finite dimension* is bijective
(`LinearMap.injective_iff_surjective_of_finrank_eq_finrank`), so injectivity is
the free half of an equality that was already proved for its other half.

Note the direction of use: `finrank_hecke_eq_factorial` obtains the **lower**
bound `(n+1)! ≤ dim H` *from* that same surjection, and the **upper** bound from
`HeckeCoset.finrank_le_factorial`. So the dimension equality is not derived from
injectivity, and using it here to get injectivity is not circular.

## What this unlocks

Bean `qou-ejde` records the route: with faithfulness, `heckeIncl` is injective —
compose with `SeminormalBlockEquality.compress_seminormalRep_heckeIncl`, which
identifies the upstairs block of `heckeIncl y` with the downstairs block of `y`.
`heckeIncl` injectivity is in turn the single input to Mathlib's
`Ring.DirectLimit.of_injective`, which yields the Hecke colimit with injective
canonical maps — and with it the bridge from the level-indexed
`HeckeCoset.MarkovTraceFamily` (which carries the genuine Ocneanu trace, proved
in `MarkovTraceInstance`) to the single-algebra `OcneanuTrace.MarkovTrace` that
`TowerSpanReduction` and `DisjointBlockTraceLaw` consume.

🛑 **Only the faithfulness step is proved here.** The `heckeIncl` corollary and
the colimit are *not* in this file; they are the remainder of `qou-ejde`, and the
`eraseCorner`-surjectivity gap that the composition needs is recorded there.

## Scope

Generic `q` over a characteristic-zero field: `[Field K]`, `[CharZero K]`,
`q ≠ 0`, `NotRootOfUnity q` — inherited from `finrank_hecke_eq_factorial`, which
needs semisimplicity. At a root of unity `H_n(q)` is not semisimple and the
partitions stop indexing the irreducibles, so the statement would need a
different proof, not merely weaker hypotheses.

-- Ref: [leitner2026] bean qou-ejde; Geck-Pfeiffer, *Characters of Finite Coxeter
--      Groups and Iwahori-Hecke Algebras*, §8.1 (generic semisimplicity and the
--      seminormal form).
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)
open TableauCells SeminormalRep

/-- **The seminormal family is faithful.** `Φ = ⊕_λ ρ_λ` is injective, because it
is surjective between spaces of equal finite dimension `(n+1)!`. -/
theorem heckeProduct_injective {K : Type*} [Field K] [CharZero K] (q : K) (hq0 : q ≠ 0)
    (hq2 : QOU.SchurWeyl.GenericParameter.NotRootOfUnity q) (n : ℕ) :
    Function.Injective (heckeProduct q hq0 hq2 n) := by
  classical
  haveI := finiteDimensional_hecke (K := K) q q⁻¹ n
  have hfr : Module.finrank K (Hecke K q q⁻¹ n)
      = Module.finrank K (∀ lam : Partition (n + 1),
          Matrix (StandardYoungTableau (QOU.Mathlib.partitionShape lam))
            (StandardYoungTableau (QOU.Mathlib.partitionShape lam)) K) := by
    rw [finrank_hecke_eq_factorial q hq0 hq2 n, finrank_blocks_eq_factorial (K := K) n]
  exact (LinearMap.injective_iff_surjective_of_finrank_eq_finrank hfr
    (f := (heckeProduct q hq0 hq2 n).toLinearMap)).mpr
    (heckeProduct_surjective q hq0 hq2 n)

/-- Restated as separation: two elements agreeing in every seminormal block are
equal. -/
theorem eq_of_seminormalRep_eq {K : Type*} [Field K] [CharZero K] (q : K) (hq0 : q ≠ 0)
    (hq2 : QOU.SchurWeyl.GenericParameter.NotRootOfUnity q) (n : ℕ)
    {x y : Hecke K q q⁻¹ n}
    (h : ∀ lam : Partition (n + 1),
      seminormalRep q hq0 hq2 n (partitionShape_card_succ lam) x
        = seminormalRep q hq0 hq2 n (partitionShape_card_succ lam) y) :
    x = y :=
  heckeProduct_injective q hq0 hq2 n (funext h)

end QOU.SchurWeyl
