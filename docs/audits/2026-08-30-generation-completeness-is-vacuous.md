# `generation_completeness` constrains no knot, and its corollary restates its own hypothesis

**Date:** 2026-08-30 · **Bean:** `qou-0avp` · **Status:** machine-checked (`lean` exit 0)
**Subject:** [`content/quantum-observable-universe/brings-surface/generation-completeness.lean`](../../content/quantum-observable-universe/brings-surface/generation-completeness.lean)
**Reproduce:** [`scripts/lean/probes/generation-completeness-vacuity.lean`](../../scripts/lean/probes/generation-completeness-vacuity.lean)

## Summary

The file is two theorems over two definitions. Both theorems hold, and neither
says anything about knots.

```lean
def genusBound : ℕ := 4
structure KnotType where
  seifertGenus     : ℕ
  unknottingNumber : ℕ

def isEmbeddable (K : KnotType) : Prop := K.seifertGenus ≤ genusBound
def isReachable  (K : KnotType) : Prop := ∃ r : ℕ, r ≤ K.unknottingNumber

theorem generation_completeness (K : KnotType) (h_embed : isEmbeddable K) :
    isReachable K := ⟨K.unknottingNumber, le_refl _⟩

theorem spectrum_complete (K : KnotType) (h : K.seifertGenus ≤ 4) :
    isEmbeddable K ∧ isReachable K := ⟨h, generation_completeness K h⟩
```

`∃ r : ℕ, r ≤ K.unknottingNumber` is inhabited by `r = 0` for **any** `K`
whatsoever. Verified, `lean` exit 0 against the real file:

| verified | |
|---|---|
| `(K : KnotType) → isReachable K` | holds with **no** hypothesis |
| `isReachable ⟨999, 0⟩` | holds for genus 999, far outside the bound |
| `(K) → ¬ isEmbeddable K → isReachable K` | holds when the hypothesis is **negated** |
| `(K) (h : K.seifertGenus ≤ 4) → isEmbeddable K` | the corollary's first conjunct **is** `h` |

The third row is the sharpest. The docstring scopes the claim to *"any knot with
Seifert genus g(K) ≤ 4"*, but reachability holds for knots explicitly outside
that bound — so the stated scope is not a scope.

## What the prose claims

> **Generation completeness** (Theorem): Let K be any knot with Seifert genus
> g(K) ≤ 4. Then K is **reachable from the generator set G by a finite sequence
> of Skein crossing changes.** … Proof proceeds in two steps: 1. Reachability
> from the unknot … 2. Spectral filter: the Bring's surface imposes g(K) ≤ 4 …

and the corollary:

> **The Descartes particle spectrum is complete over embeddable knots** — every
> knot with g(K) ≤ 4 corresponds to a state in the algebraic direct limit
> `V_phys = colim V^⊗n`.

Neither step of the stated proof appears in the term. There is no generator set
`G`, no Skein move, no unknot, and no spectral filter anywhere in the file.
`KnotType` is two naturals; nothing distinguishes a knot from any other pair.

## Lean already said half of it

Compiling the file emits, unprompted:

```
warning: unused variable `h_embed`
```

The genus hypothesis is dead code and the linter reports it on every build. That
is a free signal that a stated hypothesis does no work, and it was available
without this audit.

## Scope of the finding

This is a **(a) scope-limited** observation in the refutation-discipline sense,
and deliberately so:

- It says the *Lean* establishes nothing about knot generation. It does **not**
  say the mathematical claim is false — generation completeness for `g(K) ≤ 4`
  may well be true, and `[kauffman1991]` is cited for the unknotting-number
  step.
- It does **not** touch any numerical prediction. Nothing downstream computes
  from these two theorems; `spectrum_complete` is the only consumer of
  `generation_completeness`, and nothing consumes `spectrum_complete`.

What it does say is that a file whose LaTeX label is `thm:generation-completeness`
and whose corollary asserts particle-spectrum completeness carries no formal
content toward either.

## Disposition

Findings only — **no Lean is changed here.** The honest fix is a content
decision, not a mechanical one, and there are two shapes it could take:

1. **State the real proposition and let it carry a `sorry` + `-- Ref:`.** The
   §1 discipline's "state-and-queue" disposition: define reachability as an
   actual reachability relation over an actual move set, state the theorem, and
   mark it open with its Kauffman citation. This is honest and makes the gap
   visible to `#print axioms`.
2. **Demote to a `conjecture` block.** If the geometric content is not close to
   formalisable, the §3b carve-out is the right home.

What is *not* acceptable is the current state, where the declaration kind is
`theorem` and the prose claims a two-step proof that the term does not perform.

The probe is kept **outside** the source file, as an appendable fragment with a
recipe in its header, so it can never be mistaken for a claim the paper makes.
The recipe was run verbatim from the committed file before this doc was written.

## Method note

Surfaced by the `major` tier of the borrowed-name audit (`qou-0avp`) during a
re-measure on current `main`, 824 commits after the previous pass. Worth noting
that the detector flagged it on *name-and-shape* grounds — a borrowed name
(`Skein`), local-only definitions, a cheap proof — and the vacuity was found by
reading, not by the detector. The kernel `defeq_collapse` signal would not have
caught it either: `⟨K.unknottingNumber, le_refl _⟩` is not a definitional
collapse, it is an honest term inhabiting a trivially-inhabited type. That is a
third shape, distinct from both signals the two detectors carry.
