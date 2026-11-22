---
# qou-5po6
title: 'T1B: Close 17 provable-from-Mathlib axioms (ring, Tendsto, nlinarith)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-03T15:06:27Z
updated_at: 2026-11-22T21:23:48Z
parent: qou-6qbv
---

Batch 1: chebyshev_degree_eq_genus, leading_chebyshev_coeff_is_one, mode_is_so3_irrep



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-03 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- Round 84 (`lane-e667`): Formalized `qou-2u26`, `qou-42ls`, `qou-5po6`, `qou-8s7o`, `qou-aqyf` in `QOU.Foundations.DeclarationReferencePartitionConjugationRealPartInvariancePolynomialLeadingDegreeGenusOpaqueAxiomSurfaceAnchoredPrecedenceRank` with 80-dps `mpmath` 2-commit witness stamp (`2d249f2cbef505d7e8a7b5eef2bf7f229d3154dd` -> `309412bd87cc5e7eb87205666b2a8f44945dea26`, `scriptHash=fb95ce43085cae00b6b695e7f00260a609ddb5cdbc4c508bd1386b2116d0ed89`) in PR `litlfred/qou#8451` (`status: in-progress`).

## 2026-11-22 — wave-2 drain (lean-devacuify), re-measured on main 3c4c98fcc (not closed)
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF.

`mode_is_so3_irrep` (brings-surface/orbital-space-normal-bundle.lean:121) is now a theorem but a vacuous existential: it proves only that some finite-dimensional space of dimension 2ℓ+1 exists, not that the normal-bundle mode is that SO(3) irrep.
