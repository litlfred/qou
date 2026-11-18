---
# qou-2u6r
title: 'CITE: Bryant 1987 / Hitchin 2000 (G2 as the generic-3-form stabiliser) is neither held nor registered — U — G2FrameDimensions.lean:75; baez2002 does not contain it'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:06:06Z
updated_at: 2026-10-04T15:17:54Z
parent: qou-mub3
---

**Class U — the fact is named in three places and the one citation attached to it
does not contain it.**

`folio/quantum-observable-universe/lean/QOU/Eightfold/G2FrameDimensions.lean`
defers three times to the same classical input:

- `:46-47` — *"(The identity is arithmetic. That the stabiliser there **is** `G₂`
  is classical input, not proved here.)"*
- `:75` — *"the classical **Hitchin/Bryant** fact, cited, not formalised."*
- `:180` — *"The classical fact that the stabiliser there is `G₂` is input, not
  proved here."*

The statement is: **`G₂` is the stabiliser in `GL(7,ℝ)` of a generic 3-form on
`ℝ⁷`, and the orbit is open (codimension 0).** The same fact is asserted at
`computations/form_stabilizer_genericity_su3_routes.py:21` (bean `qou-8p1f`), where
it is the reason the exceptional chain `Spin(7) → G₂ → SU(3)` runs *"through
3-forms in dimension 7"*.

**The file's only real `-- Ref:` is `[baez2002]`** (`:82`) — Baez, *The Octonions*,
Bull. AMS 39 (2002) 145–205. That paper's §4.1 gives `Der(𝕆) ≅ 𝔤₂`, dim 14 — which
is a *different* characterisation of `G₂` and is what `references.ts:8117` records
it as supplying (*"Cited by QOU/MathlibExt/OctonionDerivationsBound.lean for the
upper bound dim Der(𝕆) ≤ 14"*). **It does not contain the generic-3-form stabiliser
statement.** The file's other Ref is `[manuscript]`.

**Neither candidate source is registered or held.** `references.ts` (828 entries):
no `bryant`, no Hitchin-three-forms entry (`Hitchin` at `:1731` is a co-author of an
unrelated paper; `monodromyhitchiny` is *On the monodromy of the Hitchin
connection*). `library/`: `exceptional holonomy` 1 section file, `G_2 holonomy` 0,
and `INDEX.md` has no row for either work.

**Named works:**

1. **Bryant, R. L., *Metrics with exceptional holonomy*, Annals of Mathematics
   **126** (1987) 525–576** — the standard reference for `G₂` as the stabiliser of a
   generic 3-form and for the open orbit.
2. **Hitchin, N. J., *The geometry of three-forms in six and seven dimensions*,
   J. Differential Geom. **55** (2000) 547–576**, arXiv `math/0010054` — the
   variational/open-orbit treatment; this is the one to reach for if the "generic"
   and "open orbit" language is what is wanted.

Either would do; registering both is cheap and Hitchin is on arXiv, so it can be
ingested rather than merely registered.

**Priority is `normal`, not high, deliberately.** `G2FrameDimensions` proves
*dimension arithmetic* (sorry-free); the `G₂` identification is an input to the
narrative rather than to any theorem's statement. What is asserted-and-unsourced is
the reading, not a proved conclusion.

Found by the citation-gap sweep, `docs/audits/2026-09-04-citation-gap-inventory.md`.
