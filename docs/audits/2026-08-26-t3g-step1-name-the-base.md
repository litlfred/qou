# T3g step 1: naming the base is a decision, not a lookup

**Date:** 2026-08-26 · **Branch:** `claude/8-fold-way-qou-k4e8ch` (PR #5819)
**Bean:** `qou-y7vg` (T3g, live carrier)

## The task

The prior audit
([`2026-08-26-fivefold-charts-does-not-supply-t3g.md`](2026-08-26-fivefold-charts-does-not-supply-t3g.md))
ended with three steps that would settle T3g's existence question — *does the
category admit inequivalent fibre functors?* Step 1 was **name the base**, on
the grounds that Tannakian neutrality is not a property of `C` alone and that
`H¹(base, Aut^⊗)` cannot be evaluated until the base is fixed. It was expected
to be a lookup.

**It is not.** The corpus offers at least three distinct candidates, two of them
sharing a symbol, and designates none.

## The three candidates

### 1. `Spec R` with `R = ℤ[q, q⁻¹]`

`def:quantum-universe` makes `C` an `R`-linear category over a commutative ring
`R` with `R ≅ End_C(𝟏)`, and its fibre functor is `τ : C → R-Mod`. Its own note
names `R_q = ℤ[q, q⁻¹]` as *"the framework's own ground ring"*. This is the base
the fibre functor is literally linear over, so it has the strongest claim by
construction.

### 2. `Spec(R_q)` with `R_q` = the coordinate ring of **Bring's curve**

`def:categorical-mordell-weil` writes an Euler product over
`𝔪 ∈ Spec(R_q)` and says *"the product runs over maximal ideals of the
coordinate ring `R_q` of Bring's curve"*.

**This is a different ring wearing the same symbol.** `ℤ[q, q⁻¹]` is the
coordinate ring of `𝔾_m` over `ℤ` — affine, genus 0. Bring's curve is genus 4.
They are not the same object, and `R_q` appears **nowhere in the notation
register**, so nothing in the corpus adjudicates the collision.

### 3. `Spec(ξ_q)`, the Reeb-eigenvalue spectral base

The same block says, and this is the sentence T3g has been looking for:

> The fibre functor atlas of the QOU forms a `G`-gerbe over the spectral base.

and then defines the `q`-Tate–Shafarevich group as the kernel of a localisation
map indexed by `ρ ∈ Spec(ξ_q)`, the Reeb spectrum.

## Why candidate 3 matters more than the arithmetic of the collision

`qou-y7vg` records that the corpus's only assertion bearing on T3g's existence
question is `rem:fivefold-affine-charts-generations`, and the SM-side audit on
#5744 measured the *external* shelf as empty — one Tannakian hit in `library/`,
zero on gerbes.

**Both readings missed this block.** It asserts the gerbe structure directly, in
the vocabulary T3g uses, and it is not a `remark`: `def:categorical-mordell-weil`
is a `definition` with a `.lean` sibling. That is a stronger carrier than the
fivefold remark.

Two things keep it from settling anything on its own:

- Its Lean sibling is registered `validation: "not_checked"`, so the formal side
  is unverified.
- The assertion is one sentence inside a block about Mordell–Weil and
  `L`-functions. The gerbe is used as *setting*, not proved as *result*.

So this is a better lead than the fivefold remark, and it is still an assertion.
It should be read before any further T3g work, and `qou-y7vg` should cite it.

## A fourth object, and the hazard of not separating them

The same block defines

> `H¹_⊗(C, E_q)` — the first cohomology of the monoidal category, classifying
> torsors under `E_q` in `C`

This is a **categorical** `H¹`, of `C` itself, classifying torsors under an
object. T3g's question is about `H¹(base, Aut^⊗(τ))` — cohomology of a *base*,
classifying fibre functors. They are different groups answering different
questions, and both are written `H¹`.

Anyone computing "the `H¹`" here should say which one, over which base, in which
topology. Conflating them is the `da-arity-conflation` shape that this arc has
now hit three times.

## Status of step 1

**Not completed as a lookup; converted into a decision.** The honest output is
that the question *"is `H¹(base, Aut^⊗)` nontrivial?"* still cannot be posed,
and now for a sharper reason than before: not that nobody wrote the base down,
but that the corpus contains three and reconciles none.

**What is needed, and it is the author's call, not an agent's:**

1. Which ring is `R_q` — `ℤ[q, q⁻¹]`, or the coordinate ring of Bring's curve?
   One symbol cannot be both. Register the survivor and rename the other.
2. Is T3g's base the ground ring `Spec R`, or the spectral base `Spec(ξ_q)` that
   `def:categorical-mordell-weil` puts the gerbe over? These give different
   cohomology in different topologies and therefore different answers.

Until 1 and 2 are answered, steps 2 and 3 (identify `Aut^⊗(τ)`; compute or bound
`H¹`) have no determinate target.

## Deliberately not done

No symbol is renamed and no base is designated. Both are changes to mathematical
claims across chapters that already depend on them, and the `R_q` collision in
particular may be a naming slip in one place or a genuine identification the
author intends. Agents should not pick.
