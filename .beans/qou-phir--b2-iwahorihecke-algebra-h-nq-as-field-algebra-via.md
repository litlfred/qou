---
# qou-phir
title: 'B2: Iwahori–Hecke algebra H_n(q) as field-algebra (via Mathlib Coxeter T_w basis / quadratic+braid rels) + cell/Specht modules'
status: todo
type: task
priority: normal
created_at: 2026-07-24T16:21:38Z
updated_at: 2026-08-30T08:03:24Z
---

## Worked 2026-08-30 — the ALGEBRA is built; the basis and cell modules are not

This bean was a bare title with no body, so recording both what it turned out to
mean and where it now stands. It has three parts and **one of them is done**.

### First: "we already have Hecke in Lean" is true in a much weaker sense than it sounds

- **Mathlib has no Hecke algebra of any kind.** Measured against the built `.olean`
  tree, because the Mathlib **source is absent in this container** — an initial
  source grep returned zero and that was a *false negative from an empty
  directory*, not a measurement. Re-run over the oleans with `CoxeterSystem` as a
  positive control: `CoxeterSystem` in 3 modules, `Hecke` in **1**, and that one is
  `Mathlib/NumberTheory/FLT/Basic`, a docstring mention of Hecke *operators*.
- **The corpus's `QOU/IwahoriHecke/` is 1429 lines across 7 files and is entirely
  self-contained** — nothing outside that directory imports it.
- **What it builds is not a Hecke algebra.** `IwahoriHeckeQuot` imposes the
  **quadratic relation only**; braid relations were deferred. So it is the free
  product of one copy of `R[x]/((x−q)(x+1))` per generator, and every theorem
  stated about it is a theorem about that free product.
- **The generic `IwahoriHecke W R q` is worse than "quadratic-only": it is
  mis-shaped.** It is `IwahoriHeckeQuot R q (Set.univ : Set W)` — quadratic
  relations imposed on **every group element**, not on simple reflections. For the
  real Hecke algebra `T_w` with `ℓ(w) ≥ 2` does *not* satisfy `(T_w − q)(T_w+1) = 0`,
  so this is not the "well-defined intermediate object" its docstring claims. The
  construction already takes an arbitrary `S : Set W`; the defect is purely that
  this caller passes the wrong `S`. NOT fixed here — see below.
- **`IwahoriHeckeOfSn` is correctly shaped**: it passes
  `adjacentTranspositionIndex n : Set (Fin (n-1))`, i.e. the simple reflections.
  Only braid relations were missing from it.

### Second: a live AXIOM, on a stale excuse — now proved and deleted

`Defn.lean` carried `axiom universal_property`. Its docstring gave the reason: two
tactic attempts *"could not be verified locally because the remote container has no
`lake` binary and elan cannot reach the Lean release server (network policy)"*.

That obstacle is gone. Existence was already proved; only **uniqueness** was
axiomatised, and it is three steps — `RingQuot.mkAlgHom` is surjective, so two
algebra maps out of the quotient agree as soon as their composites with it do; those
are maps out of a **free** algebra, so `FreeAlgebra.hom_ext` reduces that to the
generators, which is the hypothesis. Landed as `Quotient.hom_ext`;
`universal_property` is now a theorem. Choice-free (`[propext, Quot.sound]`).

### Third: the algebra itself — DONE

`QOU/MathlibExt/IwahoriHeckeAlgebra.lean`, Mathlib-style, generic `[CommRing R]`:
`HeckeAlgebra R q M` for a Coxeter matrix `M`, as `RingQuot` of `FreeAlgebra R B`
modulo an **inductive** relation carrying both the quadratic and the braid family.
Delivers `T`, `T_quadratic`, `T_braid`, `lift`, `lift_T`, `hom_ext`,
`exists_unique_lift`. All choice-free.

Three design choices worth keeping: the relation is an inductive rather than a set
of ideal generators (`RingQuot` closes an arbitrary relation into a ring congruence,
so no ideal-membership reasoning reaches any downstream proof); `M` is a bare
`B → B → ℕ` rather than a `CoxeterMatrix` (nothing needs symmetry or the diagonal
condition, and requiring it would couple the file to an API that has drifted across
Mathlib refactors); and `altProd` plus `map_altProd` are defined here because
Mathlib has no alternating-word product over a monoid.

Type A landed alongside it in `QOU/BraidKnot/HeckeTypeAInstance.lean` and closes
`qou-0o6j`.

### What is STILL OPEN in this bean

