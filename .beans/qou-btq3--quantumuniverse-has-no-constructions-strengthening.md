---
# qou-btq3
title: 'QuantumUniverse has no constructions: strengthening it is typecheck-free and checker-invisible'
status: todo
type: task
priority: normal
created_at: 2026-08-16T03:12:45Z
updated_at: 2026-08-16T03:16:59Z
---

Opened while answering a caveat I raised on `qou-w1g8`: *"I have not verified
that every existing `QuantumUniverse` instance would still typecheck under
`[Preadditive C]` or `[Linear k C]` — it could surface an instance the paper's
prose covers but the Lean can't yet supply."*

**That caveat is answered, and it was pointed the wrong way. There are no
instances at all.**

## Measured

| claim | how it is discharged |
|---|---|
| `Nonempty (QuantumUniverse k)` | `axiom QuantumUniverse.exists_instance_axiom` (`quantum-universe-exists.lean:26`) |
| `Nonempty (QuantumObservableUniverse k)` | **`sorry`** + `-- Ref: [kassel1995] §IX` (`quantum-observable-universe-exists.lean:35`) |
| concrete `: QuantumUniverse k := ⟨…⟩` / `where` builds | **zero**, corpus-wide |

`su2QuantumUniverse` is not a counterexample — it inhabits a *different*
structure, `SU2QuantumUniverseData`.

## Why this matters more than the typecheck question

`QuantumUniverse` is a bundled structure carrying its instances as **fields**
(`catInst`, `monInst`, `zeroInst`, `braidedInst`). Adding `[preInst :
@Preadditive C catInst]` is therefore adding a field to a structure whose only
inhabitant claims are an `axiom` and a `sorry`. Both absorb a new field for
free: an `axiom` asserting `Nonempty S` asserts strictly more the moment `S`
gains a field, with **no proof obligation appearing anywhere and no checker
firing**. `#print axioms` reports the same axiom name before and after.

So the honest statement of the `qou-w1g8` decision is *not* "will it break a
construction" (nothing to break) but "are we willing to strengthen an
axiomatised existence claim silently". That is the §"Axiomatization is NOT a
Proof" class: the cost is invisible in Lean and lands entirely on whether the
cited witness — Rep(SU_q(2)) per Kassel §IX — really does satisfy the
strengthened structure. For k-linearity specifically it plainly does, so this
is a low-risk instance of a pattern worth naming rather than a blocker.

## Second finding, independent of `w1g8`

The structure's own docstring already says **"`C` is a `k`-linear braided
monoidal category"** (`CategoricalFoundations.lean:120`), and the axiom-4 field
comment says `frobWeight` and `dimQ` "land in `k` via the standard
identification of `End(𝟙)` with the ground ring of a **`k`-linear** category"
(:176-178). That identification *requires* k-linearity — so the structure is
already leaning on linearity it does not carry, before `Σ p_b = 𝟙` enters the
picture. The gap is load-bearing today, not only for completeness.

`def:quantum-universe` (`quantum-universe.md:3`) requires "an `R`-linear
braided monoidal category **C**", and `rigid-monoidal-category.md:31` defines
`R`-linear as "every hom-set is an `R`-module and composition is
`R`-bilinear" — which is exactly `Preadditive` plus a scalar action. So the
prose has committed to this all along; only the Lean has not.

## What to do

Not a fix in itself. Two things for whoever takes `qou-w1g8`:

1. **Do not justify the instance addition with "no constructions break."**
   True, but it is true because nothing is constructed — which is an argument
   for care, not for confidence.
2. **Add the linearity instance to all THREE synced copies** —
   `lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean:133`,
   `quantum-observable-universes/quantum-observable-universe.lean:106`,
   `quantum-universes/quantum-universe.lean:120` — and note that
   `QuantumObservableUniverse` *extends* `QuantumUniverse`, so it inherits the
   field and its `sorry`-backed existence claim silently strengthens too.

Worth considering separately: whether an existence claim discharged by `axiom`
or `sorry` should be *re-reviewed* whenever its structure gains a field. No
mechanism does that today, and this is the case that shows why one might want
one.


RELATED 2026-08-16: bean qou-omuz — the same blind spot from the other side.
QuantumUniverse is typed over [Field k] while the paper says commutative ring R,
and the framework's own ground ring R_q = LaurentPolynomial Z is NOT a field. An
over-strong parameter is invisible for exactly the reason recorded here: nothing
constructs the structure, so nothing has ever tried to instantiate it at a ring
that fails.
