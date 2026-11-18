---
# c370
title: Finish pre-existing structural cleanup — deferred items (blocked by active PRs / author judgment)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-29T20:02:32Z
updated_at: 2026-10-04T15:19:10Z
parent: qou-5vkl
---


## Context
Follow-up to the atomic-content drain (PRs #2982, #3117) + first pre-existing
fix (PR #3133: 3 missing definition .lean siblings) + this PR
(sec:enveloping-algebras cross-chapter block-label dedup).

Remaining pre-existing structural items, each DEFERRED with its blocker:

1. **q-Bessel proof cluster** — `proof:jackson-q-bessel-contiguity`,
   `proof:q-bessel-c-k-recurrence-cfinite`, `proof:q-bessel-second-order-qdifference`
   (no .md, unregistered) + `rem:brings-q-hyperbolic-geometry` (unregistered, the
   `of:`/interprets target). NOT dead — active Lean refs (QOU.QBeta.*) + compute
   witnesses (computations/qbeta/), `BindingQBesselKernel.lean` on main.
   BLOCKER: in-progress feature in the sibling-churned mass-theory/brings-surface
   area (active PRs #3032, #3134, #3126). Completing = feature authoring (write 3
   proof .md narratives + register 4 blocks). Owner/qbeta-keystone (bean kehn) call.

2. **UGB superseded parallel set** — `def:leading-terms`, `lem:ugb-generator-choice`,
   `def:remainder-modules`, `proof:ugb-main`, `def:unital-groebner-basis` in
   unital-groebner-bases-chapter/ (unregistered; names map to the registered
   canonical set leading-term-data/generator-choice-lemma/remainder-module/
   groebner-basis). 4/5 have 0 external refs; `def:unital-groebner-basis` is
   referenced by an UNREGISTERED parallel paper structure (introduction/,
   buchberger-and-pbw/ — chapters not in the paper manifest).
   BLOCKER: all 5 have .lean siblings → in the orphan-drain PRs' (#3134/#3126)
   active scope; AND the introduction/buchberger parallel paper org needs author
   judgment (remove the old set + its parallel chapters, or register them).

3. **3 orphan remarks** — `rem:isospin-mirror-v9-empirical-near-match`,
   `rem:substrate-anchor-alternatives` (observations), `rem:inductive-gb-complexity`
   (particle-interactions). Unregistered; the first two `interprets` parents
   (`rem:option-e-isospin-test`, `prop:proton-mass-substrate-identity`) are NOT
   live in their chapter; the third has no `interprets`.
   BLOCKER: parked research-status drafts — registering would interpret absent
   parents. Author call: revive (restore parents) or delete.

4. **382 broken content-sibling .lean orphans** — tracked by bean `2ti7`; actively
   drained by sibling sessions (r13b/r13d, PRs #3134/#3126). Not ours.

## Done in this line of work
- PR #3133: 3 definition .lean siblings (q-reeb-flow-on-color-coords,
  embeddable-knot-operator, algebraic-primality) — sorry-free, lean-direct verified.
- This PR: sec:enveloping-algebras block-label dedup (models block renamed
  sec:enveloping-algebras-models; braids section keeps sec:enveloping-algebras).
