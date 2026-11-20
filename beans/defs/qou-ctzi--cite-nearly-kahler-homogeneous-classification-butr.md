---
# qou-ctzi
title: 'CITE: nearly-Kahler homogeneous classification (Butruille 2005; Gray; Fernandez-Gray) is neither held nor registered — U — the S^6 = G2/SU(3) leg'
status: todo
pr: 8209
type: task
priority: normal
tags:
    - 8f-lit
    - reorg-2026-10-04
created_at: 2026-09-04T09:06:06Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

**Class U — a classical coset identification with nothing behind it.**

The eightfold arc's `S⁶` leg (bean `qou-uq5x`,
`docs/audits/2026-09-04-the-g2-frame.md`, and
`lean/QOU/Eightfold/G2FrameDimensions.lean`) rests on the identification
**`S⁶ = G₂/SU(3)`** and on the surrounding homogeneous nearly-Kähler picture —
`G₂/SO(4)` being the other `G₂` quotient, excluded there on isotropy grounds.

**Measured 2026-09-04.** `library/`, all four tiers: `nearly Kähler` **0**,
`nearly-Kahler` **0**, `G_2 holonomy` **0**, `Wolf space` **0**,
`quaternionic-Kähler` **0**, `exceptional holonomy` 1; `INDEX.md` 0 rows.
`references.ts` (828 entries): no `gray`, no `fernandez`, no `butruille`, no
`salamon`, no `joyce` on `G₂` (`joyce1982` is David Joyce, *A classifying invariant
of knots, the knot quandle*, JPAA 23 — a different Joyce entirely, and a trap for
anyone grepping the surname). `.beans/`: `Butruille` 0, `Bryant` 0.

**Named works:**

1. **Butruille, J.-B., *Classification des variétés approximativement kähleriennes
   homogènes*, Ann. Global Anal. Geom. **27** (2005) 201–225**, arXiv
   `math/0612655` — the classification of homogeneous nearly-Kähler 6-manifolds:
   exactly four, `S⁶ = G₂/SU(3)`, `S³×S³`, `ℂP³`, `F₁,₂`. This is the paper that
   makes "`S⁶ = G₂/SU(3)` is *the* nearly-Kähler 6-sphere" a theorem rather than an
   example.
2. **Gray, A., *Nearly Kähler manifolds*, J. Differential Geom. **4** (1970)
   283–309** — the original definition.
3. **Fernández, M. & Gray, A., *Riemannian manifolds with structure group `G₂`*,
   Ann. Mat. Pura Appl. **132** (1982) 19–45** — the 16-class `G₂`-structure
   taxonomy, if the arc goes past the coset.

Butruille alone is probably sufficient and is on arXiv, so it can be ingested.

**Scope caution before anyone spends the upload.** The corpus already carries a
standing exclusion on the *next* step:
`docs/coordination/s5-so3-keystone.md:31,47,51` — no compact / finite-dimensional
Sasakian or MTC arena can host `W_λ` at `q₀ ≈ 1.10998` (real `> 1`, not a root of
unity). That is scope-**(a)** against a homogeneous-coset route (different
construction, must be re-run), but it means an upload here buys *citability* for the
frame, not a route to `W`. `docs/audits/2026-09-04-the-cr-dimension-decision-full-context.md`
§5 says the same thing from the dimension side: no resolution of the CR-dimension
decision supplies `W`.

Found by the citation-gap sweep, `docs/audits/2026-09-04-citation-gap-inventory.md`.

## Progress (2026-11-16, PR #8209)
- [x] Non-vacuous Lean 4 theorem proved (`0` `sorry`, `0` vacuity advisories) in `folio/quantum-observable-universe/lean/QOU/Eightfold/RankOneSpinSingletThreeGenerationsLadderChargeAndNearlyKahlerCosets.lean`
- [x] 50-dps `mpmath` probe and witness stamped (`9c4fe9d8065c7167caac7a61ef4becd45df1573f`, `scriptHash: e6bdb7c63ac7`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8209`

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8209, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
