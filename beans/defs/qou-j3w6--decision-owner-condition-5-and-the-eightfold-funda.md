---
# qou-j3w6
title: 'DECISION (owner): condition 5 and the eightfold fundamental — keep N=2 + second object W, weaken to epimorphism, top-power Λ^N, or nothing'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
    - 8f-decide
created_at: 2026-09-03T15:35:48Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

Frame: docs/audits/2026-09-03-eightfold-axiom-5-decision-frame.md (PR #6458). Every single-fibre route to flavour SU(3) is closed by a proved invariant (Sym2 parity, Ocneanu, fibre-functor CG parity, octonionic rank). The missing object needs Lambda^3 W = 1, which condition 5 (Lambda^2 V = 1, N = 2) forbids for V. Options: A keep N=2 + second fundamental W (recommended, formalize-first, labelled axiom datum); B weaken to epimorphism (breaks convention-D forcing chain, 10 su2-emergence consumers — not recommended); C top-power Lambda^N V with N a datum (forces the multi-universe picture); D nothing (default). Owner was asked 2026-09-03 and dismissed the question; awaiting a decision.

## 2026-10-10 — owner decision

Owner decision 4d (ofri, 2026-10-10): nothing changes for now. Condition 5 ($\Lambda^2 V \cong \mathbf 1$) stays as it is, and the flavour chapter stays conditional on "$N = 3$". Option (a) (a second object $W$ with $\Lambda^3 W \cong \mathbf 1$) is the suggested later route, once the generation question (`qou-xtcl`) settles. Related evidence from the same day: the level-3 channel test (PR #7634, `qou-lxh5`) found that choosing level $r = 3$ is equivalent to assuming such a 3-dimensional module, so colour enters by assumption on that route too.


## Progress Update — 2026-11-16 (`litlfred/qou#8155`, `f3af82fd1d99fc5eb05c0bd46bbd812b46330432`)

- **Lean 4 formalization of Owner Decision 4d two-object split (`folio/quantum-observable-universe/lean/QOU/Eightfold/FlavourCartanOctetDecuplet.lean`, `0` `sorry`, wired into `QOU.lean`)**:
  - Proves `su6_spin_flavour_56_and_condition5_split`: keeps Condition 5 ($\Lambda^2 V \cong \mathbf{1}$, $N = 2$) on the single-fibre spin/weak module $V$ (where $\dim \Lambda^3 V = \binom{2}{3} = 0$, killing the 3-row antisymmetric spin diagram) while introducing the conditional $N = 3$ flavour module $W$ ($\Lambda^3 W \cong \mathbf{1}$, $\dim \Lambda^3 W = \binom{3}{3} = 1$), and proves that their tensor product $W \otimes V \cong \mathbb{C}^6$ yields the exact ground-state baryon spectrum $\mathrm{Sym}^3(\mathbb{C}^6) = (\mathbf{10}, \mathbf{4}) \oplus (\mathbf{8}, \mathbf{2}) \oplus (\mathbf{1}, \mathbf{0}) = 40 + 16 + 0 = 56$.
- **Witness (`computations/probes/flavour-cartan-octet-decuplet-degeneration.witness.json`)**: `allPassed: true` (`q0Anchor: "independent"`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8155, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-09-03: "beans(qou-icj2): eightfold session closed — PR #6458 merged, four fronts completed, qou-j3w6 decision left open for the "). The work may be partly or fully done. Read the bean before you close it.
