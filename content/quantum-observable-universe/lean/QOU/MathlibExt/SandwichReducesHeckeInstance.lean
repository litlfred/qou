/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.SandwichReducesFromBraid
import QOU.MathlibExt.HeckeTowerWitness

/-!
# The Hecke instance of `BraidRelations`, and exactly how far it goes

Bean `qou-301d`. `SandwichReducesFromBraid` proves

    BraidRelations T h  ⟹  TowerSpan T  ⟹  DisjointBlockMultiplicative T

which is worth nothing until `BraidRelations` is inhabited by something that is
not degenerate. This file supplies the instance and then **measures** it, because
the previous two attempts in this arc were both degenerate in ways their authors
(me) did not notice until asked to prove their own assertions.

## The instance

`HeckeTowerWitness.heckeTowerMarkovTrace h z hz` is the presented infinite
Iwahori-Hecke tower `H_∞`, in which the three relations hold **by construction**
(`twGen_quad`, `twGen_braid`, `twGen_far`), so `braidRelations_heckeTower` is
three field assignments. `h` is a free parameter of the construction, so `h ≠ 0`
is genuinely available — `exists_braidRelations_h_ne_zero` exhibits `h = 3/2`,
`z = 2` over `ℚ`.

## What is non-degenerate here — the filtration

`towerSpan_heckeTower` is **not** covered by
`DisjointBlockTraceLaw.towerSpan_of_constant`, the escape hatch that made
`towerSpan_unit` worthless: `HeckeTowerWitness.twH_zero_lt_one` proves
`H 0 < H 1` for any non-trivial `R`, so this filtration genuinely grows. And
unlike `SymmetricGroupTowerWitness` it is not at `q = 1`: the quadratic scalar is
free.

So `TowerSpan` — a statement about the **algebra**, which is what the whole
`SandwichReduces` argument is about — is witnessed here at `h ≠ 0` with a growing
filtration, which no earlier witness achieved.

## 🛑 What is DEGENERATE here — the trace

`disjointBlock_heckeTower` is a true statement about this witness and it carries
**no information**, because for this trace it is free:

`ocneanuTrace_mul_of_markov` below proves that the rank-2 Ocneanu trace is
**multiplicative** exactly when `z * z = h * z + 1` — and that equation is
precisely the hypothesis `heckeTowerMarkovTrace` requires in order to be a
`MarkovTrace` at all. `towerTrace` is `ocneanuTrace ∘ collapse` with `collapse`
an algebra hom, so `towerTrace_mul` makes the whole trace an algebra
homomorphism, and *every* pair multiplies, disjoint blocks or not.

This is the same shape as `HeckeRankTwoMarkov.ocneanuTrace_mul_defect`, whose
defect is literally `h * z + 1 - z * z`: the rank-2 trace is non-multiplicative
*in general*, and the Markov condition is exactly the locus where it stops being
so. The corpus already recorded the defect; what it had not recorded is that the
`MarkovTrace` hypothesis **kills** it.

## The gap this leaves, stated sharply

| witness | filtration grows | `h ≠ 0` | trace not a hom |
|---|---|---|---|
| `OcneanuTrace.unitMarkovTrace` | ✗ | ✓ | ✗ |
| `SymmetricGroupTowerWitness` | ✓ | ✗ (`h = 0`, `z = 0`) | ✓ (`idCoeff_not_mul_hom`) |
| `HeckeTowerWitness` (here) | ✓ | ✓ | ✗ (proved below) |

**No witness yet has all three.** So the *trace* content of
`DisjointBlockMultiplicative` at `q ≠ 1` is still not exercised by any inhabited
instance, even though the *theorem* deriving it is unconditional. Closing that
needs the faithful Ocneanu trace on `H_∞(q)` — Jones' theorem, bean `qou-g8i1`.
Nothing here should be read as having closed it.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [manuscript] bean qou-301d.
-/

namespace QOU.MathlibExt.SandwichReducesHeckeInstance

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.DisjointBlockTrace
open QOU.MathlibExt.SandwichReducesFromBraid
open QOU.MathlibExt.HeckeRankTwoMarkov QOU.MathlibExt.HeckeRankTwoMarkov.Hecke2
open QOU.MathlibExt.HeckeTowerWitness

