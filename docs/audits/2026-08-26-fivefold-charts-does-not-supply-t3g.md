# The fivefold-charts remark does not supply T3g's premise

**Date:** 2026-08-26 · **Branch:** `claude/8-fold-way-qou-k4e8ch` (PR #5819)
**Beans:** `qou-y7vg` (T3g, live carrier), `qou-8pl3` (Route A)
**Subject:** `rem:fivefold-affine-charts-generations`

## Why this was checked

`qou-y7vg` records that the corpus "already asserts an answer" to T3g's
existence question — *does QOU's braided category admit inequivalent fibre
functors?* — pointing at `rem:fivefold-affine-charts-generations`, which states
*"There are five topologically distinct embeddings of a fibre functor."* The
bean's own next step is **promote or refute** that claim, since it is a `remark`
with no `.lean`, no proof and no witness.

Result: **it does not supply the premise**, for three independent reasons. This
is scope-(a) — the remark as written does not establish what T3g needs. It is
**not** a claim that inequivalent fibre functors fail to exist; that question is
untouched here.

## Gap 1 — the target category contradicts the definition it interprets

This one is literal, not interpretive. `def:quantum-universe` item 3 reads:

> an $R$-linear faithful fibre functor $\tau \colon \mathbf{C} \to R\text{-}\mathbf{Mod}$

and the same block states, under **On the ground ring**, that

> $R$ is a commutative ring, **not a field**: the framework's own ground ring
> $R_q = \mathbb{Z}[q, q^{-1}]$ is not one

The remark opens *"Each fibre functor $\tau \colon \mathbf{C} \to
\mathbf{Vect}$…"*, and its manifest declares `interprets:
"def:quantum-universe"`. So the block names a different target category from the
definition it is declared to interpret — `Vect` in place of `R`-`Mod`.

This is not pedantry about notation, because the whole of Tannakian neutrality
is sensitive to it. Fibre functors to `Vect`*_k_* over a field are classified by
`H¹(k, Aut^⊗)` in Galois cohomology; fibre functors to `R`-`Mod` over
`R = ℤ[q, q⁻¹]` are a question about `Spec R` — a Tannakian *gerbe over a base
scheme*, with `H¹` taken in the fppf or étale topology. Deligne's theorem, which
`qou-y7vg` invokes, is a statement relative to a base. **Until the base is
named, "does the category admit inequivalent fibre functors" does not have a
determinate answer to promote or refute.**

## Gap 2 — embeddings are not isomorphism classes

T3g needs: fibre functors `τ₁`, `τ₂` with `τ₁ ≇ τ₂` as tensor functors —
equivalently a non-trivial class in `H¹(base, Aut^⊗)`.

The remark supplies: *"five topologically distinct **embeddings** of a fibre
functor"*. An embedding is a placement of a functor, not a functor. Five
distinct placements of one functor are consistent with exactly **one**
isomorphism class, and the remark's own phrasing — "embeddings of *a* fibre
functor", singular — reads that way. Nothing in it asserts that distinct charts
carry non-isomorphic functors, and that assertion is the entire content T3g
requires.

This is the `da-arity-conflation` shape: counting one thing and concluding about
another.

## Gap 3 — a transitive orbit is what *one* class looks like

The remark says the `S₅` symmetry *acts* on the space of charts and that the
five sheets *correspond to* five classes of chart. A group acting transitively
on a five-element set is the ordinary picture of **a single object with an
index-5 stabiliser** — it is evidence of symmetry, not of multiplicity of
isomorphism classes.

Whether an `S₅` element moves the *isomorphism class* of `τ` (rather than
permuting charts while fixing `τ` up to isomorphism) is exactly the unproved
step, and it is the step that would decide neutrality. Precomposition with a
tensor-autoequivalence can move the class — so this is genuinely open, not
settled either way — but the remark does not address it, and a reader could
easily take the orbit as evidence for the conclusion when it is neutral between
the two readings.

## What would actually settle it

Stated so the next attempt is not another reading of this remark:

1. **Name the base.** `Spec R` with `R = ℤ[q, q⁻¹]`, or a specialisation to a
   field, or something else. Neutrality is not a property of `C` alone.
2. **Identify `Aut^⊗(τ)`** as a group scheme over that base.
3. **Compute or bound `H¹`** of the base in the relevant topology. Non-vanishing
   is T3g's premise; vanishing refutes it.

Step 1 is cheap and is a prerequisite for both of the others. It is where the
next agent should start.

## Two facts that make this safe to act on

- **Nothing cites the block.** A repository-wide grep across `content/`,
  `docs/` and `.beans/` returns no consumer of
  `rem:fivefold-affine-charts-generations` other than the beans discussing it.
  It is load-bearing for nothing, so scoping or correcting it breaks no
  downstream argument.
- **Its own numbers do not match T3g's target anyway.** `qou-y7vg` already
  records this: three of the five sheets carry *generations*, not colour or
  flavour. Even granting the remark in full, the structure delivered is a
  five-fold one with a 3+2 split, not an `SU(3)`.

## Deliberately not done

- **The remark is not rewritten.** The `Vect` / `R`-`Mod` mismatch could be a
  typo or could mean the author intends an implicit base change to a field, and
  those call for different repairs. Correcting it either way is a change to a
  mathematical claim, not a fix, and belongs with the author.
- **No Lean.** The finding is that two prose claims differ from each other and
  from what a third needs. There is no invariant here to prove, and a toy
  formalisation of "five placements can share one isomorphism class" would be a
  trivial-true dressing up a reading. AGENTS.md forbids exactly that, and this
  note is the honest form of the result.