1. **The `T_w` basis.** The bean's title says "via Mathlib Coxeter `T_w` basis". Not
   built. The construction above is by generators and relations; the standard basis
   indexed by `W` with the length-based multiplication rule
   (`T_s T_w = T_{sw}` when `ℓ(sw) > ℓ(w)`, else `q T_{sw} + (q−1) T_w`) is a
   separate theorem — and it is the one that needs Matsumoto / reduced expressions,
   i.e. the genuinely hard part.
2. **Cell / Specht modules.** Not started.
3. **The mis-shaped generic `IwahoriHecke W R q`** (`Set.univ` over `W`). Deliberately
   not touched: changing which `S` it passes is a signature change across the five
   consumers in that directory, and it is a different job from building the algebra.
   Worth its own bean.

Note for whoever takes (1): the blocker this arc has cited for a year — the Coxeter
order accessor being "in flux in Mathlib's `CoxeterSystem` API" — is not a blocker
for the *presentation*. `m_{st}` is just `orderOf (s * t : W)`. It may still bite for
the basis, where reduced expressions really are needed.


### Correction + coordination (same day): Mathlib HAS `CoxeterMatrix.Aₙ`, and a sibling proved the S_n bridge

Two amendments to the survey above, both found by reading sibling PR #6053
(`qou-lrz1`) rather than by my own greps:

1. **`CoxeterMatrix.Aₙ : (n : ℕ) → CoxeterMatrix (Fin n)` is in Mathlib**, with
   exactly the entries my `typeAMatrix` computes. I wrote mine without knowing it
   existed. The ℕ-indexing is kept deliberately — it is what buys the *unbounded*
   `HeckeGenerators`, where `Aₙ N` is `Fin N`-indexed and pins one `n` — but
   `typeAMatrix_eq_An` now states the agreement so the two are connected rather
   than parallel. **This does not weaken "Mathlib has no Hecke algebra":** the
   Coxeter *theory* is there (that was never in doubt); the *algebra* is not.
2. **`S_{n+1}` IS the Coxeter group of type `Aₙ`, formalized** —
   `QOU/Hecke/SymmetricCoxeter.lean::permCoxeterSystem` on #6053, sorry-free at
   general `n`, plus the `IsCoxeterGroup` instance. That sibling also measured
   that Mathlib has **zero** `IsCoxeterGroup` instances, so `cs.length` and all of
   `Coxeter/Length.lean` / `Coxeter/Inversion.lean` had never been applied to a
   concrete group before.

**This changes the outlook on open item (1), the `T_w` basis.** My note above
said the basis "needs Matsumoto / reduced expressions, i.e. the genuinely hard
part". #6053 is taking the **Bourbaki route instead**, which sidesteps Matsumoto
entirely: build the free module `W →₀ R`, define right multiplication `Rs i`
directly on the basis by the length dichotomy, and get well-definedness as a
*consequence* of having a representation rather than as a prerequisite. Their
`Rs_sq` (the quadratic relation) is proved; the braid relation for `Rs` is the
remaining step.

So the two halves fit: their `Rs` needs braid, and once it has it,
`exists_unique_lift` from `QOU/MathlibExt/IwahoriHeckeAlgebra.lean` is exactly the
map `H_n(q) → End (W →₀ R)` — no hand-built algebra map required. Recorded on
#6053. **The `T_w` basis stays theirs**; this bean should not duplicate it.


---

## 2026-08-30 — the `T_w` basis LANDED (on #6053), and my survey had a gap

**Open item (1) is closed, by the sibling, not by me.** `QOU/Hecke/TwBasisField.lean`
on #6053: `basisTwOfField : Module.Basis (Equiv.Perm (Fin (n+1))) K (IwahoriHecke K q n)`
and `finrank_eq_factorial : Module.finrank K (IwahoriHecke K q n) = (n+1)!`, sorry-free
at general `n`, `#print axioms` clean.

They went **around Matsumoto**, not through it — `T_w` is the product along *some*
reduced word, and well-definedness is never invoked because along any reduced word the
operators merely walk the basis. Matsumoto remains an open Mathlib TODO
(`Coxeter/Basic.lean:78`) and is still unproved here. My note above called the basis
"the genuinely hard part"; that framing was pessimistic about the *route*, not wrong
about Matsumoto.

They also proved `TwBasisBraid.Rs_braid`, the step I had flagged as open.

## My survey had a real gap — recorded because it affects `qou-b5gu` too

