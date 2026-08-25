---
# qou-ajfl
title: Add disclosure — 3 projections that assert **Theorem/Proposition** with none
status: todo
type: task
priority: high
tags:
    - vacuity
    - issue-2472
created_at: 2026-08-10T01:47:53Z
updated_at: 2026-08-10T01:49:54Z
parent: qou-5p7n
---

**3 declarations** whose docstring asserts `**Theorem**` / `**Proposition**` / `**Lemma**` while the body projects a class field verbatim, with no disclosure that the content is class-carried.

Criterion (2) of the honest-placeholder criterion — *no assertion of establishment*. This is the sharpest of the disclosure classes: a reader who stops at the docstring comes away believing a proof happened.

All three are **non-exempt** after the `isDefProof` narrowing, so they are live defects in the scanner, not deferred.

Fix per declaration: either add the disclosure sentence (stating the content is carried by the context-class axiom with derivation pending), or drop the `**Theorem**` framing.

- `content/quantum-observable-universe/lean/QOU/BraidKnot/Cl3Zeta5PslqIndependence.lean:37` — `pslq_independence`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/KnotIndexedConvolutionGrid.lean:35` — `grid_placement`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/QHeckeSeminormalCharacterClosure.lean:33` — `character_closure_holds`

Criterion: `docs/audits/2026-08-09-honest-placeholder-criterion.md`