variable {R : Type*} [CommRing R]

/-! ## The instance -/

/-- **The presented Hecke tower satisfies `BraidRelations`** — by construction,
since the three relations are the ones imposed in the presentation. -/
instance braidRelations_heckeTower (h z : R) (hz : z * z = h * z + 1) :
    BraidRelations (heckeTowerMarkovTrace h z hz) h where
  quadratic := twGen_quad h
  braid := twGen_braid h
  farComm := fun m j hj => twGen_far h m j hj

/-- **`TowerSpan` for a tower whose filtration genuinely grows, at `h ≠ 0`.**

Not covered by `towerSpan_of_constant`: `twH_zero_lt_one` gives `H 0 < H 1`. -/
theorem towerSpan_heckeTower (h z : R) (hz : z * z = h * z + 1) :
    TowerSpan (heckeTowerMarkovTrace h z hz) :=
  towerSpan_of_braidRelations (h := h)

/-- The disjoint-block trace law for the presented Hecke tower.

🛑 **True but degenerate for this witness** — see `towerTrace_mul` below, which
shows the trace is an algebra homomorphism under exactly the hypothesis `hz`
that `heckeTowerMarkovTrace` needs, so every pair multiplies. -/
theorem disjointBlock_heckeTower (h z : R) (hz : z * z = h * z + 1) :
    DisjointBlockMultiplicative (heckeTowerMarkovTrace h z hz) :=
  disjointBlock_of_braidRelations (h := h)

/-! ## Measuring the degeneracy, rather than asserting it -/

/-- **The Markov hypothesis makes the rank-2 Ocneanu trace multiplicative.**

`HeckeRankTwoMarkov.ocneanuTrace_mul_defect` computes the defect on `σ · σ` as
`h * z + 1 - z * z`; this shows the defect vanishes on *every* pair precisely
under `z * z = h * z + 1`, which is the Markov condition. -/
theorem ocneanuTrace_mul_of_markov {h : R} (z : R) (hz : z * z = h * z + 1)
    (x y : Hecke2 R h) :
    ocneanuTrace z (x * y) = ocneanuTrace z x * ocneanuTrace z y := by
  simp only [ocneanuTrace_apply, mul_const, mul_gen]
  linear_combination (-(x.gen * y.gen)) * hz

/-- **Hence the tower's trace is an algebra homomorphism**, and
`disjointBlock_heckeTower` holds for every pair of elements whatever their
levels — so it exercises none of the disjoint-block content. -/
theorem towerTrace_mul (h z : R) (hz : z * z = h * z + 1) (x y : HeckeTower R h) :
    towerTrace h z (x * y) = towerTrace h z x * towerTrace h z y := by
  simp only [towerTrace_apply, map_mul]
  exact ocneanuTrace_mul_of_markov z hz _ _

/-- The same statement in the form that makes the degeneracy unmissable: the
trace law holds for *arbitrary* `a` and `b`, with no hypothesis about levels. -/
theorem heckeTower_tr_mul_unconditional (h z : R) (hz : z * z = h * z + 1)
    (a b : HeckeTower R h) :
    (heckeTowerMarkovTrace h z hz).tr (a * b)
      = (heckeTowerMarkovTrace h z hz).tr a * (heckeTowerMarkovTrace h z hz).tr b :=
  towerTrace_mul h z hz a b

/-! ## `h ≠ 0` is genuinely reachable -/

/-- **A concrete instance with `h ≠ 0`**: over `ℚ`, `z = 2` and `h = 3/2` satisfy
the Markov quadratic `z * z = h * z + 1` (`4 = 3 + 1`).

This is what separates the present instance from `SymmetricGroupTowerWitness`,
where `h = 0` forces the symmetric-group (`q = 1`) specialisation. -/
theorem exists_braidRelations_h_ne_zero :
    ∃ (h z : ℚ) (hz : z * z = h * z + 1), h ≠ 0 ∧
      Nonempty (BraidRelations (heckeTowerMarkovTrace h z hz) h) := by
  refine ⟨3 / 2, 2, by norm_num, by norm_num, ⟨braidRelations_heckeTower _ _ _⟩⟩

end QOU.MathlibExt.SandwichReducesHeckeInstance