I reported "the corpus's `IwahoriHecke` cluster is 1429 lines over 7 files and is
entirely self-contained." True **of that cluster**; I stated it as though it
characterised the corpus's Hecke situation. It does not. I never found
`QOU/Hecke/IwahoriHecke.lean` or `QOU/BraidKnot/IwahoriHeckeAPI.lean`, because I
grepped for **consumers of the names I already had** rather than for Hecke-algebra
**definitions as a class**. The `qou-b5gu` blast-radius measurement inherits that
narrowness.

## Measured: TEN Hecke-algebra-shaped definitions, not six

The sibling opened `qou-img9` listing six. Re-measured with a definition-shaped grep:
**ten**. The four extra are all `structure HeckeAlgebra`, and they are a *different*
defect — three are verbatim identical:

```lean
structure HeckeAlgebra where
  n : ℕ ; carrier : Type* ; q : R_q ; q_ne_zero : q ≠ 0
```

`carrier : Type*` with **no relation of any kind** and nothing tying it to `n` or `q`;
the only assertion is `q ≠ 0`. (`knot-eigenbasis-complete.lean:53`,
`QOU/PathIntegrals.lean:294`, `QOU/BraidKnot/CasimirShared.lean:176`.) The fourth,
`frobenius-antipode-lean-stub.lean:35`, wraps a single real: `{coeff : ℝ}`, both
parameters underscore-prefixed, over `ℝ`.

So the bare name `HeckeAlgebra` resolves to **five** things, four carrying no Hecke
content. That is a naming defect, not a reconciliation problem, and belongs as its own
rows in `qou-img9`.

**Measurement trap for whoever re-runs this:** the raw grep returns **twelve**. Two are
false positives from my own docstrings — the `Defn.lean` and `TypeA.lean` rebuilds
quote the superseded definitions inside ` ```lean ` fences to show what changed, and a
line-oriented grep counts those as live.

## What is still open in this bean

**Cell / Specht modules only.** Not started. The `T_w` basis is done and is not mine to
redo.

Two caveats on the basis, from the sibling and not contested: it is at `Q = q` while
`HeckeAlgebra R q M` here is used at `Q = q²`, and **the transport across the
convention bridge is unproved** — do not cite the basis as applying to `HeckeAlgebra`
until someone proves it. The field hypothesis is confined to the dimension squeeze;
everything upstream holds over a commutative ring.


## 2026-08-30 — the T_w basis TRANSPORTS: two presentations proved equal

`QOU/BraidKnot/HeckeTypeAPresentationEquiv.lean`:

```lean
noncomputable def algEquiv :
    IwahoriHeckeOfSn K q (n + 1) ≃ₐ[K] QOU.Hecke.IwahoriHecke K q n
```

sorry-free, `#print axioms` clean, generic `[CommRing K]`.

This closes the gap #6053's author flagged and explicitly did **not** claim: their
`finrank_eq_factorial` (`dim H = (n+1)!`) is proved against *their* presentation, and
whether it reached mine was unproved. An `AlgEquiv` carries a basis and a finrank, so it
now does — and through `IwahoriHeckeOfSn` it reaches the `HeckeGenerators` instance and
the whole JM/full-twist arc.

**It went through because the two are the same relations in different shape.** Both are
`RingQuot (FreeAlgebra K (Fin n))`; theirs writes quadratic / braid / commute as three
constructors with `Fin`-index side conditions, mine packages the last two into one
`altProd` family indexed by the Coxeter matrix. Built from the two universal properties,
so neither presentation is privileged.

Two reconciliation details worth keeping:

- **My family has a case theirs has no constructor for.** `altProd (σ i) (σ j) (M i j)`
  at `i = j` gives `M i i = 1`, `altProd a b 1 = a`, so the diagonal is `rfl`. Theirs
  omits it. It is the first case in every split.
- **Their `commute` is one-sided** (`j + 2 ≤ i`), mine symmetric — so the far case
  splits on `lt_or_gt_of_ne` and uses `σ_commute` one way and `.symm` the other.

**Index offset:** theirs has `Fin n` generators and is `H_{n+1}(q)`; mine at `m` has
`Fin (m-1)`. The match is `m = n+1`.

**Not done:** the `finrank_eq_factorial` corollary itself. `TwBasisField` is on their
branch, not main, so it cannot be written yet — `algEquiv` is the mechanism, the
one-line corollary waits on their merge. Offered it to them since the basis is theirs.

**This changes the read on `qou-b5gu` / `qou-img9`.** If presentations can be *proved
equal* pairwise, "retire vs repair" is less pressing than it looked: the cost of an
extra name is bounded by whether an equivalence exists, and here one did. That argues
for proving more of these before deleting any.
