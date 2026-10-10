---
# qou-cyay
title: Four editorial cycles, and what each one's direction actually is
status: completed
type: bug
created_at: 2026-08-15T23:21:49Z
updated_at: 2026-08-15T23:21:49Z
---

Counting `interprets` as an editorial edge (folio-assistant `i8ad`) made four
cycles visible. Each says a reader must read A before B **and** B before A, so
each has a wrong leg. Four edges removed; no prose changed.

**Three of the four were already failing** `detangler-no-dependency-cycle` — the
pure-`uses[]` ones. They were known findings, not new. The fourth was invisible
because its return leg is an `interprets` edge, fixed in folio-assistant `wesu`.

## The cuts, and the reason for each

**1. `conj:mass-volume-factorization` drops `rem:frobenius-packing-density`.**
That remark declares `interprets: "conj:mass-volume-factorization"` — it exists
to interpret this conjecture. Requiring it back made the conjecture a
prerequisite of its own interpretation. `interprets` already carries the
relation in the direction that is true.

**2. `thm:ns-singularity-descartes` drops `prop:ns-kummer-specialisation`.**
Decided on prose asymmetry: the proposition's narrative links to the theorem;
the theorem's never links to the proposition. The dependency runs
specialisation → theorem.

**3. `conj:q-collatz` drops `rem:skein-filtration-trichotomy`.** Same shape as
(1) without the `interprets` field to say so. The remark — *"One length
filtration, three problems"* — synthesises across three problems of which this
conjecture is one. A problem statement does not require the remark that
discusses it; the reader meets the conjecture first and the synthesis after.

**4. `conj:q-collatz` drops `prop:ns-kummer-specialisation`.** The prose says
*"**Compare** the same caveat on the P versus NP leg … and on the Navier--Stokes
leg ([Kummer specialisation](#prop:ns-kummer-specialisation))"* — an explicit
parallel, not a prerequisite.

That last one is worth naming: a prose link is **prima facie** evidence of a
dependency and no more. This arc restored 18 edges on exactly that signal, and
the tranche sheets carry the warning that a link can contrast, disclaim, or
compare rather than depend. Here is the case the warning was written for — and
link counts alone would have got it wrong, since all three legs of that cycle
are linked in prose.

## Verified

| | before | after |
|---|---|---|
| union-graph editorial cycles | 4 | **0** |
| blocks failing `detangler-no-dependency-cycle` | 6 | **0** |
| forward references | 196 | **195** |

The forward-reference drop is a side effect of cut (2), not a target:
`prop:ns-kummer-specialisation` sits later in its chapter than the theorem, so
that edge was a forward reference too. Removing a wrong dependency removed a
real forward reference with it.

`content_validate` ✓ Valid, 42 issues, unchanged.

## What this does not claim

That these four blocks now have correct `uses[]`. Each cut removes one edge that
demonstrably ran the wrong way; whether the remaining entries are complete is
the `prn1` question, and 107 sources there still need reading.
