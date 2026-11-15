---
# qou-nkd8
title: HeckeAlgebra class is too weak — rank-1 model satisfies it at every n; add the Iwahori-basis axiom
status: completed
type: task
priority: normal
created_at: 2026-08-09T12:31:34Z
updated_at: 2026-08-09T12:48:47Z
---


Machine-checked in `QOU/Hecke/InstanceH2.lean` as `rankOneModel`:

```lean
instance rankOneModel (n : ℕ) : HeckeAlgebra ℚ n 1 ℚ where
  embed := fun _ => 1
  quadratic := by intro i; norm_num
  braid := by intro i j _; simp
  farCommute := by intro i j _; simp
  spans := Subsingleton.elim _ _
```

At `q = 1`, `h = q - q⁻¹ = 0`, so `x = 1` solves `x² = h·x + 1`; braid and
far-commutativity are automatic in a commutative ring; `spans` holds because
`Subalgebra ℚ ℚ` is a subsingleton.

**`ℚ` is a `HeckeAlgebra ℚ n 1 ℚ` for every `n`**, including levels where
`H_n(1)` has dimension 6, 24, 120.

## Why it matters

`HeckeAlgebra` asks for generators + three relations + spanning. It never asks
that `A` be free of rank `n!`. So every corpus result proved from
`[HeckeAlgebra R n q A]` also holds of `ℚ` at `q = 1` — not false, but far
weaker than it reads. All five hypothesis sites are generic in `n`
(`StaircaseCornerHook`, `Braiding/hecke_mass_trace`,
`BraidsKnots/tmli_constituent_composite_agreement`, `Shared/MarkovTraceClaim`,
`Machinery/MarkovTraceOnHecke`), so all are affected equally.

It also means **building H3/H4 instances against the class as written adds
nothing** — `rankOneModel` already inhabits it everywhere.

## Fix

Add the **Iwahori basis**: `A` free of rank `n!` over `R` on `{T_w}_{w ∈ S_n}`.

Prefer a **companion predicate** (`IsHeckeOfFullRank R n q A`) over
strengthening `HeckeAlgebra` in place: existing consumers keep compiling, and
each can be upgraded deliberately where the result genuinely needs `A` to be
the Hecke algebra rather than merely to satisfy the relations.

`H2` already qualifies — `AdjoinRoot` of a monic quadratic is free of rank
`2 = 2!` — so `instHeckeAlgebraH2` is the genuine two-strand algebra; the class
just cannot say so.

Full survey: `docs/audits/2026-08-09-hecke-infrastructure-what-is-needed.md`.

## DONE — `QOU/Hecke/FullRank.lean`

Companion predicate, as recommended. `HeckeAlgebra` untouched, so all five
hypothesis sites still compile.

```lean
class IsHeckeOfFullRank (R : Type u) (n : ℕ) (A : Type u)
    [Field R] [Ring A] [Algebra R A] : Prop where
  free : Module.Free R A
  finrank_eq : Module.finrank R A = n.factorial
```

Shipped and axiom-clean (`propext, Classical.choice, Quot.sound`; the numeric
induction depends on no axioms at all):

| declaration | content |
|---|---|
| `not_isHeckeOfFullRank_rankOne` | the rank-1 model fails the predicate at **every** `n ≥ 2` |
| `not_isHeckeOfFullRank_rankOne_three` | the `n = 3` case spelled out |
| `heckePoly_monic`, `heckePoly_natDegree` | `X² − hX − 1` monic of degree 2 |
| `finrank_H2` | `finrank R (H2 R q) = 2` |
| `instIsHeckeOfFullRankH2` | **`H₂(q)` has full rank `2 = 2!`** |
| `finrank_succ_of_rung` | tower law: rung of rank `n+1` over a level of rank `n!` gives `(n+1)!` |
| `finrank_of_rank_recursion` | `d 0 = 1`, `d (n+1) = (n+1)·d n` ⟹ `d n = n!` |
| `isHeckeOfFullRank_succ` | the two composed, ready to `exact` inside an `induction` |
| `instIsHeckeOfFullRankBase/One` | `R` itself at `n = 0, 1` |

Rank `n!` is not the full Iwahori statement — it fixes the dimension, not the
`{T_w}` labelling. That is deliberate and documented in the module: dimension is
what every downstream argument uses and what the degenerate models fail. Given
Iwahori's theorem (not formalised, and nothing here depends on it), `spans` +
`finrank = n!` pins `A` to `H_n(q)` up to isomorphism.

**Consequence for the roadmap:** the rank condition is now inductive, so a tower
owes one rung at a time — `H_{n+1}` free of rank `n+1` over `H_n` — instead of a
from-scratch dimension computation per level. qou-jr3k (H3) is now a single rung.
