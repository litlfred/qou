---
# qou-10zv
title: 'G1-opt4 (flavour Cartan): S/C as a q-graded / bar-grade flavour index (speculative).'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-flavour
created_at: 2026-08-02T20:19:13Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---


## Progress Update — 2026-11-16 (`litlfred/qou#8159`, `4a5bd83fa5c08b2011cfb42b8d918e41431e6d96`)

- **Lean 4 formalization (`folio/quantum-observable-universe/lean/QOU/Eightfold/MagnusTripleLinkingAndFlavourGradings.lean`, `0` `sorry`, wired into `QOU.lean`)**:
  - Formalizes the torus-knot generation bar-grade `barGrade (β : BraidWord) : Int := (intAbs (writhe β) - 1) / 2` and proves `barGrade_torus_carriers` (`[sigma1Pow 1, sigma1Pow 3, sigma1Pow 5, sigma1Pow 7].map barGrade = [0, 1, 2, 3]`).
  - Defines `strangenessFromBarGrade` ($S(g) = -\delta_{g,2}$) and `charmFromBarGrade` ($C(g) = +\delta_{g,3}$), and proves `combined_barGrade_ribbonTwist_reproduces_quarks` showing that pairing `barGrade` $g \in \{1, 2, 3\}$ with the 3-strand ribbon twist $T \in \{-1, +2\}$ injectively reproduces $(2I_3, S, C, 6Q)$ across all 4 quark flavours $(u, d, s, c)$.
- **Witness (`computations/probes/magnus-triple-linking-and-flavour-gradings.witness.json`)**: `allPassed: true` (`q0Anchor: "independent"`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8159, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
