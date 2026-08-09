---
# qou-nkd8
title: HeckeAlgebra class is too weak — rank-1 model satisfies it at every n; add the Iwahori-basis axiom
status: todo
type: task
created_at: 2026-08-09T12:31:34Z
updated_at: 2026-08-09T12:31:34Z
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
