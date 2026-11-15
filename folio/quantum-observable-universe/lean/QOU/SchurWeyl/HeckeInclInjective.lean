/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.HeckeProductInjective
import QOU.SchurWeyl.SeminormalBlockEquality
import QOU.Mathlib.YoungDiagramEraseCornerSurjective

/-!
# `heckeIncl` is injective — the composition bean `qou-ejde` mapped

The tower inclusion `H_m(q) → H_{m+1}(q)` is **injective**. This is the third and last step of
the route recorded on bean `qou-ejde`, and the file that composes it; the other two were already
on `main`.

## The three steps, and which file owns each

| step | statement | where |
|---|---|---|
| 1 | the seminormal family is faithful: `heckeProduct` is injective | `HeckeProductInjective` |
| 2 | the upstairs block of `heckeIncl y`, compressed to a corner, IS the downstairs block of `y` | `SeminormalBlockEquality.compress_seminormalRep_heckeIncl` |
| 3 | **compose them** | this file |

Step 3 is two lemmas. `seminormalRep_eq_of_heckeIncl_eq` says that if `heckeIncl` identifies `x`
and `y` then every downstairs seminormal block does too — for an *arbitrary* diagram `ν` of the
right size, which is where the surjectivity of corner removal is consumed. `heckeIncl_injective`
then feeds that to step 1's separation form `eq_of_seminormalRep_eq`.

## Why `ν` is a variable and not `partitionShape lam`

Step 2 is stated upstairs: its conclusion mentions `seminormalRep` at the diagram
`eraseCorner μ c hc`, while the goal mentions it at `ν`. `seminormalRep`'s *output type* depends on
the diagram (it is a matrix indexed by that diagram's standard tableaux), so relating the two is a
dependent rewrite and transporting along an equation of diagrams would land in `HEq`.

Quantifying over `ν` as a **variable** avoids the transport entirely: `exists_eraseCorner_eq`
returns an equation `eraseCorner μ c hc = ν` whose right side is that variable, so `subst` replaces
`ν` — carrying `hν` with it — and step 2 then applies on the nose, with `hν` itself as its `hNs`.
No transport, no `HEq`, no `congr`. The call site instantiates `ν := partitionShape lam`, which is
an ordinary application of a `∀`-statement and needs nothing.

## Scope — inherited, and to be stated downstream

`ℝ`, `q ≠ 0`, `NotRootOfUnity q`: **generic `q`**. Step 1 needs `[Field K] [CharZero K]` and
genericity because `finrank_hecke_eq_factorial` needs semisimplicity; step 2 is stated over `ℝ`
with `qi = q⁻¹`. At a root of unity `H_n(q)` is not semisimple, the partitions stop indexing the
irreducibles, and this proof does not merely weaken — it fails. Every downstream consequence
inherits that hypothesis.

## What this does NOT give

Injectivity of the *tower* inclusion, not of anything about a colimit. In particular it does **not**
prove that `ofLim n` is injective for `heckeColimitMarkovTrace`, and it does not make `trLim`
faithful. `qou-ejde`'s own later note measures that the Hecke **colimit and its canonical maps
exist without any injectivity hypothesis** (`@DirectLimit` / `@DirectLimit.Ring.of` carry none), so
what this unlocks is the *strict*-growth question (bean `qou-p8yg`), not the bridge. Nor is
`Ring.DirectLimit.of_injective` the lemma to reach for: under the pinned Mathlib v4.24.0 the
namespace is unified and no lemma of that name exists — `qou-ejde` records this correction.

-- Ref: [leitner2026] bean qou-ejde, steps 1-3; Geck-Pfeiffer, *Characters of Finite Coxeter
--      Groups and Iwahori-Hecke Algebras*, §8.1 (generic semisimplicity, seminormal form).
-/

namespace QOU.SchurWeyl
namespace SeminormalRep

variable {K : Type*} [Field K] [CharZero K]

open QOU.Mathlib QOU.SchurWeyl.TableauCells QOU.SchurWeyl.HeckeInclusion

omit [CharZero K] in
/-- **Step 3, first half.** If the tower inclusion identifies `x` and `y`, then so does every
downstairs seminormal block — at an *arbitrary* diagram of the right size. The diagram is a
variable so that `exists_eraseCorner_eq` can be `subst`ed into it; see the module docstring. -/
theorem seminormalRep_eq_of_heckeIncl_eq {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) {x y : Hecke K q q⁻¹ m}
    (h : heckeIncl K q q⁻¹ m x = heckeIncl K q q⁻¹ m y)
    (ν : YoungDiagram) (hν : ν.cells.card = m + 1) :
    seminormalRep q hq0 hq2 m hν x = seminormalRep q hq0 hq2 m hν y := by
  obtain ⟨μ, c, hc, rfl⟩ := exists_eraseCorner_eq ν
  have hN : μ.cells.card = m + 2 := by
    have hcard := card_eraseCorner μ c hc
    omega
  rw [← compress_seminormalRep_heckeIncl hq0 hq2 m hN c hc hν x,
    ← compress_seminormalRep_heckeIncl hq0 hq2 m hN c hc hν y, h]

/-- **The tower inclusion is injective.** `H_m(q) ↪ H_{m+1}(q)` at generic `q`. -/
theorem heckeIncl_injective {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    Function.Injective (heckeIncl K q q⁻¹ m) := fun _ _ h =>
  eq_of_seminormalRep_eq q hq0 hq2 m fun lam =>
    seminormalRep_eq_of_heckeIncl_eq hq0 hq2 m h _ (partitionShape_card_succ lam)

end SeminormalRep
end QOU.SchurWeyl
