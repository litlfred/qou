---
# qou-gmfz
title: 'Kazhdan-Lusztig classical limit: the KL-basis identification and monoidality are still unstated'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T19:39:51Z
updated_at: 2026-11-18T08:59:30Z
parent: qou-k4oq
---

`QOU/BraidKnot/KazhdanLusztigClassicalLimit.lean`. Follow-up to the repair
landed 2026-08-24 on `claude/mt7r-archimedean-eval-2026-08-24`; this bean is the
**remainder**, and the file's own docstring already names it.

## What was repaired (do not redo)

- `statSign` retyped from `Z` to the ground ring `R`, so a root of unity can
  live there and the collapse can fail;
- the sibling axiom `statSign_pm_one : forall b, statSign b = 1 \/ statSign b = -1`
  **deleted** — it axiomatised the very collapse the conjecture claims, making
  `kl_compatible_with_tau` derivable in every model;
- `kl_compatible_with_tau` guarded by `q = 1`, so it asserts nothing away from
  the classical point;
- `canonical` demoted `instance` -> `def` (it was `KLBasisElt := PUnit`,
  `statSign _ := 1`, discharging by `Or.inl rfl` — and its docstring had claimed
  it "carries the conjecture as a sorry", which was false; no `sorry` existed).

## What is still owed

The module docstring states the conjecture as three claims:

> as `q -> 1`, the KLR canonical basis `{b_w}` of `H_n(R,q)` **flattens to the
> Kazhdan-Lusztig basis** `{C_w}` of `Z[S_n]`, and the resulting classical-limit
> functor **is monoidal** and **compatible with the observation functor tau**.

The class states one of them, weakly:

```
class KazhdanLusztigClassicalLimit (R) [CommRing R] (q : R) [H : ...] [C : ...] where
  KLBasisElt : Type u                       -- an ARBITRARY type
  klMap : H.NormalForm -> KLBasisElt        -- an ARBITRARY function
  statSign : KLBasisElt -> R
  kl_compatible_with_tau : q = 1 -> forall T, statSign (klMap T) = 1 \/ statSign (klMap T) = -1
```

- **The KL basis is not there.** `KLBasisElt` is an opaque type with no
  Kazhdan-Lusztig structure — no Hecke algebra of `S_n`, no bar involution, no
  KL polynomials, no defining property. So "flattens to the KL basis" is not
  stated; any type at all satisfies the signature.
- **Monoidality is not there.** No tensor structure on either side, no
  comparison morphism, nothing to be monoidal about.
- **`tau` is not there.** The field is *named* `kl_compatible_with_tau` and
  `tau` appears nowhere in the class. What the field says is that a phase is
  `+-1` at `q = 1`. That is a consequence one might want *from* tau-compatibility,
  not tau-compatibility.

## What it costs

Both missing claims need `tau` and the KL basis as **independent data** — the
whole point being that `klMap`'s target is not free to be chosen. Concretely:

1. a `KLBasis` structure over `Z[S_n]` carrying the bar involution and the
   defining self-duality, so `KLBasisElt` can be *required* to be it rather than
   permitted to be anything;
2. `tau` as a field (the observation functor already exists upstream in
   `HeckeAnyonicSubstrate` / `CrystalGraphRealization` — check before
   re-declaring), and `kl_compatible_with_tau` restated as a square that
   commutes, with the `+-1` statement demoted to a corollary;
3. monoidal structure on the source and target and a `klMap`-is-monoidal field.

(1) is the useful one and is independently valuable — nothing else in the corpus
has a Kazhdan-Lusztig basis. (3) is the largest and the least load-bearing for
anything downstream today.

## State

`statSign_klMap_pm_one` and `statSign_sq_eq_one` are the only consumers, both in
this file, both now correctly conditional on `q = 1`. No instance exists outside
`canonical` (a `def`). Nothing breaks while this is open; the risk is only that
the module docstring keeps promising three things the Lean states one of.
Consider trimming that docstring in the same change so the gap is visible from
the top of the file, not just from this bean.


---

## Infrastructure built 2026-08-25 — item (1) landed, sorry-free

Owner's direction: build out the needed infra. Item (1) — "a `KLBasis`
structure over `Z[S_n]` carrying the bar involution and the defining
self-duality, so `KLBasisElt` can be *required* to be it rather than permitted
to be anything" — is done.

**`QOU/Mathlib/KazhdanLusztigBasis.lean`**, registered in `QOU.lean`.

- `BarInvolution R M` — a ring involution `barR` plus a semilinear module
  involution `barM`, with `barM (r • m) = barR r • barM m` written out rather
  than routed through Mathlib's `sigma`-semilinear maps (which would force a
  `RingHomInvPair` for a map that is only involutive).
- `KLBasis W R M B` — a `Module.Basis W R M` every element of which is
  bar-invariant. The basis field is the substantive one: it is what
  `KLBasisElt : Type u` was missing.
- **`nontrivial_of_klBasis`** — the point. A module carrying a KL basis over a
  nonempty index is nontrivial, so `KLBasisElt := PUnit` cannot inhabit the
  structure. This is the theorem that converts a signature into a constraint.
- `bar_smul_self_iff` — `r • C w` is bar-invariant iff `barR r = r`. Shows
  bar-invariance is a condition on something, which it was not before.
- Plus `ne_zero`, `basis_injective`, `barM_bijective`.

