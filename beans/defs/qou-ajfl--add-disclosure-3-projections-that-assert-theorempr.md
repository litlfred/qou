---
# qou-ajfl
title: Add disclosure — 3 projections that assert **Theorem/Proposition** with none
status: completed
type: task
priority: high
tags:
    - vacuity
    - issue-2472
    - reorg-2026-10-04
created_at: 2026-08-10T01:47:53Z
updated_at: 2026-11-22T21:35:00Z
parent: qou-6qbv
---

**3 declarations** whose docstring asserts `**Theorem**` / `**Proposition**` / `**Lemma**` while the body projects a class field verbatim, with no disclosure that the content is class-carried.

Criterion (2) of the honest-placeholder criterion — *no assertion of establishment*. This is the sharpest of the disclosure classes: a reader who stops at the docstring comes away believing a proof happened.

All three are **non-exempt** after the `isDefProof` narrowing, so they are live defects in the scanner, not deferred.

Fix per declaration: either add the disclosure sentence (stating the content is carried by the context-class axiom with derivation pending), or drop the `**Theorem**` framing.

- `folio/quantum-observable-universe/lean/QOU/BraidKnot/Cl3Zeta5PslqIndependence.lean:37` — `pslq_independence`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/KnotIndexedConvolutionGrid.lean:35` — `grid_placement`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/QHeckeSeminormalCharacterClosure.lean:33` — `character_closure_holds`

Criterion: `docs/audits/2026-08-09-honest-placeholder-criterion.md`

## 2026-11-15 — PR opened (`Q-6QBV-1 = 1`)

- PR: https://github.com/litlfred/qou/pull/8001 (`claude/qou-z3k1-ajfl-z9fx-2026-11-15`, head `dc257cfe44475b4d418b26d8e48c2b5566459344`)
- Replaced the tautological `claim_placement_well_defined` in `folio/quantum-observable-universe/lean/QOU/BraidKnot/KnotIndexedConvolutionGrid.lean` with the genuine injectivity statement `(bar_class k₁, depth k₁) = (bar_class k₂, depth k₂) → k₁ = k₂` and verified downstream consumer `folio/quantum-observable-universe/mass-theory/knot-indexed-convolution-grid.lean` compiles cleanly.

## 2026-11-22 honesty-roundtrip (bean-drain wave 2, session_01Qmmkt63qmS4AFFfqMq2Z2e; issue #8813, branch claude/honesty-roundtrip-pass3-2026-11-22)
Completed, evidence: all three declarations are gone from main 3c4c98fcc, removed 2026-08-30 under bean qou-z9ws as self-assuming projections with zero references. Each file records the removal: Cl3Zeta5PslqIndependence.lean:141 (pslq_independence), KnotIndexedConvolutionGrid.lean:34 (grid_placement), QHeckeSeminormalCharacterClosure.lean:99 (character_closure_holds). No **Theorem** framing over a projection remains.

## 2026-11-22 applicability review (owner instruction 2026-11-22; wave 2, session_01Qmmkt63qmS4AFFfqMq2Z2e)
**ALREADY-DONE**: the 3 declarations were removed 2026-08-30 under qou-z9ws. Premise check against docs/coordination/owner-rulings.md on main: the bean rests on no retired premise (photon form, trefoil electron, convention C, z=1 Q_β base, census selection, absolute mass, muon pin A, virtual photons, adopted quark charges).
