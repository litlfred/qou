---
# qou-de7r
title: 'Fibration LES infra: homotopy lifting property + pi_n functoriality + middle exactness'
status: in-progress
type: task
created_at: 2026-08-24T19:05:22Z
updated_at: 2026-08-24T19:05:22Z
blocking:
    - qou-jbfx
---

Item 2 of qou-pan0. Building the topological side that would feed QOU/Mathlib/LongExactSequence.lean.

Branch: claude/mt7r-archimedean-eval-2026-08-24

Mathlib survey (against the pinned oleans, by enumerating module contents, not guessing):
- HAS: HomotopyGroup / GenLoop / Cube.boundary, ContinuousMap.Homotopy{,With,Rel}, HomotopicRel.comp_continuousMap, Topology.Homotopy.Lifting (covering maps only: IsCoveringMap.liftHomotopy etc).
- ABSENT: any topological fibration predicate. 'Fibration' in the olean tree occurs only in Order/UpperLower/Fibration and the abstract CategoryTheory model-category / simplicial-set files, none of which touch HomotopyGroup.
- ABSENT: any induced map pi_n(X) -> pi_n(Y). GenLoop has no 'map'.

Scope: (1) HasHomotopyLiftingProperty predicate, (2) induced maps, (3) exactness at the middle spot. (4) connecting map delta is out of scope.