`#print axioms` on all six: `[propext, Classical.choice, Quot.sound]`, no
`sorryAx`. Checked directly rather than inferred from a green build — a
mid-session trim of one proof compiled clean while silently emitting
`declaration uses 'sorry'`, which is exactly the failure this corpus keeps
finding.

**Also landed:** the module docstring of `KazhdanLusztigClassicalLimit.lean` no
longer promises three claims the Lean states one of. It now says which one is
carried and why the other two are not — this bean suggested exactly that, and
it is done in the same change.

## Two things blocked on Mathlib SOURCES, not on difficulty

This checkout carries Mathlib as **oleans only** (`.lake/packages/mathlib/`
has no source tree), so lemma names cannot be searched, only guessed and
compiled. Two shallow facts are consequently unproved and are left stated
rather than `sorry`ed:

- [ ] `Function.Involutive LaurentPolynomial.invert`. Needed to instantiate
      `BarInvolution` at the actual ground ring `R_q = Z[q, q^-1]`, which would
      stop this file being purely abstract. `LaurentPolynomial.invert_invert`
      does not exist and `simp` does not close it.
- [ ] The *converse* of `bar_smul_self_iff` was briefly weakened for the same
      reason before the real cause surfaced — see below — and is now proved.

Cheap for anyone with sources to hand.

## The real bug, worth recording

Every proof in the first four compile attempts failed in confusing ways —
unsolved `case w : W`, tactics reported as "never executed", one silent
`sorry`. The cause was a single line: this Mathlib has **`Module.Basis`, not
`Basis`**. With `-DautoImplicit=false` the unknown identifier gave the structure
field an error type, and every downstream proof failed *downstream of that*
rather than at the source. Time was spent rewriting correct proofs.

Lesson for the next agent on an olean-only checkout: when a proof fails in a
way that makes no sense, `#check` the types it mentions in a three-line scratch
file before touching the proof. That probe costs one compile; guessing cost
five.

## Still owed — items (2) and (3), and the wiring

- [ ] **Wire `KLBasisElt` to `KLBasis`.** Not done, and the obstacle is
      specific: requiring `KLBasis (Equiv.Perm (Fin n)) R _ _` needs an `n`,
      and `KazhdanLusztigClassicalLimit` takes only `(R) (q)
      [HeckeAnyonicSubstrate] [CrystalGraphRealization]` — the strand count is
      not in scope. Adding a `KLBasis` over an unconstrained index would tighten
      the class without ruling out the trivial model, since `KLBasisElt :=
      PUnit` still admits the rank-one module `R`. **Pinning the index to
      `S_n` is what makes the constraint bite.**
- [ ] **(2) `tau` as a field**, with `kl_compatible_with_tau` restated as a
      commuting square and the `pm 1` statement demoted to a corollary. Check
      `HeckeAnyonicSubstrate` / `CrystalGraphRealization` for an existing `tau`
      before re-declaring.
- [ ] **(3) Monoidality.** Unchanged: largest, least load-bearing.
- [ ] **Unitriangularity** is deliberately absent from `KLBasis` — `C_w = T_w +
      sum_{v<w} P_{v,w} T_v` with the degree bound needs the `T`-basis and
      Bruhat order, i.e. the Hecke algebra this tree does not have. Without it
      `KLBasis` specifies what a KL basis *satisfies* rather than pinning it, so
      downstream may use it to constrain but never to conclude uniqueness. The
      module docstring says so.


## UNBLOCKED 2026-09-13 by the `library/` ingestion (merge `3cb26d4b9f8`)

This bean's blocker is *"the KLR canonical basis flattens to the
Kazhdan-Lusztig basis … **The KL basis is not there.** `KLBasisElt` is an opaque
type."* The primary literature is now held and greppable via corpus-grep path 5:

- **`library/arxiv-1304.0323v3/`** — *Symmetric Quiver Hecke Algebras*, **154**
  on-topic hits.
- **`library/arxiv-1108.1048v3/`** — *Irreducible representations over KLR
  algebras*, **45** hits.

This is **not** an enrichment of what was already held: the eight pre-existing
holdings are passing mentions, 1–5 hits each (`arxiv-1409.2799v2` 5,
`arxiv-2607.03827v1` 3, `arxiv-2210.09583v1` 1).

The same two documents are also the missing primary literature for **AGENTS.md
§7b** (Type B folding / symmetric crystals / decategorifying to KL bases), which
cites no source at all. Also newly held: `arxiv-1801.05145v1`,
`arxiv-2004.04939v1`, `arxiv-2101.05931v3`, and `arxiv-0804.0917v1`
(*Composition–Diamond Lemma for Modules* → GS / the `ugb` package).

Holding a source is a **citation**, not a derivation — this unblocks the read,
not the proof. §13a: stays open.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- Round 76 (`lane-e667`): Formalized `qou-gmfz`, `qou-img9`, `qou-phir`, `qou-siin`, `qou-l25z` in `QOU.Foundations.TriangularBarInvolutionLengthTwoQuadraticDefectRightMultiplicationDichotomyRootParameterRescalingWritheHomomorphism` with 80-dps `mpmath` 2-commit witness stamp (`1d514d8cc14cab86cdbfe50f0bca4313a91a6db7` -> `8fbc40e0a853ba6aa21eab5cf4d1947155a2d115`, `scriptHash=b5b4b562fbd04cd73aa5a68e31eebc858e55abd805cb24915d3a249d657d689c`) in PR `litlfred/qou#8409` (`status: in-progress`).
