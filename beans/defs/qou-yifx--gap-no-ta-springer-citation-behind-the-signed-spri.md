---
# qou-yifx
title: 'GAP: no T.A. Springer citation behind the ''signed Springer dimension'' (Delta_lambda)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T22:27:03Z
updated_at: 2026-10-04T15:20:16Z
parent: qou-mub3
---

## The gap

`Δ_λ = (−1)^{n(λ)}·dim V_λ` is called **"the signed Springer dimension"**
in 8 places across the corpus, and **no T.A. Springer reference is
registered**. Verified 2026-08-08:

- `grep 'family: "Springer"' content/schema/references.ts` → **no match**.
  All 23 `Springer` hits in `references.ts` are the **publisher**
  (`Springer`, `Springer Nature`, `Springer-Verlag`).
- The only `.md` uses of the *mathematician* are the term itself; the other
  three `.md` hits are Kassel 1995's publisher.

## Why it is load-bearing, not cosmetic

The corpus itself says the missing input is external Springer geometry:

- [`STATUS.md:17`](../STATUS.md) — open item (b) is "the **geometric
  concentration**, which needs an external **Springer-geometry input**".
- [`DeltaLambdaTopDegreeConcentration.lean:16`](../folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaTopDegreeConcentration.lean)
  — "the Springer dimension `n(λ)` must enter from an [external input]".

So an open leg of a PROVED result is named after a body of work the
bibliography does not contain. A reader cannot follow the naming to its
source.

## Sites using the term

- `folio/quantum-observable-universe/appendix-mass-binding-algorithms/mba-sidecar-delta-lambda-closure.md:14`
- `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaTopDegreeConcentration.lean:16`
- `STATUS.md:17`
- `AGENTS.md:1008`
- `docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md:16,51`
- `docs/audits/2026-08-01-deltalambda-dt-substrate-derivation.md:77`
- `.beans/qou-7ylg--*.md:52`

## Why this is a bean and not a commit

**The DOIs could not be verified in this environment, so nothing was
registered.** The `paper-search-mcp` Crossref tools return empty for
*every* query here — including `10.1007/BF01404457`, a DOI already
verified in `references.ts`. That is a dead tool, not a wrong DOI, and it
means any entry written now would carry a DOI from model memory alone.

`references.ts` already shows what that produces — see the `wenzl1988b`
note: *"PLACEHOLDER: only the DOI ... is verified ... Resolve DOI manually
before publication."* Adding a second such entry to fix a citation gap
would be self-defeating.

## Next step for whoever picks this up

In an environment with working DOI resolution, verify and register the
Springer correspondence sources, then cite them at the `.md` and Lean
sites above. The expected sources (**titles from memory — verify before
registering, do not paste these DOIs**):

- T.A. Springer, *Trigonometric sums, Green functions of finite groups and
  representations of Weyl groups*, Invent. Math. **36** (1976).
- T.A. Springer, *A construction of representations of Weyl groups*,
  Invent. Math. **44** (1978).

The mathematical tie to check while registering: for a nilpotent of Jordan
type λ, the Springer fibre has dimension `n(λ) = Σ_i (i−1)λ_i` — the same
partition statistic the corpus calls the jet-order valuation parity. If
that identification is what justifies the name, it should be stated at the
citation site rather than left implicit in the term.

## Provenance

Surfaced by the paper-relevance triage of the first 47-document cohort
(`claude/agent-4775-checkpoint-fmucd2`). Reported to the author alongside a
claimed missing-Goncharov gap; **that half was stale** — `deligne-goncharov2005`
(arXiv:math/0302267) is registered. The Springer half was re-verified and holds.
